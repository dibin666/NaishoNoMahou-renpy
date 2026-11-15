#!/usr/bin/env python3
"""
Transpiles all 77 KAG3 scenario scripts (.ks) from Data1.cab (with patch.xp3 overlay)
into Ren'Py 8 scenario modules under renpy_project/game/scenario/.
"""

import os
import re
import shlex
import struct
import subprocess
import zlib
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CAB_PATH = ROOT_DIR / "おジャ魔女あどべんちゃ～「ないしょのまほう」" / "Data1.cab"
PATCH_XP3_PATH = ROOT_DIR / "No CD Patch" / "patch.xp3"
SCENARIO_OUT_DIR = ROOT_DIR / "renpy_project" / "game" / "scenario"


def cab_read(filename: str) -> bytes:
    return subprocess.check_output(["cabextract", "-p", "-F", filename, str(CAB_PATH)])


def parse_xp3(data: bytes) -> dict[str, bytes]:
    magic = b"XP3\r\n \n\x1a\x8b\x67\x01"
    idx = data.find(magic)
    table_off = struct.unpack_from("<Q", data, idx + 11)[0]
    pos = idx + table_off
    flags = data[pos]
    pos += 1
    if flags & 1:
        zsize, _ = struct.unpack_from("<QQ", data, pos)
        pos += 16
        raw = zlib.decompress(data[pos : pos + zsize])
    else:
        osize = struct.unpack_from("<Q", data, pos)[0]
        pos += 8
        raw = data[pos : pos + osize]
    files: dict[str, bytes] = {}
    p = 0
    while p < len(raw):
        tag = raw[p : p + 4]
        sz = struct.unpack_from("<Q", raw, p + 4)[0]
        p += 12
        chunk = raw[p : p + sz]
        p += sz
        if tag != b"File":
            continue
        cp = 0
        fname = None
        segs = []
        while cp < len(chunk):
            stag = chunk[cp : cp + 4]
            ssz = struct.unpack_from("<Q", chunk, cp + 4)[0]
            cp += 12
            sc = chunk[cp : cp + ssz]
            cp += ssz
            if stag == b"info":
                nlen = struct.unpack_from("<H", sc, 20)[0]
                fname = sc[22 : 22 + nlen * 2].decode("utf-16le").replace("\\", "/")
            elif stag == b"segm":
                sp = 0
                while sp < len(sc):
                    segs.append(struct.unpack_from("<IQQQ", sc, sp))
                    sp += 28
        if fname is not None:
            out = bytearray()
            for sflag, soff, _sosz, szsz in segs:
                segdata = data[idx + soff : idx + soff + szsz]
                if sflag & 7:
                    segdata = zlib.decompress(segdata)
                out.extend(segdata)
            files[fname] = bytes(out)
    return files


ATTR_RE = re.compile(r'([A-Za-z0-9_]+)(?:\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s\]]+)))?')


