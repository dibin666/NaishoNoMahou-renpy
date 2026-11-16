# Internationalization (Japanese default / Simplified Chinese zh_cn) & TTC font consistency

default persistent.kag_language = None       # None = Japanese, "zh_cn" = Simplified Chinese
default persistent.kag_font_mode = "mono"    # "mono" = MS Gothic parity (fixed-pitch), "prop" = proportional
default persistent.kag_text_speed = "normal" # "fast" (10ms), "normal" (30ms), "slow" (50ms)

init -5 python:
    # Standalone OpenType faces extracted from NotoSansCJK-Regular/Bold.ttc:
    #   NotoSansMonoCJKjp/sc -> monospace matching MS Gothic / SimHei fixed pitch
    #   NotoSansCJKjp/sc     -> proportional Noto Sans CJK
    config.font_replacement_map[("fonts/NotoSansMonoCJKjp-Regular.otf", True, False)] = ("fonts/NotoSansMonoCJKjp-Bold.otf", False, False)
    config.font_replacement_map[("fonts/NotoSansCJKjp-Regular.otf", True, False)] = ("fonts/NotoSansCJKjp-Bold.otf", False, False)
    config.font_replacement_map[("fonts/NotoSansMonoCJKsc-Regular.otf", True, False)] = ("fonts/NotoSansMonoCJKsc-Bold.otf", False, False)
    config.font_replacement_map[("fonts/NotoSansCJKsc-Regular.otf", True, False)] = ("fonts/NotoSansCJKsc-Bold.otf", False, False)
    # Use MS Gothic's native Windows TrueType bytecode hinting rather than FreeType's auto hinter,
    # and map bold weights to Noto Sans CJK JP Bold because MS Gothic's embedded bitmap strikes vanish under synthetic embolden.
    config.font_hinting["fonts/msgothic.ttc"] = "bytecode"
    config.font_hinting["2@fonts/msgothic.ttc"] = "bytecode"
    for _msg_cand in ("fonts/msgothic.ttc", "fonts/msgothic.ttf", "fonts/MS-Gothic.ttf"):
        for _it in (False, True):
            config.font_replacement_map[(_msg_cand, True, _it)] = ("fonts/NotoSansMonoCJKjp-Bold.otf", False, _it)
    for _it in (False, True):
        config.font_replacement_map[("2@fonts/msgothic.ttc", True, _it)] = ("fonts/NotoSansCJKjp-Bold.otf", False, _it)

    def kag_get_jp_font():
        mode = persistent.kag_font_mode or "mono"
        if mode == "mono":
            for _cand in ("fonts/msgothic.ttc", "fonts/msgothic.ttf", "fonts/MS-Gothic.ttf"):
                if renpy.loadable(_cand):
                    return _cand
            return "fonts/NotoSansMonoCJKjp-Regular.otf"
        if renpy.loadable("fonts/msgothic.ttc"):
            return "2@fonts/msgothic.ttc"
        return "fonts/NotoSansCJKjp-Regular.otf"

    def kag_get_jp_bold_font():
        mode = persistent.kag_font_mode or "mono"
        if mode == "mono":
            return "fonts/NotoSansMonoCJKjp-Bold.otf"
        return "fonts/NotoSansCJKjp-Bold.otf"

    def kag_get_sc_font(bold=False):
        mode = persistent.kag_font_mode or "mono"
        if bold:
            return "fonts/NotoSansMonoCJKsc-Bold.otf" if mode == "mono" else "fonts/NotoSansCJKsc-Bold.otf"
        return "fonts/NotoSansMonoCJKsc-Regular.otf" if mode == "mono" else "fonts/NotoSansCJKsc-Regular.otf"

    def kag_get_active_font():
        lang = persistent.kag_language or _preferences.language
        if lang == "zh_cn":
            return kag_get_sc_font(bold=False)
        return kag_get_jp_font()

    def kag_get_active_bold_font():
        lang = persistent.kag_language or _preferences.language
        if lang == "zh_cn":
            return kag_get_sc_font(bold=True)
        return kag_get_jp_bold_font()

    def kag_text_needs_sc_font(txt):
        if not txt:
            return False
        import re as _re
        plain = _re.sub(r"\{[^{}]*\}", "", str(txt))
        for _ch in plain:
            if _ch == "\u25a1":
                continue
            try:
                _ch.encode("cp932")
            except UnicodeEncodeError:
                return True
        return False

    def kag_get_dialogue_font(txt=None):
        lang = persistent.kag_language or _preferences.language
        if kag_text_needs_sc_font(txt):
            return kag_get_sc_font(bold=False)
        if lang == "zh_cn":
            if txt and any("\u3040" <= _ch <= "\u30ff" for _ch in str(txt)):
                return kag_get_jp_font()
            return kag_get_sc_font(bold=False)
        return kag_get_jp_font()

    def kag_apply_typography():
        fnt = kag_get_active_font()
        bold_fnt = kag_get_active_bold_font()
        gui.text_font = fnt
        gui.name_text_font = fnt
        gui.interface_text_font = fnt
        gui.button_text_font = fnt
        gui.choice_button_text_font = fnt
        gui.system_font = fnt
        for _b in (False, True):
            for _i in (False, True):
                config.font_replacement_map[("DejaVuSans.ttf", _b, _i)] = (bold_fnt if _b else fnt, False, _i)
                config.font_replacement_map[("DejaVuSans-Bold.ttf", _b, _i)] = (bold_fnt, False, _i)
        for st_name in (
            "default", "text", "button_text", "label_text", "prompt_text",
            "input", "kag_menu_item_text",
            "notify_text", "skip_indicator", "_default",
            "say_dialogue", "say_label",
        ):
            st = getattr(style, st_name, None)
            if st is not None:
                st.font = fnt
        if hasattr(style, "say_dialogue"):
            style.say_dialogue.size = 24
            style.say_dialogue.line_spacing = 4
            style.say_dialogue.color = "#ffffff"
            style.say_dialogue.drop_shadow = (2, 2)
            style.say_dialogue.drop_shadow_color = "#000000"
        if not renpy.game.context().init_phase:
            renpy.style.rebuild()

    def kag_set_language(lang):
        persistent.kag_language = lang
        renpy.change_language(lang)
        kag_apply_typography()
        renpy.restart_interaction()

    def kag_set_font_mode(mode):
        persistent.kag_font_mode = mode
        kag_apply_typography()
        renpy.restart_interaction()

    def kag_set_text_speed(speed_name):
        persistent.kag_text_speed = speed_name
        cps_map = {
            "fast": 100,    # 10ms / char
            "normal": 33,   # 30ms / char
            "slow": 20,     # 50ms / char
            "instant": 0,
        }
        preferences.text_cps = cps_map.get(speed_name, 33)
        renpy.restart_interaction()

    def kag_sync_on_start():
        if persistent.kag_language is not None and _preferences.language != persistent.kag_language:
            renpy.change_language(persistent.kag_language)
        _preferences.skip_unseen = True
        kag_apply_typography()
        if persistent.kag_text_speed in ("fast", "normal", "slow", "instant"):
            kag_set_text_speed(persistent.kag_text_speed)
        if "kag_apply_shortcuts" in globals():
            kag_apply_shortcuts()
        nb = globals().get("_kag_native_menubar")
        if nb is not None:
            nb.ensure_initialized()
        if "kag_apply_android_orientation" in globals() and kag_is_android_ui():
            kag_apply_android_orientation()

    config.start_callbacks.append(kag_sync_on_start)
    config.after_load_callbacks.append(kag_apply_typography)
    config.language_callbacks[None].append(kag_apply_typography)
    config.language_callbacks["zh_cn"].append(kag_apply_typography)

    def kag_tr(s):
        return renpy.translate_string(s)

init 10 python:
    kag_apply_typography()

style default:
    font kag_get_active_font()

style text is default:
    font kag_get_active_font()

style button_text is default:
    font kag_get_active_font()

style label_text is default:
    font kag_get_active_font()

style prompt_text is default:
    font kag_get_active_font()

style input is default:
    font kag_get_active_font()

style say_dialogue is default:
    font kag_get_active_font()
    size 24
    line_spacing 4
    color "#ffffff"
    drop_shadow (2, 2)
    drop_shadow_color "#000000"

style say_label is default:
    font kag_get_active_font()
    size 24
    color "#ffffff"
    drop_shadow (2, 2)
    drop_shadow_color "#000000"
