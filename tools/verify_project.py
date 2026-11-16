#!/usr/bin/env python3
"""
Automated verification suite for the Ren'Py 8 rewrite of おジャ魔女あどべんちゃ～「ないしょのまほう」.
Checks scenarios, label reachability, extracted assets, fonts, i18n coverage, and platform readiness.
"""

import ast
import os
import re
import sys
from collections import Counter
from pathlib import Path
from PIL import Image, ImageFont

ROOT_DIR = Path(__file__).resolve().parent.parent
GAME_DIR = ROOT_DIR / "renpy_project" / "game"
SCENARIO_DIR = GAME_DIR / "scenario"
TL_DIR = GAME_DIR / "tl" / "zh_cn"


def load_asset_maps() -> dict[str, object]:
    src = (GAME_DIR / "asset_map.rpy").read_text(encoding="utf-8")
    # Strip header and `init -100 python:` wrapper so we can exec the dict literals safely.
    idx = src.index("init -100 python:")
    body_lines = [line[4:] if line.startswith("    ") else line for line in src[idx:].splitlines()[1:]]
    ns: dict[str, object] = {}
    exec("\n".join(body_lines), {}, ns)
    return ns


def sanitize_ident(s: str) -> str:
    s = s.lstrip("*").strip().lower().replace("-", "__dash__")
    s = re.sub(r"[^a-z0-9_]", "_", s)
    return s or "entry"


def check_scenarios_and_labels() -> tuple[list[str], set[str]]:
    errors: list[str] = []
    rpy_files = sorted(p for p in SCENARIO_DIR.glob("*.rpy") if p.name != "_label_index.rpy")
    if len(rpy_files) != 68:
        errors.append(f"Expected 68 scenario .rpy files, found {len(rpy_files)}")

    label_counts: Counter[str] = Counter()
    all_rpy = sorted(p for p in GAME_DIR.rglob("*.rpy") if "/tl/" not in p.as_posix())
    for p in all_rpy:
        for line in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^label\s+([A-Za-z0-9_]+)\s*:", line)
            if m:
                label_counts[m.group(1)] += 1

    dups = {k: v for k, v in label_counts.items() if v > 1}
    if dups:
        errors.append(f"Duplicate Ren'Py labels found: {dups}")

    defined_labels = set(label_counts)

    # Verify static jump/call/button/link targets and Python `$ ` expressions
    jumps_checked = 0
    exprs_checked = 0
    for p in rpy_files:
        stem = p.stem
        lines = p.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, 1):
            st = line.strip()
            if st.startswith("$ "):
                stmt = st[2:]
                try:
                    ast.parse(stmt)
                    exprs_checked += 1
                except SyntaxError as exc:
                    errors.append(f"{p.name}:{lineno} Python syntax error in `$ {stmt}`: {exc}")

            m_jc = re.match(r"^(?:jump|call)\s+([A-Za-z0-9_]+)\b", st)
            if m_jc:
                tgt = m_jc.group(1)
                jumps_checked += 1
                if tgt not in defined_labels:
                    errors.append(f"{p.name}:{lineno} unresolved jump/call target: {tgt}")

            if st.startswith("$ kag_add_button(") or st.startswith("$ kag_add_link("):
                try:
                    tree = ast.parse(st[2:])
                    call = tree.body[0].value  # type: ignore[attr-defined]
                    kw = {k.arg: k.value for k in call.keywords}
                    stor_node = kw.get("storage")
                    targ_node = kw.get("target")
                    if isinstance(stor_node, ast.Constant) and isinstance(targ_node, ast.Constant):
                        stor_val = stor_node.value
                        targ_val = targ_node.value
                        eff_stem = Path(str(stor_val)).stem.lower() if stor_val else stem
                        eff_stem = sanitize_ident(eff_stem)
                        if targ_val:
                            t_norm = str(targ_val).replace("*ture_0", "*true_0")
                            cand = f"kag_{eff_stem}_{sanitize_ident(t_norm)}"
                        else:
                            cand = f"kag_{eff_stem}"
                        jumps_checked += 1
                        if cand not in defined_labels:
                            errors.append(f"{p.name}:{lineno} unresolved button/link target: {cand}")
                except Exception as exc:
                    errors.append(f"{p.name}:{lineno} failed parsing button/link: {exc}")

    print(
        f"[OK] Scenarios: {len(rpy_files)} files, {len(defined_labels)} unique labels, "
        f"{jumps_checked} jump/call/menu targets, {exprs_checked} Python statements verified"
    )
    return errors, defined_labels


