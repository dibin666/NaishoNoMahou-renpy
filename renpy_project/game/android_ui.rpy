# Android Portrait / Landscape Orientation Switcher & Bottom Touch Control Deck

default persistent.kag_android_orientation = "portrait"
default _kag_android_stage_pos = (0, 0)
default _kag_android_bar_bottom_pad = 28
default _kag_android_vw = 800
default _kag_android_vh = 600

init -5 python:
    def kag_is_android_ui():
        return bool(renpy.android or os.environ.get("KAG_FORCE_ANDROID_UI") == "1")

    def kag_get_android_orientation():
        mode = getattr(persistent, "kag_android_orientation", "portrait")
        return "landscape" if mode == "landscape" else "portrait"

    def _kag_query_android_insets_px():
        if not renpy.android:
            return (0, 0)
        try:
            from jnius import autoclass
            BuildVersion = autoclass("android.os.Build$VERSION")
            PythonSDLActivity = autoclass("org.renpy.android.PythonSDLActivity")
            act = PythonSDLActivity.mActivity
            if act is None:
                return (0, 0)
            win = act.getWindow()
            if win is None:
                return (0, 0)
            decor = win.getDecorView()
            if decor is None:
                return (0, 0)
            insets = decor.getRootWindowInsets()
            if insets is None:
                return (0, 0)
            top_px = 0
            bot_px = 0
            if int(BuildVersion.SDK_INT) >= 28:
                cutout = insets.getDisplayCutout()
                if cutout is not None:
                    top_px = max(top_px, int(cutout.getSafeInsetTop()))
                    bot_px = max(bot_px, int(cutout.getSafeInsetBottom()))
            if int(BuildVersion.SDK_INT) >= 30:
                WindowInsetsType = autoclass("android.view.WindowInsets$Type")
                sys_insets = insets.getInsets(WindowInsetsType.systemBars() | WindowInsetsType.displayCutout())
                if sys_insets is not None:
                    top_px = max(top_px, int(sys_insets.top))
                    bot_px = max(bot_px, int(sys_insets.bottom))
            else:
                top_px = max(top_px, int(insets.getStableInsetTop()))
                bot_px = max(bot_px, int(insets.getStableInsetBottom()))
            return (max(0, top_px), max(0, bot_px))
        except Exception:
            return (0, 0)

    def _kag_compute_android_geometry():
        mode = kag_get_android_orientation()
        pw, ph = (0, 0)
        try:
            if renpy.display.draw is not None:
                pw, ph = renpy.get_physical_size()
        except Exception:
            pw, ph = (0, 0)

        short_e = min(pw, ph) if (pw > 0 and ph > 0) else 0
        long_e = max(pw, ph) if (pw > 0 and ph > 0) else 0
        ratio = max(1.3333, min(2.45, float(long_e) / float(short_e))) if short_e > 0 else (16.0 / 9.0)

        top_px, bot_px = _kag_query_android_insets_px()

        if mode == "portrait":
            target_w = 800
            target_h = max(1040, int(round(800.0 * ratio)))
            if short_e > 0 and top_px > 0:
                top_v = int(round(float(top_px) * 800.0 / float(short_e)))
                top_pad = max(32, min(110, top_v + 8))
            else:
                top_pad = 40 if target_h >= 1200 else 20
            if short_e > 0 and bot_px > 0:
                bot_v = int(round(float(bot_px) * 800.0 / float(short_e)))
                bot_pad = max(24, min(90, bot_v + 8))
            else:
                bot_pad = 28 if target_h >= 1200 else 16
            # Ensure bottom deck keeps comfortable room even on short aspect ratios
            if top_pad + 600 + 260 > target_h:
                top_pad = max(12, target_h - 600 - 260)
            stage_x = 0
            stage_y = top_pad
        else:
            if short_e > 0 and bot_px > 0:
                bot_v = int(round(float(bot_px) * 668.0 / float(short_e)))
                bot_pad = max(10, min(42, bot_v + 6))
            else:
                bot_pad = 12
            bar_h = 58
            target_h = 600 + bar_h + bot_pad
            target_w = max(800, int(round(float(target_h) * ratio)))
            stage_x = max(0, (target_w - 800) // 2)
            stage_y = 0

        return (target_w, target_h, stage_x, stage_y, bot_pad)

    def kag_sync_android_layout(force=False):
        if not kag_is_android_ui():
            if config.screen_width != 800 or config.screen_height != 600:
                config.screen_width = 800
                config.screen_height = 600
                persistent._virtual_size = (800, 600)
                _preferences.virtual_size = (800, 600)
            store._kag_android_vw = 800
            store._kag_android_vh = 600
            store._kag_android_stage_pos = (0, 0)
            config.layer_transforms[None] = []
            return False

        target_w, target_h, stage_x, stage_y, bot_pad = _kag_compute_android_geometry()
        changed = (
            force
            or config.screen_width != target_w
            or config.screen_height != target_h
            or getattr(store, "_kag_android_vw", None) != target_w
            or getattr(store, "_kag_android_vh", None) != target_h
            or getattr(store, "_kag_android_stage_pos", None) != (stage_x, stage_y)
            or getattr(store, "_kag_android_bar_bottom_pad", None) != bot_pad
        )

        config.screen_width = target_w
        config.screen_height = target_h
        store._kag_android_vw = target_w
        store._kag_android_vh = target_h
        persistent._virtual_size = (target_w, target_h)
        _preferences.virtual_size = (target_w, target_h)
        store._kag_android_stage_pos = (stage_x, stage_y)
        store._kag_android_bar_bottom_pad = bot_pad
        config.layer_transforms[None] = [Transform(xpos=stage_x, ypos=stage_y)]

        rd = renpy.display
        if rd.draw is not None and getattr(rd.draw, "virtual_size", None) != (target_w, target_h):
            rd.draw.virtual_size = (target_w, target_h)
            rd.draw.on_resize()
            if rd.interface is not None:
                rd.interface.kill_textures(keep_const_size=False)
                rd.interface.force_redraw = True
            return True
        if changed and rd.interface is not None:
            rd.interface.force_redraw = True
        return changed

    def kag_apply_android_orientation(mode=None):
        if mode is None:
            mode = kag_get_android_orientation()
        mode = "landscape" if mode == "landscape" else "portrait"
        persistent.kag_android_orientation = mode

        if renpy.android:
            try:
                from jnius import autoclass
                ActivityInfo = autoclass("android.content.pm.ActivityInfo")
                PythonSDLActivity = autoclass("org.renpy.android.PythonSDLActivity")
                act = PythonSDLActivity.mActivity
                if act is not None:
                    req = (
                        ActivityInfo.SCREEN_ORIENTATION_SENSOR_LANDSCAPE
                        if mode == "landscape"
                        else ActivityInfo.SCREEN_ORIENTATION_PORTRAIT
                    )
                    act.setRequestedOrientation(req)
            except Exception as exc:
                renpy.log("Android setRequestedOrientation skipped: %r" % (exc,))

        kag_sync_android_layout(force=True)

    def kag_toggle_android_orientation():
        cur = kag_get_android_orientation()
        nxt = "landscape" if cur == "portrait" else "portrait"
        kag_apply_android_orientation(nxt)
        try:
            renpy.restart_interaction()
        except Exception:
            pass

    def kag_open_android_menu():
        kag_capture_gameplay_screenshot(force=True)
        if not renpy.get_screen("kag_android_menu"):
            renpy.show_screen("kag_android_menu")
            renpy.restart_interaction()

    def kag_toggle_android_menu():
        if renpy.get_screen("kag_android_menu"):
            renpy.hide_screen("kag_android_menu")
            if kag_is_clean_gameplay(excluding_screen="kag_android_menu"):
                kag_clear_saved_screenshot()
            renpy.restart_interaction()
        else:
            kag_open_android_menu()

    _kag_android_last_phys_size = None

    def kag_periodic_android_layout():
        global _kag_android_last_phys_size
        if not kag_is_android_ui():
            return
        try:
            phys = renpy.get_physical_size() if renpy.display.draw is not None else None
        except Exception:
            phys = None
        if phys != _kag_android_last_phys_size:
            _kag_android_last_phys_size = phys
            if kag_sync_android_layout(force=False):
                try:
                    renpy.restart_interaction()
                except Exception:
                    pass

init 999 python:
    if "kag_android_backdrop" not in config.always_shown_screens:
        config.always_shown_screens.append("kag_android_backdrop")
    if "kag_android_controls" not in config.overlay_screens:
        config.overlay_screens.append("kag_android_controls")
    if kag_periodic_android_layout not in config.periodic_callbacks:
        config.periodic_callbacks.append(kag_periodic_android_layout)
    if kag_sync_android_layout not in config.after_load_callbacks:
        config.after_load_callbacks.append(kag_sync_android_layout)
    kag_sync_android_layout(force=True)

screen kag_android_backdrop():
    layer "bottom"
    zorder -100
    if kag_is_android_ui():
        add Solid("#1a0918", xysize=(_kag_android_vw, _kag_android_vh))

screen kag_android_controls():
    layer "top"
    zorder 100
    if kag_is_android_ui():
        $ _and_mode = kag_get_android_orientation()
        $ _vw = _kag_android_vw
        $ _vh = _kag_android_vh
        $ _sx, _sy = _kag_android_stage_pos
        $ _bot_pad = _kag_android_bar_bottom_pad
        $ _overlay_busy = kag_in_overlay_menu()
        $ _text_input_busy = kag_in_text_input()
        $ _menu_open = bool(renpy.get_screen("kag_android_menu"))
        $ _skip_active = bool(renpy.is_skipping())
        $ _auto_active = bool(preferences.afm_enable)
        $ _can_play_ctrl = (not _overlay_busy and not kag_in_title)
        $ _can_orient = (not _text_input_busy and not renpy.get_screen("confirm"))
        $ _can_menu = (not _text_input_busy and not renpy.get_screen("confirm") and (not _overlay_busy or _menu_open))
        $ _fnt = kag_get_active_font()

        # Top safe-area header mask above the 800x600 stage
        if _sy > 0:
            add Solid("#1a0918", xpos=0, ypos=0, xsize=_vw, ysize=_sy)
            add Solid("#ff4da666", xpos=0, ypos=max(0, _sy - 2), xsize=_vw, ysize=2)

        # Left & right masks in landscape mode
        if _sx > 0:
            add Solid("#1a0918", xpos=0, ypos=_sy, xsize=_sx, ysize=600)
            add Solid("#ff4da655", xpos=max(0, _sx - 2), ypos=_sy, xsize=2, ysize=600)
        $ _rx = _sx + 800
        if _rx < _vw:
            add Solid("#1a0918", xpos=_rx, ypos=_sy, xsize=(_vw - _rx), ysize=600)
            add Solid("#ff4da655", xpos=_rx, ypos=_sy, xsize=2, ysize=600)

        if _and_mode == "portrait":
            $ _deck_y = _sy + 600
            $ _deck_h = max(0, _vh - _deck_y)
            $ _compact = (_deck_h < 340)
            $ _btn_h = 62 if _compact else 82
            $ _row_gap = 10 if _compact else 14
            $ _dock_pad_top = 12 if _compact else 18
            $ _dock_h = _dock_pad_top + _btn_h * 2 + _row_gap + max(16, _bot_pad)
            $ _dock_y = max(_deck_y + 2, _vh - _dock_h)
            $ _touch_h = max(0, _dock_y - (_deck_y + 2))

            add Solid("#ff4da6", xpos=0, ypos=_deck_y, xsize=_vw, ysize=2)

            # Non-blocking lower touch zone (tapping advances dialogue / waits)
            if _touch_h > 0:
                add Solid("#1e0b1c", xpos=0, ypos=(_deck_y + 2), xsize=_vw, ysize=_touch_h)
                if _touch_h >= 120:
                    $ _card_pad_y = 14 if _touch_h < 220 else 24
                    $ _card_h = max(84, _touch_h - _card_pad_y * 2)
                    frame:
                        xpos 20
                        ypos (_deck_y + 2 + _card_pad_y)
                        xsize 760
                        ysize _card_h
                        background "#2b1128cc"
                        padding (20, 14)
                        vbox align (0.5, 0.5) spacing 10:
                            if _skip_active:
                                text kag_tr("スキップ中...") xalign 0.5 font _fnt size 20 bold True color "#ff88cc"
                            elif _auto_active:
                                text kag_tr("オート再生中...") xalign 0.5 font _fnt size 20 bold True color "#ff88cc"
                            elif not kag_in_title and kag_current_bookmark:
                                $ _bm_disp = kag_tr(kag_current_bookmark)
                                text _bm_disp xalign 0.5 font kag_get_dialogue_font(_bm_disp) size 18 color "#ffd6eb"

                            if kag_in_title or kag_menu_buttons or kag_menu_links:
                                text kag_tr("上の画面のボタンや選択肢をタップしてください") xalign 0.5 text_align 0.5 font _fnt size 19 color "#d6b8cc"
                            else:
                                text kag_tr("ここ、または画面をタップして次へ") xalign 0.5 text_align 0.5 font _fnt size 21 color "#f5dceb"

            # Bottom 2x4 Action Button Dock
            frame:
                xpos 0
                ypos _dock_y
                xsize _vw
                ysize max(0, _vh - _dock_y)
                background "#240d22"
                padding (14, _dock_pad_top, 14, max(12, _bot_pad))
                vbox spacing _row_gap xalign 0.5:
                    hbox spacing 14 xalign 0.5:
                        textbutton kag_tr("履歴"):
                            xsize 182
                            ysize _btn_h
                            background "#4d2048"
                            hover_background "#ff0099"
                            insensitive_background "#2d142a"
                            text_font _fnt
                            text_size 21
                            text_bold True
                            text_color "#ffffff"
                            text_insensitive_color "#7c5a76"
                            text_align (0.5, 0.5)
                            sensitive (_can_play_ctrl and kag_history_enabled)
                            action Function(kag_open_history)
                        textbutton kag_tr("スキップ"):
                            xsize 182
                            ysize _btn_h
                            background ("#ff0099" if _skip_active else "#4d2048")
                            hover_background "#ff33aa"
                            insensitive_background "#2d142a"
                            text_font _fnt
                            text_size 21
                            text_bold True
                            text_color "#ffffff"
                            text_insensitive_color "#7c5a76"
                            text_align (0.5, 0.5)
                            sensitive (_can_play_ctrl and kag_clickskip_enabled)
                            action Function(kag_start_skip)
                        textbutton kag_tr("オート"):
                            xsize 182
                            ysize _btn_h
                            background ("#ff0099" if _auto_active else "#4d2048")
                            hover_background "#ff33aa"
                            insensitive_background "#2d142a"
                            text_font _fnt
                            text_size 21
                            text_bold True
                            text_color "#ffffff"
                            text_insensitive_color "#7c5a76"
                            text_align (0.5, 0.5)
                            sensitive _can_play_ctrl
                            action Preference("auto-forward", "toggle")
                        textbutton kag_tr("非表示"):
                            xsize 182
                            ysize _btn_h
                            background "#4d2048"
                            hover_background "#ff0099"
                            insensitive_background "#2d142a"
                            text_font _fnt
                            text_size 21
                            text_bold True
                            text_color "#ffffff"
                            text_insensitive_color "#7c5a76"
                            text_align (0.5, 0.5)
                            sensitive _can_play_ctrl
                            action HideInterface()
                    hbox spacing 14 xalign 0.5:
                        textbutton kag_tr("セーブ"):
                            xsize 182
                            ysize _btn_h
                            background "#4d2048"
                            hover_background "#ff0099"
                            insensitive_background "#2d142a"
                            text_font _fnt
                            text_size 21
                            text_bold True
                            text_color "#ffffff"
                            text_insensitive_color "#7c5a76"
                            text_align (0.5, 0.5)
                            sensitive (_can_play_ctrl and kag_rclick_enabled)
                            action Function(kag_open_saveload_from_menubar, "save")
                        textbutton kag_tr("ロード"):
                            xsize 182
                            ysize _btn_h
                            background "#4d2048"
                            hover_background "#ff0099"
                            insensitive_background "#2d142a"
                            text_font _fnt
                            text_size 21
                            text_bold True
                            text_color "#ffffff"
                            text_insensitive_color "#7c5a76"
                            text_align (0.5, 0.5)
                            sensitive (not _overlay_busy)
                            action Function(kag_open_saveload_from_menubar, "load")
                        textbutton kag_tr("横画面"):
                            xsize 182
                            ysize _btn_h
                            background "#6b2661"
                            hover_background "#ff0099"
                            insensitive_background "#2d142a"
                            text_font _fnt
                            text_size 21
                            text_bold True
                            text_color "#ffe0f0"
                            text_insensitive_color "#7c5a76"
                            text_align (0.5, 0.5)
                            sensitive _can_orient
                            action Function(kag_toggle_android_orientation)
                        textbutton kag_tr("メニュー"):
                            xsize 182
                            ysize _btn_h
                            background ("#ff0099" if _menu_open else "#4d2048")
                            hover_background "#ff33aa"
                            insensitive_background "#2d142a"
                            text_font _fnt
                            text_size 21
                            text_bold True
                            text_color "#ffffff"
                            text_insensitive_color "#7c5a76"
                            text_align (0.5, 0.5)
                            sensitive _can_menu
                            action Function(kag_toggle_android_menu)
        else:
            # Landscape Bottom 1x8 Action Bar
            $ _bar_y = 600
            $ _bar_h = max(56, _vh - _bar_y)
            $ _l_btn_h = max(42, min(50, _bar_h - max(8, _bot_pad) - 8))
            $ _l_btn_w = max(84, min(140, (_vw - 40 - 7 * 8) // 8))

            add Solid("#ff4da6", xpos=0, ypos=_bar_y, xsize=_vw, ysize=2)
            frame:
                xpos 0
                ypos (_bar_y + 2)
                xsize _vw
                ysize max(0, _vh - (_bar_y + 2))
                background "#240d22"
                padding (16, 4, 16, max(6, _bot_pad))
                hbox spacing 8 align (0.5, 0.5):
                    textbutton kag_tr("履歴"):
                        xsize _l_btn_w
                        ysize _l_btn_h
                        background "#4d2048"
                        hover_background "#ff0099"
                        insensitive_background "#2d142a"
                        text_font _fnt
                        text_size 18
                        text_bold True
                        text_color "#ffffff"
                        text_insensitive_color "#7c5a76"
                        text_align (0.5, 0.5)
                        sensitive (_can_play_ctrl and kag_history_enabled)
                        action Function(kag_open_history)
                    textbutton kag_tr("スキップ"):
                        xsize _l_btn_w
                        ysize _l_btn_h
                        background ("#ff0099" if _skip_active else "#4d2048")
                        hover_background "#ff33aa"
                        insensitive_background "#2d142a"
                        text_font _fnt
                        text_size 18
                        text_bold True
                        text_color "#ffffff"
                        text_insensitive_color "#7c5a76"
                        text_align (0.5, 0.5)
                        sensitive (_can_play_ctrl and kag_clickskip_enabled)
                        action Function(kag_start_skip)
                    textbutton kag_tr("オート"):
                        xsize _l_btn_w
                        ysize _l_btn_h
                        background ("#ff0099" if _auto_active else "#4d2048")
                        hover_background "#ff33aa"
                        insensitive_background "#2d142a"
                        text_font _fnt
                        text_size 18
                        text_bold True
                        text_color "#ffffff"
                        text_insensitive_color "#7c5a76"
                        text_align (0.5, 0.5)
                        sensitive _can_play_ctrl
                        action Preference("auto-forward", "toggle")
                    textbutton kag_tr("非表示"):
                        xsize _l_btn_w
                        ysize _l_btn_h
                        background "#4d2048"
                        hover_background "#ff0099"
                        insensitive_background "#2d142a"
                        text_font _fnt
                        text_size 18
                        text_bold True
                        text_color "#ffffff"
                        text_insensitive_color "#7c5a76"
                        text_align (0.5, 0.5)
                        sensitive _can_play_ctrl
                        action HideInterface()
                    textbutton kag_tr("セーブ"):
                        xsize _l_btn_w
                        ysize _l_btn_h
                        background "#4d2048"
                        hover_background "#ff0099"
                        insensitive_background "#2d142a"
                        text_font _fnt
                        text_size 18
                        text_bold True
                        text_color "#ffffff"
                        text_insensitive_color "#7c5a76"
                        text_align (0.5, 0.5)
                        sensitive (_can_play_ctrl and kag_rclick_enabled)
                        action Function(kag_open_saveload_from_menubar, "save")
                    textbutton kag_tr("ロード"):
                        xsize _l_btn_w
                        ysize _l_btn_h
                        background "#4d2048"
                        hover_background "#ff0099"
                        insensitive_background "#2d142a"
                        text_font _fnt
                        text_size 18
                        text_bold True
                        text_color "#ffffff"
                        text_insensitive_color "#7c5a76"
                        text_align (0.5, 0.5)
                        sensitive (not _overlay_busy)
                        action Function(kag_open_saveload_from_menubar, "load")
                    textbutton kag_tr("縦画面"):
                        xsize _l_btn_w
                        ysize _l_btn_h
                        background "#6b2661"
                        hover_background "#ff0099"
                        insensitive_background "#2d142a"
                        text_font _fnt
                        text_size 18
                        text_bold True
                        text_color "#ffe0f0"
                        text_insensitive_color "#7c5a76"
                        text_align (0.5, 0.5)
                        sensitive _can_orient
                        action Function(kag_toggle_android_orientation)
                    textbutton kag_tr("メニュー"):
                        xsize _l_btn_w
                        ysize _l_btn_h
                        background ("#ff0099" if _menu_open else "#4d2048")
                        hover_background "#ff33aa"
                        insensitive_background "#2d142a"
                        text_font _fnt
                        text_size 18
                        text_bold True
                        text_color "#ffffff"
                        text_insensitive_color "#7c5a76"
                        text_align (0.5, 0.5)
                        sensitive _can_menu
                        action Function(kag_toggle_android_menu)

# Touch-friendly mobile Settings & System sheet rendered inside the 800x600 stage
screen kag_android_menu():
    modal True
    zorder 125
    on "hide" action Function(kag_on_overlay_screen_hide, "kag_android_menu")
    key "game_menu" action Hide("kag_android_menu")
    key "K_ESCAPE" action Hide("kag_android_menu")
    key "mouseup_3" action Hide("kag_android_menu")

    $ _fnt = kag_get_active_font()
    $ _cur_orient = kag_get_android_orientation()
    $ _cur_lang = persistent.kag_language or _preferences.language
    $ _spd = persistent.kag_text_speed or "normal"
    $ _fmode = persistent.kag_font_mode or "mono"
    $ _mov_on = bool(persistent.movieSkip != 0)

    fixed xysize (800, 600):
        add Solid("#00000099", xysize=(800, 600))

        frame align (0.5, 0.5) xsize 740 ysize 560 padding (22, 18) background "#fff5faf8":
            vbox spacing 12 xfill True:
                hbox xfill True:
                    text kag_tr("メニュー・設定") font _fnt size 24 bold True color "#cc0066" yalign 0.5
                    textbutton kag_tr("閉じる"):
                        xalign 1.0
                        background "#ff0099"
                        hover_background "#ff33aa"
                        padding (18, 8)
                        text_font _fnt
                        text_size 18
                        text_bold True
                        text_color "#ffffff"
                        action Hide("kag_android_menu")

                viewport xsize 696 ysize 476 scrollbars "vertical" mousewheel True draggable True:
                    vbox spacing 14 xsize 672:
                        # 1. Orientation
                        vbox spacing 6:
                            text kag_tr("画面の向き") font _fnt size 17 bold True color "#cc0066"
                            hbox spacing 12:
                                textbutton kag_tr("縦画面 (デフォルト)"):
                                    xsize 260
                                    ysize 44
                                    background ("#ff0099" if _cur_orient == "portrait" else "#ecdbe6")
                                    hover_background "#ff33aa"
                                    text_font _fnt
                                    text_size 17
                                    text_bold True
                                    text_color ("#ffffff" if _cur_orient == "portrait" else "#222222")
                                    text_align (0.5, 0.5)
                                    action Function(kag_apply_android_orientation, "portrait")
                                textbutton kag_tr("横画面"):
                                    xsize 260
                                    ysize 44
                                    background ("#ff0099" if _cur_orient == "landscape" else "#ecdbe6")
                                    hover_background "#ff33aa"
                                    text_font _fnt
                                    text_size 17
                                    text_bold True
                                    text_color ("#ffffff" if _cur_orient == "landscape" else "#222222")
                                    text_align (0.5, 0.5)
                                    action Function(kag_apply_android_orientation, "landscape")

                        # 2. Language
                        vbox spacing 6:
                            text kag_tr("言語(L)") font _fnt size 17 bold True color "#cc0066"
                            hbox spacing 12:
                                textbutton "日本語 (Original)":
                                    xsize 260
                                    ysize 44
                                    background ("#ff0099" if _cur_lang != "zh_cn" else "#ecdbe6")
                                    hover_background "#ff33aa"
                                    text_font kag_get_jp_font()
                                    text_size 17
                                    text_bold True
                                    text_color ("#ffffff" if _cur_lang != "zh_cn" else "#222222")
                                    text_align (0.5, 0.5)
                                    action Function(kag_set_language, None)
                                textbutton "简体中文":
                                    xsize 260
                                    ysize 44
                                    background ("#ff0099" if _cur_lang == "zh_cn" else "#ecdbe6")
                                    hover_background "#ff33aa"
                                    text_font kag_get_sc_font()
                                    text_size 17
                                    text_bold True
                                    text_color ("#ffffff" if _cur_lang == "zh_cn" else "#222222")
                                    text_align (0.5, 0.5)
                                    action Function(kag_set_language, "zh_cn")

                        # 3. Text Speed
                        vbox spacing 6:
                            text kag_tr("文字表示速度") font _fnt size 17 bold True color "#cc0066"
                            hbox spacing 10:
                                for _sp_id, _sp_lbl in [("fast", "速い (10ms)"), ("normal", "普通 (30ms)"), ("slow", "遅い (50ms)"), ("instant", "ノーウェイト")]:
                                    textbutton kag_tr(_sp_lbl):
                                        xsize 158
                                        ysize 42
                                        background ("#ff0099" if _spd == _sp_id else "#ecdbe6")
                                        hover_background "#ff33aa"
                                        text_font _fnt
                                        text_size 15
                                        text_bold True
                                        text_color ("#ffffff" if _spd == _sp_id else "#222222")
                                        text_align (0.5, 0.5)
                                        action Function(kag_set_text_speed, _sp_id)

                        # 4. Font Mode & Movie
                        hbox spacing 24:
                            vbox spacing 6:
                                text kag_tr("フォント選択") font _fnt size 17 bold True color "#cc0066"
                                hbox spacing 10:
                                    textbutton kag_tr("等幅ゴシック"):
                                        xsize 190
                                        ysize 42
                                        background ("#ff0099" if _fmode == "mono" else "#ecdbe6")
                                        hover_background "#ff33aa"
                                        text_font _fnt
                                        text_size 16
                                        text_bold True
                                        text_color ("#ffffff" if _fmode == "mono" else "#222222")
                                        text_align (0.5, 0.5)
                                        action Function(kag_set_font_mode, "mono")
                                    textbutton kag_tr("プロポーショナル"):
                                        xsize 210
                                        ysize 42
                                        background ("#ff0099" if _fmode == "prop" else "#ecdbe6")
                                        hover_background "#ff33aa"
                                        text_font _fnt
                                        text_size 16
                                        text_bold True
                                        text_color ("#ffffff" if _fmode == "prop" else "#222222")
                                        text_align (0.5, 0.5)
                                        action Function(kag_set_font_mode, "prop")
                            vbox spacing 6:
                                text kag_tr("ムービー(M)") font _fnt size 17 bold True color "#cc0066"
                                textbutton (kag_tr("再生する (ON)") if _mov_on else kag_tr("スキップ (OFF)")):
                                    xsize 210
                                    ysize 42
                                    background ("#ff0099" if _mov_on else "#ecdbe6")
                                    hover_background "#ff33aa"
                                    text_font _fnt
                                    text_size 16
                                    text_bold True
                                    text_color ("#ffffff" if _mov_on else "#222222")
                                    text_align (0.5, 0.5)
                                    action SetField(persistent, "movieSkip", 0 if _mov_on else 1)

                        # 5. Volume Controls
                        vbox spacing 8:
                            text kag_tr("音量(V)") font _fnt size 17 bold True color "#cc0066"
                            for _m_label, _m_name in [(kag_tr("ＢＧＭ(B)"), "music"), (kag_tr("ボイス(V)"), "voice"), (kag_tr("効果音(S)"), "sfx")]:
                                $ _cur_pct = kag_get_mixer_percent(_m_name)
                                hbox spacing 8:
                                    fixed xsize 140 ysize 40:
                                        text _m_label font _fnt size 16 color "#222222" yalign 0.5
                                    for _step_pct in (0, 20, 40, 60, 80, 100):
                                        $ _step_on = (_cur_pct == 0) if _step_pct == 0 else (_cur_pct > 0 and abs(_cur_pct - _step_pct) <= 5)
                                        textbutton ("0%" if _step_pct == 0 else "{}%".format(_step_pct)):
                                            xsize 80
                                            ysize 40
                                            background ("#ff0099" if _step_on else "#ecdbe6")
                                            hover_background "#ff33aa"
                                            text_font _fnt
                                            text_size 15
                                            text_bold True
                                            text_color ("#ffffff" if _step_on else "#222222")
                                            text_align (0.5, 0.5)
                                            action Function(kag_set_mixer_percent, _m_name, _step_pct)

                        # 6. System Actions
                        vbox spacing 6:
                            text kag_tr("システム(S)") font _fnt size 17 bold True color "#cc0066"
                            hbox spacing 12:
                                textbutton kag_tr("最初に戻る (タイトル)"):
                                    xsize 250
                                    ysize 44
                                    background "#7a4468"
                                    hover_background "#ff0099"
                                    insensitive_background "#cccccc"
                                    text_font _fnt
                                    text_size 16
                                    text_bold True
                                    text_color "#ffffff"
                                    text_insensitive_color "#888888"
                                    text_align (0.5, 0.5)
                                    sensitive (not kag_in_title)
                                    action [Hide("kag_android_menu"), Function(kag_open_confirm, kag_tr("タイトルへ戻りますか？"), Function(kag_return_to_title))]
                                textbutton kag_tr("このソフトについて"):
                                    xsize 220
                                    ysize 44
                                    background "#7a4468"
                                    hover_background "#ff0099"
                                    text_font _fnt
                                    text_size 16
                                    text_bold True
                                    text_color "#ffffff"
                                    text_align (0.5, 0.5)
                                    action [Hide("kag_android_menu"), Function(kag_open_about_dialog)]
                                textbutton kag_tr("終了"):
                                    xsize 160
                                    ysize 44
                                    background "#555555"
                                    hover_background "#cc0044"
                                    text_font _fnt
                                    text_size 16
                                    text_bold True
                                    text_color "#ffffff"
                                    text_align (0.5, 0.5)
                                    action [Hide("kag_android_menu"), Function(kag_open_confirm, kag_tr("終了しますか？"), Function(kag_quit_game))]
