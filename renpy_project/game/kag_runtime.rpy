# Core KAG3 / KiriKiri2 Runtime Emulation Layer for Ren'Py 8

init -20 python:
    import re
    import datetime

    class KAGVars(object):
        """Mimics TJS f.* dictionary with default 0 for uninitialized flags while preserving pickle/rollback."""
        def __init__(self):
            self.ma = "マジョリズム"
            self.player = "りずむ"
            self.spell = ""
            self.route = ""
            self.testmode = 0
            self.c_num = 0
            self.re_scenario = 0
            self.re_movie = 0
            self.loadmode = 0
            self.judgeflag = 0
            self.movie = 1
            self.page = 0
            self.cgPage = 0
            self.gallery = 0
            self.ly = 0
            self.skip = 0
            self.event_01 = 0
            self.event_04 = 0
            self.case = ""
            self.case1 = ""
            self.case2 = ""
            self.sn_doremi = 0
            self.sn_hazuki = 0
            self.sn_ai = 0
            self.sn_onpu = 0
            self.sn_momo = 0
            self.sn_hana = 0

        def __getattr__(self, name):
            if name.startswith("_"):
                raise AttributeError(name)
            return 0

    def kag_resolve_image(storage):
        if not storage:
            return None
        key = str(storage).replace("\\", "/").strip().lower()
        if key in KAG_IMAGE_MAP:
            return KAG_IMAGE_MAP[key]
        stem = key.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        if stem in KAG_IMAGE_MAP:
            return KAG_IMAGE_MAP[stem]
        return None

    def kag_resolve_button_states(graphic):
        if not graphic:
            return None
        key = str(graphic).replace("\\", "/").strip().lower()
        stem = key.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        return KAG_BUTTON_STATES.get(stem)

    def kag_resolve_rule(rule):
        if not rule:
            return None
        key = str(rule).replace("\\", "/").strip().lower()
        if key in KAG_RULE_MAP:
            return KAG_RULE_MAP[key]
        stem = key.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        return KAG_RULE_MAP.get(stem)

    def kag_resolve_bgm(storage):
        if not storage:
            return None
        key = str(storage).replace("\\", "/").strip().lower()
        if key in KAG_BGM_MAP:
            return KAG_BGM_MAP[key]
        stem = key.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        return KAG_BGM_MAP.get(stem)

    def kag_resolve_se(storage):
        if not storage:
            return None
        key = str(storage).replace("\\", "/").strip().lower()
        if key in KAG_SE_MAP:
            return KAG_SE_MAP[key]
        stem = key.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        return KAG_SE_MAP.get(stem)

    def kag_resolve_video(storage):
        if not storage:
            return "video/doremi_op.webm"
        key = str(storage).replace("\\", "/").strip().lower()
        return KAG_VIDEO_MAP.get(key, "video/doremi_op.webm")

    def kag_make_displayable(storage, sepia=False):
        key_low = str(storage).replace("\\", "/").strip().lower()
        if key_low in ("black", "black.tlg", "black.png") and kag_resolve_image(storage) is None:
            disp = Solid("#000000", xysize=(800, 600))
        elif key_low in ("white", "white.tlg", "white.png") and kag_resolve_image(storage) is None:
            disp = Solid("#ffffff", xysize=(800, 600))
        else:
            path = kag_resolve_image(storage)
            if path is None:
                renpy.log("KAG Warning: missing image asset: " + repr(storage))
                disp = Solid("#00000000", xysize=(800, 600))
            else:
                disp = Image(path)
        if sepia:
            # Matches KiriKiri grayscale=true rgamma=1.3 ggamma=1.1 warm sepia
            disp = Transform(disp, matrixcolor=SaturationMatrix(0.0) * TintMatrix("#f2dcb8"))
        return disp

    def kag_make_transition(time_ms, method="", rule="", bgcolor="0x000000"):
        sec = max(0.0, float(time_ms) / 1000.0)
        if sec <= 0.001:
            return None
        rpath = kag_resolve_rule(rule)
        if rpath:
            return ImageDissolve(rpath, sec, ramplen=100, reverse=False)
        m = (method or "").lower()
        if m == "wave":
            return Dissolve(sec)
        if m == "mosaic":
            return Pixellate(sec, 8)
        if m in ("turn", "rotateswap", "rotatevanish", "rotatezoom"):
            return Dissolve(sec)
        return Dissolve(sec)

# Global persistent sf.* flags initialized matching first.ks + AfterInit.tjs
default persistent.firstclear = 0
default persistent.clearChar = 0
default persistent.NormalCnt = 0
default persistent.TrueCnt = 0
default persistent.movieSkip = 1
default persistent.m_skip = 0

default persistent.cgd1 = 0
default persistent.cgd2 = 0
default persistent.cgd3 = 0
default persistent.cgd4 = 0
default persistent.cgd5 = 0
default persistent.cgd6 = 0
default persistent.cghz1 = 0
default persistent.cghz2 = 0
default persistent.cghz3 = 0
default persistent.cghz4 = 0
default persistent.cghz5 = 0
default persistent.cghz6 = 0
default persistent.cghz7 = 0
default persistent.cga1 = 0
default persistent.cga2 = 0
default persistent.cga3 = 0
default persistent.cga4 = 0
default persistent.cga5 = 0
default persistent.cga6 = 0
default persistent.cgm1 = 0
default persistent.cgm2 = 0
default persistent.cgm3 = 0
default persistent.cgm4 = 0
default persistent.cgm4_1 = 0
default persistent.cgm4_2 = 0
default persistent.cgm4_3 = 0
default persistent.cgm4_4 = 0
default persistent.cgm5 = 0
default persistent.cgm6 = 0
default persistent.cgo1 = 0
default persistent.cgo2 = 0
default persistent.cgo3 = 0
default persistent.cgo4 = 0
default persistent.cgo5 = 0
default persistent.cgo6 = 0
default persistent.cghn1 = 0
default persistent.cghn2 = 0
default persistent.cghn3 = 0
default persistent.cghn4 = 0
default persistent.cghn5 = 0
default persistent.cghn6 = 0
default persistent.cghn7 = 0
default persistent.cgot1 = 0
default persistent.cgot2 = 0
default persistent.cgot3 = 0
default persistent.cgot4 = 0
default persistent.cgot5 = 0
default persistent.cgot6 = 0