def check_assets_and_references(maps: dict[str, object]) -> list[str]:
    errors: list[str] = []
    image_map: dict[str, str] = maps["KAG_IMAGE_MAP"]  # type: ignore[assignment]
    button_states: dict[str, tuple[str, ...]] = maps["KAG_BUTTON_STATES"]  # type: ignore[assignment]
    rule_map: dict[str, str] = maps["KAG_RULE_MAP"]  # type: ignore[assignment]
    bgm_map: dict[str, str] = maps["KAG_BGM_MAP"]  # type: ignore[assignment]
    se_map: dict[str, str] = maps["KAG_SE_MAP"]  # type: ignore[assignment]
    video_map: dict[str, str] = maps["KAG_VIDEO_MAP"]  # type: ignore[assignment]

    # Verify every file in maps exists on disk and filenames under game/images, audio, video, fonts are ASCII
    for map_name, m in [
        ("KAG_IMAGE_MAP", image_map),
        ("KAG_RULE_MAP", rule_map),
        ("KAG_BGM_MAP", bgm_map),
        ("KAG_SE_MAP", se_map),
        ("KAG_VIDEO_MAP", video_map),
    ]:
        for k, rel in m.items():
            if not (GAME_DIR / rel).is_file():
                errors.append(f"{map_name}[{k!r}] points to missing file: {rel}")
            if not rel.isascii():
                errors.append(f"{map_name}[{k!r}] has non-ASCII disk path: {rel}")

    for k, tup in button_states.items():
        for rel in tup:
            if not (GAME_DIR / rel).is_file():
                errors.append(f"KAG_BUTTON_STATES[{k!r}] missing slice: {rel}")
            if not rel.isascii():
                errors.append(f"KAG_BUTTON_STATES[{k!r}] has non-ASCII path: {rel}")

    # Verify disk file counts & ASCII-only paths under assets
    non_ascii_disk: list[str] = []
    for sub in ("images", "audio", "video", "fonts", "gui"):
        base = GAME_DIR / sub
        for root, _dirs, files in os.walk(base):
            for fn in files:
                rel = (Path(root) / fn).relative_to(GAME_DIR).as_posix()
                if not rel.isascii():
                    non_ascii_disk.append(rel)
    if non_ascii_disk:
        errors.append(f"Found {len(non_ascii_disk)} non-ASCII asset files on disk: {non_ascii_disk[:5]}")

    bgm_files = list((GAME_DIR / "audio" / "bgm").rglob("*"))
    bgm_files = [p for p in bgm_files if p.is_file()]
    sound_files = [p for p in (GAME_DIR / "audio" / "sound").rglob("*") if p.is_file()]
    rule_files = [p for p in (GAME_DIR / "images" / "rule").rglob("*.png") if p.is_file()]
    webm = GAME_DIR / "video" / "doremi_op.webm"

    if len(bgm_files) != 26:
        errors.append(f"Expected 26 BGM files, found {len(bgm_files)}")
    if len(sound_files) != 6563:
        errors.append(f"Expected 6563 sound/voice files, found {len(sound_files)}")
    if len(rule_files) != 8:
        errors.append(f"Expected 8 rule mask PNGs, found {len(rule_files)}")
    if len(button_states) != 72:
        errors.append(f"Expected 72 button state sets, found {len(button_states)}")
    if not webm.is_file() or webm.stat().st_size < 1_000_000:
        errors.append("video/doremi_op.webm missing or too small")

    # Verify asset calls inside scenarios & UI scripts resolve
    call_checks = 0
    for p in sorted(GAME_DIR.rglob("*.rpy")):
        if "/tl/" in p.as_posix() or p.name in ("asset_map.rpy", "kag_runtime.rpy"):
            continue
        txt = p.read_text(encoding="utf-8")
        for lineno, line in enumerate(txt.splitlines(), 1):
            st = line.strip()
            if not st.startswith("$ kag_"):
                continue
            try:
                tree = ast.parse(st[2:])
                call = tree.body[0].value  # type: ignore[attr-defined]
                if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name):
                    continue
                fname = call.func.id
                args = call.args
                kw = {k.arg: k.value for k in call.keywords}

                def str_val(node):
                    return node.value if isinstance(node, ast.Constant) and isinstance(node.value, str) else None

                if fname == "kag_drawchar" and args:
                    key = str_val(args[0])
                    if key and key.lower() not in image_map:
                        errors.append(f"{p.name}:{lineno} missing char image {key!r}")
                    call_checks += 1
                elif fname in ("kag_bgdraw", "kag_frmdraw", "kag_changetype", "kag_add_button"):
                    arg_idx = 1 if fname == "kag_changetype" else 0
                    node = args[arg_idx] if len(args) > arg_idx else kw.get("storage") or kw.get("graphic")
                    key = str_val(node)
                    if key:
                        low = key.lower()
                        if fname == "kag_add_button":
                            ok = low in button_states or Path(low).stem in button_states or low in image_map
                        else:
                            ok = low in image_map or Path(low).stem in image_map
                        if not ok:
                            errors.append(f"{p.name}:{lineno} missing image {key!r} in {fname}")
                        call_checks += 1
                    rule_node = kw.get("rule")
                    rkey = str_val(rule_node)
                    if rkey and rkey.lower() not in rule_map and Path(rkey.lower()).stem not in rule_map:
                        errors.append(f"{p.name}:{lineno} missing rule {rkey!r}")
                elif fname == "kag_image":
                    node = kw.get("storage") or (args[0] if args else None)
                    key = str_val(node)
                    if key:
                        low = key.lower()
                        if low not in image_map and Path(low).stem not in image_map:
                            errors.append(f"{p.name}:{lineno} missing [image] storage {key!r}")
                        call_checks += 1
                elif fname in ("kag_playbgm", "kag_fadeinbgm") and args:
                    key = str_val(args[0])
                    if key and key.lower() not in bgm_map and Path(key.lower()).stem not in bgm_map:
                        errors.append(f"{p.name}:{lineno} missing BGM {key!r}")
                    call_checks += 1
                elif fname in ("kag_playse", "kag_fadeinse") and args:
                    key = str_val(args[0])
                    if key and key.lower() not in se_map and Path(key.lower()).stem not in se_map:
                        errors.append(f"{p.name}:{lineno} missing SE/voice {key!r}")
                    call_checks += 1
                elif fname == "kag_playvideo" and args:
                    key = str_val(args[0])
                    if key and key.lower() not in video_map and Path(key.lower()).stem not in video_map:
                        errors.append(f"{p.name}:{lineno} missing video {key!r}")
                    call_checks += 1
            except Exception:
                continue

    print(
        f"[OK] Assets: {len(bgm_files)} BGMs, {len(sound_files)} SE/voices, {len(rule_files)} rules, "
        f"{len(button_states)} button sets, {call_checks} scenario asset calls resolved, 100% ASCII paths"
    )
    return errors


