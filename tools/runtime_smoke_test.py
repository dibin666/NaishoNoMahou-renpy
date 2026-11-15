#!/usr/bin/env python3
"""
Automated headless runtime smoke & integration test for the Ren'Py 8 project.
Launches the real Ren'Py 8.6.0 engine in an isolated --savedir so all displayables,
transitions, quake, WebM movie decoding, audio channels, 30-slot save/load/lock/
comment operations, i18n language/font switching, all 12 custom screens, and real
scenario playthrough routes are executed end-to-end.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = ROOT_DIR / "renpy_project"
GAME_DIR = PROJECT_DIR / "game"
RENPY_SH = Path(os.environ.get("RENPY_SDK", str(Path.home() / ".local/opt/renpy-8.6.0-sdk"))) / "renpy.sh"

SMOKE_RPY = r'''# Temporary headless smoke & playthrough test module (auto-deleted after run)
label kag__smoke_test_phase1:
    $ _smoke_entry = True
    python hide:
        import glob, os, types
        # Prevent MultiLocation from reading/writing user ~/.renpy or renpy_project/game/saves during headless smoke runs
        for _sloc in list(renpy.loadsave.location.locations):
            if os.path.abspath(getattr(_sloc, "directory", "")) != os.path.abspath(config.savedir):
                _sloc.active = False
        renpy.loadsave.location.scan()

        log_step = _smoke_log_step
        chk = _smoke_chk
        store._smoke_errors = []

        log_step("start phase1 developer=%r context_level=%d" % (config.developer, renpy.context_nesting_level()))
        config.check_conflicting_properties = True

        # 1. Boot / Entry context checks
        chk(not renpy.has_label("splashscreen"), "splashscreen label should be removed for single-context mode")
        chk(renpy.has_label("main_menu"), "main_menu label missing")
        chk(renpy.has_label("start"), "start label missing")
        chk(renpy.context_nesting_level() == 0, "expected context nesting level 0")
        chk(len(renpy.get_return_stack()) == 0, "expected clean return_stack at boot: %r" % (renpy.get_return_stack(),))
        chk(not main_menu, "main_menu flag must be False during normal game context")
        renpy.call_in_new_context("main_menu")
        kag_sync_on_start()
        chk(_preferences.skip_unseen is True, "_preferences.skip_unseen should default to True")
        exp_init_font = "fonts/NotoSansMonoCJKsc-Regular.otf" if _preferences.language == "zh_cn" else "fonts/NotoSansMonoCJKjp-Regular.otf"
        chk(kag_get_active_font() == exp_init_font, "unexpected initial font: %s (lang=%r)" % (kag_get_active_font(), _preferences.language))
        log_step("checked 1: context & font")

        # 2. Verify all 68 scenario image/SE/BGM/video references resolve cleanly
        scen_files = sorted(glob.glob(os.path.join(config.gamedir, "scenario", "*.rpy")))
        chk(len(scen_files) >= 68, "expected >= 68 scenario .rpy files, got %d" % len(scen_files))
        img_pat = re.compile(r"kag_(?:changetype\([^,]+,\s*|drawchar\(|image\()(['\"])([^'\"]+)\1")
        bgm_pat = re.compile(r"kag_(?:playbgm|fadeinbgm)\((['\"])([^'\"]+)\1")
        se_pat = re.compile(r"kag_(?:playse|fadeinse|sound_se|se_loop)\((['\"])([^'\"]+)\1")
        vid_pat = re.compile(r"kag_playvideo\((['\"])([^'\"]+)\1")

        missing_assets = []
        for sf_path in scen_files:
            txt = open(sf_path, encoding="utf-8").read()
            for m in img_pat.finditer(txt):
                st = m.group(2)
                if st.lower() in ("black", "white"):
                    continue
                resolved = kag_resolve_image(st)
                if not resolved or not renpy.loadable(resolved):
                    missing_assets.append(("img", os.path.basename(sf_path), st))
            for m in bgm_pat.finditer(txt):
                st = m.group(2)
                resolved = kag_resolve_bgm(st)
                if not resolved or not renpy.loadable(resolved):
                    missing_assets.append(("bgm", os.path.basename(sf_path), st))
            for m in se_pat.finditer(txt):
                st = m.group(2)
                resolved = kag_resolve_se(st) or kag_resolve_bgm(st)
                if not resolved or not renpy.loadable(resolved):
                    missing_assets.append(("se", os.path.basename(sf_path), st))
            for m in vid_pat.finditer(txt):
                st = m.group(2)
                resolved = kag_resolve_video(st)
                if not resolved or not renpy.loadable(resolved):
                    missing_assets.append(("video", os.path.basename(sf_path), st))
        chk(not missing_assets, "Unloadable scenario assets: %r" % (missing_assets[:10],))
        log_step("checked 2: assets (%d files)" % len(scen_files))

        # 3. Verify measure/indent/skip/text-speed primitives
        chk(kag_measure_text_width("魔女の子「") == 120, "bad CJK width: %r" % kag_measure_text_width("魔女の子「"))
        chk(kag_measure_text_width("ABC「") == 60, "bad mixed width: %r" % kag_measure_text_width("ABC「"))
        kag_set_clickskip(False)
        chk(store.kag_clickskip_enabled is False and store._skipping is False, "clickskip False failed")
        kag_set_clickskip(True)
        chk(store.kag_clickskip_enabled is True and store._skipping is True, "clickskip True failed")
        store.kag_in_title = False
        kag_start_skip()
        chk(config.skipping == "slow", "kag_start_skip did not enable skipping")
        kag_cancelskip()
        chk(config.skipping is None, "kag_cancelskip did not clear config.skipping")
        for spd, cps in [("fast", 100), ("normal", 33), ("slow", 20), ("instant", 0)]:
            kag_set_text_speed(spd)
            chk(preferences.text_cps == cps, "text_speed %s expected %d got %d" % (spd, cps, preferences.text_cps))
        kag_set_text_speed("normal")
        log_step("checked 3: text/skip/speed")

        # 4. Visual transitions, drawchar (normal + sepia), quake, layers, and real WebM video decoding
        kag_image("black", layer="base", page="fore")
        kag_image("bg001", layer="base", page="back")
        kag_trans(10, method="crossfade")
        for ctype in ("left", "right", "up", "down", "circle01", "circle02", "blind01",
                      "cross", "wave", "mosaic", "turn", "r_zoom", "r_vanish", "r_swap",
                      "sepia", "note"):
            kag_changetype(ctype, "bg001", time_ms=10, bgcolor="0x000000")
        chk(not store.kag_in_title, "bg001 should not mark kag_in_title")
        kag_changetype("left", "maintitle", time_ms=10, bgcolor="0x000000")
        chk(store.kag_in_title is True, "maintitle should mark kag_in_title")
        kag_startanchor()
        chk(store.kag_in_title is True, "kag_startanchor should mark kag_in_title")

        kag_prepare_new_game()
        chk(store.kag_in_title is False, "kag_prepare_new_game should clear kag_in_title")
        kag_drawchar("d_02.tlg", time_ms=10, sepia=False)
        kag_drawchar("d_02.tlg", time_ms=10, sepia=True)
        kag_bgdraw()
        kag_frmdraw()
        kag_quake(time_ms=80, hmax=12, vmax=8)
        kag_freeimage(layer="0", page="fore")
        kag_freeimage(layer="1", page="fore")
        kag_freeimage(layer="3", page="fore")
        # Exercise real WebM movie decoding briefly (0.15s)
        renpy.movie_cutscene("video/doremi_op.webm", delay=0.15, loops=0, stop_music=True)
        log_step("checked 4: visual transitions, quake & WebM video")

        # 5. Audio primitives including endroll bgm-v02 on se0 + fadeoutbgm cleanup
        kag_playbgm("m63", loop=True)
        chk(store.kag_bgm_looping is True, "kag_playbgm loop=True mismatch")
        kag_pausebgm()
        kag_resumebgm()
        kag_bgmopt(volume=80)
        kag_wl(canskip=True)  # Must return immediately while looping
        kag_fadeoutbgm(10)
        kag_playbgm("bgm-v04", loop=False)
        chk(store.kag_bgm_looping is False, "kag_playbgm loop=False mismatch")
        kag_stopbgm()

        kag_playse("1-0001.ogg", buf=0, loop=False)
        chk(store.kag_se0_is_bgm is False, "voice SE should not set kag_se0_is_bgm")
        kag_stopse(buf=0)
        kag_fadeinse("bgm-v02", time_ms=10, buf=0)
        chk(store.kag_se0_is_bgm is True, "bgm-v02 on se0 must set kag_se0_is_bgm")
        kag_fadeoutbgm(10)
        chk(store.kag_se0_is_bgm is False, "kag_fadeoutbgm must clear kag_se0_is_bgm and stop se0")
        kag_se_loop("se-005.ogg")
        kag_fadeoutse(10, buf=2)
        log_step("checked 5: audio & se0-bgm")

        # 6. Save / Lock / Overwrite-Protection / Comment / Clear-Comment test
        renpy.take_screenshot((config.thumbnail_width, config.thumbnail_height))
        kag_set_bookmark("りずむのお仕事")
        kag_save_to_slot(0)
        chk(renpy.can_load(kag_slot_name(0)), "slot 0 failed to save")
        chk(persistent.kag_bookmarks[0] == "りずむのお仕事", "slot 0 bookmark mismatch")
        kag_update_slot_comment(0, "テストコメント123")
        chk(persistent.kag_comments[0] == "テストコメント123", "slot 0 comment mismatch")
        kag_toggle_slot_lock(0)
        chk(persistent.kag_locks[0] is True, "slot 0 lock failed")
        kag_set_bookmark("ロック中テスト")
        kag_save_to_slot(0)
        chk(persistent.kag_bookmarks[0] == "りずむのお仕事", "locked slot 0 was overwritten!")
        kag_toggle_slot_lock(0)
        chk(persistent.kag_locks[0] is False, "slot 0 unlock failed")
        kag_set_bookmark("上書き後テスト")
        kag_save_to_slot(0)
        chk(persistent.kag_bookmarks[0] == "上書き後テスト", "slot 0 overwrite failed")
        chk(persistent.kag_comments[0] == "", "slot 0 comment was not cleared on overwrite")
        chk(FileSaveName(kag_slot_name(0), slot=True) == "上書き後テスト", "FileSaveName(slot=True) mismatch: %r" % (FileSaveName(kag_slot_name(0), slot=True),))
        _ss_disp = FileScreenshot(kag_slot_name(0), empty="images/ui/thm_no.png", slot=True)
        chk(not isinstance(_ss_disp, Null), "FileScreenshot(slot=True) returned Null for saved slot")
        _ss_rnd = renpy.render(_ss_disp, 133, 100, 0, 0)
        chk(_ss_rnd.width >= 100 and _ss_rnd.height >= 80, "FileScreenshot(slot=True) size unexpected: %sx%s" % (_ss_rnd.width, _ss_rnd.height))

        # 6b. Shortcut configuration tests
        kag_set_shortcut("save", "K_z")
        chk(kag_get_shortcuts().get("save") == "K_z", "kag_set_shortcut failed")
        chk("noshift_K_z" in config.keymap.get("kag_sc_save", []), "config.keymap['kag_sc_save'] missing noshift_K_z")
        kag_clear_shortcut("save")
        chk(kag_get_shortcuts().get("save") is None, "kag_clear_shortcut failed")
        chk(config.keymap.get("kag_sc_save") == [], "config.keymap['kag_sc_save'] not cleared")
        kag_reset_shortcuts()
        chk(kag_get_shortcuts().get("save") == "K_s", "kag_reset_shortcuts failed")
        chk("noshift_K_s" in config.keymap.get("kag_sc_save", []), "config.keymap['kag_sc_save'] missing noshift_K_s after reset")
        log_step("checked 6: save/lock/comment/thumbnail & shortcuts")

        # 7. Screen rendering verification in both Japanese & Simplified Chinese (modal=False avoids blocking!)
        def test_show_and_hide(scr_name, **kwargs):
            try:
                renpy.show_screen(scr_name, **kwargs)
                renpy.pause(0.01, hard=True, modal=False)
            finally:
                renpy.hide_screen(scr_name)

        renpy.show("kag_bg", what=kag_make_displayable("bg001"), layer="master", zorder=0)
        _jp_exp_mono = "fonts/msgothic.ttc" if renpy.loadable("fonts/msgothic.ttc") else "fonts/NotoSansMonoCJKjp-Regular.otf"
        _jp_exp_prop = "2@fonts/msgothic.ttc" if renpy.loadable("fonts/msgothic.ttc") else "fonts/NotoSansCJKjp-Regular.otf"
        for lang_code, exp_mono, exp_prop in [
            (None, _jp_exp_mono, _jp_exp_prop),
            ("zh_cn", "fonts/NotoSansMonoCJKsc-Regular.otf", "fonts/NotoSansCJKsc-Regular.otf"),
        ]:
            kag_set_language(lang_code)
            kag_set_font_mode("mono")
            chk(kag_get_active_font() == exp_mono, "lang %r mono font mismatch: %s" % (lang_code, kag_get_active_font()))
            kag_set_font_mode("prop")
            chk(kag_get_active_font() == exp_prop, "lang %r prop font mismatch: %s" % (lang_code, kag_get_active_font()))
            kag_set_font_mode("mono")

            if lang_code == "zh_cn":
                chk(kag_tr("システム(S)") == "系统(S)", "zh_cn sys translation failed")
                chk(kag_tr("ショートカット設定(K)...") == "快捷键设置(K)...", "zh_cn shortcuts menu translation failed")
                chk(kag_tr("解除") == "取消设置", "zh_cn unbind label translation failed")
                chk(kag_tr("ＭＯＶＩＥを見ますか？") == "要观看开场动画吗？", "zh_cn movie prompt translation failed")
                chk(kag_tr("{color=#ff0066}春風どれみシナリオ{/color}") == "{color=#ff0066}春风DoReMi剧情{/color}", "zh_cn omoide header translation failed")
                chk(kag_tr("終了しますか？") == "确定要退出游戏吗？", "zh_cn quit confirm translation failed")

            store.kag_mesframe_visible = False
            kag_on_say_display("{color=#ff0066}春風どれみシナリオ{/color}")
            store.kag_hold_box_active = True
            test_show_and_hide("kag_mesframe_overlay")

            store.kag_mesframe_visible = True
            kag_on_say_display("ＭＯＶＩＥを見ますか？")
            store.kag_hold_box_active = True
            test_show_and_hide("say", who=None, what="ＭＯＶＩＥを見ますか？")
            test_show_and_hide("say", who="どれみ", what="どれみ「テスト！」")
            test_show_and_hide(
                "kag_interactive_menu",
                buttons=[{"graphic": "main_btn_newgame", "current_stem": "menu", "storage": None, "target": "*newgame", "exp": None, "x": 478, "y": 390}],
                links=[
                    {"caption": "はい", "current_stem": "option", "storage": None, "target": "*yes", "exp": None, "x": None, "y": None, "color": None, "size": None},
                    {"caption": "いいえ", "current_stem": "option", "storage": None, "target": "*no", "exp": None, "x": None, "y": None, "color": None, "size": None},
                ],
            )
            test_show_and_hide(
                "kag_interactive_menu",
                buttons=[],
                links=[
                    {"caption": "「１日目」最初のお仕事！失敗してもがんばろう！", "current_stem": "extra", "storage": None, "target": "*s_d1", "exp": None, "x": 20, "y": 150, "color": "#ff0066", "size": 20},
                    {"caption": "戻る", "current_stem": "extra", "storage": None, "target": "*return_s0", "exp": None, "x": 20, "y": 450, "color": "#ff0066", "size": None},
                ],
            )
            for dd in (None, "sys", "text", "movie", "vol", "disp", "lang", "help"):
                store._kag_active_dropdown = dd
                test_show_and_hide("kag_menubar")
            store._kag_active_dropdown = None
            test_show_and_hide("kag_rclick_menu")
            test_show_and_hide("kag_save_load", mode="save", from_rclick=True)
            test_show_and_hide("kag_save_load", mode="load", from_load_ks=True)
            store._kag_editing_comment_slot = 0
            store._kag_editing_comment_text = "編集テスト"
            test_show_and_hide("kag_comment_editor")
            for _hi in range(36):
                _htxt = (
                    "魔女の子「履歴テスト行 %d：{w=0.6}長い台詞の折り返しとスクロールバー表示を確認します！」" % _hi
                    if _hi % 2 else
                    "光り輝く太陽。(%d)" % _hi
                )
                store._history_list.append(types.SimpleNamespace(who=None, what=_htxt))
            try:
                renpy.show_screen("history")
                renpy.pause(0.01, hard=True, modal=False)
                _hscr = renpy.get_screen("history")
                chk(_hscr is not None, "history screen did not open for lang=%r" % (lang_code,))
                _hrnd = renpy.render(_hscr, 800, 600, 0, 0)
                _hsurf = _hrnd.pygame_surface(True)
                _h_bright = sum(
                    1
                    for _py in range(32, 576, 3)
                    for _px in range(24, 756, 3)
                    if sum(_hsurf.get_at((_px, _py))[:3]) > 450
                )
                chk(_h_bright > 250, "history screen rendered blank (bright pixels=%d) for lang=%r" % (_h_bright, lang_code))
                _hbar = sum(
                    1
                    for _py in range(32, 576, 4)
                    for _px in range(768, 784, 3)
                    if sum(_hsurf.get_at((_px, _py))[:3]) > 150
                )
                chk(_hbar > 20, "history scrollbar did not render (pixels=%d) for lang=%r" % (_hbar, lang_code))
            finally:
                renpy.hide_screen("history")
            store._history_list[:] = []
            test_show_and_hide("kag_input_dialog", prompt="※呪文を20文字以内で入力してください。", title="呪文の入力", default_val="ピリカピリララ")
            test_show_and_hide("kag_about_dialog")
            test_show_and_hide("kag_shortcuts_dialog")
            store._kag_capturing_shortcut = "save"
            test_show_and_hide("kag_shortcuts_dialog")
            store._kag_capturing_shortcut = None
            test_show_and_hide("confirm", message=kag_tr("タイトルへ戻りますか？"), yes_action=Return(True), no_action=Return(False))
            test_show_and_hide("notify", message=kag_tr("セーブしました。"))

        # Verify real Character/_Extend + screen say flow without blocking
        renpy.say(None, "一行目テスト", interact=False)
        store._last_say_who = None
        store._last_say_what = "一行目テスト"
        store._last_raw_what = "\n二行目extendテスト"
        renpy.say(extend, "\n二行目extendテスト", interact=False)
        renpy.pause(0.01, hard=True, modal=False)
        renpy.hide_screen("say")
        kag_cm()
        store._history_list[:] = []

        kag_set_language(None)
        log_step("checked 7: all 12 screens + extend say rendered in jp & zh_cn")

        # 7b. Live Ren'Py font rendering verification (all 8 CJK OpenType fonts, glyph ink, 1:2 mono parity, indent, PNG export)
        def _run_font_render_checks():
            all_fonts = [
                ("fonts/NotoSansMonoCJKjp-Regular.otf", "春風どれみ「ピリカピリララ！」ＭＯＶＩＥを見ますか？123ABC"),
                ("fonts/NotoSansMonoCJKjp-Bold.otf", "春風どれみ「ピリカピリララ！」太字テスト123ABC"),
                ("fonts/NotoSansCJKjp-Regular.otf", "春風どれみ「ピリカピリララ！」プロポーショナル123ABC"),
                ("fonts/NotoSansCJKjp-Bold.otf", "春風どれみ「ピリカピリララ！」太字プロポーショナル123ABC"),
                ("fonts/NotoSansMonoCJKsc-Regular.otf", "春风DoReMi「霹雳卡霹雳拉拉！」系统(S) 确定要退出游戏吗？123ABC"),
                ("fonts/NotoSansMonoCJKsc-Bold.otf", "春风DoReMi「霹雳卡霹雳拉拉！」粗体测试123ABC"),
                ("fonts/NotoSansCJKsc-Regular.otf", "春风DoReMi「霹雳卡霹雳拉拉！」比例字体123ABC"),
                ("fonts/NotoSansCJKsc-Bold.otf", "春风DoReMi「霹雳卡霹雳拉拉！」粗体比例字体123ABC"),
            ]
            for fpath, sample_txt in all_fonts:
                txt_disp = Text(sample_txt, font=fpath, size=24, color="#ffffff", outlines=[(1, "#000000", 1, 1)])
                rnd = renpy.render(txt_disp, 800, 600, 0, 0)
                chk(rnd.width > 200 and rnd.height >= 24, "Font render bounds too small for %s: %sx%s" % (fpath, rnd.width, rnd.height))
                has_opaque = any(
                    rnd.is_pixel_opaque(px, py)
                    for px in range(4, int(rnd.width), 6)
                    for py in range(4, int(rnd.height), 4)
                )
                chk(has_opaque, "Font Render has no opaque glyph pixels for %s" % fpath)
                surf = rnd.pygame_surface(True)
                bbox = surf.get_bounding_rect()
                chk(bbox.width > 150 and bbox.height >= 16, "Font surface bounding rect empty for %s: %r" % (fpath, bbox))

            for mono_f in ("fonts/NotoSansMonoCJKjp-Regular.otf", "fonts/NotoSansMonoCJKsc-Regular.otf"):
                r_half = renpy.render(Text("AAAAAAAAAA", font=mono_f, size=24, outlines=[]), 800, 600, 0, 0)
                r_full = renpy.render(Text("あああああ", font=mono_f, size=24, outlines=[]), 800, 600, 0, 0)
                chk(abs(r_half.width - 120) <= 2, "%s 10 ASCII width expected ~120 got %r" % (mono_f, r_half.width))
                chk(abs(r_full.width - 120) <= 2, "%s 5 CJK width expected ~120 got %r" % (mono_f, r_full.width))

            kag_set_next_indent("魔女の子「")
            chk(store.kag_hold_box_indent == 120, "kag_hold_box_indent expected 120 got %r" % store.kag_hold_box_indent)
            kag_on_say_display("魔女の子「テスト\n次の行！」")
            chk(store.kag_hold_box_indent == 120, "kag_on_say_display indent expected 120 got %r" % store.kag_hold_box_indent)
            test_show_and_hide("say", who=None, what="魔女の子「テスト\n次の行！」")
            kag_cm()

            png_out = os.environ["KAG_SMOKE_PNG_FILE"]
            sample_png_disp = Text(
                "どれみ「ピリカピリララ！」 / 简中测试：系统(S) 確定？",
                font="fonts/NotoSansMonoCJKsc-Regular.otf",
                size=24,
                color="#ffffff",
                outlines=[(1, "#000000", 1, 1)],
            )
            renpy.render_to_file(sample_png_disp, png_out, width=800, height=64)
            chk(os.path.isfile(png_out) and os.path.getsize(png_out) > 200, "Font render_to_file PNG missing or too small")

            # Verify style-inherited rendering (no explicit font= override!) against .notdef tofu in jp & zh_cn
            def _glyph_sig(disp_obj):
                r = renpy.render(disp_obj, 800, 600, 0, 0)
                s = r.pygame_surface(True)
                sw, sh = s.get_size()
                return (sw, sh, tuple(tuple(s.get_at((px, py))) for py in range(sh) for px in range(sw)))

            _ui_inherited_styles = (
                "default", "text", "button_text", "label_text", "prompt_text",
                "input", "kag_menu_item_text", "say_dialogue", "say_label",
            )
            _jp_probes = ("デ", "ー", "タ", "～", "あ", "漢", "✓", "ロ")
            _sc_probes = _jp_probes + ("简", "吗", "话", "这", "见", "过", "认", "阵", "发", "说", "给", "还", "伤", "对", "护", "车", "察", "愣", "觉", "噗")
            _sc_screenshot_lines = (
                "女孩「是有哪里不舒服吗？」",
                "突然被人搭话，吓得我差点从秋千上摔下来。",
                "这个人，好像哪里有点面熟，又好像没见过……",
                "小魔女「这个人我认得，好像前阵子在魔女界见过……」",
                "女孩「哇哇哇～！怎么了怎么了！？是哪里痛吗！！」",
                "女孩「都哭成这样了可不是小事呀！发生什么事了？说给我听听嘛！？还是说哪里受伤了？对了！呃～找医生、叫救护车、还要叫警察～」",
                "看着手足无措的女孩，我一下愣住了。",
                "女孩完全没察觉我的神情，反倒越发慌乱起来。",
                "小魔女「噗嗤！」",
                "小魔女「啊、对不起！突然笑出声来……」",
            )
            for _lang_val in (None, "zh_cn"):
                kag_set_language(_lang_val)
                _active_probes = _sc_probes if _lang_val == "zh_cn" else _jp_probes
                for _fmode in ("mono", "prop"):
                    kag_set_font_mode(_fmode)
                    _exp_ui_fnt = kag_get_active_font()
                    _exp_jp_fnt = kag_get_jp_font()
                    _exp_sc_fnt = kag_get_sc_font(bold=False)
                    if renpy.loadable("fonts/msgothic.ttc"):
                        _wanted_jp = "fonts/msgothic.ttc" if _fmode == "mono" else "2@fonts/msgothic.ttc"
                        chk(_exp_jp_fnt == _wanted_jp, "Expected msgothic font %r for mode=%s, got %r" % (_wanted_jp, _fmode, _exp_jp_fnt))
                    for _st_n in _ui_inherited_styles:
                        _got_fnt = Text("テスト", style=_st_n).style.font
                        chk(_got_fnt == _exp_ui_fnt, "Style %s font mismatch for lang=%r mode=%s: got %r expected %r" % (_st_n, _lang_val, _fmode, _got_fnt, _exp_ui_fnt))
                    chk(kag_get_dialogue_font("魔女の子「テスト！」") == _exp_jp_fnt, "kag_get_dialogue_font must keep JP font for Japanese dialogue in lang=%r" % (_lang_val,))
                    # Even when _lang_val is None, lines containing non-cp932 Simplified Chinese characters must use SC font
                    for _sc_line in _sc_screenshot_lines:
                        chk(kag_get_dialogue_font(_sc_line) == _exp_sc_fnt, "kag_get_dialogue_font failed to select SC font for %r in lang=%r mode=%s" % (_sc_line, _lang_val, _fmode))
                    if _lang_val == "zh_cn":
                        chk(kag_get_dialogue_font("要观看开场动画吗？") == _exp_ui_fnt, "kag_get_dialogue_font must use SC font for translated zh_cn prompt")
                        chk(kag_get_dialogue_font("音律「小花？小花去哪里了！？」") == _exp_ui_fnt, "kag_get_dialogue_font must use SC font for zh_cn scenario line")
                        chk(kag_get_dialogue_font("咦？") == _exp_ui_fnt, "kag_get_dialogue_font must use SC font for short zh_cn line")
                        chk(kag_measure_indent_from_what("DoReMi「大家早安！」") == kag_measure_text_width("DoReMi「") > 0, "kag_measure_indent_from_what failed on zh_cn speaker prefix")
                        chk(renpy.open_file("images/ui/slices/main_btn_newgame_idle.png", encoding=False).read() == renpy.open_file("tl/zh_cn/images/ui/slices/main_btn_newgame_idle.png", encoding=False).read(), "zh_cn localized UI slice override did not load")
                        chk(renpy.open_file("images/bg/option.png", encoding=False).read() == renpy.open_file("tl/zh_cn/images/bg/option.png", encoding=False).read(), "zh_cn localized BG override did not load")
                        _tr = renpy.game.script.translator
                        _miss_tr = [tid for tid in _tr.default_translates if (tid, "zh_cn") not in _tr.language_translates]
                        chk(not _miss_tr, "Missing runtime zh_cn dialogue translations: %s" % (_miss_tr[:5],))
                    else:
                        chk(renpy.open_file("images/ui/slices/main_btn_newgame_idle.png", encoding=False).read() != renpy.open_file("tl/zh_cn/images/ui/slices/main_btn_newgame_idle.png", encoding=False).read(), "JP mode unexpectedly loaded zh_cn UI slice")
                    _notdef_sig = _glyph_sig(Text("\uffff", style="default", size=24, color="#ffffff", outlines=[]))
                    for _st_n in ("default", "button_text", "say_dialogue"):
                        _char_sigs = {}
                        for _ch in _active_probes:
                            _sig = _glyph_sig(Text(_ch, style=_st_n, size=24, color="#ffffff", outlines=[]))
                            chk(_sig != _notdef_sig, "Tofu (.notdef) rendered for %r (U+%04X) under style=%s lang=%r mode=%s" % (_ch, ord(_ch), _st_n, _lang_val, _fmode))
                            _char_sigs[_ch] = _sig
                        chk(len(set(_char_sigs.values())) == len(_active_probes), "Duplicate glyph renders under style=%s lang=%r mode=%s" % (_st_n, _lang_val, _fmode))
                    # Ensure language switcher SC label never renders tofu even when UI is Japanese (msgothic.ttc)
                    _sc_btn_nd = _glyph_sig(Text("\uffff", font=kag_get_sc_font(), size=24, color="#ffffff", outlines=[]))
                    chk(_glyph_sig(Text("简", font=kag_get_sc_font(), size=24, color="#ffffff", outlines=[])) != _sc_btn_nd, "Tofu rendered in kag_get_sc_font() for '简'")

            # Render the exact screenshot Chinese lines in screen say, screen kag_mesframe_overlay, and screen history
            kag_set_language("zh_cn")
            kag_set_font_mode("mono")
            store.kag_mesframe_visible = True
            for _sc_line in _sc_screenshot_lines:
                kag_on_say_display(_sc_line)
                test_show_and_hide("say", who=None, what=_sc_line)
                test_show_and_hide("kag_mesframe_overlay")
                store._history_list.append(types.SimpleNamespace(who=None, what=_sc_line))
            test_show_and_hide("history")
            store._history_list[:] = []

            # Verify native top menu bar action dispatch queue
            _kag_native_menu_queue.extend(["speed:fast", "font:prop", "movie_toggle", "vol:music:80", "lang:zh_cn", "lang:ja", "speed:normal", "font:mono"])
            while _kag_native_menu_queue:
                kag_dispatch_native_menu_action()
            chk(persistent.kag_text_speed == "normal", "native menu dispatch speed failed")
            chk(persistent.kag_font_mode == "mono", "native menu dispatch font failed")
            chk(persistent.kag_language is None, "native menu dispatch lang failed")
            persistent.movieSkip = 1
            kag_set_font_mode("mono")
            kag_set_language(None)

        _run_font_render_checks()
        del _run_font_render_checks
        log_step("checked 7b: all 8 OpenType CJK fonts rendered & verified (glyph ink, 1:2 mono parity, indent, PNG)")

        # 7c. Regression check: save-slot thumbnails must capture actual gameplay frame, never UI/confirm/menu overlays
        def _run_save_thumbnail_checks():
            import glob

            def _read_slot_png(slot_idx):
                import zipfile
                pattern = os.path.join(config.savedir, kag_slot_name(slot_idx) + "-*.save")
                matches = sorted(glob.glob(pattern))
                chk(bool(matches), "No save file found for slot %d (%s)" % (slot_idx, pattern))
                if not matches:
                    return b""
                with zipfile.ZipFile(matches[0], "r") as zf:
                    return zf.read("screenshot.png")

            def _cleanup_test_slots(slot_indices):
                locks = list(persistent.kag_locks)
                bms = list(persistent.kag_bookmarks)
                dts = list(persistent.kag_dates)
                cmts = list(persistent.kag_comments)
                for idx in slot_indices:
                    locks[idx] = False
                    bms[idx] = ""
                    dts[idx] = ""
                    cmts[idx] = ""
                    for fpath in glob.glob(os.path.join(config.savedir, kag_slot_name(idx) + "*.save")):
                        try:
                            os.unlink(fpath)
                        except OSError:
                            pass
                persistent.kag_locks = locks
                persistent.kag_bookmarks = bms
                persistent.kag_dates = dts
                persistent.kag_comments = cmts

            test_slots = (20, 21, 22, 23, 24, 25, 26)
            _cleanup_test_slots(test_slots)
            _tstate = {"step": "idle", "ticks": 0, "captures": {}, "done": False, "error": None}

            def _end_interact(val):
                raise renpy.display.core.EndInteraction(val)

            def _thumb_driver():
                if _tstate["step"] == "idle" or _tstate["done"]:
                    return
                _tstate["ticks"] += 1
                try:
                    step = _tstate["step"]
                    ticks = _tstate["ticks"]
                    if step == "rclick_wait_menu":
                        if renpy.get_screen("kag_rclick_menu") and ticks >= 2:
                            _tstate["captures"]["rclick_ui"] = renpy.screenshot_to_bytes((config.thumbnail_width, config.thumbnail_height))
                            _tstate["step"] = "rclick_wait_saveload"
                            _tstate["ticks"] = 0
                            _end_interact("save")
                    elif step == "rclick_wait_saveload":
                        if renpy.get_screen("kag_save_load") and ticks >= 2:
                            # Entering kag_save_load restores pinned gameplay screenshot despite checkpoint()
                            chk(getattr(renpy.game.interface, "screenshot", None) is not None and getattr(renpy.game.interface, "screenshot", None) == getattr(renpy.game.interface, "_kag_saved_screenshot", None), "expected kag_save_load entry to restore pinned gameplay screenshot")
                            _tstate["captures"]["saveload_ui"] = renpy.screenshot_to_bytes((config.thumbnail_width, config.thumbnail_height))
                            kag_save_to_slot(20)
                            # Even if interface.screenshot is cleared while in Save/Confirm, subsequent saves still restore _kag_saved_screenshot
                            renpy.game.interface.lose_screenshot()
                            chk(getattr(renpy.game.interface, "screenshot", None) is None, "expected lose_screenshot() to clear interface.screenshot")
                            kag_save_to_slot(21)
                            renpy.game.interface.lose_screenshot()
                            _tstate["step"] = "rclick_wait_confirm"
                            _tstate["ticks"] = 0
                            renpy.run(Confirm(kag_tr("上書きセーブしますか？"), Function(kag_save_to_slot, 20)))
                    elif step == "rclick_wait_confirm":
                        if renpy.get_screen("confirm") and ticks >= 2:
                            _tstate["captures"]["confirm_ui"] = renpy.screenshot_to_bytes((config.thumbnail_width, config.thumbnail_height))
                            _tstate["step"] = "rclick_after_confirm"
                            _tstate["ticks"] = 0
                            renpy.run([Hide("confirm"), Function(kag_save_to_slot, 20)])
                    elif step == "rclick_after_confirm":
                        if not renpy.get_screen("confirm") and renpy.get_screen("kag_save_load") and ticks >= 1:
                            _tstate["step"] = "rclick_close_menu"
                            _tstate["ticks"] = 0
                            _end_interact("back")
                    elif step == "rclick_close_menu":
                        if renpy.get_screen("kag_rclick_menu") and ticks >= 1:
                            _tstate["done"] = True
                            _tstate["step"] = "idle"
                            _end_interact("close")
                    elif step == "menubar_wait_saveload":
                        if renpy.get_screen("kag_save_load") and ticks >= 2:
                            kag_save_to_slot(_tstate["target_slot"])
                            _tstate["done"] = True
                            _tstate["step"] = "idle"
                            _end_interact("back")
                    elif step == "load_switch_to_save":
                        if renpy.get_screen("kag_save_load") and ticks >= 2:
                            kag_open_saveload_from_menubar("save")
                            _tstate["step"] = "menubar_wait_saveload"
                            _tstate["ticks"] = 0
                    elif step == "about_wait_then_save":
                        if renpy.get_screen("kag_about_dialog") and ticks >= 2:
                            _tstate["captures"]["about_ui"] = renpy.screenshot_to_bytes((config.thumbnail_width, config.thumbnail_height))
                            _tstate["step"] = "about_wait_saveload_close"
                            _tstate["ticks"] = 0
                            kag_open_saveload_from_menubar("save")
                    elif step == "about_wait_saveload_close":
                        if renpy.get_screen("kag_save_load") and ticks >= 2:
                            kag_save_to_slot(_tstate["target_slot"])
                            _tstate["step"] = "about_close"
                            _tstate["ticks"] = 0
                            _end_interact("back")
                    elif step == "about_close":
                        if not renpy.get_screen("kag_save_load") and renpy.get_screen("kag_about_dialog") and ticks >= 1:
                            chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is not None, "saved screenshot must stay pinned while kag_about_dialog remains open")
                            _tstate["done"] = True
                            _tstate["step"] = "idle"
                            renpy.run(Hide("kag_about_dialog"))
                    elif step == "shortcuts_wait_then_save":
                        if renpy.get_screen("kag_shortcuts_dialog") and ticks >= 2:
                            _tstate["step"] = "shortcuts_wait_saveload_close"
                            _tstate["ticks"] = 0
                            kag_open_saveload_from_menubar("save")
                    elif step == "shortcuts_wait_saveload_close":
                        if renpy.get_screen("kag_save_load") and ticks >= 2:
                            kag_save_to_slot(_tstate["target_slot"])
                            _tstate["step"] = "shortcuts_close"
                            _tstate["ticks"] = 0
                            _end_interact("back")
                    elif step == "shortcuts_close":
                        if not renpy.get_screen("kag_save_load") and renpy.get_screen("kag_shortcuts_dialog") and ticks >= 1:
                            _tstate["done"] = True
                            _tstate["step"] = "idle"
                            renpy.run(Hide("kag_shortcuts_dialog"))
                    elif step == "history_wait_then_save":
                        if renpy.get_screen("history") and ticks >= 2:
                            _tstate["captures"]["history_ui"] = renpy.screenshot_to_bytes((config.thumbnail_width, config.thumbnail_height))
                            _tstate["step"] = "history_wait_saveload_close"
                            _tstate["ticks"] = 0
                            kag_open_saveload_from_menubar("save")
                    elif step == "history_wait_saveload_close":
                        if renpy.get_screen("kag_save_load") and ticks >= 2:
                            kag_save_to_slot(_tstate["target_slot"])
                            _tstate["step"] = "history_close"
                            _tstate["ticks"] = 0
                            _end_interact("back")
                    elif step == "history_close":
                        if not renpy.get_screen("kag_save_load") and renpy.get_screen("history") and ticks >= 1:
                            chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is not None, "saved screenshot must stay pinned while history remains open")
                            _tstate["done"] = True
                            _tstate["step"] = "idle"
                            _end_interact(None)
                    elif step == "dropdown_wait_then_save":
                        if store._kag_active_dropdown == "sys" and ticks >= 2:
                            _tstate["captures"]["dropdown_ui"] = renpy.screenshot_to_bytes((config.thumbnail_width, config.thumbnail_height))
                            _tstate["step"] = "menubar_wait_saveload"
                            _tstate["ticks"] = 0
                            kag_open_saveload_from_menubar("save")
                except renpy.display.core.EndInteraction:
                    raise
                except Exception as exc:
                    _tstate["error"] = repr(exc)
                    _tstate["done"] = True
                    _tstate["step"] = "idle"
                    if len(renpy.game.contexts) > 1 or renpy.context()._menu:
                        _end_interact(None)

            config.periodic_callbacks.append(_thumb_driver)
            try:
                kag_prepare_new_game()
                kag_set_language("zh_cn")
                kag_set_font_mode("mono")
                store.kag_rclick_enabled = True
                store.kag_history_enabled = True
                store.kag_in_title = False
                store.main_menu = False
                store._kag_active_dropdown = None

                # Render Scene A: bg001 + dialogue box
                kag_image("bg001", layer="base", page="fore")
                store.kag_mesframe_visible = True
                _scene_a_text = "小魔女「我本来就是个路痴，最不擅长跑腿了，不过这次可一定要加油才行呢。」"
                kag_on_say_display(_scene_a_text)
                renpy.show_screen("say", who=None, what=_scene_a_text)
                renpy.show_screen("kag_mesframe_overlay")
                renpy.pause(0.05, hard=True, modal=False)
                scene_a_png = renpy.screenshot_to_bytes((config.thumbnail_width, config.thumbnail_height))
                chk(scene_a_png.startswith(b"\x89PNG"), "expected valid Scene A PNG bytes")
                renpy.game.interface.lose_screenshot()
                chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is None, "clean gameplay must start with empty _kag_saved_screenshot")

                # A) Right-click menu -> Save -> multi-slot save -> overwrite confirm -> close
                _tstate.update({"step": "rclick_wait_menu", "ticks": 0, "done": False, "error": None})
                kag_handle_game_menu_request()
                chk(_tstate["error"] is None, "rclick thumbnail test error: %s" % (_tstate["error"],))
                chk(_tstate["captures"].get("rclick_ui") != scene_a_png, "headless renderer failed to reflect kag_rclick_menu change")
                chk(_tstate["captures"].get("saveload_ui") != scene_a_png, "headless renderer failed to reflect kag_save_load change")
                chk(_tstate["captures"].get("confirm_ui") != scene_a_png, "headless renderer failed to reflect confirm change")
                chk(_read_slot_png(20) == scene_a_png, "slot 20 overwrite thumbnail must match clean Scene A gameplay frame, not Save/Confirm UI")
                chk(_read_slot_png(21) == scene_a_png, "slot 21 second save in same visit must still match clean Scene A gameplay frame")
                chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is None, "returning from _kag_rclick_context must clear _kag_saved_screenshot")

                # B) Menubar -> Load -> switch to Save -> save slot 22
                renpy.pause(0.03, hard=True, modal=False)
                _tstate.update({"step": "load_switch_to_save", "ticks": 0, "done": False, "error": None, "target_slot": 22})
                kag_open_saveload_from_menubar("load")
                chk(_tstate["error"] is None, "load->save thumbnail test error: %s" % (_tstate["error"],))
                chk(_read_slot_png(22) == scene_a_png, "slot 22 load->save thumbnail must match Scene A")
                chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is None, "returning from menubar saveload must clear _kag_saved_screenshot")

                # C) About dialog open -> Menubar Save -> close About cleanly
                renpy.pause(0.03, hard=True, modal=False)
                _tstate.update({"step": "about_wait_then_save", "ticks": 0, "done": False, "error": None, "target_slot": 23})
                kag_open_about_dialog()
                while not _tstate["done"]:
                    renpy.pause(0.02, hard=True, modal=False)
                renpy.pause(0.03, hard=True, modal=False)
                chk(_tstate["error"] is None, "about->save thumbnail test error: %s" % (_tstate["error"],))
                chk(_tstate["captures"].get("about_ui") != scene_a_png, "about dialog screen failed to render distinctively")
                chk(_read_slot_png(23) == scene_a_png, "slot 23 about->save thumbnail must match Scene A, not About dialog")
                chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is None, "hiding kag_about_dialog must clear _kag_saved_screenshot")

                # D) Shortcuts dialog open -> Menubar Save -> close Shortcuts cleanly
                _tstate.update({"step": "shortcuts_wait_then_save", "ticks": 0, "done": False, "error": None, "target_slot": 24})
                kag_open_shortcuts_dialog()
                while not _tstate["done"]:
                    renpy.pause(0.02, hard=True, modal=False)
                renpy.pause(0.03, hard=True, modal=False)
                chk(_tstate["error"] is None, "shortcuts->save thumbnail test error: %s" % (_tstate["error"],))
                chk(_read_slot_png(24) == scene_a_png, "slot 24 shortcuts->save thumbnail must match Scene A")
                chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is None, "hiding kag_shortcuts_dialog must clear _kag_saved_screenshot")

                # E) History open -> Menubar Save -> close History cleanly
                _tstate.update({"step": "history_wait_then_save", "ticks": 0, "done": False, "error": None, "target_slot": 25})
                kag_open_history()
                chk(_tstate["error"] is None, "history->save thumbnail test error: %s" % (_tstate["error"],))
                chk(_read_slot_png(25) == scene_a_png, "slot 25 history->save thumbnail must match Scene A, not History screen")
                chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is None, "returning from history must clear _kag_saved_screenshot")

                # F) Fallback kag_menubar dropdown open -> Save -> verify dropdown excluded
                renpy.show_screen("kag_menubar")
                renpy.pause(0.03, hard=True, modal=False)
                pre_dropdown_png = renpy.screenshot_to_bytes((config.thumbnail_width, config.thumbnail_height))
                renpy.game.interface.lose_screenshot()
                _tstate.update({"step": "dropdown_wait_then_save", "ticks": 0, "done": False, "error": None, "target_slot": 26})
                kag_toggle_menubar_dropdown("sys")
                while not _tstate["done"]:
                    renpy.pause(0.02, hard=True, modal=False)
                chk(_tstate["error"] is None, "dropdown->save thumbnail test error: %s" % (_tstate["error"],))
                chk(_tstate["captures"].get("dropdown_ui") != pre_dropdown_png, "dropdown failed to render distinctively")
                chk(_read_slot_png(26) == pre_dropdown_png, "slot 26 thumbnail must match pre-dropdown frame")
                chk(_read_slot_png(26) != _tstate["captures"].get("dropdown_ui"), "slot 26 thumbnail must exclude open menubar dropdown")
                renpy.hide_screen("kag_menubar")
                store._kag_active_dropdown = None
                renpy.pause(0.03, hard=True, modal=False)
                chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is None, "returning from fallback menubar save must clear _kag_saved_screenshot")

                # G) Advance to Scene B (distinct background & line) -> must capture Scene B, not stale Scene A
                kag_image("bg002", layer="base", page="fore")
                _scene_b_text = "音律「现在换成第二个场景，封面应该同步更新才对。」"
                kag_on_say_display(_scene_b_text)
                renpy.show_screen("say", who=None, what=_scene_b_text)
                renpy.pause(0.05, hard=True, modal=False)
                scene_b_png = renpy.screenshot_to_bytes((config.thumbnail_width, config.thumbnail_height))
                chk(scene_b_png != scene_a_png, "Scene B PNG must differ from Scene A PNG")
                renpy.game.interface.lose_screenshot()
                _tstate.update({"step": "menubar_wait_saveload", "ticks": 0, "done": False, "error": None, "target_slot": 26})
                kag_open_saveload_from_menubar("save")
                chk(_read_slot_png(26) == scene_b_png, "slot 26 after scene transition must match Scene B, not stale Scene A")
                chk(getattr(renpy.game.interface, "_kag_saved_screenshot", None) is None, "returning from Scene B save must clear _kag_saved_screenshot")
            finally:
                if _thumb_driver in config.periodic_callbacks:
                    config.periodic_callbacks.remove(_thumb_driver)
                for scr in ("confirm", "kag_save_load", "kag_rclick_menu", "kag_about_dialog", "kag_shortcuts_dialog", "kag_menubar", "kag_mesframe_overlay", "say"):
                    if renpy.get_screen(scr):
                        renpy.hide_screen(scr)
                store._kag_active_dropdown = None
                kag_clear_saved_screenshot()
                _cleanup_test_slots(test_slots)
                kag_prepare_new_game()
                kag_set_font_mode("mono")
                kag_set_language(None)

        _run_save_thumbnail_checks()
        del _run_save_thumbnail_checks
        log_step("checked 7c: save-slot thumbnails capture clean gameplay across rclick, confirm overwrite, menubar, dialogs, history, dropdown & scene advance")

        # 8. Install live playthrough driver for Phase 2 real scenario traversal
        _smoke_install_phase2()

        if store._smoke_errors:
            raise AssertionError("PHASE 1 SMOKE TEST FAILURES:\n" + "\n".join(store._smoke_errors))
        store._kag_smoke_phase1_ok = True
        log_step("starting Phase 2 real playthrough: menu -> load -> extra -> newgame(prologue -> part_a)")

    $ persistent.firstclear = 0
    $ persistent.d_n_end = 0
    $ persistent.d_t_end = 0
    $ kag_f = KAGVars()
    jump start

# Intercept right after d_b1 starts (before 1000 lines of day 1 replay) to also exercise rclick, kag_return_to_title, d_c -> endroll_d, and firstclear=1 boot!
init 999 python:
    def _smoke_log_step(msg):
        with open(os.environ["KAG_SMOKE_LOG_FILE"], "a", encoding="utf-8") as lf:
            lf.write(msg + "\n")
        print("SMOKE:", msg, flush=True)

    def _smoke_chk(cond, msg):
        if not cond:
            store._smoke_errors.append(msg)
            _smoke_log_step("FAIL: " + msg)

    def _smoke_fast_say(who, what, *args, **kwargs):
        orig_pause = renpy._kag_smoke_orig_funcs[1]
        store._smoke_say_count += 1
        cur_node = renpy.game.context().current
        if cur_node:
            store._smoke_visited_labels.add(str(cur_node))
        kag_on_say_display(what)
        # Resolve Character/_Extend so screen say always receives str or None
        who_str = who if isinstance(who, str) else getattr(who, "name", None)
        if who is extend or store._smoke_say_count % 120 == 1:
            try:
                renpy.show_screen("say", who=who_str, what=what)
                orig_pause(0.01, hard=True, modal=False)
            finally:
                renpy.hide_screen("say")

    def _smoke_fast_pause(delay=None, **kwargs):
        return False

    def _smoke_fast_with(trans, always=False, paired=None, clear=True):
        return False

    def _smoke_fast_movie(filename, delay=None, loops=0, stop_music=True):
        return False

    def _smoke_fast_is_playing(channel="music"):
        orig_is_playing = renpy._kag_smoke_orig_funcs[5]
        # During Phase 2 playthrough fast-forward, avoid blocking in kag_ws / kag_wl
        if channel != "music" or not getattr(store, "kag_bgm_looping", True):
            return False
        return orig_is_playing(channel=channel)

    def _smoke_fast_ui_interact(*args, **kwargs):
        orig_ui_interact = renpy._kag_smoke_orig_funcs[6]
        # Allow _hide_windows (msgclr) ui.interact to render one hidden-window frame then auto-dismiss
        if getattr(store, "_windows_hidden", False):
            ui.pausebehavior(0.01)
        return orig_ui_interact(*args, **kwargs)

    def _smoke_driven_call_screen(scr_name, *args, **kwargs):
        orig_pause = renpy._kag_smoke_orig_funcs[1]
        # Actually render the screen before returning the scripted action
        try:
            renpy.show_screen(scr_name, *args, **kwargs)
            orig_pause(0.01, hard=True, modal=False)
        finally:
            renpy.hide_screen(scr_name)

        if scr_name == "kag_input_dialog":
            return "ピリカピリララ"
        if scr_name == "kag_rclick_menu":
            if store._smoke_rclick_queue:
                return store._smoke_rclick_queue.pop(0)
            return "close"
        if scr_name == "kag_save_load":
            return "back"
        if scr_name == "confirm":
            return True
        if scr_name != "kag_interactive_menu":
            return None

        buttons = kwargs.get("buttons", [])
        links = kwargs.get("links", [])
        stage = store._smoke_phase2_stage

        def pick_target(tgt):
            for it in list(buttons) + list(links):
                if it.get("target") == tgt:
                    return (it.get("storage"), it.get("target"), it.get("exp"), it.get("current_stem"))
            raise AssertionError("Expected target %r not found in stage %r (buttons=%r links=%r)" % (
                tgt, stage, [b.get("target") for b in buttons], [l.get("target") for l in links]
            ))

        if len(renpy.get_return_stack()) > 1:
            raise AssertionError("Leaked return_stack frames (%d): %r" % (len(renpy.get_return_stack()), renpy.get_return_stack()))

        # Main Title Menu orchestration across all features!
        if buttons and buttons[0].get("current_stem") == "menu":
            _smoke_chk(store.kag_mesframe_visible is False, "mesFrame bubble must be hidden on title menu (stage=%r)" % (stage,))
            _smoke_chk(store.kag_hold_box_active is False, "hold_box_active must be False on title menu (stage=%r)" % (stage,))
            if stage == "boot_menu":
                _smoke_chk(store.kag_in_title is True, "kag_in_title must be True on initial title menu")
                store._smoke_phase2_stage = "load_from_title"
                _smoke_log_step("reached title menu directly on boot (firstclear=0) -> entering loadgame")
                return pick_target("*loadgame")
            elif stage == "load_from_title":
                store._smoke_phase2_stage = "extra"
                _smoke_log_step("returned from loadgame -> entering omake/extra")
                return pick_target("*omake")
            elif stage == "extra":
                store._smoke_phase2_stage = "newgame"
                _smoke_log_step("returned from extra -> entering newgame (prologue -> part_a)")
                return pick_target("*newgame")
            elif stage == "after_backtitle":
                _smoke_chk(store.kag_in_title is True, "kag_in_title must be True after kag_return_to_title")
                store._smoke_phase2_stage = "endroll"
                _smoke_log_step("returned to title via kag_return_to_title() -> starting d_c -> endroll_d")
                if renpy.get_return_stack():
                    renpy.pop_call()
                renpy.jump("kag__smoke_test_start_dc")
            elif stage == "endroll":
                _smoke_chk(persistent.firstclear == 1, "endroll_d must set persistent.firstclear = 1")
                store._smoke_phase2_stage = "verify_start_firstclear1"
                _smoke_log_step("returned to menu after endroll_d (firstclear=1 verified!) -> testing boot with firstclear=1")
                if renpy.get_return_stack():
                    renpy.pop_call()
                renpy.jump("start")
            elif stage == "verify_start_firstclear1":
                store._smoke_phase2_stage = "test_rclick_and_save"
                _smoke_log_step("verified label start with firstclear=1 skipped prologue directly to menu")
                if renpy.get_return_stack():
                    renpy.pop_call()
                renpy.jump("kag__smoke_test_phase3")
            else:
                raise AssertionError("Unexpected menu entry at stage %r" % (stage,))

        if buttons and buttons[0].get("current_stem") == "extra" or (links and links[0].get("current_stem") == "extra"):
            if not store._smoke_extra_queue:
                raise AssertionError("extra queue exhausted unexpectedly")
            nxt = store._smoke_extra_queue.pop(0)
            _smoke_log_step("extra -> " + nxt)
            return pick_target(nxt)

        # Option menu
        if links and links[0].get("current_stem") == "option":
            return pick_target("*yes")

        # Inside part_a choices -> pick AAAABA route leading into d_b1
        if links and links[0].get("current_stem") == "part_a":
            for it in links:
                if it.get("target") == "*choices05-2":
                    _smoke_log_step("part_a choice -> *choices05-2 (route AAAABA)")
                    return (it.get("storage"), it.get("target"), it.get("exp"), it.get("current_stem"))
            _smoke_log_step("part_a choice -> %s" % links[0].get("target"))
            return (links[0].get("storage"), links[0].get("target"), links[0].get("exp"), links[0].get("current_stem"))

        if links:
            return (links[0].get("storage"), links[0].get("target"), links[0].get("exp"), links[0].get("current_stem"))
        if buttons:
            return (buttons[0].get("storage"), buttons[0].get("target"), buttons[0].get("exp"), buttons[0].get("current_stem"))
        return None

    def _smoke_install_phase2():
        renpy._kag_smoke_orig_funcs = (
            renpy.say,
            renpy.pause,
            renpy.call_screen,
            renpy.with_statement,
            renpy.movie_cutscene,
            renpy.music.is_playing,
            ui.interact,
        )
        store._smoke_phase2_stage = "boot_menu"
        store._smoke_saw_prologue = False
        store._smoke_visited_labels = set()
        store._smoke_say_count = 0
        store._smoke_extra_queue = [
            "*gallery", "*page00", "*page01", "*page02", "*page03", "*page04", "*page05", "*page06",
            "*backselect", "*return_s",
            "*s_doremi", "*return_s0",
            "*s_hazuki", "*return_s0",
            "*s_ai", "*return_s0",
            "*s_onpu", "*return_s0",
            "*s_momo", "*return_s0",
            "*s_hana", "*return_s0",
            "*s_etc", "*return_s0",
            "*resetmenu", "*back",
        ]
        store._smoke_rclick_queue = ["save", "load", "msgclr", "msgskip"]
        renpy.say = _smoke_fast_say
        renpy.exports.say = _smoke_fast_say
        renpy.pause = _smoke_fast_pause
        renpy.call_screen = _smoke_driven_call_screen
        renpy.with_statement = _smoke_fast_with
        renpy.movie_cutscene = _smoke_fast_movie
        renpy.music.is_playing = _smoke_fast_is_playing
        ui.interact = _smoke_fast_ui_interact
        renpy.ui.interact = _smoke_fast_ui_interact

    def _smoke_uninstall_phase2():
        orig_say, orig_pause, orig_call_screen, orig_with, orig_movie, orig_is_playing, orig_ui_interact = renpy._kag_smoke_orig_funcs
        renpy.say = orig_say
        renpy.exports.say = orig_say
        renpy.pause = orig_pause
        renpy.call_screen = orig_call_screen
        renpy.with_statement = orig_with
        renpy.movie_cutscene = orig_movie
        renpy.music.is_playing = orig_is_playing
        ui.interact = orig_ui_interact
        renpy.ui.interact = orig_ui_interact

    def _kag_smoke_stmt_tracer(name):
        if getattr(store, "_kag_smoke_phase1_ok", False):
            ctx_cur = str(getattr(renpy.game.context(), "current", "") or "")
            stage = getattr(store, "_smoke_phase2_stage", "")
            if stage in ("boot_menu", "verify_start_firstclear1") and "kag_prologue_gamestart" in ctx_cur:
                raise AssertionError("label start wrongly entered prologue instead of title menu (stage=%r)!" % (stage,))
            if stage == "newgame" and "kag_prologue_gamestart" in ctx_cur:
                store._smoke_saw_prologue = True
            if stage == "newgame" and "kag_d_b1_d__dash__01_00" in ctx_cur:
                assert getattr(store, "_smoke_saw_prologue", False), "*newgame did not pass through prologue before part_a/d_b1!"
                assert len(renpy.get_return_stack()) == 0, "Leaked return_stack before d_b1: %r" % (renpy.get_return_stack(),)
                store._smoke_phase2_stage = "rclick_then_backtitle"
                with open(os.environ["KAG_SMOKE_LOG_FILE"], "a", encoding="utf-8") as lf:
                    lf.write("newgame passed prologue -> part_a (route=%s) into kag_d_b1 with clean return_stack!\n" % getattr(kag_f, "route", "?"))
                renpy.jump("kag__smoke_test_phase2_rclick_and_endroll")

    if "KAG_SMOKE_LOG_FILE" in os.environ:
        config.statement_callbacks.append(_kag_smoke_stmt_tracer)

        def _kag_smoke_exc_handler(te):
            import sys as _sys
            msg = getattr(te, "full", str(te))
            with open(os.environ["KAG_SMOKE_LOG_FILE"], "a", encoding="utf-8") as lf:
                lf.write("EXCEPTION:\n" + msg + "\n")
            print("EXCEPTION:", msg, file=_sys.stderr, flush=True)
            renpy.quit(status=1)
            return True

        config.exception_handler = _kag_smoke_exc_handler

label kag__smoke_test_phase2_rclick_and_endroll:
    python hide:
        # Exercise full _kag_rclick_context loop (save -> back -> load -> back -> msgclr -> msgskip)
        store._kag_hook_msgskip = False
        renpy.call_in_new_context("_kag_rclick_context")
        assert config.skipping == "slow", "msgskip in _kag_rclick_context must set config.skipping='slow'"
        config.skipping = None
        # Exercise kag_return_to_title from nested _kag_rclick_context back to top-context menu
        store._smoke_rclick_queue = ["backtitle"]
        store._smoke_phase2_stage = "after_backtitle"
        renpy.call_in_new_context("_kag_rclick_context")
    return

label kag__smoke_test_start_dc:
    $ kag_prepare_new_game()
    $ kag_f.judgeflag = 3
    jump kag_d_c_gamestart

label kag__smoke_test_phase3:
    python hide:
        _smoke_uninstall_phase2()
        _smoke_log_step("saving slot 1 and testing live renpy.load()")
    $ kag_prepare_new_game()
    $ kag_f.test_loaded_flag = 42
    $ kag_set_bookmark("煙テスト読込確認")
    $ renpy.pause(0.01, hard=True, checkpoint=True)
    $ renpy.checkpoint(hard=True)
    $ renpy.pause(0.01, hard=True, checkpoint=True)
    $ renpy.checkpoint(hard=True)
    $ renpy.take_screenshot((config.thumbnail_width, config.thumbnail_height))
    $ kag_save_to_slot(1)
    $ kag_load_from_slot(1)
    return

label after_load:
    python:
        if getattr(store, "_kag_smoke_phase1_ok", False):
            assert kag_f.test_loaded_flag == 42, "Loaded state missing kag_f.test_loaded_flag"
            assert not kag_in_title, "kag_in_title must be False after load"
            assert kag_rclick_enabled, "kag_rclick_enabled must be True after load"
            if store._smoke_errors:
                raise AssertionError("SMOKE TEST FAILURES:\n" + "\n".join(store._smoke_errors))
            with open(os.environ["KAG_SMOKE_LOG_FILE"], "a", encoding="utf-8") as lf:
                lf.write("SMOKE: after_load verified!\n")
            with open(os.environ["KAG_SMOKE_RESULT_FILE"], "w", encoding="utf-8") as f:
                f.write("ALL_RUNTIME_SMOKE_TESTS_AND_PLAYTHROUGH_PASSED\n")
            renpy.quit()
    return
'''


def main() -> int:
    smoke_path = GAME_DIR / "_runtime_smoke_test.rpy"
    saves_dir = PROJECT_DIR / "game" / "saves"
    had_saves_dir = saves_dir.exists()
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        savedir = tmp_path / "saves"
        savedir.mkdir()
        saves_backup = tmp_path / "saves_backup"
        if had_saves_dir:
            shutil.copytree(saves_dir, saves_backup)
        result_file = tmp_path / "result.txt"
        log_file = tmp_path / "progress.log"
        png_file = tmp_path / "font_render.png"

        smoke_lines = SMOKE_RPY.splitlines()
        warp_line = None
        for idx, line in enumerate(smoke_lines, 1):
            if line.strip() in ("python:", "python hide:"):
                warp_line = idx
                break
        assert warp_line is not None

        try:
            smoke_path.write_text(SMOKE_RPY, encoding="utf-8")
            rpyc_path = GAME_DIR / "_runtime_smoke_test.rpyc"
            if rpyc_path.exists():
                rpyc_path.unlink()

            env = os.environ.copy()
            env["SDL_VIDEODRIVER"] = "dummy"
            env["SDL_AUDIODRIVER"] = "dummy"
            env["RENPY_PERFORMANCE_TEST"] = "0"
            env["RENPY_SIMPLE_EXCEPTIONS"] = "1"
            env["KAG_SMOKE_RESULT_FILE"] = str(result_file)
            env["KAG_SMOKE_LOG_FILE"] = str(log_file)
            env["KAG_SMOKE_PNG_FILE"] = str(png_file)

            cmd = [
                str(RENPY_SH),
                str(PROJECT_DIR),
                "--savedir",
                str(savedir),
                "--warp",
                f"game/_runtime_smoke_test.rpy:{warp_line}",
            ]
            print("Running headless Ren'Py runtime smoke & playthrough test...")
            try:
                proc = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=60)
            except subprocess.TimeoutExpired as exc:
                print("TIMEOUT after 60s!")
                if log_file.exists():
                    print("=== progress.log ===\n", log_file.read_text(encoding="utf-8"))
                else:
                    print("=== NO progress.log WRITTEN ===")
                if exc.stdout:
                    print("=== STDOUT ===\n", exc.stdout)
                if exc.stderr:
                    print("=== STDERR ===\n", exc.stderr)
                return 1

            if log_file.exists():
                print("=== progress.log ===\n", log_file.read_text(encoding="utf-8"))
            if proc.returncode != 0 or not result_file.exists():
                print("Return code:", proc.returncode)
                print("=== STDOUT ===\n", proc.stdout)
                print("=== STDERR ===\n", proc.stderr)
                tb = PROJECT_DIR / "traceback.txt"
                if tb.exists():
                    print("=== traceback.txt ===\n", tb.read_text(encoding="utf-8", errors="replace"))
                return 1

            print("Smoke test result:", result_file.read_text(encoding="utf-8").strip())
            return 0
        finally:
            if smoke_path.exists():
                smoke_path.unlink()
            rpyc_path = GAME_DIR / "_runtime_smoke_test.rpyc"
            if rpyc_path.exists():
                rpyc_path.unlink()
            if not had_saves_dir:
                shutil.rmtree(saves_dir, ignore_errors=True)
            elif saves_backup.exists():
                shutil.rmtree(saves_dir, ignore_errors=True)
                shutil.copytree(saves_backup, saves_dir)


if __name__ == "__main__":
    sys.exit(main())