default persistent.d1_s = 0
default persistent.d2_s = 0
default persistent.d3_s = 0
default persistent.d4_s = 0
default persistent.d5_s = 0
default persistent.d6_s = 0
default persistent.d7_s = 0
default persistent.d8_s = 0
default persistent.dc_s = 0
default persistent.hz1_s = 0
default persistent.hz2_s = 0
default persistent.hz3_s = 0
default persistent.hz4_s = 0
default persistent.hz5_s = 0
default persistent.hz6_s = 0
default persistent.hz7_s = 0
default persistent.hz8_s = 0
default persistent.hzc_s = 0
default persistent.a1_s = 0
default persistent.a2_s = 0
default persistent.a3_s = 0
default persistent.a4_s = 0
default persistent.a5_s = 0
default persistent.a6_s = 0
default persistent.a7_s = 0
default persistent.a8_s = 0
default persistent.ac_s = 0
default persistent.m1_s = 0
default persistent.m2_s = 0
default persistent.m3_s = 0
default persistent.m4_s = 0
default persistent.m5_s = 0
default persistent.m6_s = 0
default persistent.m7_s = 0
default persistent.m8_s = 0
default persistent.mc_s = 0
default persistent.o1_s = 0
default persistent.o2_s = 0
default persistent.o3_s = 0
default persistent.o4_s = 0
default persistent.o5_s = 0
default persistent.o6_s = 0
default persistent.o7_s = 0
default persistent.o8_s = 0
default persistent.oc_s = 0
default persistent.hn1_s = 0
default persistent.hn2_s = 0
default persistent.hn3_s = 0
default persistent.hn4_s = 0
default persistent.hn5_s = 0
default persistent.hn6_s = 0
default persistent.hn7_s = 0
default persistent.hn8_s = 0
default persistent.hnc_s = 0
default persistent.d_n_end = 0
default persistent.d_t_end = 0
default persistent.hz_n_end = 0
default persistent.hz_t_end = 0
default persistent.a_n_end = 0
default persistent.a_t_end = 0
default persistent.o_n_end = 0
default persistent.o_t_end = 0
default persistent.m_n_end = 0
default persistent.m_t_end = 0
default persistent.hn_n_end = 0
default persistent.hn_t_end = 0

# Custom 30-slot Save metadata matching plug_rclick_tjs.ks
default persistent.kag_locks = [False] * 30
default persistent.kag_comments = [""] * 30
default persistent.kag_bookmarks = [""] * 30
default persistent.kag_dates = [""] * 30
default persistent.kag_shortcuts = None

default _kag_capturing_shortcut = None

# Per-game / rollback-aware runtime state
default kag_f = KAGVars()
default kag_click_count = 0
default kag_rclick_enabled = True
default kag_clickskip_enabled = True
default kag_history_output = True
default kag_history_enabled = True
default kag_mesframe_visible = False
default kag_mesframe_fade = False
default kag_bgm_looping = False
default kag_current_bookmark = ""
default kag_next_indent_prefix = ""
default kag_hold_box_text = ""
default kag_hold_box_active = False
default kag_hold_box_indent = 0
default kag_box_clicked_skip = False
default kag_menu_buttons = []
default kag_menu_links = []
default kag_in_choices = False
default kag_saveload_page = 0
default kag_saveload_mode = "save"
default kag_saveload_from_rclick = False
default kag_about_open = False
default kag_pending_menu_skip = False
default kag_video_visible = False
default kag_msg_opacity = 0
default kag_msg_rect = (20, 465, 768, 105)
default kag_in_title = False
default kag_se0_is_bgm = False