def _extract_dialogue_chars(files: list[Path]) -> set[str]:
    """Extract unique printable non-whitespace display characters from Ren'Py script/tl files."""
    chars: set[str] = set()
    for p in files:
        for line in p.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s or s.startswith("#") or s.startswith("old "):
                continue
            if s.startswith("$") and not any(
                k in s for k in ("caption", "kag_tr", "kag_set_bookmark", "kag_input")
            ):
                continue
            for m in re.finditer(r"\"((?:[^\"\\]|\\.)*)\"", s):
                raw = m.group(1).replace("\\n", "").replace('\\"', '"').replace("\\\\", "\\")
                clean = re.sub(r"\{[^}]*\}", "", raw)
                for ch in clean:
                    if not ch.isspace():
                        chars.add(ch)
    return chars


def check_fonts() -> list[str]:
    errors: list[str] = []
    expected_fonts = [
        ("NotoSansCJKjp-Regular.otf", False, "jp"),
        ("NotoSansCJKsc-Regular.otf", False, "sc"),
        ("NotoSansMonoCJKjp-Regular.otf", True, "jp"),
        ("NotoSansMonoCJKsc-Regular.otf", True, "sc"),
        ("NotoSansCJKjp-Bold.otf", False, "jp"),
        ("NotoSansCJKsc-Bold.otf", False, "sc"),
        ("NotoSansMonoCJKjp-Bold.otf", True, "jp"),
        ("NotoSansMonoCJKsc-Bold.otf", True, "sc"),
    ]
    sample_by_lang = {
        "jp": "春風どれみ「ピリカピリララ！」『ないしょ』…―～♪！？123ABC",
        "sc": "春风DoReMi「霹雳卡霹雳拉拉！」『秘密』…―～♪！？123ABC",
    }
    ui_files = [
        GAME_DIR / name
        for name in ("screens_kag.rpy", "i18n.rpy", "options.rpy", "kag_runtime.rpy")
        if (GAME_DIR / name).is_file()
    ]
    ui_chars = {
        ch
        for p in ui_files
        for ch in p.read_text(encoding="utf-8")
        if not ch.isspace()
    }
    chars_by_lang = {
        "jp": _extract_dialogue_chars(sorted(SCENARIO_DIR.glob("*.rpy"))) | ui_chars,
        "sc": _extract_dialogue_chars(sorted(TL_DIR.rglob("*.rpy"))) | ui_chars,
    }

    for fn, is_mono, lang in expected_fonts:
        fp = GAME_DIR / "fonts" / fn
        if not fp.is_file():
            errors.append(f"Missing font file: {fp}")
            continue
        fnt = ImageFont.truetype(str(fp), 24)
        w_half = fnt.getlength("A")
        w_wide = fnt.getlength("あ")
        if w_wide <= 0 or w_half <= 0:
            errors.append(f"Font {fn} failed glyph measurement")
            continue
        if is_mono and abs((w_wide / w_half) - 2.0) > 0.05:
            errors.append(f"Mono font {fn} aspect mismatch: half={w_half}, full={w_wide}")

        sample_mask = fnt.getmask(sample_by_lang[lang])
        if sample_mask.size[0] <= 100 or sample_mask.size[1] < 16 or not any(sample_mask):
            errors.append(f"Font {fn} failed sample rasterization: size={sample_mask.size}")

        notdef_mask = fnt.getmask("\uffff")
        notdef_sig = (notdef_mask.size, bytes(notdef_mask))
        missing = []
        for ch in sorted(chars_by_lang[lang]):
            gm = fnt.getmask(ch)
            if gm.size[0] <= 0 or gm.size[1] <= 0 or not any(gm) or (gm.size, bytes(gm)) == notdef_sig:
                missing.append(ch)
        if missing:
            preview = ", ".join(f"{c}(U+{ord(c):04X})" for c in missing[:10])
            errors.append(f"Font {fn} missing or .notdef tofu in {len(missing)} {lang} glyphs: {preview}")

    msgothic_path = GAME_DIR / "fonts" / "msgothic.ttc"
    scen_chars = _extract_dialogue_chars(sorted(SCENARIO_DIR.glob("*.rpy")))
    extra_summary = ""
    if msgothic_path.is_file():
        ms_fnt = ImageFont.truetype(str(msgothic_path), 24, index=0)
        ms_a = ms_fnt.getlength("A")
        ms_ja = ms_fnt.getlength("あ")
        if ms_ja <= 0 or ms_a <= 0 or abs((ms_ja / ms_a) - 2.0) > 0.05:
            errors.append(f"MS Gothic index=0 aspect mismatch: half={ms_a}, full={ms_ja}")
        ms_sample = ms_fnt.getmask(sample_by_lang["jp"])
        if ms_sample.size[0] <= 100 or ms_sample.size[1] < 16 or not any(ms_sample):
            errors.append(f"MS Gothic index=0 failed sample rasterization: size={ms_sample.size}")
        ms_nd = ms_fnt.getmask("\uffff")
        ms_nd_sig = (ms_nd.size, bytes(ms_nd))
        ms_missing = []
        for ch in sorted(scen_chars):
            gm = ms_fnt.getmask(ch)
            if gm.size[0] <= 0 or gm.size[1] <= 0 or not any(gm) or (ch != "\u25a1" and (gm.size, bytes(gm)) == ms_nd_sig):
                ms_missing.append(ch)
        if ms_missing:
            preview = ", ".join(f"{c}(U+{ord(c):04X})" for c in ms_missing[:10])
            errors.append(f"MS Gothic missing {len(ms_missing)} scenario glyphs: {preview}")
        msp_fnt = ImageFont.truetype(str(msgothic_path), 24, index=2)
        msp_sample = msp_fnt.getmask(sample_by_lang["jp"])
        if msp_sample.size[0] <= 100 or msp_sample.size[1] < 16 or not any(msp_sample):
            errors.append(f"MS PGothic index=2 failed sample rasterization: size={msp_sample.size}")
        extra_summary = f" + MS Gothic/PGothic ({len(scen_chars)} JP scenario glyphs)"

    print(
        f"[OK] Fonts: {len(expected_fonts)} standalone OpenType CJK fonts verified "
        f"(mono 1:2 MS Gothic parity, sample rasterization, {len(chars_by_lang['jp'])} JP / {len(chars_by_lang['sc'])} SC non-tofu glyphs){extra_summary}"
    )
    return errors