def parse_attrs(attr_str: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for m in ATTR_RE.finditer(attr_str):
        k = m.group(1).lower()
        if m.group(2) is not None:
            v = m.group(2)
        elif m.group(3) is not None:
            v = m.group(3)
        elif m.group(4) is not None:
            v = m.group(4)
        else:
            v = "true"
        attrs[k] = v
    return attrs


def sanitize_ident(s: str) -> str:
    s = s.lstrip("*").strip().lower().replace("-", "__dash__")
    s = re.sub(r"[^a-z0-9_]", "_", s)
    return s or "entry"


def file_stem(ks_name: str) -> str:
    return Path(ks_name).stem.lower()


def kag_label_name(stem: str, target: str) -> str:
    return f"kag_{sanitize_ident(stem)}_{sanitize_ident(target)}"


def safe_int(val: object, default: int = 0) -> int:
    if val is None:
        return default
    m = re.match(r"[-+]?\d+", str(val).strip())
    return int(m.group(0)) if m else default


def tjs_to_py(expr: str) -> str:
    s = expr.strip()
    if s.startswith("&"):
        s = s[1:].strip()
    # Fix known original script typo *ture_0 -> *true_0
    s = s.replace("*ture_0", "*true_0")
    s = s.replace("WaveSoundBuffer.freeDirectSound()", "kag_noop()")
    s = s.replace("kag.close()", "kag_quit_game()")
    s = s.replace("kag.bgm.currentBuffer.status", "kag_bgm_status()")
    s = s.replace("kag.skipMode", "kag_get_skip_mode()")
    s = s.replace("kag.clickCount", "kag_get_click_count()")
    s = s.replace("intrandom(", "renpy.random.randint(")

    # Protect string literals while rewriting identifiers & operators
    parts = re.split(r"(\"(?:\\.|[^\"])*\"|'(?:\\.|[^'])*')", s)
    out = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            out.append(part)
            continue
        p = part
        p = p.replace("===", "==").replace("!==", "!=")
        p = p.replace("&&", " and ").replace("||", " or ")
        # Negation ! before identifiers or '(' without touching !=
        p = re.sub(r"(?<![=!<>])!\s*(?=[A-Za-z_(])", " not ", p)
        p = re.sub(r"\bsf\.([A-Za-z_][A-Za-z0-9_]*)", r"persistent.\1", p)
        p = re.sub(r"\bf\.([A-Za-z_][A-Za-z0-9_]*)", r"kag_f.\1", p)
        # x++ / x-- -> x += 1 / x -= 1
        p = re.sub(r"\b([A-Za-z_][A-Za-z0-9_\.]*)\s*\+\+", r"\1 += 1", p)
        p = re.sub(r"\b([A-Za-z_][A-Za-z0-9_\.]*)\s*--", r"\1 -= 1", p)
        # void -> None
        p = re.sub(r"\bvoid\b", "None", p)
        # true/false -> True/False
        p = re.sub(r"\btrue\b", "True", p)
        p = re.sub(r"\bfalse\b", "False", p)
        out.append(p)
    res = "".join(out).strip()
    # Convert TJS string.length -> len(string)
    res = re.sub(r"\b((?:kag_f|persistent)\.[A-Za-z_][A-Za-z0-9_]*)\.length\b", r"len(\1)", res)
    # Coerce string + int concatenation like '*false_0'+renpy.random.randint(1,3) or '*choices_p'+kag_f.c_num
    res = re.sub(
        r"((?:'[^']*'|\"[^\"]*\")\s*\+\s*)(renpy\.random\.randint\([^)]+\)|kag_f\.[A-Za-z_][A-Za-z0-9_]*)",
        lambda m: m.group(1) + "str(" + m.group(2) + ")",
        res,
    )
    # Map kag.clickCount assignment case
    if res.startswith("kag_get_click_count()="):
        res = "kag_click_count = " + res.split("=", 1)[1].strip()
    return res


def escape_renpy_str(s: str) -> str:
    # Escape backslashes, double quotes, %, [ (for Ren'Py interpolation unless already intentional), { unless tag
    # Note: raw dialogue text uses literal [ unless emb, so escape [, %, quotes
    out = s.replace("\\", "\\\\").replace('"', '\\"')
    return out


def escape_renpy_text(s: str) -> str:
    # Preserve nothing raw as [ or { — escape [, {, %, quotes; Ren'Py tags will be added AFTER escaping chunks
    return (
        s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("{", "{{")
        .replace("[", "[[")
        .replace("%", "%%")
    )


def tjs_color_to_hex(val: str) -> str:
    v = val.strip().lower()
    if v.startswith("0x"):
        v = v[2:]
    elif v.startswith("#"):
        v = v[1:]
    v = re.sub(r"[^0-9a-f]", "", v)
    if len(v) == 6:
        return "#" + v
    if len(v) == 8:
        return "#" + v[2:]
    return "#ffffff"


class Transpiler:
    def __init__(self, ks_name: str, text: str, all_stems: set[str]):
        self.ks_name = ks_name
        self.stem = file_stem(ks_name)
        self.text = text.replace("\r\n", "\n").replace("\r", "\n")
        self.all_stems = all_stems
        self.labels_seen: list[str] = []
        self.emitted_renpy_labels: set[str] = set()
        self.lines_out: list[str] = []
        self.if_stack: list[int] = []  # track statement count per open if/elif/else suite
        self.cur_text: list[str] = []
        self.has_indent_flag = False
        self.say_in_box = False
        self.in_link = False
        self.link_attrs: dict[str, str] = {}
        self.link_text: list[str] = []
        self.link_locate: tuple[int | None, int | None] = (None, None)
        self.link_font_color: str | None = None
        self.link_font_size: int | None = None
        self.open_font_colors = 0
        self.open_font_sizes = 0
        self.pending_locate: tuple[int | None, int | None] = (None, None)
        self.in_choices = False
        self.current_renpy_label: str = ""

    def indent_prefix(self) -> str:
        return "    " * (1 + len(self.if_stack))

    def emit(self, line: str) -> None:
        if self.if_stack:
            self.if_stack[-1] += 1
        self.lines_out.append(self.indent_prefix() + line)

    def resolve_jump_args(self, attrs: dict[str, str]) -> tuple[str | None, str | None]:
        storage = attrs.get("storage")
        target = attrs.get("target")
        if storage is not None and storage.startswith("&"):
            s_expr = tjs_to_py(storage)
        elif storage is not None:
            s_expr = repr(file_stem(storage))
        else:
            s_expr = None

        if target is not None and target.startswith("&"):
            t_expr = tjs_to_py(target)
        elif target is not None:
            t_expr = repr(target)
        else:
            t_expr = None
        return s_expr, t_expr

    def is_static_jump(self, attrs: dict[str, str]) -> str | None:
        storage = attrs.get("storage")
        target = attrs.get("target")
        if (storage and storage.startswith("&")) or (target and target.startswith("&")):
            return None
        tgt_stem = file_stem(storage) if storage else self.stem
        if tgt_stem not in self.all_stems and not storage:
            tgt_stem = self.stem
        if target:
            return kag_label_name(tgt_stem, target)
        return f"kag_{sanitize_ident(tgt_stem)}"

    def close_open_font_tags(self) -> None:
        while self.open_font_colors > 0:
            self.cur_text.append("{/color}")
            self.open_font_colors -= 1
        while self.open_font_sizes > 0:
            self.cur_text.append("{/size}")
            self.open_font_sizes -= 1

    def flush_dialogue(self, auto_continue: bool = True, clear_after: bool = False) -> None:
        if not self.cur_text:
            return
        self.close_open_font_tags()
        raw = "".join(self.cur_text).strip("\n")
        self.cur_text.clear()
        # Drop pure whitespace strings unless explicit pause
        if not raw.strip(" 　\t"):
            self.has_indent_flag = False
            if clear_after:
                self.say_in_box = False
            return

        payload = raw + ("{nw}" if auto_continue else "")
        if self.has_indent_flag and "「" in payload and not self.say_in_box:
            # Measure prefix before first 「 for exact hanging indent in screen say
            prefix_candidate = payload.split("「", 1)[0]
            # Remove Ren'Py tags from prefix measurement
            clean_pref = re.sub(r"\{[^{}]*\}", "", prefix_candidate) + "「"
            self.emit(f"$ kag_set_next_indent({clean_pref!r})")
        self.has_indent_flag = False

        if self.say_in_box:
            self.emit(f'extend "{payload}"')
        else:
            self.emit(f'"{payload}"')
            self.say_in_box = True

        if clear_after:
            self.say_in_box = False

    def handle_tag(self, name: str, attr_str: str, has_following_text: bool) -> None:
        t = name.lower()
        attrs = parse_attrs(attr_str)
        cond_expr = attrs.get("cond")
        cond_py = tjs_to_py(cond_expr) if cond_expr else None

        def wrap_cond(stmt: str) -> None:
            if cond_py:
                self.emit(f"if {cond_py}:")
                self.emit("    " + stmt)
            else:
                self.emit(stmt)

        # Control flow
        if t == "if":
            self.flush_dialogue(auto_continue=True)
            exp = tjs_to_py(attrs.get("exp", "False"))
            self.lines_out.append(self.indent_prefix() + f"if {exp}:")
            self.if_stack.append(0)
            return
        if t == "elsif":
            self.flush_dialogue(auto_continue=True)
            if self.if_stack:
                if self.if_stack[-1] == 0:
                    self.emit("pass")
                self.if_stack.pop()
            exp = tjs_to_py(attrs.get("exp", "False"))
            self.lines_out.append(self.indent_prefix() + f"elif {exp}:")
            self.if_stack.append(0)
            return
        if t == "else":
            self.flush_dialogue(auto_continue=True)
            if self.if_stack:
                if self.if_stack[-1] == 0:
                    self.emit("pass")
                self.if_stack.pop()
            self.lines_out.append(self.indent_prefix() + "else:")
            self.if_stack.append(0)
            return
        if t == "endif":
            self.flush_dialogue(auto_continue=True)
            if self.if_stack:
                if self.if_stack[-1] == 0:
                    self.emit("pass")
                self.if_stack.pop()
            return

        # Inside [link] ... [endlink]
        if self.in_link:
            if t == "endlink":
                self.in_link = False
                caption = "".join(self.link_text).strip()
                # Keep fullwidth padding trimmed inside choice cards when not located, or preserve raw caption
                clean_cap = caption.rstrip("　 ") if not self.pending_locate[0] and not self.link_locate[0] else caption.rstrip("　 ")
                if not clean_cap:
                    clean_cap = caption
                lx = self.link_locate[0] if self.link_locate[0] is not None else self.pending_locate[0]
                ly = self.link_locate[1] if self.link_locate[1] is not None else self.pending_locate[1]
                self.pending_locate = (None, None)
                s_expr, t_expr = self.resolve_jump_args(self.link_attrs)
                exp_val = self.link_attrs.get("exp")
                exp_py = tjs_to_py(exp_val) if exp_val else None
                c_val = self.link_attrs.get("cond")
                c_py = tjs_to_py(c_val) if c_val else None
                call_stmt = (
                    f"$ kag_add_link({clean_cap!r}, current_stem={self.stem!r}, "
                    f"storage={s_expr}, target={t_expr}, exp={exp_py!r}, "
                    f"x={lx!r}, y={ly!r}, color={self.link_font_color!r}, size={self.link_font_size!r})"
                )
                if c_py:
                    self.emit(f"if {c_py}:")
                    self.emit("    " + call_stmt)
                else:
                    self.emit(call_stmt)
                return
            elif t == "locate":
                x = safe_int(attrs["x"]) if "x" in attrs else self.link_locate[0]
                y = safe_int(attrs["y"]) if "y" in attrs else self.link_locate[1]
                self.link_locate = (x, y)
                return
            elif t == "font":
                if "color" in attrs and attrs["color"].lower() != "default":
                    self.link_font_color = tjs_color_to_hex(attrs["color"])
                elif "color" in attrs and attrs["color"].lower() == "default":
                    pass
                if "size" in attrs and attrs["size"].lower() != "default":
                    self.link_font_size = safe_int(attrs["size"], 24)
                return
            elif t == "r":
                self.link_text.append("\n")
                return
            return

        # Link start
        if t == "link":
            self.flush_dialogue(auto_continue=True)
            self.in_link = True
            self.link_attrs = attrs
            self.link_text = []
            self.link_locate = (None, None)
            self.link_font_color = tjs_color_to_hex(attrs["color"]) if "color" in attrs else None
            self.link_font_size = None
            return

        # Dialogue formatting inline tags
        if t == "indent":
            self.has_indent_flag = True
            return
        if t == "endindent":
            return
        if t == "r":
            if self.cur_text or self.say_in_box:
                self.cur_text.append("\\n")
            return
        if t == "emb":
            exp = tjs_to_py(attrs.get("exp", ""))
            # Convert kag_f.spell -> [kag_f.spell]
            if self.in_link:
                self.link_text.append("[" + exp + "]")
            else:
                self.cur_text.append("[" + exp + "]")
            return
        if t == "font":
            if self.cur_text or has_following_text:
                if "color" in attrs:
                    if attrs["color"].lower() == "default":
                        if self.open_font_colors > 0:
                            self.cur_text.append("{/color}")
                            self.open_font_colors -= 1
                    else:
                        if self.open_font_colors > 0:
                            self.cur_text.append("{/color}")
                            self.open_font_colors -= 1
                        self.cur_text.append("{color=" + tjs_color_to_hex(attrs["color"]) + "}")
                        self.open_font_colors += 1
                if "size" in attrs:
                    if attrs["size"].lower() == "default":
                        if self.open_font_sizes > 0:
                            self.cur_text.append("{/size}")
                            self.open_font_sizes -= 1
                    else:
                        if self.open_font_sizes > 0:
                            self.cur_text.append("{/size}")
                            self.open_font_sizes -= 1
                        self.cur_text.append("{size=" + attrs["size"] + "}")
                        self.open_font_sizes += 1
            return
        if t == "resetfont":
            self.close_open_font_tags()
            return
        if t == "delay":
            # Respect script-requested nowait / user speed outside choices
            return
        if t == "style":
            return

        # Wait tags: inline {w=sec} if inside dialogue line with following text
        if t in ("wait1", "wait2", "wait"):
            ms = safe_int(attrs.get("time", "0"))
            canskip = attrs.get("canskip", "false" if t == "wait2" else "true").lower() != "false"
            if self.cur_text and has_following_text:
                self.cur_text.append(f"{{w={ms / 1000.0:.3g}}}")
            else:
                self.flush_dialogue(auto_continue=True)
                if cond_py:
                    self.emit(f"if {cond_py}:")
                    self.emit(f"    $ kag_wait({ms}, canskip={canskip!r})")
                else:
                    self.emit(f"$ kag_wait({ms}, canskip={canskip!r})")
            return

        # Click waits / page clear
        if t in ("l", "p"):
            if self.cur_text:
                self.flush_dialogue(auto_continue=False, clear_after=False)
            else:
                self.emit("$ kag_waitclick()")
            return
        if t in ("cm", "er", "ct"):
            if self.cur_text:
                self.flush_dialogue(auto_continue=True, clear_after=True)
            self.say_in_box = False
            self.has_indent_flag = False
            self.pending_locate = (None, None)
            self.emit(f"$ kag_{t}()")
            return

        # Before any non-dialogue tag executes, flush any accumulated text with {nw}
        self.flush_dialogue(auto_continue=True)

        if t == "choices":
            self.in_choices = True
            self.say_in_box = False
            self.emit("$ kag_choices_begin()")
        elif t == "endchoices":
            self.in_choices = False
            self.emit("$ kag_choices_end()")
        elif t == "locate":
            lx = safe_int(attrs["x"]) if "x" in attrs else self.pending_locate[0]
            ly = safe_int(attrs["y"]) if "y" in attrs else self.pending_locate[1]
            self.pending_locate = (lx, ly)
        elif t == "button":
            graphic = attrs.get("graphic", "")
            s_expr, t_expr = self.resolve_jump_args(attrs)
            exp_val = attrs.get("exp")
            exp_py = tjs_to_py(exp_val) if exp_val else None
            bx, by = self.pending_locate
            self.pending_locate = (None, None)
            bx = safe_int(attrs["x"]) if "x" in attrs else (bx if bx is not None else 0)
            by = safe_int(attrs["y"]) if "y" in attrs else (by if by is not None else 0)
            wrap_cond(
                f"$ kag_add_button({graphic!r}, current_stem={self.stem!r}, storage={s_expr}, "
                f"target={t_expr}, exp={exp_py!r}, x={bx!r}, y={by!r})"
            )
        elif t == "eval":
            exp = tjs_to_py(attrs.get("exp", ""))
            if exp:
                wrap_cond(f"$ {exp}")
        elif t == "input":
            var_name = attrs.get("name", "f.spell")
            if var_name.startswith("f."):
                var_name = var_name[2:]
            prompt = attrs.get("prompt", "")
            title = attrs.get("title", "")
            self.emit(f"$ kag_input({var_name!r}, prompt={prompt!r}, title={title!r})")
        elif t == "jump":
            static_lbl = self.is_static_jump(attrs)
            if static_lbl:
                # Start Game enters prologue first; prologue end/skip enters part_a
                if self.current_renpy_label == "kag_menu_newgame" and static_lbl == "kag_part_a_gamestart":
                    static_lbl = "kag_prologue_gamestart"
                elif self.current_renpy_label == "kag_prologue_quit" and static_lbl == "kag_menu_gamestart":
                    static_lbl = "kag_part_a_gamestart"
                if cond_py:
                    self.emit(f"if {cond_py}:")
                    self.emit(f"    jump {static_lbl}")
                else:
                    self.emit(f"jump {static_lbl}")
            else:
                s_expr, t_expr = self.resolve_jump_args(attrs)
                wrap_cond(f"$ kag_jump({self.stem!r}, storage={s_expr}, target={t_expr})")
        elif t == "call":
            storage = attrs.get("storage", "")
            target = attrs.get("target", "")
            if "plug_rclick" in storage.lower():
                wrap_cond("call kag_open_rclick_menu")
            else:
                static_lbl = self.is_static_jump(attrs)
                if static_lbl:
                    wrap_cond(f"call {static_lbl}")
        elif t == "s":
            self.emit("call kag_s_wait")
        elif t == "mesframe":
            self.emit("$ kag_mesframe()")
        elif t.startswith("changetype_"):
            ctype = t[len("changetype_") :]
            storage = attrs.get("storage", "")
            time_ms = safe_int(attrs.get("time", "500"), 500)
            bgcolor = attrs.get("bgcolor", "0x000000")
            self.say_in_box = False
            wrap_cond(f"$ kag_changetype({ctype!r}, {storage!r}, time_ms={time_ms}, bgcolor={bgcolor!r})")
        elif t == "drawchar":
            storage = attrs.get("storage", "")
            time_ms = safe_int(attrs.get("time", "300"), 300)
            wrap_cond(f"$ kag_drawchar({storage!r}, time_ms={time_ms}, sepia=False, canskip=True)")
        elif t == "drawchared":
            storage = attrs.get("storage", "")
            time_ms = safe_int(attrs.get("time", "300"), 300)
            wrap_cond(f"$ kag_drawchar({storage!r}, time_ms={time_ms}, sepia=False, canskip=False)")
        elif t == "drawcharsepia":
            storage = attrs.get("storage", "")
            time_ms = safe_int(attrs.get("time", "300"), 300)
            wrap_cond(f"$ kag_drawchar({storage!r}, time_ms={time_ms}, sepia=True, canskip=True)")
        elif t == "bgdraw":
            self.emit("$ kag_bgdraw()")
        elif t == "frmdraw":
            self.emit("$ kag_frmdraw()")
        elif t == "image":
            storage = attrs.get("storage", "")
            layer = str(attrs.get("layer", "base")).lower()
            page = attrs.get("page", "fore").lower()
            left = safe_int(attrs["left"]) if "left" in attrs else 0
            top = safe_int(attrs["top"]) if "top" in attrs else 0
            visible = attrs.get("visible", "true").lower() != "false"
            sepia = attrs.get("grayscale", "false").lower() == "true"
            wrap_cond(f"$ kag_image({storage!r}, layer={layer!r}, page={page!r}, left={left}, top={top}, visible={visible!r}, sepia={sepia!r})")
        elif t == "freeimage":
            layer = str(attrs.get("layer", "0")).lower()
            page = attrs.get("page", "fore").lower()
            wrap_cond(f"$ kag_freeimage(layer={layer!r}, page={page!r})")
        elif t == "trans":
            time_ms = safe_int(attrs.get("time", "500"), 500)
            method = attrs.get("method", "").lower()
            rule = attrs.get("rule", "")
            vague = safe_int(attrs.get("vague", "64"), 64)
            wrap_cond(f"$ kag_trans(time_ms={time_ms}, method={method!r}, rule={rule!r}, vague={vague})")
        elif t == "wt":
            canskip = attrs.get("canskip", "true").lower() != "false"
            self.emit(f"$ kag_wt(canskip={canskip!r})")
        elif t == "cwt":
            self.emit("$ kag_cwt()")
        elif t == "stoptrans":
            self.emit("$ kag_stoptrans()")
        elif t == "quake":
            time_ms = safe_int(attrs.get("time", "500"), 500)
            vmax = safe_int(attrs.get("vmax", "10"), 10)
            hmax = safe_int(attrs.get("hmax", "10"), 10)
            self.emit(f"$ kag_quake(time_ms={time_ms}, hmax={hmax}, vmax={vmax})")
        elif t == "playbgm":
            storage = attrs.get("storage", "")
            loop = attrs.get("loop", "true").lower() != "false"
            wrap_cond(f"$ kag_playbgm({storage!r}, loop={loop!r})")
        elif t == "stopbgm":
            wrap_cond("$ kag_stopbgm()")
        elif t == "pausebgm":
            self.emit("$ kag_pausebgm()")
        elif t == "resumebgm":
            self.emit("$ kag_resumebgm()")
        elif t == "fadeoutbgm":
            time_ms = safe_int(attrs.get("time", "1000"), 1000)
            wrap_cond(f"$ kag_fadeoutbgm({time_ms})")
        elif t == "fadeinbgm":
            storage = attrs.get("storage", "")
            time_ms = safe_int(attrs.get("time", "1000"), 1000)
            wrap_cond(f"$ kag_fadeinbgm({storage!r}, {time_ms})")
        elif t == "bgmopt":
            vol = safe_int(attrs["volume"]) if "volume" in attrs else None
            gvol = safe_int(attrs["gvolume"]) if "gvolume" in attrs else None
            self.emit(f"$ kag_bgmopt(volume={vol!r}, gvolume={gvol!r})")
        elif t == "playse":
            storage = attrs.get("storage", "")
            buf = safe_int(attrs.get("buf", "0"))
            loop = attrs.get("loop", "false").lower() == "true"
            wrap_cond(f"$ kag_playse({storage!r}, buf={buf}, loop={loop!r})")
        elif t == "stopse":
            buf = safe_int(attrs["buf"]) if "buf" in attrs else 0
            wrap_cond(f"$ kag_stopse(buf={buf})")
        elif t == "fadeinse":
            storage = attrs.get("storage", "")
            time_ms = safe_int(attrs.get("time", "500"), 500)
            buf = safe_int(attrs.get("buf", "0"))
            wrap_cond(f"$ kag_fadeinse({storage!r}, time_ms={time_ms}, buf={buf})")
        elif t == "fadeoutse":
            time_ms = safe_int(attrs.get("time", "500"), 500)
            buf = safe_int(attrs.get("buf", "0"))
            wrap_cond(f"$ kag_fadeoutse(time_ms={time_ms}, buf={buf})")
        elif t == "seopt":
            buf = safe_int(attrs.get("buf", "0"))
            vol = safe_int(attrs["volume"]) if "volume" in attrs else None
            gvol = safe_int(attrs["gvolume"]) if "gvolume" in attrs else None
            self.emit(f"$ kag_seopt(buf={buf}, volume={vol!r}, gvolume={gvol!r})")
        elif t == "ws":
            buf = safe_int(attrs.get("buf", "0"))
            canskip = attrs.get("canskip", "true").lower() != "false"
            wrap_cond(f"$ kag_ws(buf={buf}, canskip={canskip!r})")
        elif t == "wl":
            canskip = attrs.get("canskip", "true").lower() != "false"
            self.emit(f"$ kag_wl(canskip={canskip!r})")
        elif t == "sound_se":
            storage = attrs.get("storage", "")
            buf = safe_int(attrs.get("buf", "1"), 1)
            self.emit(f"$ kag_sound_se({storage!r}, buf={buf})")
        elif t == "se_loop":
            storage = attrs.get("storage", "")
            self.emit(f"$ kag_se_loop({storage!r})")
        elif t == "video":
            visible = attrs.get("visible", "true").lower() != "false"
            self.emit(f"$ kag_video_opt(visible={visible!r})")
        elif t == "playvideo":
            storage = attrs.get("storage", "")
            self.emit(f"$ kag_playvideo({storage!r})")
        elif t == "stopvideo":
            self.emit("$ kag_stopvideo()")
        elif t == "wv":
            canskip = attrs.get("canskip", "true").lower() != "false"
            self.emit(f"$ kag_wv(canskip={canskip!r})")
        elif t == "waitclick":
            self.emit("$ kag_waitclick()")
        elif t == "rclick":
            enabled = attrs.get("enabled", "true").lower() != "false"
            self.emit(f"$ kag_set_rclick({enabled!r})")
        elif t == "clickskip":
            enabled = attrs.get("enabled", "true").lower() != "false"
            self.emit(f"$ kag_set_clickskip({enabled!r})")
        elif t == "history":
            output = attrs.get("output")
            enabled = attrs.get("enabled")
            out_arg = "None" if output is None else ("True" if output.lower() != "false" else "False")
            en_arg = "None" if enabled is None else ("True" if enabled.lower() != "false" else "False")
            self.emit(f"$ kag_history_opt(output={out_arg}, enabled={en_arg})")
        elif t == "cancelskip":
            self.emit("$ kag_cancelskip()")
        elif t == "startanchor":
            self.emit("$ kag_startanchor()")
        elif t == "staffrollinit":
            self.emit("$ kag_staffroll_init()")
        elif t == "staffrollstart":
            h = safe_int(attrs.get("height", "3300"), 3300)
            tm = safe_int(attrs.get("time", "10000"), 10000)
            self.emit(f"$ kag_staffroll_start(height={h}, time_ms={tm})")
        elif t == "staffrolluninit":
            self.emit("$ kag_staffroll_uninit()")
        elif t in ("position", "layopt", "laycount", "backlay"):
            if t == "position" and attrs.get("layer", "message0") == "message0":
                left = attrs.get("left")
                top = attrs.get("top")
                width = attrs.get("width")
                height = attrs.get("height")
                opacity = attrs.get("opacity")
                if any(x is not None for x in (left, top, width, height, opacity)):
                    self.emit(
                        f"$ kag_position(left={left!r}, top={top!r}, width={width!r}, height={height!r}, opacity={opacity!r})"
                    )
            elif t == "layopt":
                layer = str(attrs.get("layer", "0")).lower()
                vis = attrs.get("visible")
                if vis is not None:
                    self.emit(f"$ kag_layopt(layer={layer!r}, visible={vis.lower() != 'false'!r})")
            elif t == "backlay":
                self.emit("$ kag_backlay()")
        elif t in ("layerposition_def", "layerposition_use"):
            self.emit(f"$ {t}()")
        else:
            raise ValueError(f"Unhandled KAG tag [{t} {attr_str}] in {self.ks_name}")

    def transpile(self) -> tuple[str, list[str]]:
        raw_lines = self.text.split("\n")
        self.lines_out.append(f"# Auto-generated from {self.ks_name} by tools/transpile_ks.py")
        top_label = f"kag_{sanitize_ident(self.stem)}"
        self.lines_out.append(f"label {top_label}:")

        in_iscript = False
        iscript_buf: list[str] = []
        emitted_first_label = False

        for line in raw_lines:
            stripped = line.strip()
            if in_iscript:
                if stripped.lower().startswith("[endscript]"):
                    in_iscript = False
                    code = "\n".join(iscript_buf).strip()
                    iscript_buf.clear()
                    for cl in code.splitlines():
                        cl = cl.strip().rstrip(";")
                        if cl:
                            self.emit(f"$ {tjs_to_py(cl)}")
                else:
                    iscript_buf.append(line)
                continue

            if not stripped or stripped.startswith(";"):
                continue

            # Check @command line (only @staffrollinit/start/uninit)
            if stripped.startswith("@"):
                parts = stripped[1:].strip().split(None, 1)
                tname = parts[0]
                tattrs = parts[1] if len(parts) > 1 else ""
                if tname.lower() == "iscript":
                    in_iscript = True
                    continue
                self.handle_tag(tname, tattrs, has_following_text=False)
                continue

            # Check *label line
            if stripped.startswith("*"):
                self.flush_dialogue(auto_continue=True)
                while self.if_stack:
                    if self.if_stack[-1] == 0:
                        self.emit("pass")
                    self.if_stack.pop()
                self.say_in_box = False
                self.has_indent_flag = False
                if "|" in stripped:
                    lbl_raw, bookmark = stripped[1:].split("|", 1)
                    bookmark = bookmark.strip()
                else:
                    lbl_raw, bookmark = stripped[1:], ""
                lbl_name = kag_label_name(self.stem, lbl_raw)
                self.current_renpy_label = lbl_name
                # Avoid duplicate label emissions when original .ks repeats an unreferenced saveable bookmark label
                if not emitted_first_label:
                    emitted_first_label = True
                if lbl_name not in self.emitted_renpy_labels:
                    self.emitted_renpy_labels.add(lbl_name)
                    self.labels_seen.append(lbl_raw.strip().lower())
                    self.lines_out.append(f"\nlabel {lbl_name}:")
                    if lbl_name == "kag_menu_gamestart":
                        self.emit("if kag_in_boot_splash:")
                        self.emit("    $ kag_in_boot_splash = False")
                        self.emit("    return")
                    elif lbl_name == "kag_prologue_gamestart" and not bookmark:
                        self.emit("$ kag_set_bookmark('プロローグ\\u3000\\u3000魔女界編')")
                    elif lbl_name == "kag_prologue_prologue":
                        self.emit("if kag_f.re_scenario==0:")
                        self.emit("    $ kag_set_rclick(True)")
                        self.emit("    $ kag_set_clickskip(True)")
                if bookmark:
                    self.emit(f"$ kag_set_bookmark({bookmark!r})")
                continue

            # Normal script/text line — remove trailing KAG '\'
            work = stripped
            if work.endswith("\\"):
                work = work[:-1]

            # Tokenize tags vs text on this line
            pos = 0
            n = len(work)
            tokens: list[tuple[str, str, str]] = []  # ("tag", name, attrs) or ("text", raw, "")
            while pos < n:
                idx = work.find("[", pos)
                if idx == -1:
                    txt = work[pos:]
                    if txt:
                        tokens.append(("text", txt, ""))
                    break
                if idx > pos:
                    tokens.append(("text", work[pos:idx], ""))
                # Find matching closing ']' respecting quotes
                end = idx + 1
                quote = None
                while end < n:
                    ch = work[end]
                    if quote:
                        if ch == quote:
                            quote = None
                    else:
                        if ch in ('"', "'"):
                            quote = ch
                        elif ch == "]":
                            break
                    end += 1
                if end >= n:
                    # Unclosed bracket -> treat as text
                    tokens.append(("text", work[idx:], ""))
                    break
                inner = work[idx + 1 : end].strip()
                if inner:
                    sp = re.split(r"\s+", inner, maxsplit=1)
                    tname = sp[0]
                    tattrs = sp[1] if len(sp) > 1 else ""
                    if tname.lower() == "iscript":
                        in_iscript = True
                    elif tname.lower() == "endfif":
                        tname = "endif"
                    tokens.append(("tag", tname, tattrs))
                pos = end + 1

            for idx_tok, (kind, a, b) in enumerate(tokens):
                if kind == "text":
                    if self.in_link:
                        self.link_text.append(a)
                    else:
                        self.cur_text.append(escape_renpy_text(a))
                else:
                    if a.lower() == "iscript":
                        continue
                    # Check whether meaningful text or inline formatting follows later on this line (or before clear)
                    has_more_text = any(
                        (tk == "text" and ta.strip())
                        or (tk == "tag" and ta.lower() in ("emb", "r", "font", "indent", "endindent"))
                        for tk, ta, _ in tokens[idx_tok + 1 :]
                    )
                    self.handle_tag(a, b, has_following_text=has_more_text)

        self.flush_dialogue(auto_continue=False)
        while self.if_stack:
            if self.if_stack[-1] == 0:
                self.emit("pass")
            self.if_stack.pop()
        self.emit("return")
        return "\n".join(self.lines_out) + "\n", self.labels_seen


def main() -> None:
    SCENARIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Remove any old stale .rpy in scenario/
    for old in SCENARIO_OUT_DIR.glob("*.rpy"):
        old.unlink()

    scen_files = parse_xp3(cab_read("scenario.xp3"))
    if PATCH_XP3_PATH.exists():
        patch_files = parse_xp3(PATCH_XP3_PATH.read_bytes())
        scen_files.update(patch_files)

    ks_entries = {
        k: v
        for k, v in sorted(scen_files.items())
        if k.lower().endswith(".ks") and Path(k).name.lower() != "first.ks"
    }
    stems = {file_stem(k) for k in ks_entries}
    assert len(stems) == len(ks_entries), "Scenario filename collision detected!"

    all_labels: dict[str, set[str]] = {}
    dialogue_lines = 0

    for ks_name, raw in sorted(ks_entries.items()):
        txt = raw.decode("cp932", errors="replace")
        tr = Transpiler(ks_name, txt, stems)
        rpy_src, labels = tr.transpile()
        stem = file_stem(ks_name)
        all_labels[stem] = set(labels)
        out_path = SCENARIO_OUT_DIR / f"{stem}.rpy"
        out_path.write_text(rpy_src, encoding="utf-8")
        dialogue_lines += sum(1 for l in rpy_src.splitlines() if l.strip().startswith(('"', 'extend "')))

    # Write label registry index for dynamic jumps
    reg_path = SCENARIO_OUT_DIR / "_label_index.rpy"
    with reg_path.open("w", encoding="utf-8") as f:
        f.write("# Auto-generated scenario label index\n\ninit -90 python:\n    KAG_SCENARIO_LABELS = {\n")
        for stem in sorted(all_labels):
            lbls = sorted(all_labels[stem])
            f.write(f"        {stem!r}: {lbls!r},\n")
        f.write("    }\n")

    print(f"Transpiled {len(ks_entries)} .ks scenarios into {SCENARIO_OUT_DIR}")
    print(f"Total Ren'Py dialogue statements emitted: {dialogue_lines}")


if __name__ == "__main__":
    main()