init -1 python:
    def kag_noop():
        return None

    def kag_get_skip_mode():
        return 2 if renpy.is_skipping() else 0

    def kag_get_click_count():
        return store.kag_click_count

    def kag_bgm_status():
        return "stop" if not renpy.music.is_playing(channel="music") else "play"

    def kag_set_bookmark(title):
        store.kag_current_bookmark = title or ""

    def kag_set_rclick(enabled):
        store.kag_rclick_enabled = bool(enabled)

    def kag_set_clickskip(enabled):
        en = bool(enabled)
        store.kag_clickskip_enabled = en
        store._skipping = en
        if not en:
            config.skipping = None

    def kag_start_skip():
        if not store.kag_clickskip_enabled or store.kag_in_title:
            return
        config.skipping = None if config.skipping else "slow"
        renpy.restart_interaction()

    def kag_history_opt(output=None, enabled=None):
        if output is not None:
            store.kag_history_output = bool(output)
            store._history = bool(output)
        if enabled is not None:
            store.kag_history_enabled = bool(enabled)

    def kag_cancelskip():
        config.skipping = None
        store._skipping = bool(store.kag_clickskip_enabled)

    def kag_startanchor():
        store.kag_in_title = True
        store.kag_mesframe_visible = False
        store.kag_mesframe_fade = False
        kag_cm()
        config.skipping = None
        renpy.block_rollback()

    def kag_measure_text_width(txt):
        if not txt:
            return 0
        # Active dialogue font is 24px (fullwidth CJK glyphs = 24px, ASCII = 12px)
        plain = re.sub(r"\{[^{}]*\}", "", str(txt))
        return sum(24 if ord(c) > 127 else 12 for c in plain)

    def kag_set_next_indent(prefix):
        store.kag_next_indent_prefix = prefix or ""
        store.kag_hold_box_indent = kag_measure_text_width(prefix) if prefix else 0

    def kag_clear_menu_items():
        store.kag_menu_buttons = []
        store.kag_menu_links = []

    def kag_choices_begin():
        store.kag_in_choices = True
        kag_clear_menu_items()

    def kag_choices_end():
        store.kag_in_choices = False

    def kag_cm():
        store.kag_hold_box_active = False
        store.kag_hold_box_text = ""
        store.kag_hold_box_indent = 0
        store.kag_next_indent_prefix = ""
        store.kag_box_clicked_skip = False
        kag_clear_menu_items()

    def kag_er():
        kag_cm()

    def kag_ct():
        kag_cm()

    def kag_position(left=None, top=None, width=None, height=None, opacity=None):
        l = int(left) if left is not None else store.kag_msg_rect[0]
        t = int(top) if top is not None else store.kag_msg_rect[1]
        w = int(width) if width is not None else store.kag_msg_rect[2]
        h = int(height) if height is not None else store.kag_msg_rect[3]
        store.kag_msg_rect = (l, t, w, h)
        if opacity is not None:
            store.kag_msg_opacity = int(opacity)

    def layerposition_def():
        store.kag_msg_rect = (16, 16, 768, 568)
        store.kag_msg_opacity = 0

    def layerposition_use():
        store.kag_msg_rect = (16, 475, 768, 105)
        store.kag_msg_opacity = 128

    def kag_layopt(layer="0", visible=True):
        if str(layer) == "3":
            store.kag_mesframe_visible = bool(visible)
        elif not visible:
            renpy.hide("kag_fg_" + str(layer))

    def kag_backlay():
        return None

    def kag_mesframe():
        store.kag_msg_rect = (20, 465, 768, 105)
        store.kag_msg_opacity = 0
        store.kag_mesframe_fade = True
        store.kag_mesframe_visible = True

    def kag_freeimage(layer="0", page="fore"):
        ly = str(layer).lower()
        if ly == "3":
            store.kag_mesframe_visible = False
            store.kag_mesframe_fade = False
            return
        tag = "kag_fg_" + ly
        renpy.hide(tag, layer="master")
        if page == "fore":
            renpy.with_statement(None)

    def _kag_layer_tag(layer):
        ly = str(layer).lower()
        if ly == "base":
            return "kag_bg", 0
        return "kag_fg_" + ly, 10 + (int(ly) if ly.isdigit() else 5) * 10

    def kag_image(storage, layer="base", page="fore", left=0, top=0, visible=True, sepia=False):
        tag, z = _kag_layer_tag(layer)
        if not visible:
            renpy.hide(tag, layer="master")
            if page == "fore":
                renpy.with_statement(None)
            return
        disp = kag_make_displayable(storage, sepia=sepia)
        pos_tr = Position(xpos=int(left), ypos=int(top), xanchor=0, yanchor=0)
        renpy.show(tag, what=disp, at_list=[pos_tr], layer="master", zorder=z)
        if page == "fore":
            renpy.with_statement(None)

    def kag_trans(time_ms=500, method="", rule="", vague=64):
        tr = kag_make_transition(time_ms, method=method, rule=rule)
        renpy.with_statement(tr)

    def kag_changetype(ctype, storage, time_ms=500, bgcolor="0x000000"):
        kag_ct()
        store.kag_msg_opacity = 0
        store.kag_mesframe_visible = False
        store.kag_mesframe_fade = False
        s_low = str(storage or "").strip().lower()
        store.kag_in_title = s_low.startswith("maintitle")
        if store.kag_in_title:
            config.skipping = None
        sepia = (ctype == "sepia")
        disp = kag_make_displayable(storage, sepia=sepia)
        renpy.show("kag_bg", what=disp, at_list=[Position(xpos=0, ypos=0, xanchor=0, yanchor=0)], layer="master", zorder=0)
        rule_map = {
            "left": "trans01",
            "right": "trans02",
            "up": "trans03",
            "down": "trans04",
            "note": "trans05",
            "circle01": "circle1",
            "circle02": "circle2",
            "blind01": "blind_01",
        }
        rule_name = rule_map.get(ctype, "")
        tr = kag_make_transition(time_ms, method=ctype, rule=rule_name, bgcolor=bgcolor)
        renpy.with_statement(tr)

    def kag_drawchar(storage, time_ms=300, sepia=False, canskip=True):
        store.kag_mesframe_visible = True
        disp = kag_make_displayable(storage, sepia=sepia)
        renpy.show("kag_fg_0", what=disp, at_list=[Position(xpos=0, ypos=0, xanchor=0, yanchor=0)], layer="master", zorder=10)
        tr = Dissolve(max(0.01, time_ms / 1000.0)) if time_ms > 0 else None
        renpy.with_statement(tr)

    def kag_bgdraw():
        disp = kag_make_displayable("bg017_a")
        renpy.show("kag_fg_1", what=disp, at_list=[Position(xpos=0, ypos=0, xanchor=0, yanchor=0)], layer="master", zorder=20)
        tr = kag_make_transition(500, rule="trans01")
        renpy.with_statement(tr)

    def kag_frmdraw():
        disp = kag_make_displayable("c_frm")
        renpy.show("kag_fg_1", what=disp, at_list=[Position(xpos=0, ypos=0, xanchor=0, yanchor=0)], layer="master", zorder=20)
        renpy.with_statement(Dissolve(0.6))

    def kag_wt(canskip=True):
        return None

    def kag_cwt():
        return None

    def kag_stoptrans():
        return None

    def kag_quake(time_ms=500, hmax=10, vmax=10):
        dur = max(0.1, float(time_ms) / 1000.0)
        if renpy.is_skipping():
            return
        hx = abs(int(hmax))
        vy = abs(int(vmax))
        shake = Move((hx, vy), (-hx, -vy), 0.08, bounce=True, repeat=True, delay=dur)
        renpy.with_statement(shake)

    def kag_wait(ms, canskip=True):
        sec = max(0.0, float(ms) / 1000.0)
        if sec <= 0.0:
            return
        effective_skip = bool(canskip and store.kag_clickskip_enabled)
        if effective_skip and (renpy.is_skipping() or (store.kag_hold_box_active and store.kag_box_clicked_skip)):
            return
        clicked = renpy.pause(sec, hard=not effective_skip)
        if clicked and effective_skip and store.kag_hold_box_active:
            store.kag_box_clicked_skip = True

    def kag_waitclick():
        store.kag_click_count = 1
        renpy.pause()

    # Audio Playback (BGM + SE buf 0..2)
    def kag_playbgm(storage, loop=True):
        path = kag_resolve_bgm(storage)
        if not path:
            renpy.log("KAG Warning: missing BGM: " + repr(storage))
            return
        store.kag_bgm_looping = bool(loop)
        renpy.music.play(path, channel="music", loop=bool(loop), fadein=0.0)

    def kag_stopbgm():
        store.kag_bgm_looping = False
        renpy.music.stop(channel="music", fadeout=0.0)
        if store.kag_se0_is_bgm:
            store.kag_se0_is_bgm = False
            renpy.music.stop(channel="se0", fadeout=0.0)

    def kag_pausebgm():
        renpy.music.set_pause(True, channel="music")

    def kag_resumebgm():
        renpy.music.set_pause(False, channel="music")

    def kag_fadeoutbgm(time_ms=1000):
        store.kag_bgm_looping = False
        sec = max(0.0, float(time_ms) / 1000.0)
        renpy.music.stop(channel="music", fadeout=sec)
        if store.kag_se0_is_bgm:
            store.kag_se0_is_bgm = False
            renpy.music.stop(channel="se0", fadeout=sec)

    def kag_fadeinbgm(storage, time_ms=1000):
        path = kag_resolve_bgm(storage)
        if not path:
            return
        store.kag_bgm_looping = True
        renpy.music.play(path, channel="music", loop=True, fadein=max(0.0, float(time_ms) / 1000.0))

    def kag_bgmopt(volume=None, gvolume=None):
        vol = gvolume if gvolume is not None else volume
        if vol is not None:
            renpy.music.set_volume(max(0.0, min(1.0, float(vol) / 100.0)), delay=0.0, channel="music")

    def _se_channel(buf):
        b = int(buf)
        if b == 0:
            return "se0"
        if b == 2:
            return "se2"
        return "se1"

    def kag_playse(storage, buf=0, loop=False):
        path = kag_resolve_se(storage) or kag_resolve_bgm(storage)
        if not path:
            renpy.log("KAG Warning: missing SE: " + repr(storage))
            return
        ch = _se_channel(buf)
        if ch == "se0":
            store.kag_se0_is_bgm = str(storage or "").strip().lower().startswith("bgm")
        renpy.music.play(path, channel=ch, loop=bool(loop or ch == "se2"))

    def kag_stopse(buf=0):
        ch = _se_channel(buf)
        if ch == "se0":
            store.kag_se0_is_bgm = False
        renpy.music.stop(channel=ch)

    def kag_fadeinse(storage, time_ms=500, buf=0):
        path = kag_resolve_se(storage) or kag_resolve_bgm(storage)
        if not path:
            renpy.log("KAG Warning: missing fadeinse: " + repr(storage))
            return
        ch = _se_channel(buf)
        if ch == "se0":
            store.kag_se0_is_bgm = str(storage or "").strip().lower().startswith("bgm")
        renpy.music.play(path, channel=ch, loop=False, fadein=max(0.0, float(time_ms) / 1000.0))

    def kag_fadeoutse(time_ms=500, buf=0):
        ch = _se_channel(buf)
        if ch == "se0":
            store.kag_se0_is_bgm = False
        renpy.music.stop(channel=ch, fadeout=max(0.0, float(time_ms) / 1000.0))

    def kag_seopt(buf=0, volume=None, gvolume=None):
        vol = gvolume if gvolume is not None else volume
        if vol is not None:
            renpy.music.set_volume(max(0.0, min(1.0, float(vol) / 100.0)), delay=0.0, channel=_se_channel(buf))

    def kag_ws(buf=0, canskip=True):
        ch = _se_channel(buf)
        if canskip and store.kag_hold_box_active and store.kag_box_clicked_skip:
            renpy.music.stop(channel=ch)
            return
        iters = 0
        while renpy.music.is_playing(channel=ch) and iters < 6000:
            if canskip and renpy.is_skipping():
                renpy.music.stop(channel=ch)
                break
            clicked = renpy.pause(0.08, hard=not canskip)
            if clicked and canskip:
                renpy.music.stop(channel=ch)
                if store.kag_hold_box_active:
                    store.kag_box_clicked_skip = True
                break
            iters += 1

    def kag_wl(canskip=True):
        # Match MainWindow.tjs:4058 — if looping or stopped, return immediately
        if store.kag_bgm_looping or not renpy.music.is_playing(channel="music"):
            return
        iters = 0
        while renpy.music.is_playing(channel="music") and iters < 6000:
            if canskip and renpy.is_skipping():
                break
            clicked = renpy.pause(0.08, hard=not canskip)
            if clicked and canskip:
                renpy.music.stop(channel="music")
                break
            iters += 1

    def kag_sound_se(storage, buf=1):
        if not renpy.is_skipping():
            kag_playse(storage, buf=buf, loop=False)
            kag_ws(buf=buf, canskip=True)
            kag_stopse(buf=buf)

    def kag_se_loop(storage):
        if not renpy.is_skipping():
            kag_playse(storage, buf=2, loop=True)

    # Video playback (どれみ1015.mpg -> doremi_op.webm)
    def kag_video_opt(visible=True):
        store.kag_video_visible = bool(visible)

    def kag_playvideo(storage):
        vpath = kag_resolve_video(storage)
        store._kag_pending_video = vpath

    def kag_stopvideo():
        store.kag_video_visible = False
        store._kag_pending_video = None

    def kag_wv(canskip=True):
        vpath = getattr(store, "_kag_pending_video", None)
        if not vpath:
            return
        effective_skip = bool(canskip and store.kag_clickskip_enabled)
        skipped = renpy.movie_cutscene(vpath, delay=None, loops=0, stop_music=True)
        store._kag_pending_video = None
        if effective_skip and skipped:
            store.kag_click_count = 1
        elif not effective_skip:
            store.kag_click_count = 0

    def kag_staffroll_init():
        return None

    def kag_staffroll_start(height=3300, time_ms=10000):
        return None

    def kag_staffroll_uninit():
        return None

    # Say character hook: keeps dialogue box visible across {nw} -> [ws]/[wait]
    def kag_say_callback(event, interact=True, **kwargs):
        if event == "show":
            pass
        elif event == "end":
            # Retain hold box when auto-continuing via {nw} until [cm]/[er]/[ct] clears it
            pass

    def kag_capture_hold_text(who, what):
        clean = what.replace("{nw}", "") if what else ""
        store.kag_hold_box_text = clean
        store.kag_hold_box_active = "{nw}" in (what or "")

    def kag_say_arguments_cb(who, *args, **kwargs):
        return args, kwargs

    def kag_input(var_name, prompt="", title=""):
        kag_capture_gameplay_screenshot(force=True)
        try:
            res = renpy.call_screen("kag_input_dialog", prompt=prompt, title=title, default_val=getattr(store.kag_f, var_name, ""))
        finally:
            _kag_clear_saved_screenshot_on_gameplay()
        setattr(store.kag_f, var_name, res)

    def kag_add_button(graphic, current_stem="", storage=None, target=None, exp=None, x=0, y=0):
        store.kag_menu_buttons.append({
            "graphic": graphic,
            "current_stem": current_stem,
            "storage": storage,
            "target": target,
            "exp": exp,
            "x": x,
            "y": y,
        })

    def kag_add_link(caption, current_stem="", storage=None, target=None, exp=None, x=None, y=None, color=None, size=None):
        store.kag_menu_links.append({
            "caption": caption,
            "current_stem": current_stem,
            "storage": storage,
            "target": target,
            "exp": exp,
            "x": x,
            "y": y,
            "color": color,
            "size": size,
        })

    def kag_resolve_label(current_stem, storage=None, target=None):
        stem = (storage or current_stem or "menu").lower().replace("-", "__dash__")
        stem = re.sub(r"[^a-z0-9_]", "_", stem)
        if target:
            t_norm = str(target).replace("*ture_0", "*true_0").lstrip("*").strip().lower().replace("-", "__dash__")
            t_norm = re.sub(r"[^a-z0-9_]", "_", t_norm)
            cand = f"kag_{stem}_{t_norm}"
            if renpy.has_label(cand):
                return cand
        base_lbl = f"kag_{stem}"
        if renpy.has_label(base_lbl):
            return base_lbl
        return "kag_menu_mainmenu"

    def kag_jump(current_stem, storage=None, target=None):
        lbl = kag_resolve_label(current_stem, storage=storage, target=target)
        renpy.jump(lbl)

    def kag_exec_exp(exp_str):
        if not exp_str:
            return
        exec(exp_str, renpy.store.__dict__)

    def kag_clear_saved_screenshot():
        iface = getattr(renpy.game, "interface", None)
        if iface is not None:
            iface._kag_saved_screenshot = None
            iface._kag_saved_screenshot_surface = None

    def kag_can_capture_gameplay_screenshot():
        if store.kag_in_title or store.main_menu or renpy.context()._menu:
            return False
        if getattr(store, "_kag_active_dropdown", None) is not None:
            return False
        if kag_in_overlay_menu():
            return False
        return len(renpy.game.contexts) == 1 or bool(getattr(store, "_windows_hidden", False))

    def kag_is_clean_gameplay(excluding_screen=None):
        if len(renpy.game.contexts) != 1:
            return False
        if store.kag_in_title or store.main_menu or renpy.context()._menu:
            return False
        if getattr(store, "_windows_hidden", False):
            return False
        if getattr(store, "_kag_active_dropdown", None) is not None:
            return False
        if kag_in_overlay_menu(excluding_screen=excluding_screen):
            return False
        return True

    def kag_capture_gameplay_screenshot(force=False):
        iface = getattr(renpy.game, "interface", None)
        if iface is None:
            return False
        if not kag_can_capture_gameplay_screenshot():
            return getattr(iface, "_kag_saved_screenshot", None) is not None
        if force or getattr(iface, "_kag_saved_screenshot", None) is None:
            captured_ok = False
            if "kag_is_android_ui" in globals() and kag_is_android_ui() and getattr(iface, "surftree", None) is not None and renpy.display.draw is not None:
                try:
                    import io as _io
                    full_surf = renpy.display.draw.screenshot(iface.surftree)
                    fw, fh = full_surf.get_size()
                    vw = max(1, int(config.screen_width))
                    vh = max(1, int(config.screen_height))
                    sx, sy = getattr(store, "_kag_android_stage_pos", (0, 0))
                    rx = max(0, min(fw - 1, int(round(float(sx) * fw / vw))))
                    ry = max(0, min(fh - 1, int(round(float(sy) * fh / vh))))
                    rw = max(1, min(fw - rx, int(round(800.0 * fw / vw))))
                    rh = max(1, min(fh - ry, int(round(600.0 * fh / vh))))
                    sub = full_surf.subsurface((rx, ry, rw, rh))
                    thumb = renpy.display.scale.smoothscale(sub, (config.thumbnail_width, config.thumbnail_height))
                    renpy.display.render.mutated_surface(thumb)
                    with _io.BytesIO() as _sio:
                        renpy.display.module.save_png(thumb, _sio, 0)
                        iface.screenshot = _sio.getvalue()
                    iface.screenshot_surface = thumb
                    captured_ok = True
                except Exception:
                    captured_ok = False
            if not captured_ok:
                renpy.take_screenshot((config.thumbnail_width, config.thumbnail_height))
            shot = getattr(iface, "screenshot", None)
            if shot is not None:
                iface._kag_saved_screenshot = shot
                iface._kag_saved_screenshot_surface = getattr(iface, "screenshot_surface", None)
                iface.clear_screenshot = False
                return True
        return getattr(iface, "_kag_saved_screenshot", None) is not None

    def kag_restore_saved_screenshot():
        iface = getattr(renpy.game, "interface", None)
        if iface is None:
            return False
        saved = getattr(iface, "_kag_saved_screenshot", None)
        if saved is not None:
            iface.screenshot = saved
            iface.screenshot_surface = getattr(iface, "_kag_saved_screenshot_surface", None)
            iface.clear_screenshot = False
            return True
        return False

    def _kag_clear_saved_screenshot_on_gameplay():
        if kag_is_clean_gameplay():
            kag_clear_saved_screenshot()

    def _kag_on_after_load():
        kag_clear_saved_screenshot()

    def kag_on_overlay_screen_hide(hiding_screen=None):
        if kag_is_clean_gameplay(excluding_screen=hiding_screen):
            kag_clear_saved_screenshot()

    def kag_close_menubar_dropdown(clear_saved=True):
        if getattr(store, "_kag_active_dropdown", None) is not None:
            store._kag_active_dropdown = None
            renpy.restart_interaction()
        if clear_saved and kag_is_clean_gameplay():
            kag_clear_saved_screenshot()

    def kag_toggle_menubar_dropdown(name):
        cur = getattr(store, "_kag_active_dropdown", None)
        if cur == name:
            store._kag_active_dropdown = None
            if kag_is_clean_gameplay():
                kag_clear_saved_screenshot()
        else:
            if cur is None:
                kag_capture_gameplay_screenshot(force=True)
            store._kag_active_dropdown = name
        renpy.restart_interaction()

    def kag_open_history():
        kag_capture_gameplay_screenshot(force=True)
        kag_close_menubar_dropdown(clear_saved=False)
        if not store.kag_history_enabled or store.kag_in_title or renpy.get_screen("history"):
            _kag_clear_saved_screenshot_on_gameplay()
            return
        try:
            renpy.run(ShowMenu("history"))
        finally:
            _kag_clear_saved_screenshot_on_gameplay()

    def kag_open_about_dialog():
        kag_capture_gameplay_screenshot(force=True)
        kag_close_menubar_dropdown(clear_saved=False)
        if not renpy.get_screen("kag_about_dialog"):
            renpy.show_screen("kag_about_dialog")
            renpy.restart_interaction()

    def kag_open_shortcuts_dialog():
        kag_capture_gameplay_screenshot(force=True)
        kag_close_menubar_dropdown(clear_saved=False)
        if not renpy.get_screen("kag_shortcuts_dialog"):
            renpy.show_screen("kag_shortcuts_dialog")
            renpy.restart_interaction()

    def kag_open_confirm(message, yes_action, no_action=None):
        kag_capture_gameplay_screenshot(force=True)
        kag_close_menubar_dropdown(clear_saved=False)
        if not renpy.get_screen("confirm"):
            renpy.run(Confirm(message, yes_action, no_action))

    def kag_quit_game():
        renpy.quit()

    def kag_handle_game_menu_request():
        if not store.kag_rclick_enabled or store.kag_in_title:
            return
        if kag_in_overlay_menu():
            return
        config.skipping = None
        kag_capture_gameplay_screenshot(force=True)
        kag_close_menubar_dropdown(clear_saved=False)
        if renpy.get_screen("kag_menubar"):
            renpy.hide_screen("kag_menubar")
        kag_restore_saved_screenshot()
        try:
            renpy.call_in_new_context("_kag_rclick_context")
        finally:
            _kag_clear_saved_screenshot_on_gameplay()

    def kag_open_saveload_from_menubar(mode="save"):
        config.skipping = None
        kag_capture_gameplay_screenshot(force=True)
        kag_close_menubar_dropdown(clear_saved=False)
        renpy.hide_screen("kag_menubar")
        if renpy.get_screen("kag_save_load"):
            kag_restore_saved_screenshot()
            renpy.show_screen("kag_save_load", mode=mode, from_load_ks=False, from_rclick=False)
            renpy.restart_interaction()
            return
        kag_restore_saved_screenshot()
        try:
            renpy.call_in_new_context("_kag_menubar_saveload_context", mode=mode)
        finally:
            _kag_clear_saved_screenshot_on_gameplay()

    def kag_set_mixer_percent(mixer_name, pct):
        val = max(0.0, min(1.0, float(pct) / 100.0))
        _preferences.set_volume(mixer_name, val)
        renpy.restart_interaction()

    def kag_get_mixer_percent(mixer_name):
        return int(round(_preferences.get_volume(mixer_name) * 100.0))

    def kag_slot_name(idx):
        return "kag_{}".format(idx + 1)

    def kag_save_to_slot(idx):
        if persistent.kag_locks[idx]:
            renpy.notify(kag_tr("ロックされているため上書きできません。"))
            return
        bm = store.kag_current_bookmark or "ないしょのまほう"
        bms = list(persistent.kag_bookmarks)
        dts = list(persistent.kag_dates)
        cmts = list(persistent.kag_comments)
        bms[idx] = bm
        dts[idx] = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        # Clear previous slot comment on overwrite (matching plug_rclick_tjs.ks)
        cmts[idx] = ""
        persistent.kag_bookmarks = bms
        persistent.kag_dates = dts
        persistent.kag_comments = cmts
        store.save_name = bm
        kag_restore_saved_screenshot()
        renpy.save(kag_slot_name(idx), extra_info=bm)
        renpy.notify(kag_tr("セーブしました。"))
        renpy.restart_interaction()

    def kag_load_from_slot(idx):
        sname = kag_slot_name(idx)
        if not renpy.can_load(sname):
            return
        kag_clear_saved_screenshot()
        store.kag_in_title = False
        store.kag_rclick_enabled = True
        renpy.load(sname)

    def kag_toggle_slot_lock(idx):
        locks = list(persistent.kag_locks)
        locks[idx] = not locks[idx]
        persistent.kag_locks = locks
        renpy.restart_interaction()

    def kag_update_slot_comment(idx, txt):
        comments = list(persistent.kag_comments)
        comments[idx] = txt[:48]
        persistent.kag_comments = comments

    def kag_prepare_new_game():
        kag_clear_saved_screenshot()
        store.kag_f = KAGVars()
        store._history_list[:] = []
        store.kag_in_title = False
        store.kag_rclick_enabled = True
        store.kag_history_output = True
        store._history = True
        store.kag_history_enabled = True
        kag_cm()
        if renpy.game.contexts:
            renpy.game.contexts[0].set_return_stack([])

    def kag_return_to_title():
        kag_clear_saved_screenshot()
        for ch in ("music", "se0", "se1", "se2"):
            renpy.music.stop(channel=ch, fadeout=0.3)
        store.kag_se0_is_bgm = False
        store.kag_bgm_looping = False
        config.skipping = None
        kag_cm()
        store.kag_in_choices = False
        store.kag_mesframe_visible = False
        store.kag_mesframe_fade = False
        store._kag_active_dropdown = None
        store._kag_capturing_shortcut = None
        for scr in ("kag_menubar", "kag_save_load", "kag_rclick_menu", "kag_comment_editor", "kag_about_dialog", "kag_shortcuts_dialog", "kag_android_menu"):
            if renpy.get_screen(scr):
                renpy.hide_screen(scr)
        renpy.hide("kag_fg_0", layer="master")
        renpy.hide("kag_fg_1", layer="master")
        renpy.hide("kag_fg_2", layer="master")
        if renpy.game.contexts:
            renpy.game.contexts[0].set_return_stack([])
        if renpy.context_nesting_level() > 0:
            renpy.jump_out_of_context("kag_menu_gamestart")
        else:
            renpy.jump("kag_menu_gamestart")

    def kag_measure_indent_from_what(what):
        # Measure translated or original speaker「 prefix so zh_cn indent matches rendered text.
        if not what:
            return 0
        plain = re.sub(r"\{[^{}]*\}", "", str(what))
        if "「" in plain and plain.index("「") <= 12 and "\n" not in plain.split("「", 1)[0]:
            pref = plain.split("「", 1)[0] + "「"
            if (len(pref) >= 2 or store.kag_next_indent_prefix == "「") and not any(c in pref for c in "。、！？，, "):
                return kag_measure_text_width(pref)
        if store.kag_next_indent_prefix:
            return kag_measure_text_width(store.kag_next_indent_prefix)
        return 0

    def kag_on_say_display(what):
        # Keep translated text synchronized for hold box during subsequent [ws]/[wait]
        store.kag_hold_box_text = what or ""
        store.kag_hold_box_indent = kag_measure_indent_from_what(what)
        store.kag_hold_box_active = True

    def kag_format_history_line(h):
        raw = (((h.who + " ") if getattr(h, "who", None) else "") + (getattr(h, "what", "") or ""))
        return re.sub(r"\{(?:w|nw|fast|p)(?:=[^{}]*)?\}", "", raw)

    def kag_get_msg_inner_rect():
        l, t, w, h = store.kag_msg_rect
        if store.kag_mesframe_visible and (l, t, w, h) == (20, 465, 768, 105):
            return (36, 480, 732, 85)
        return (l + 12, t + 8, max(100, w - 24), max(40, h - 16))

    def kag_in_overlay_menu(excluding_screen=None):
        for scr in (
            "kag_save_load",
            "kag_rclick_menu",
            "kag_comment_editor",
            "kag_input_dialog",
            "kag_about_dialog",
            "kag_shortcuts_dialog",
            "kag_android_menu",
            "history",
            "confirm",
        ):
            if scr != excluding_screen and renpy.get_screen(scr):
                return True
        return False

    def kag_in_text_input():
        return bool(
            renpy.get_screen("kag_comment_editor")
            or renpy.get_screen("kag_input_dialog")
            or renpy.get_screen("kag_shortcuts_dialog")
            or getattr(store, "_kag_capturing_shortcut", None)
        )

    KAG_SHORTCUT_SPEC = [
        ("save", "栞をはさむ (セーブ)", "K_s"),
        ("load", "栞をたどる (ロード)", "K_l"),
        ("history", "メッセージ履歴を見る", "K_r"),
        ("hide_msg", "メッセージを消す", "K_h"),
        ("toggle_skip", "次に進むまでスキップ", "K_TAB"),
        ("fast_skip", "早送りスキップ (押し続け)", "K_LCTRL"),
        ("fullscreen", "全画面 / ウィンドウ切替", "K_F11"),
        ("game_menu", "右クリックメニュー / 戻る", "K_ESCAPE"),
        ("menubar", "メニューバーを開く", "K_F10"),
        ("screenshot", "スクリーンショット", "K_F12"),
        ("shortcuts", "ショートカット設定", "K_F9"),
        ("title", "最初に戻る (タイトル)", "alt_K_r"),
        ("quit", "終了", "alt_K_q"),
    ]

    _KAG_MODIFIER_KEYSYMS = frozenset((
        "K_LCTRL", "K_RCTRL",
        "K_LALT", "K_RALT",
        "K_LSHIFT", "K_RSHIFT",
        "K_LGUI", "K_RGUI",
        "K_LMETA", "K_RMETA",
    ))

    _KAG_KEY_LABELS = {
        "K_ESCAPE": "Esc",
        "K_RETURN": "Enter",
        "K_KP_ENTER": "NumEnter",
        "K_SPACE": "Space",
        "K_TAB": "Tab",
        "K_BACKSPACE": "Backspace",
        "K_INSERT": "Insert",
        "K_DELETE": "Delete",
        "K_HOME": "Home",
        "K_END": "End",
        "K_PAGEUP": "PageUp",
        "K_PAGEDOWN": "PageDown",
        "K_UP": "Up",
        "K_DOWN": "Down",
        "K_LEFT": "Left",
        "K_RIGHT": "Right",
        "K_LCTRL": "L-Ctrl",
        "K_RCTRL": "R-Ctrl",
        "K_LALT": "L-Alt",
        "K_RALT": "R-Alt",
        "K_LSHIFT": "L-Shift",
        "K_RSHIFT": "R-Shift",
        "K_LGUI": "L-Super",
        "K_RGUI": "R-Super",
        "K_COMMA": ",",
        "K_PERIOD": ".",
        "K_SLASH": "/",
        "K_SEMICOLON": ";",
        "K_QUOTE": "'",
        "K_LEFTBRACKET": "[",
        "K_RIGHTBRACKET": "]",
        "K_BACKSLASH": "\\",
        "K_MINUS": "-",
        "K_EQUALS": "=",
        "K_BACKQUOTE": "`",
        "K_CAPSLOCK": "CapsLock",
        "K_PAUSE": "Pause",
        "K_MENU": "Menu",
        "K_PRINT": "PrintScreen",
        "K_SYSREQ": "PrintScreen",
    }

    _KAG_SDK_CONFLICT_KEYMAPS = (
        "screenshot",
        "reload_game",
        "toggle_fullscreen",
        "toggle_skip",
        "fast_skip",
        "self_voicing",
        "clipboard_voicing",
        "screenreader_voicing",
        "debug_voicing",
        "director",
        "help",
        "developer",
        "inspector",
        "full_inspector",
        "launch_editor",
        "choose_renderer",
        "progress_screen",
        "bubble_editor",
        "accessibility",
    )

    def _kag_sc_keymap_tokens(key_str):
        if not key_str:
            return []
        parts = str(key_str).split("_")
        mods = []
        idx = 0
        while idx < len(parts) and parts[idx] in ("anymod", "shift", "noshift", "ctrl", "alt", "meta", "osctrl", "any", "repeat", "anyrepeat"):
            mods.append(parts[idx])
            idx += 1
        base = "_".join(parts[idx:]) if idx < len(parts) else str(key_str)
        if base in _KAG_MODIFIER_KEYSYMS and "anymod" not in mods:
            return ["anymod_" + str(key_str)]
        if "shift" not in mods and "noshift" not in mods and "anymod" not in mods and base.startswith("K_"):
            return ["noshift_" + str(key_str)]
        return [str(key_str)]

    def _kag_key_signature(tok):
        parts = str(tok).split("_")
        mods = set()
        idx = 0
        ignored = {"anymod", "any", "repeat", "anyrepeat", "noshift", "keydown", "keyup", "caps", "nocaps", "num", "nonum"}
        known = {"alt", "ctrl", "shift", "meta", "osctrl"}
        while idx < len(parts) and (parts[idx] in ignored or parts[idx] in known):
            if parts[idx] in known:
                mods.add("ctrl" if parts[idx] == "osctrl" else parts[idx])
            idx += 1
        base = "_".join(parts[idx:]) if idx < len(parts) else str(tok)
        return (frozenset(mods), base)

    def kag_get_shortcuts():
        cur = persistent.kag_shortcuts
        res = {}
        for sid, _lbl, default_k in KAG_SHORTCUT_SPEC:
            if isinstance(cur, dict) and sid in cur:
                val = cur[sid]
                res[sid] = str(val) if val else None
            else:
                res[sid] = default_k
        return res

    def kag_format_shortcut_key(key_str):
        if not key_str:
            return kag_tr("未設定")
        parts = str(key_str).split("_")
        mod_names = []
        seen_mods = set()
        idx = 0
        skip_mods = {"anymod", "noshift", "any", "repeat", "anyrepeat", "keydown", "keyup", "caps", "nocaps", "num", "nonum"}
        mod_labels = {"ctrl": "Ctrl", "osctrl": "Ctrl", "alt": "Alt", "shift": "Shift", "meta": "Meta"}
        while idx < len(parts) and (parts[idx] in skip_mods or parts[idx] in mod_labels):
            p = parts[idx]
            if p in mod_labels and mod_labels[p] not in seen_mods:
                seen_mods.add(mod_labels[p])
                mod_names.append(mod_labels[p])
            idx += 1
        base = "_".join(parts[idx:]) if idx < len(parts) else str(key_str)
        if base in _KAG_KEY_LABELS:
            k_lbl = _KAG_KEY_LABELS[base]
        elif base.startswith("K_KP"):
            k_lbl = "Num" + base[4:]
        elif base.startswith("K_F") and base[3:].isdigit():
            k_lbl = base[2:]
        elif base.startswith("K_") and len(base) == 3:
            k_lbl = base[2:].upper()
        elif base.startswith("K_"):
            k_lbl = base[2:].capitalize()
        else:
            k_lbl = base
        if mod_names:
            return "+".join(mod_names + [k_lbl])
        return k_lbl

    def kag_apply_shortcuts(*_args, **_kwargs):
        sc = kag_get_shortcuts()
        if not hasattr(store, "_kag_orig_sdk_keymaps"):
            store._kag_orig_sdk_keymaps = {k: list(config.keymap.get(k, [])) for k in _KAG_SDK_CONFLICT_KEYMAPS}
        active_sigs = set()
        for sid, val in sc.items():
            if val:
                active_sigs.add(_kag_key_signature(val))
        for k in _KAG_SDK_CONFLICT_KEYMAPS:
            if k in ("screenshot", "toggle_fullscreen", "toggle_skip", "fast_skip"):
                config.keymap[k] = []
                continue
            orig = store._kag_orig_sdk_keymaps.get(k, [])
            filtered = []
            for tok in orig:
                if k == "reload_game" and tok == "alt_K_r":
                    continue
                if _kag_key_signature(tok) in active_sigs:
                    continue
                filtered.append(tok)
            config.keymap[k] = filtered
        config.keymap["skip"] = _kag_sc_keymap_tokens(sc.get("fast_skip"))
        config.keymap["hide_windows"] = _kag_sc_keymap_tokens(sc.get("hide_msg")) + ["mouseup_2"]
        config.keymap["game_menu"] = _kag_sc_keymap_tokens(sc.get("game_menu")) + ["mouseup_3", "K_MENU", "K_PAUSE"]
        for sid in ("save", "load", "history", "hide_msg", "toggle_skip", "fullscreen", "menubar", "screenshot", "shortcuts", "title", "quit"):
            config.keymap["kag_sc_" + sid] = _kag_sc_keymap_tokens(sc.get(sid))
        try:
            renpy.display.behavior.clear_keymap_cache()
        except Exception:
            pass

    if kag_apply_shortcuts not in config.after_load_callbacks:
        config.after_load_callbacks.append(kag_apply_shortcuts)

    def kag_set_shortcut(sc_id, key_str):
        sc = kag_get_shortcuts()
        if sc_id not in sc:
            return
        new_sig = _kag_key_signature(key_str) if key_str else None
        for other_id in list(sc.keys()):
            if other_id != sc_id and sc[other_id] and new_sig is not None:
                if _kag_key_signature(sc[other_id]) == new_sig:
                    sc[other_id] = None
        sc[sc_id] = str(key_str) if key_str else None
        persistent.kag_shortcuts = dict(sc)
        kag_apply_shortcuts()
        renpy.restart_interaction()

    def kag_clear_shortcut(sc_id):
        sc = kag_get_shortcuts()
        if sc_id not in sc:
            return
        sc[sc_id] = None
        persistent.kag_shortcuts = dict(sc)
        kag_apply_shortcuts()
        renpy.restart_interaction()

    def kag_reset_shortcuts():
        persistent.kag_shortcuts = {sid: default_k for sid, _lbl, default_k in KAG_SHORTCUT_SPEC}
        store._kag_capturing_shortcut = None
        kag_apply_shortcuts()
        renpy.notify(kag_tr("ショートカットを初期設定に戻しました。"))
        renpy.restart_interaction()

    def kag_trigger_shortcut_action(sc_id):
        if kag_in_text_input():
            return
        if sc_id == "menubar":
            if kag_in_overlay_menu():
                return
            nm = getattr(store, "_kag_native_menubar", None)
            if nm and getattr(store, "_kag_native_menubar_active", False):
                nm.open_gtk_menu("top_sys")
            else:
                cur = getattr(store, "_kag_active_dropdown", None)
                kag_toggle_menubar_dropdown("sys" if cur is None else cur)
            return
        if sc_id in ("fullscreen", "screenshot", "hide_msg", "toggle_skip"):
            kag_close_menubar_dropdown(clear_saved=True)
        if sc_id == "fullscreen":
            nm = getattr(store, "_kag_native_menubar", None)
            if nm and nm.backend == "gtk3" and nm.gtk_win and not nm._cleaned_up:
                nm.set_display_mode("window" if nm.is_fullscreen else "fullscreen")
            else:
                renpy.run(Preference("display", "window" if preferences.fullscreen else "fullscreen"))
            return
        if sc_id == "screenshot":
            renpy.run(Screenshot())
            return
        if sc_id == "shortcuts":
            kag_open_shortcuts_dialog()
            return
        if sc_id == "quit":
            kag_open_confirm(kag_tr("終了しますか？"), Function(kag_quit_game))
            return
        if sc_id == "load":
            if kag_in_overlay_menu():
                return
            kag_open_saveload_from_menubar("load")
            return
        if kag_in_overlay_menu():
            return
        if sc_id == "save":
            if not store.kag_in_title and store.kag_rclick_enabled:
                kag_open_saveload_from_menubar("save")
        elif sc_id == "history":
            if store.kag_history_enabled and not store.kag_in_title:
                kag_open_history()
        elif sc_id == "hide_msg":
            if not store.kag_in_title:
                renpy.run(HideInterface())
        elif sc_id == "toggle_skip":
            if not store.kag_in_title and store.kag_clickskip_enabled:
                kag_start_skip()
        elif sc_id == "title":
            if not store.kag_in_title and not renpy.get_screen("confirm"):
                kag_open_confirm(kag_tr("タイトルへ戻りますか？"), Function(kag_return_to_title))

