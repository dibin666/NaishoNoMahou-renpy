#!/usr/bin/env python3
"""
Extracts and converts all assets from Data1.cab + No CD Patch/patch.xp3
into the Ren'Py 8 project structure under renpy_project/game/.
"""

import ctypes
import hashlib
import io
import os
import pprint
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parent.parent
CAB_PATH = ROOT_DIR / "おジャ魔女あどべんちゃ～「ないしょのまほう」" / "Data1.cab"
APP_ICO_PATH = ROOT_DIR / "おジャ魔女あどべんちゃ～「ないしょのまほう」" / "appl.ico"
PATCH_XP3_PATH = ROOT_DIR / "No CD Patch" / "patch.xp3"
LIBTLG5_PATH = Path(__file__).resolve().parent / "libtlg5.so"

GAME_DIR = ROOT_DIR / "renpy_project" / "game"
IMAGES_DIR = GAME_DIR / "images"
AUDIO_DIR = GAME_DIR / "audio"
VIDEO_DIR = GAME_DIR / "video"
FONTS_DIR = GAME_DIR / "fonts"
GUI_DIR = GAME_DIR / "gui"

SYSTEM_FONTS = [
    Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
    Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"),
]

# Load C TLG5.0 decoder (compile from tlg5_fast.c on first run if needed)
if not LIBTLG5_PATH.exists():
    subprocess.run(
        ["gcc", "-O3", "-shared", "-fPIC", str(LIBTLG5_PATH.with_name("tlg5_fast.c")), "-o", str(LIBTLG5_PATH)],
        check=True,
    )
libtlg5 = ctypes.CDLL(str(LIBTLG5_PATH))
libtlg5.tlg5_get_info.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_size_t),
]
libtlg5.tlg5_get_info.restype = ctypes.c_int
libtlg5.tlg5_decode_rgba.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_void_p,
]
libtlg5.tlg5_decode_rgba.restype = ctypes.c_int


def cab_read(filename: str) -> bytes:
    cmd = ["cabextract", "-p", "-F", filename, str(CAB_PATH)]
    return subprocess.check_output(cmd)


def parse_xp3(data: bytes) -> dict[str, bytes]:
    magic = b"XP3\r\n \n\x1a\x8b\x67\x01"
    idx = data.find(magic)
    if idx == -1:
        raise ValueError("XP3 signature not found")
    table_off = struct.unpack_from("<Q", data, idx + 11)[0]
    pos = idx + table_off
    flags = data[pos]
    pos += 1
    if flags & 1:
        zsize, _osize = struct.unpack_from("<QQ", data, pos)
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


def decode_tlg5(raw: bytes) -> Image.Image:
    w = ctypes.c_int()
    h = ctypes.c_int()
    c = ctypes.c_int()
    off = ctypes.c_size_t()
    buf = ctypes.create_string_buffer(raw, len(raw))
    rc = libtlg5.tlg5_get_info(buf, len(raw), ctypes.byref(w), ctypes.byref(h), ctypes.byref(c), ctypes.byref(off))
    if rc != 0:
        raise RuntimeError(f"tlg5_get_info failed rc={rc}")
    out_buf = (ctypes.c_uint8 * (w.value * h.value * 4))()
    rc2 = libtlg5.tlg5_decode_rgba(buf, len(raw), out_buf)
    if rc2 != 0:
        raise RuntimeError(f"tlg5_decode_rgba failed rc={rc2}")
    return Image.frombuffer("RGBA", (w.value, h.value), bytes(out_buf), "raw", "RGBA", 0, 1).copy()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def ascii_safe_part(part: str, is_file: bool = False) -> str:
    if part.isascii():
        return part
    if is_file:
        p = Path(part)
        stem, suf = p.stem, p.suffix
    else:
        stem, suf = part, ""
    keep = "".join(c if (c.isascii() and (c.isalnum() or c in "-_. ")) else "" for c in stem).strip(" ._-")
    digest = hashlib.sha256(part.encode("utf-8")).hexdigest()[:10]
    base = f"{keep}_{digest}" if keep else f"u_{digest}"
    return f"{base}{suf}"