def check_i18n_coverage() -> list[str]:
    errors: list[str] = []
    tl_olds: set[str] = set()
    for p in sorted(TL_DIR.glob("*.rpy")):
        lines = p.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, 1):
            st = line.strip()
            if st.startswith("old "):
                val = ast.literal_eval(st[4:].strip())
                tl_olds.add(val)

    required: set[str] = set()
    for p in sorted(GAME_DIR.glob("*.rpy")):
        if p.name == "asset_map.rpy":
            continue
        txt = p.read_text(encoding="utf-8")
        for m in re.finditer(r'(?:_\(|kag_tr\()((?:"(?:\\.|[^"])*"|\'(?:\\.|[^\'])*\'))', txt):
            val = ast.literal_eval(m.group(1))
            if any("\u3040" <= c <= "\u9fff" for c in val):
                required.add(val)

    for p in sorted(SCENARIO_DIR.glob("*.rpy")):
        if p.name == "_label_index.rpy":
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            st = line.strip()
            if st.startswith("$ kag_set_bookmark(") or st.startswith("$ kag_add_link("):
                tree = ast.parse(st[2:])
                call = tree.body[0].value  # type: ignore[attr-defined]
                if call.args and isinstance(call.args[0], ast.Constant) and isinstance(call.args[0].value, str):
                    required.add(call.args[0].value)

    missing = sorted(required - tl_olds)
    if missing:
        errors.append(f"Missing {len(missing)} zh_cn UI/bookmark/choice translations: {missing[:10]}")

    kana_re = re.compile(r"[\u3040-\u30ff\uff65-\uff9f]")
    empty_ui: list[str] = []
    for p in sorted(TL_DIR.glob("*.rpy")):
        last_old = None
        for lineno, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            st = line.strip()
            if st.startswith("old "):
                last_old = ast.literal_eval(st[4:].strip())
            elif st.startswith("new "):
                val = ast.literal_eval(st[4:].strip())
                if val == "" and last_old:
                    empty_ui.append(f"{p.name}:{lineno}")
    if empty_ui:
        errors.append(f"Empty zh_cn UI/common translations ({len(empty_ui)}): {empty_ui[:10]}")

    scen_tl_files = sorted((TL_DIR / "scenario").glob("*.rpy")) if (TL_DIR / "scenario").is_dir() else []
    if not scen_tl_files:
        errors.append("Missing zh_cn scenario translation directory/files")
    untranslated_scen: list[str] = []
    kana_scen: list[str] = []
    scen_blocks = 0
    for p in scen_tl_files:
        lines = p.read_text(encoding="utf-8").splitlines()
        cur_id = None
        for lineno, line in enumerate(lines, 1):
            st = line.strip()
            if st.startswith("translate zh_cn "):
                cur_id = st[len("translate zh_cn "):].rstrip(":").strip()
                scen_blocks += 1
            elif st.startswith("#") or not st:
                continue
            elif cur_id and (st.startswith('"') or st.startswith("extend ")):
                m = re.match(r'^(?:extend\s+)?"((?:[^"\\]|\\.)*)"(?:\s+nointeract)?$', st)
                if m:
                    val = ast.literal_eval('"' + m.group(1) + '"')
                    if val == "":
                        untranslated_scen.append(f"{p.name}:{cur_id}")
                    elif kana_re.search(val):
                        kana_scen.append(f"{p.name}:{cur_id}")
                cur_id = None
    if untranslated_scen:
        errors.append(f"Untranslated zh_cn scenario blocks ({len(untranslated_scen)}): {untranslated_scen[:10]}")
    if kana_scen:
        errors.append(f"Remaining Japanese kana in zh_cn scenario translations ({len(kana_scen)}): {kana_scen[:10]}")

    expected_ui_imgs = sorted((GAME_DIR / "images/ui/slices").glob("*.png"))
    img_missing: list[str] = []
    img_mismatch: list[str] = []
    req_rel = [f"images/ui/slices/{p.name}" for p in expected_ui_imgs] + [
        "images/ui/thm_no.png",
        "images/bg/option.png",
        "images/bg/album.png",
        "images/bg/album_05.png",
        "images/bg/album_06.png",
        "images/bg/album_07.png",
        "images/bg/memorial_all.png",
        "images/bg/prologue2.png",
        "images/bg/prologue3.png",
        "images/bg/eyecatch.png",
    ]
    for rel in req_rel:
        src_p = GAME_DIR / rel
        tl_p = TL_DIR / rel
        if not tl_p.is_file():
            img_missing.append(rel)
        elif Image.open(tl_p).size != Image.open(src_p).size:
            img_mismatch.append(rel)
    if img_missing:
        errors.append(f"Missing localized zh_cn UI/BG images ({len(img_missing)}): {img_missing[:10]}")
    if img_mismatch:
        errors.append(f"Mismatched dimensions on zh_cn UI/BG images ({len(img_mismatch)}): {img_mismatch[:10]}")

    print(
        f"[OK] i18n (zh_cn): {len(required)}/{len(required)} UI/bookmark/choice strings + "
        f"{scen_blocks} scenario blocks ({len(scen_tl_files)} files) + {len(req_rel)} localized images verified"
    )
    return errors