init 1200 python:
    kag_apply_shortcuts()
    if _kag_clear_saved_screenshot_on_gameplay not in config.start_interact_callbacks:
        config.start_interact_callbacks.append(_kag_clear_saved_screenshot_on_gameplay)
    if kag_clear_saved_screenshot not in config.start_callbacks:
        config.start_callbacks.append(kag_clear_saved_screenshot)
    if _kag_on_after_load not in config.after_load_callbacks:
        config.after_load_callbacks.append(_kag_on_after_load)

# Animated wait cursors matching LineBreak.asd / pageBreak.asd
image kag_ctc_linebreak:
    "images/ui/linebreak_f00.png"
    pause 0.07
    "images/ui/linebreak_f01.png"
    pause 0.07
    "images/ui/linebreak_f02.png"
    pause 0.07
    "images/ui/linebreak_f03.png"
    pause 0.07
    "images/ui/linebreak_f04.png"
    pause 0.07
    "images/ui/linebreak_f05.png"
    pause 0.07
    "images/ui/linebreak_f06.png"
    pause 0.07
    "images/ui/linebreak_f07.png"
    pause 0.07
    "images/ui/linebreak_f08.png"
    pause 0.07
    "images/ui/linebreak_f09.png"
    pause 0.07
    "images/ui/linebreak_f10.png"
    pause 0.07
    "images/ui/linebreak_f11.png"
    pause 0.07
    "images/ui/linebreak_f12.png"
    pause 0.07
    "images/ui/linebreak_f13.png"
    pause 0.07
    "images/ui/linebreak_f14.png"
    pause 0.07
    repeat