def ascii_safe_relpath(rel_path: Path | str) -> Path:
    parts = list(Path(rel_path).parts)
    if not parts:
        return Path(rel_path)
    out = [ascii_safe_part(p, is_file=(i == len(parts) - 1)) for i, p in enumerate(parts)]
    return Path(*out)


def _otf_checksum(data: bytes) -> int:
    pad = (4 - len(data) % 4) % 4
    padded = data + b"\x00" * pad
    vals = struct.unpack(f">{len(padded) // 4}I", padded)
    return sum(vals) & 0xFFFFFFFF


def extract_ttc_face(ttc_bytes: bytes, face_idx: int) -> bytes:
    """Extracts a single standalone OpenType (.otf) face from a .ttc collection."""
    magic, _ver, num_fonts = struct.unpack_from(">4sII", ttc_bytes, 0)
    if magic != b"ttcf" or face_idx >= num_fonts:
        raise ValueError(f"Invalid TTC face {face_idx} (num_fonts={num_fonts})")
    face_off = struct.unpack_from(">I", ttc_bytes, 12 + 4 * face_idx)[0]
    sfnt_ver, num_tables, sr, es, rs = struct.unpack_from(">4sHHHH", ttc_bytes, face_off)
    tables = []
    for i in range(num_tables):
        tag, _csum, off, length = struct.unpack_from(">4sIII", ttc_bytes, face_off + 12 + i * 16)
        tables.append((tag, ttc_bytes[off : off + length]))
    tables.sort(key=lambda x: x[0])
    header_size = 12 + 16 * num_tables
    out = bytearray(header_size)
    struct.pack_into(">4sHHHH", out, 0, sfnt_ver, num_tables, sr, es, rs)
    cur_off = header_size
    head_pos = None
    for idx, (tag, tdata) in enumerate(tables):
        if tag == b"head":
            buf = bytearray(tdata)
            struct.pack_into(">I", buf, 8, 0)
            tdata = bytes(buf)
            head_pos = cur_off
        csum = _otf_checksum(tdata)
        struct.pack_into(">4sIII", out, 12 + idx * 16, tag, csum, cur_off, len(tdata))
        pad = (4 - len(tdata) % 4) % 4
        out.extend(tdata)
        out.extend(b"\x00" * pad)
        cur_off += len(tdata) + pad
    if head_pos is not None:
        whole_csum = (0xB1B0AFBA - _otf_checksum(bytes(out))) & 0xFFFFFFFF
        struct.pack_into(">I", out, head_pos + 8, whole_csum)
    return bytes(out)


def write_png(img: Image.Image, dest: Path) -> None:
    ensure_parent(dest)
    img.save(dest, format="PNG")


def slice_horizontal(img: Image.Image, states: int, out_dir: Path, stem: str) -> tuple[str, ...]:
    w, h = img.size
    if w % states != 0:
        raise ValueError(f"Cannot slice {stem} ({w}x{h}) cleanly into {states} states")
    fw = w // states
    names = ["idle", "down", "hover", "focus"][:states]
    rel_paths = []
    for i, sname in enumerate(names):
        crop = img.crop((i * fw, 0, (i + 1) * fw, h))
        dest = out_dir / f"{stem}_{sname}.png"
        write_png(crop, dest)
        rel_paths.append(dest.relative_to(GAME_DIR).as_posix())
    return tuple(rel_paths)


def register_asset(mapping: dict[str, str], conflicts: dict[str, list[str]], key: str, value: str, overwrite_priority: bool = True) -> None:
    k = key.lower().replace("\\", "/")
    if k in mapping and mapping[k] != value:
        conflicts.setdefault(k, [mapping[k]])
        if value not in conflicts[k]:
            conflicts[k].append(value)
        if not overwrite_priority:
            return
    mapping[k] = value


def is_dummy_file(name: str) -> bool:
    return "削除してかまいません" in name