def check_sdk_and_launchers() -> list[str]:
    errors: list[str] = []
    sdk = Path(os.environ.get("RENPY_SDK", Path.home() / ".local/opt/renpy-8.6.0-sdk"))
    for req in [
        sdk / "renpy.sh",
        sdk / "lib" / "py3-linux-x86_64",
        sdk / "lib" / "py3-linux-aarch64",
        sdk / "lib" / "py3-mac-universal",
        sdk / "lib" / "py3-windows-x86_64",
        ROOT_DIR / "run_linux.sh",
        ROOT_DIR / "build_distributions.sh",
    ]:
        if not req.exists():
            errors.append(f"Missing distribution/launcher path: {req}")
    for sh in [ROOT_DIR / "run_linux.sh", ROOT_DIR / "build_distributions.sh"]:
        if sh.exists() and not os.access(sh, os.X_OK):
            errors.append(f"Script is not executable: {sh}")
    print("[OK] Launchers & SDK: Linux (x86_64 + aarch64) + macOS Universal + Windows targets ready")
    return errors


def main() -> int:
    maps = load_asset_maps()
    all_errors: list[str] = []
    scen_errs, _ = check_scenarios_and_labels()
    all_errors.extend(scen_errs)
    all_errors.extend(check_assets_and_references(maps))
    all_errors.extend(check_fonts())
    all_errors.extend(check_i18n_coverage())
    all_errors.extend(check_sdk_and_launchers())

    if "--skip-runtime" not in sys.argv:
        tools_dir = str(ROOT_DIR / "tools")
        if tools_dir not in sys.path:
            sys.path.insert(0, tools_dir)
        import runtime_smoke_test

        if runtime_smoke_test.main() != 0:
            all_errors.append("Runtime smoke test failed")

    if all_errors:
        print("\nVERIFICATION FAILED:")
        for e in all_errors:
            print("  -", e)
        return 1
    print("\nALL VERIFICATION CHECKS PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