image kag_ctc_pagebreak:
    "images/ui/pagebreak_f00.png"
    pause 0.05
    "images/ui/pagebreak_f01.png"
    pause 0.05
    "images/ui/pagebreak_f02.png"
    pause 0.05
    "images/ui/pagebreak_f03.png"
    pause 0.05
    "images/ui/pagebreak_f04.png"
    pause 0.05
    "images/ui/pagebreak_f05.png"
    pause 0.05
    "images/ui/pagebreak_f06.png"
    pause 0.05
    "images/ui/pagebreak_f07.png"
    pause 0.05
    "images/ui/pagebreak_f08.png"
    pause 0.05
    "images/ui/pagebreak_f09.png"
    pause 0.05
    "images/ui/pagebreak_f10.png"
    pause 0.05
    "images/ui/pagebreak_f11.png"
    pause 0.20
    repeat

define narrator = Character(None, what_style="say_dialogue", ctc="kag_ctc_pagebreak", ctc_position="nestled")

default kag_in_boot_splash = False

# Single-context KAG3 entry routing matching first.ks -> prologue.ks / menu.ks
label hide_windows:
    if kag_in_title or kag_in_overlay_menu() or kag_in_text_input():
        return True
    return False

label main_menu:
    return

label start:
    $ main_menu = False
    $ kag_sync_on_start()
    $ kag_in_boot_splash = False
    $ kag_f = KAGVars()
    jump kag_menu_gamestart