def main() -> None:
    for d in (IMAGES_DIR, AUDIO_DIR, VIDEO_DIR, FONTS_DIR, GUI_DIR):
        d.mkdir(parents=True, exist_ok=True)

    image_map: dict[str, str] = {}
    image_conflicts: dict[str, list[str]] = {}
    button_states: dict[str, tuple[str, ...]] = {}
    rule_map: dict[str, str] = {}
    bgm_map: dict[str, str] = {}
    bgm_conflicts: dict[str, list[str]] = {}
    se_map: dict[str, str] = {}
    se_conflicts: dict[str, list[str]] = {}

    four_state_btns = {
        "btn_rclick_backtitle",
        "btn_rclick_cancel",
        "btn_rclick_gamestop",
        "btn_rclick_load",
        "btn_rclick_msgclr",
        "btn_rclick_msgskip",
        "btn_rclick_save",
        "btn_saveload_back",
    }
    three_state_btns = {
        "album_btn_01",
        "album_btn_02",
        "album_btn_03",
        "album_btn_04",
        "album_btn_05",
        "album_btn_06",
        "album_btn_07",
        "album_btn_back",
        "main_btn_end",
        "main_btn_gameload",
        "main_btn_newgame",
        "main_btn_option",
        "option_btn_album",
        "option_btn_back",
        "option_btn_memorial",
        "title_load",
        "title_save",
    }

    tlg_count = 0
    other_img_count = 0

    print("[1/7] Extracting image.xp3 (UI graphics & button slices)...")
    img_xp3 = parse_xp3(cab_read("image.xp3"))
    for name, raw in sorted(img_xp3.items()):
        if is_dummy_file(name):
            continue
        p_obj = Path(name)
        stem = p_obj.stem
        if p_obj.suffix.lower() == ".tlg":
            img = decode_tlg5(raw)
            tlg_count += 1
            dest = IMAGES_DIR / "ui" / ascii_safe_relpath(p_obj.with_suffix(".png"))
            write_png(img, dest)
            rel = dest.relative_to(GAME_DIR).as_posix()
            register_asset(image_map, image_conflicts, name, rel)
            register_asset(image_map, image_conflicts, p_obj.with_suffix("").as_posix(), rel)
            register_asset(image_map, image_conflicts, stem, rel)

            low_stem = stem.lower()
            if low_stem in four_state_btns:
                button_states[low_stem] = slice_horizontal(img, 4, IMAGES_DIR / "ui" / "slices", stem)
            elif low_stem in three_state_btns:
                button_states[low_stem] = slice_horizontal(img, 3, IMAGES_DIR / "ui" / "slices", stem)
        else:
            dest = IMAGES_DIR / "ui" / ascii_safe_relpath(name)
            ensure_parent(dest)
            dest.write_bytes(raw)
            other_img_count += 1
            rel = dest.relative_to(GAME_DIR).as_posix()
            register_asset(image_map, image_conflicts, name, rel)
            register_asset(image_map, image_conflicts, stem, rel)

    print("[2/7] Extracting fgimage.xp3 (characters, events, cgmode thumbnails)...")
    fg_xp3 = parse_xp3(cab_read("fgimage.xp3"))
    for name, raw in sorted(fg_xp3.items()):
        if is_dummy_file(name):
            continue
        p_obj = Path(name)
        stem = p_obj.stem
        if p_obj.suffix.lower() == ".tlg":
            img = decode_tlg5(raw)
            tlg_count += 1
            rel_noext = p_obj.with_suffix("").as_posix()
            dest = IMAGES_DIR / "fg" / ascii_safe_relpath(p_obj.with_suffix(".png"))
            write_png(img, dest)
            rel = dest.relative_to(GAME_DIR).as_posix()
            register_asset(image_map, image_conflicts, name, rel)
            register_asset(image_map, image_conflicts, rel_noext, rel)
            register_asset(image_map, image_conflicts, p_obj.name, rel)
            register_asset(image_map, image_conflicts, stem, rel)

            if name.lower().startswith("cgmode/") and img.size[0] % 3 == 0:
                button_states[stem.lower()] = slice_horizontal(img, 3, IMAGES_DIR / "ui" / "cg_slices", stem)

    print("[3/7] Extracting bgimage.xp3 (backgrounds, frames, eyecatch, endrolls)...")
    bg_xp3 = parse_xp3(cab_read("bgimage.xp3"))
    for name, raw in sorted(bg_xp3.items()):
        if is_dummy_file(name):
            continue
        p_obj = Path(name)
        stem = p_obj.stem
        ext = p_obj.suffix.lower()
        rel_noext = p_obj.with_suffix("").as_posix()
        if ext == ".tlg":
            img = decode_tlg5(raw)
            tlg_count += 1
            dest = IMAGES_DIR / "bg" / ascii_safe_relpath(p_obj.with_suffix(".png"))
            write_png(img, dest)
        elif ext in (".png", ".jpg", ".jpeg", ".bmp"):
            dest = IMAGES_DIR / "bg" / ascii_safe_relpath(name)
            ensure_parent(dest)
            dest.write_bytes(raw)
            other_img_count += 1
        else:
            continue
        rel = dest.relative_to(GAME_DIR).as_posix()
        register_asset(image_map, image_conflicts, name, rel)
        register_asset(image_map, image_conflicts, rel_noext, rel)
        register_asset(image_map, image_conflicts, p_obj.name, rel)
        register_asset(image_map, image_conflicts, stem, rel)

    print("[4/7] Extracting system.xp3 & New_File (cursors, rule masks, icon, fonts)...")
    sys_xp3 = parse_xp3(cab_read("system.xp3"))
    for fn in ("LineBreak.png", "pageBreak.png", "check.png"):
        if fn in sys_xp3:
            dest = IMAGES_DIR / "ui" / fn
            ensure_parent(dest)
            dest.write_bytes(sys_xp3[fn])
            other_img_count += 1
            register_asset(image_map, image_conflicts, fn, dest.relative_to(GAME_DIR).as_posix())
            register_asset(image_map, image_conflicts, Path(fn).stem, dest.relative_to(GAME_DIR).as_posix())

    if "LineBreak_a.png" in sys_xp3:
        lb_img = Image.open(io.BytesIO(sys_xp3["LineBreak_a.png"])).convert("RGBA")
        # 270x24 -> 15 frames of 18x24
        fw = 18
        n_frames = lb_img.width // fw
        for i in range(n_frames):
            write_png(lb_img.crop((i * fw, 0, (i + 1) * fw, lb_img.height)), IMAGES_DIR / "ui" / f"linebreak_f{i:02d}.png")

    if "pageBreak_a.png" in sys_xp3:
        pb_img = Image.open(io.BytesIO(sys_xp3["pageBreak_a.png"])).convert("RGBA")
        # 288x24 -> 12 frames of 24x24
        fw = 24
        n_frames = pb_img.width // fw
        for i in range(n_frames):
            write_png(pb_img.crop((i * fw, 0, (i + 1) * fw, pb_img.height)), IMAGES_DIR / "ui" / f"pagebreak_f{i:02d}.png")

    if "infoI.png" in sys_xp3 and "infoI_m.png" in sys_xp3:
        info_rgb = Image.open(io.BytesIO(sys_xp3["infoI.png"])).convert("RGBA")
        info_mask = Image.open(io.BytesIO(sys_xp3["infoI_m.png"])).convert("L")
        info_rgb.putalpha(info_mask)
        write_png(info_rgb, IMAGES_DIR / "ui" / "infoI.png")
        register_asset(image_map, image_conflicts, "infoi", "images/ui/infoI.png")
        register_asset(image_map, image_conflicts, "infoi.png", "images/ui/infoI.png")

    new_file_xp3 = parse_xp3(cab_read("New_File"))
    for name, raw in sorted(new_file_xp3.items()):
        low = name.lower()
        if low.startswith("rule/") and low.endswith(".png"):
            p_obj = Path(name)
            dest = IMAGES_DIR / "rule" / p_obj.name
            ensure_parent(dest)
            dest.write_bytes(raw)
            rel = dest.relative_to(GAME_DIR).as_posix()
            rule_map[p_obj.stem.lower()] = rel
            rule_map[p_obj.name.lower()] = rel
            rule_map[low] = rel

    # Icon
    if APP_ICO_PATH.exists():
        shutil.copy2(APP_ICO_PATH, GUI_DIR / "icon.ico")
        ico = Image.open(APP_ICO_PATH)
        # Pick largest frame from ico if multi-size
        best = ico.convert("RGBA")
        if hasattr(ico, "info") and "sizes" in ico.info:
            max_sz = max(ico.info["sizes"])
            ico.size = max_sz
            best = ico.convert("RGBA")
        write_png(best, GUI_DIR / "window_icon.png")

    # Fonts (extract standalone ASCII .otf faces from system NotoSansCJK TTCs so Ren'Py lint and FreeType work without N@)
    for old_ttc in FONTS_DIR.glob("*.ttc"):
        old_ttc.unlink()
    font_specs = [
        (SYSTEM_FONTS[0], 0, "NotoSansCJKjp-Regular.otf"),
        (SYSTEM_FONTS[0], 2, "NotoSansCJKsc-Regular.otf"),
        (SYSTEM_FONTS[0], 5, "NotoSansMonoCJKjp-Regular.otf"),
        (SYSTEM_FONTS[0], 7, "NotoSansMonoCJKsc-Regular.otf"),
        (SYSTEM_FONTS[1], 0, "NotoSansCJKjp-Bold.otf"),
        (SYSTEM_FONTS[1], 2, "NotoSansCJKsc-Bold.otf"),
        (SYSTEM_FONTS[1], 5, "NotoSansMonoCJKjp-Bold.otf"),
        (SYSTEM_FONTS[1], 7, "NotoSansMonoCJKsc-Bold.otf"),
    ]
    for font_src in SYSTEM_FONTS:
        if not font_src.exists():
            raise FileNotFoundError(f"Required system font missing: {font_src}")
    ttc_cache = {p: p.read_bytes() for p in SYSTEM_FONTS}
    for font_src, face_idx, out_name in font_specs:
        (FONTS_DIR / out_name).write_bytes(extract_ttc_face(ttc_cache[font_src], face_idx))

    print("[5/7] Extracting bgm.xp3 & sound.xp3 (6589 audio files)...")
    bgm_xp3 = parse_xp3(cab_read("bgm.xp3"))
    bgm_count = 0
    for name, raw in sorted(bgm_xp3.items()):
        if is_dummy_file(name):
            continue
        p_obj = Path(name)
        dest = AUDIO_DIR / "bgm" / ascii_safe_relpath(name)
        ensure_parent(dest)
        dest.write_bytes(raw)
        bgm_count += 1
        rel = dest.relative_to(GAME_DIR).as_posix()
        register_asset(bgm_map, bgm_conflicts, name, rel)
        register_asset(bgm_map, bgm_conflicts, p_obj.with_suffix("").as_posix(), rel)
        register_asset(bgm_map, bgm_conflicts, p_obj.stem, rel)
        # Allow [fadeinse]/[playse] to also reference BGM tracks such as bgm-v02/bgm-v03
        register_asset(se_map, se_conflicts, p_obj.stem, rel, overwrite_priority=False)
        register_asset(se_map, se_conflicts, p_obj.name, rel, overwrite_priority=False)

    sound_xp3 = parse_xp3(cab_read("sound.xp3"))
    sound_count = 0
    for name, raw in sorted(sound_xp3.items()):
        if is_dummy_file(name):
            continue
        p_obj = Path(name)
        dest = AUDIO_DIR / "sound" / ascii_safe_relpath(name)
        ensure_parent(dest)
        dest.write_bytes(raw)
        sound_count += 1
        rel = dest.relative_to(GAME_DIR).as_posix()
        register_asset(se_map, se_conflicts, name, rel)
        register_asset(se_map, se_conflicts, p_obj.with_suffix("").as_posix(), rel)
        register_asset(se_map, se_conflicts, p_obj.name, rel)
        register_asset(se_map, se_conflicts, p_obj.stem, rel)
        # Also allow playing sound/11. bgm/* or bgm-v02 via BGM map if not already in bgm.xp3
        if p_obj.stem.lower() not in bgm_map:
            register_asset(bgm_map, bgm_conflicts, p_obj.stem, rel, overwrite_priority=False)
            register_asset(bgm_map, bgm_conflicts, p_obj.name, rel, overwrite_priority=False)

    # Alias known script typos
    if "se-014.1" in se_map:
        bgm_map["se-014"] = se_map["se-014.1"]
        se_map["se-014"] = se_map["se-014.1"]

    print("[6/7] Extracting & converting video.xp3 (OP movie -> WebM)...")
    webm_dest = VIDEO_DIR / "doremi_op.webm"
    if webm_dest.exists() and webm_dest.stat().st_size > 1_000_000 and "--force-video" not in sys.argv:
        print("  Reusing existing video/doremi_op.webm (pass --force-video to re-encode)")
    else:
        vid_xp3 = parse_xp3(cab_read("video.xp3"))
        mpg_bytes = vid_xp3.get("どれみ1015.mpg")
        if mpg_bytes is None:
            raise FileNotFoundError("どれみ1015.mpg not found in video.xp3")
        with tempfile.NamedTemporaryFile(suffix=".mpg") as tmp_mpg:
            tmp_mpg.write(mpg_bytes)
            tmp_mpg.flush()
            subprocess.run(
                [
                    "ffmpeg",
                    "-y",
                    "-i",
                    tmp_mpg.name,
                    "-c:v",
                    "libvpx",
                    "-crf",
                    "16",
                    "-b:v",
                    "1800k",
                    "-deadline",
                    "good",
                    "-cpu-used",
                    "2",
                    "-c:a",
                    "libvorbis",
                    "-q:a",
                    "6",
                    str(webm_dest),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
            )

    video_map = {
        "どれみ1015": "video/doremi_op.webm",
        "どれみ1015.mpg": "video/doremi_op.webm",
        "どれみ1012": "video/doremi_op.webm",
        "どれみ1012.mpg": "video/doremi_op.webm",
    }

    print("[7/7] Writing renpy_project/game/asset_map.rpy...")
    asset_map_path = GAME_DIR / "asset_map.rpy"
    with asset_map_path.open("w", encoding="utf-8") as f:
        f.write("# Auto-generated by tools/extract_and_convert.py — do not edit manually.\n\n")
        f.write("init -100 python:\n")
        f.write("    KAG_IMAGE_MAP = ")
        f.write(pprint.pformat(image_map, width=120, indent=4))
        f.write("\n\n    KAG_BUTTON_STATES = ")
        f.write(pprint.pformat(button_states, width=120, indent=4))
        f.write("\n\n    KAG_RULE_MAP = ")
        f.write(pprint.pformat(rule_map, width=120, indent=4))
        f.write("\n\n    KAG_BGM_MAP = ")
        f.write(pprint.pformat(bgm_map, width=120, indent=4))
        f.write("\n\n    KAG_SE_MAP = ")
        f.write(pprint.pformat(se_map, width=120, indent=4))
        f.write("\n\n    KAG_VIDEO_MAP = ")
        f.write(pprint.pformat(video_map, width=120, indent=4))
        f.write("\n")

    print(
        f"Extraction complete: TLGs decoded={tlg_count}, other images={other_img_count}, "
        f"button slices={len(button_states)}, rules={len(rule_map)//3}, "
        f"bgm={bgm_count}, sound={sound_count}, video={webm_dest.name}"
    )
    if image_conflicts:
        print(f"Image stem conflicts ({len(image_conflicts)}): {list(image_conflicts.items())[:10]}")
    if se_conflicts:
        print(f"SE stem conflicts ({len(se_conflicts)}): {list(se_conflicts.items())[:10]}")


if __name__ == "__main__":
    main()