label kag_s_wait:
    if kag_menu_buttons or kag_menu_links:
        $ config.skipping = None
        $ _sel = renpy.call_screen("kag_interactive_menu", buttons=list(kag_menu_buttons), links=list(kag_menu_links))
        $ kag_clear_menu_items()
        $ kag_cm()
        if isinstance(_sel, tuple) and len(_sel) == 4:
            $ _st, _tg, _ex, _cs = _sel
            if _cs == "menu" and _tg == "*newgame":
                $ kag_prepare_new_game()
            elif _cs == "menu" and _tg in ("*loadgame", "*omake", "*settei"):
                $ kag_in_title = False
            if _ex:
                $ kag_exec_exp(_ex)
            if _st is not None or _tg is not None:
                if renpy.get_return_stack():
                    $ renpy.pop_call()
                $ kag_jump(_cs, storage=_st, target=_tg)
    else:
        $ renpy.pause()
    return

label _kag_menubar_saveload_context(mode="save"):
    $ kag_restore_saved_screenshot()
    $ renpy.call_screen("kag_save_load", mode=mode, from_load_ks=False, from_rclick=False)
    return

label _kag_rclick_context:
    python:
        while True:
            _rc_res = renpy.call_screen("kag_rclick_menu")
            if _rc_res in ("save", "load"):
                kag_restore_saved_screenshot()
                renpy.call_screen("kag_save_load", mode=_rc_res, from_rclick=True)
            elif _rc_res == "msgclr":
                renpy.call_in_new_context("_hide_windows")
            elif _rc_res == "msgskip":
                if store.kag_clickskip_enabled:
                    config.skipping = "slow"
                break
            elif _rc_res == "backtitle":
                if renpy.call_screen("confirm", message=kag_tr("タイトルへ戻りますか？"), yes_action=Return(True), no_action=Return(False)):
                    kag_return_to_title()
                    break
            elif _rc_res == "quit":
                if renpy.call_screen("confirm", message=kag_tr("終了しますか？"), yes_action=Return(True), no_action=Return(False)):
                    renpy.quit()
            else:
                break
    return

label kag_open_rclick_menu:
    # Called by 08. other/load.ks (`f.loadmode == 1`)
    $ renpy.call_screen("kag_save_load", mode="load", from_load_ks=True, from_rclick=False)
    return
