# Faithful KAG3 / KiriKiri2 Screens & Native OS Top Menu Bar for Ren'Py 8 (800x600)

init python:
    import ctypes
    import os
    import sys

    if "kag_mesframe_overlay" not in config.overlay_screens:
        config.overlay_screens.append("kag_mesframe_overlay")
    if "kag_menubar_hotspot" not in config.overlay_screens:
        config.overlay_screens.append("kag_menubar_hotspot")

    def kag_get_active_dropdown():
        return getattr(store, "_kag_active_dropdown", None)

    _kag_native_menu_queue = []
    _kag_native_menubar_active = False

    def _kag_mnemonic_label(raw_label, prefix_char="_"):
        s = kag_tr(raw_label)
        if not prefix_char:
            return s
        if "(" in s and ")" in s:
            idx = s.rfind("(")
            return s[:idx + 1] + prefix_char + s[idx + 1:]
        return s

    def _kag_window_title():
        return kag_tr("おジャ魔女あどべんちゃ～「ないしょのまほう」")

    _KAG_IMMEDIATE_MENU_PREFIXES = ("speed:", "font:", "vol:", "disp:", "lang:")
    _KAG_IMMEDIATE_MENU_EXACT = ("movie_toggle", "about", "shortcuts")

    class _X11AnyEvent(ctypes.Structure):
        _fields_ = [
            ("type", ctypes.c_int),
            ("serial", ctypes.c_ulong),
            ("send_event", ctypes.c_int),
            ("display", ctypes.c_void_p),
            ("window", ctypes.c_ulong),
        ]

    class _X11KeyEvent(ctypes.Structure):
        _fields_ = [
            ("type", ctypes.c_int),
            ("serial", ctypes.c_ulong),
            ("send_event", ctypes.c_int),
            ("display", ctypes.c_void_p),
            ("window", ctypes.c_ulong),
            ("root", ctypes.c_ulong),
            ("subwindow", ctypes.c_ulong),
            ("time", ctypes.c_ulong),
            ("x", ctypes.c_int),
            ("y", ctypes.c_int),
            ("x_root", ctypes.c_int),
            ("y_root", ctypes.c_int),
            ("state", ctypes.c_uint),
            ("keycode", ctypes.c_uint),
            ("same_screen", ctypes.c_int),
        ]

    class _X11FocusChangeEvent(ctypes.Structure):
        _fields_ = [
            ("type", ctypes.c_int),
            ("serial", ctypes.c_ulong),
            ("send_event", ctypes.c_int),
            ("display", ctypes.c_void_p),
            ("window", ctypes.c_ulong),
            ("mode", ctypes.c_int),
            ("detail", ctypes.c_int),
        ]

    class _KAGNativeMenuBar(object):
        """
        Cross-platform native OS top menu bar controller:
        - Linux (X11): Native GTK3 GtkMenuBar + GtkMenu + GtkCheckMenuItem embedded at top of SDL2 X11 window.
        - Windows (Win32): Native Win32 HMENU (CreateMenu / CreatePopupMenu / SetMenu) attached to SDL2 HWND.
        """
        def __init__(self):
            self.active = False
            self.backend = None
            self._updating = False
            self._callbacks = []
            self._last_state_sig = None
            self._last_lang = "__unset__"
            self.is_fullscreen = False
            self._cleaned_up = False

            # Linux GTK3 + X11 handles
            self.gtk = None
            self.gdk = None
            self.gobj = None
            self.x11 = None
            self.dpy = None
            self.screen_num = 0
            self.root_xid = 0
            self.sdl_xid = 0
            self.gtk_win = None
            self.gdk_win = None
            self.gtk_xid = 0
            self.ebox = None
            self.ebox_xid = 0
            self.menubar = None
            self.gtk_items = {}
            self.gtk_vol_items = {}
            self._gtk_menu_open = False
            self._fs_autohide_shown = False
            self._gdk_filter_cb = None

            # Windows Win32 handles
            self.user32 = None
            self.kernel32 = None
            self.hwnd = 0
            self.hmenu = 0
            self.win_cmd_map = {}
            self.win_id_by_action = {}
            self.win_radio_groups = {}
            self._orig_wndproc = 0
            self._wndproc_ref = None
            self._win_menu_attached = False

            # macOS Cocoa / AppKit handles
            self.objc = None
            self.cocoa_target = None
            self.cocoa_items = {}
            self.cocoa_vol_items = {}
            self.cocoa_tag_map = {}

        def ensure_initialized(self):
            if self.active or self.backend == "unavailable":
                return self.active
            if "kag_is_android_ui" in globals() and kag_is_android_ui():
                self.backend = "unavailable"
                return False
            if os.environ.get("SDL_VIDEODRIVER") == "dummy":
                return False
            try:
                if sys.platform.startswith("linux") and os.environ.get("DISPLAY"):
                    if self._init_linux_gtk():
                        self.active = True
                        self.backend = "gtk3"
                        store._kag_native_menubar_active = True
                        return True
                elif sys.platform == "win32":
                    if self._init_windows_win32():
                        self.active = True
                        self.backend = "win32"
                        store._kag_native_menubar_active = True
                        return True
                elif sys.platform == "darwin" and not renpy.ios and not renpy.mobile:
                    if self._init_macos_cocoa():
                        self.active = True
                        self.backend = "cocoa"
                        store._kag_native_menubar_active = True
                        return True
            except Exception as exc:
                renpy.log("Native menubar init fallback: %r" % (exc,))
                self.backend = "unavailable"
            return False

        def _find_sdl_x11_window(self, win, target_pid, atom_pid, wa_cls):
            actual_type = ctypes.c_ulong()
            actual_format = ctypes.c_int()
            nitems = ctypes.c_ulong()
            bytes_after = ctypes.c_ulong()
            prop = ctypes.c_void_p()
            if self.x11.XGetWindowProperty(
                self.dpy, win, atom_pid, 0, 1, 0, 0,
                ctypes.byref(actual_type), ctypes.byref(actual_format),
                ctypes.byref(nitems), ctypes.byref(bytes_after),
                ctypes.byref(prop)
            ) == 0 and prop.value:
                matched = False
                if nitems.value >= 1:
                    pid = ctypes.cast(prop, ctypes.POINTER(ctypes.c_ulong)).contents.value
                    matched = (pid == target_pid)
                self.x11.XFree(prop)
                if matched:
                    wa = wa_cls()
                    if self.x11.XGetWindowAttributes(self.dpy, win, ctypes.byref(wa)) != 0:
                        if wa.c_class == 1 and not wa.override_redirect and wa.width >= 640 and wa.height >= 480:
                            return win
            root_ret = ctypes.c_ulong()
            parent_ret = ctypes.c_ulong()
            children_ptr = ctypes.c_void_p()
            nchildren = ctypes.c_uint()
            if self.x11.XQueryTree(
                self.dpy, win, ctypes.byref(root_ret), ctypes.byref(parent_ret),
                ctypes.byref(children_ptr), ctypes.byref(nchildren)
            ) != 0 and children_ptr.value:
                arr = ctypes.cast(children_ptr, ctypes.POINTER(ctypes.c_ulong * nchildren.value)).contents
                cands = list(arr)
                self.x11.XFree(children_ptr)
                for ch in cands:
                    res = self._find_sdl_x11_window(ch, target_pid, atom_pid, wa_cls)
                    if res:
                        return res
            return 0

        def _send_sdl_focus(self, focused=True):
            if self.backend != "gtk3" or not self.dpy or not self.sdl_xid or self._cleaned_up:
                return
            try:
                fev = _X11FocusChangeEvent()
                fev.type = 9 if focused else 10
                fev.serial = 0
                fev.send_event = 1
                fev.display = self.dpy
                fev.window = self.sdl_xid
                fev.mode = 0
                fev.detail = 3
                self.x11.XSendEvent(self.dpy, self.sdl_xid, 0, 0, ctypes.byref(fev))
                self.x11.XFlush(self.dpy)
            except Exception:
                pass

        def open_gtk_menu(self, top_key="top_sys"):
            if self.backend != "gtk3" or not self.menubar or top_key not in self.gtk_items:
                return
            try:
                self._gtk_menu_open = True
                if self.is_fullscreen:
                    self.gtk.gtk_widget_show(self.menubar)
                    self._fs_autohide_shown = True
                self.gtk.gtk_menu_shell_select_item(self.menubar, self.gtk_items[top_key][0])
                while self.gtk.gtk_events_pending():
                    self.gtk.gtk_main_iteration_do(0)
            except Exception:
                pass

        def set_display_mode(self, mode):
            want_full = (mode == "fullscreen")
            if self.backend == "gtk3" and self.gtk_win and not self._cleaned_up:
                if want_full and not self.is_fullscreen:
                    self.is_fullscreen = True
                    self._fs_autohide_shown = False
                    self.gtk.gtk_widget_hide(self.menubar)
                    self.gtk.gtk_window_fullscreen(self.gtk_win)
                elif not want_full and self.is_fullscreen:
                    self.is_fullscreen = False
                    self._fs_autohide_shown = False
                    self.gtk.gtk_window_unfullscreen(self.gtk_win)
                    self.gtk.gtk_widget_show(self.menubar)
                    while self.gtk.gtk_events_pending():
                        self.gtk.gtk_main_iteration_do(0)
                    mb_h = max(24, int(self.gtk.gtk_widget_get_allocated_height(self.menubar)))
                    self.gtk.gtk_window_resize(self.gtk_win, 800, 600 + mb_h)
                while self.gtk.gtk_events_pending():
                    self.gtk.gtk_main_iteration_do(0)
                if not self._gtk_menu_open and self.gtk.gtk_window_is_active(self.gtk_win):
                    self._send_sdl_focus(True)
                self.sync_state(force=True)
                try:
                    renpy.restart_interaction()
                except Exception:
                    pass
                return
            renpy.run(Preference("display", "fullscreen" if want_full else "window"))

        def _init_linux_gtk(self):
            w = renpy.pygame.display.get_window()
            if w is None:
                return False
            drv = renpy.pygame.display.get_driver()
            if drv and drv != b"x11" and drv != "x11":
                return False

            x11 = ctypes.CDLL("libX11.so.6")
            gdk = ctypes.CDLL("libgdk-3.so.0")
            gtk = ctypes.CDLL("libgtk-3.so.0")
            gobj = ctypes.CDLL("libgobject-2.0.so.0")

            class XWindowAttributes(ctypes.Structure):
                _fields_ = [
                    ("x", ctypes.c_int), ("y", ctypes.c_int),
                    ("width", ctypes.c_int), ("height", ctypes.c_int),
                    ("border_width", ctypes.c_int), ("depth", ctypes.c_int),
                    ("visual", ctypes.c_void_p), ("root", ctypes.c_ulong),
                    ("c_class", ctypes.c_int), ("bit_gravity", ctypes.c_int),
                    ("win_gravity", ctypes.c_int), ("backing_store", ctypes.c_int),
                    ("backing_planes", ctypes.c_ulong), ("backing_pixel", ctypes.c_ulong),
                    ("save_under", ctypes.c_int), ("colormap", ctypes.c_ulong),
                    ("map_installed", ctypes.c_int), ("map_state", ctypes.c_int),
                    ("all_event_masks", ctypes.c_long), ("your_event_mask", ctypes.c_long),
                    ("do_not_propagate_mask", ctypes.c_long), ("override_redirect", ctypes.c_int),
                    ("screen", ctypes.c_void_p),
                ]

            class XSetWindowAttributes(ctypes.Structure):
                _fields_ = [
                    ("background_pixmap", ctypes.c_ulong), ("background_pixel", ctypes.c_ulong),
                    ("border_pixmap", ctypes.c_ulong), ("border_pixel", ctypes.c_ulong),
                    ("bit_gravity", ctypes.c_int), ("win_gravity", ctypes.c_int),
                    ("backing_store", ctypes.c_int), ("backing_planes", ctypes.c_ulong),
                    ("backing_pixel", ctypes.c_ulong), ("save_under", ctypes.c_int),
                    ("event_mask", ctypes.c_long), ("do_not_propagate_mask", ctypes.c_long),
                    ("override_redirect", ctypes.c_int), ("colormap", ctypes.c_ulong),
                    ("cursor", ctypes.c_ulong),
                ]

            class GtkAllocation(ctypes.Structure):
                _fields_ = [
                    ("x", ctypes.c_int), ("y", ctypes.c_int),
                    ("width", ctypes.c_int), ("height", ctypes.c_int),
                ]

            x11.XOpenDisplay.argtypes = [ctypes.c_char_p]
            x11.XOpenDisplay.restype = ctypes.c_void_p
            x11.XDefaultRootWindow.argtypes = [ctypes.c_void_p]
            x11.XDefaultRootWindow.restype = ctypes.c_ulong
            x11.XDefaultScreen.argtypes = [ctypes.c_void_p]
            x11.XDefaultScreen.restype = ctypes.c_int
            x11.XInternAtom.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
            x11.XInternAtom.restype = ctypes.c_ulong
            x11.XFree.argtypes = [ctypes.c_void_p]
            x11.XWithdrawWindow.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.c_int]
            x11.XWithdrawWindow.restype = ctypes.c_int
            x11.XUnmapWindow.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
            x11.XReparentWindow.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_int, ctypes.c_int]
            x11.XMoveResizeWindow.argtypes = [
                ctypes.c_void_p, ctypes.c_ulong, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint
            ]
            x11.XMapRaised.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
            x11.XSendEvent.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.c_int, ctypes.c_long, ctypes.c_void_p]
            x11.XSendEvent.restype = ctypes.c_int
            x11.XFlush.argtypes = [ctypes.c_void_p]
            x11.XFlush.restype = ctypes.c_int
            x11.XQueryPointer.argtypes = [
                ctypes.c_void_p, ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong),
                ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
                ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
                ctypes.POINTER(ctypes.c_uint),
            ]
            x11.XSync.argtypes = [ctypes.c_void_p, ctypes.c_int]
            x11.XGetWindowAttributes.argtypes = [ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(XWindowAttributes)]
            x11.XChangeWindowAttributes.argtypes = [
                ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(XSetWindowAttributes)
            ]
            x11.XQueryTree.argtypes = [
                ctypes.c_void_p, ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong),
                ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_uint),
            ]
            x11.XGetWindowProperty.argtypes = [
                ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong,
                ctypes.c_long, ctypes.c_long, ctypes.c_int, ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_int),
                ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong),
                ctypes.POINTER(ctypes.c_void_p),
            ]
            XERR_HANDLER = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
            x11.XSetErrorHandler.argtypes = [ctypes.c_void_p]
            x11.XSetErrorHandler.restype = ctypes.c_void_p

            def _ignore_xerr(_dpy, _err):
                return 0

            c_xerr = XERR_HANDLER(_ignore_xerr)
            self._callbacks.append(c_xerr)
            x11.XSetErrorHandler(ctypes.cast(c_xerr, ctypes.c_void_p))

            if hasattr(gdk, "gdk_set_allowed_backends"):
                gdk.gdk_set_allowed_backends.argtypes = [ctypes.c_char_p]
                gdk.gdk_set_allowed_backends(b"x11")

            gtk.gtk_init_check.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_char_p)]
            gtk.gtk_init_check.restype = ctypes.c_int
            gtk.gtk_window_new.argtypes = [ctypes.c_int]
            gtk.gtk_window_new.restype = ctypes.c_void_p
            gtk.gtk_window_set_title.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
            gtk.gtk_window_set_icon_from_file.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
            gtk.gtk_window_set_icon_from_file.restype = ctypes.c_int
            gtk.gtk_window_move.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
            gtk.gtk_window_resize.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
            gtk.gtk_window_present.argtypes = [ctypes.c_void_p]
            gtk.gtk_window_is_active.argtypes = [ctypes.c_void_p]
            gtk.gtk_window_is_active.restype = ctypes.c_int
            gtk.gtk_window_fullscreen.argtypes = [ctypes.c_void_p]
            gtk.gtk_window_unfullscreen.argtypes = [ctypes.c_void_p]
            gtk.gtk_box_new.argtypes = [ctypes.c_int, ctypes.c_int]
            gtk.gtk_box_new.restype = ctypes.c_void_p
            gtk.gtk_box_pack_start.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_uint]
            gtk.gtk_event_box_new.argtypes = []
            gtk.gtk_event_box_new.restype = ctypes.c_void_p
            gtk.gtk_event_box_set_visible_window.argtypes = [ctypes.c_void_p, ctypes.c_int]
            gtk.gtk_menu_bar_new.argtypes = []
            gtk.gtk_menu_bar_new.restype = ctypes.c_void_p
            gtk.gtk_menu_new.argtypes = []
            gtk.gtk_menu_new.restype = ctypes.c_void_p
            gtk.gtk_menu_item_new_with_mnemonic.argtypes = [ctypes.c_char_p]
            gtk.gtk_menu_item_new_with_mnemonic.restype = ctypes.c_void_p
            gtk.gtk_check_menu_item_new_with_mnemonic.argtypes = [ctypes.c_char_p]
            gtk.gtk_check_menu_item_new_with_mnemonic.restype = ctypes.c_void_p
            gtk.gtk_check_menu_item_set_active.argtypes = [ctypes.c_void_p, ctypes.c_int]
            gtk.gtk_check_menu_item_get_active.argtypes = [ctypes.c_void_p]
            gtk.gtk_check_menu_item_get_active.restype = ctypes.c_int
            gtk.gtk_check_menu_item_set_draw_as_radio.argtypes = [ctypes.c_void_p, ctypes.c_int]
            gtk.gtk_separator_menu_item_new.argtypes = []
            gtk.gtk_separator_menu_item_new.restype = ctypes.c_void_p
            gtk.gtk_menu_item_set_submenu.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
            gtk.gtk_menu_item_set_label.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
            gtk.gtk_menu_item_set_use_underline.argtypes = [ctypes.c_void_p, ctypes.c_int]
            gtk.gtk_menu_shell_append.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
            gtk.gtk_menu_shell_select_item.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
            gtk.gtk_menu_shell_deselect.argtypes = [ctypes.c_void_p]
            gtk.gtk_container_add.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
            gtk.gtk_widget_set_size_request.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
            gtk.gtk_widget_set_sensitive.argtypes = [ctypes.c_void_p, ctypes.c_int]
            gtk.gtk_widget_show_all.argtypes = [ctypes.c_void_p]
            gtk.gtk_widget_show.argtypes = [ctypes.c_void_p]
            gtk.gtk_widget_hide.argtypes = [ctypes.c_void_p]
            gtk.gtk_widget_destroy.argtypes = [ctypes.c_void_p]
            gtk.gtk_widget_get_window.argtypes = [ctypes.c_void_p]
            gtk.gtk_widget_get_window.restype = ctypes.c_void_p
            gtk.gtk_widget_get_allocated_width.argtypes = [ctypes.c_void_p]
            gtk.gtk_widget_get_allocated_width.restype = ctypes.c_int
            gtk.gtk_widget_get_allocated_height.argtypes = [ctypes.c_void_p]
            gtk.gtk_widget_get_allocated_height.restype = ctypes.c_int
            gtk.gtk_widget_get_style_context.argtypes = [ctypes.c_void_p]
            gtk.gtk_widget_get_style_context.restype = ctypes.c_void_p
            gtk.gtk_style_context_add_provider.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint]
            gtk.gtk_events_pending.argtypes = []
            gtk.gtk_events_pending.restype = ctypes.c_int
            gtk.gtk_main_iteration_do.argtypes = [ctypes.c_int]
            gtk.gtk_css_provider_new.argtypes = []
            gtk.gtk_css_provider_new.restype = ctypes.c_void_p
            gtk.gtk_css_provider_load_from_data.argtypes = [
                ctypes.c_void_p, ctypes.c_char_p, ctypes.c_ssize_t, ctypes.POINTER(ctypes.c_void_p)
            ]
            gtk.gtk_css_provider_load_from_data.restype = ctypes.c_int

            gdk.gdk_x11_window_get_xid.argtypes = [ctypes.c_void_p]
            gdk.gdk_x11_window_get_xid.restype = ctypes.c_ulong
            gdk.gdk_window_get_state.argtypes = [ctypes.c_void_p]
            gdk.gdk_window_get_state.restype = ctypes.c_int
            gdk.gdk_window_add_filter.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
            gdk.gdk_window_remove_filter.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

            gobj.g_signal_connect_data.argtypes = [
                ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p,
                ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int,
            ]
            gobj.g_signal_connect_data.restype = ctypes.c_ulong

            self.x11 = x11
            self.gtk = gtk
            self.gdk = gdk
            self.gobj = gobj

            dpy = x11.XOpenDisplay(None)
            if not dpy:
                return False
            self.dpy = dpy
            self.screen_num = x11.XDefaultScreen(dpy)
            self.root_xid = x11.XDefaultRootWindow(dpy)
            atom_pid = x11.XInternAtom(dpy, b"_NET_WM_PID", 0)
            sdl_xid = self._find_sdl_x11_window(self.root_xid, os.getpid(), atom_pid, XWindowAttributes)
            if not sdl_xid:
                return False
            self.sdl_xid = sdl_xid

            orig_pos = w.get_position()
            orig_size = w.get_size()
            canvas_w = max(800, int(orig_size[0]))
            canvas_h = max(600, int(orig_size[1]))

            argc = ctypes.c_int(0)
            argv = ctypes.c_char_p(None)
            if not gtk.gtk_init_check(ctypes.byref(argc), ctypes.byref(argv)):
                return False

            x11.XWithdrawWindow(dpy, sdl_xid, self.screen_num)
            x11.XSync(dpy, 0)
            import time as _time
            for _ in range(10):
                r_ret = ctypes.c_ulong()
                p_ret = ctypes.c_ulong()
                ch_ptr = ctypes.c_void_p()
                n_ch = ctypes.c_uint()
                if x11.XQueryTree(
                    dpy, sdl_xid, ctypes.byref(r_ret), ctypes.byref(p_ret),
                    ctypes.byref(ch_ptr), ctypes.byref(n_ch)
                ) != 0:
                    if ch_ptr.value:
                        x11.XFree(ch_ptr)
                    if p_ret.value == self.root_xid:
                        break
                _time.sleep(0.01)

            gwin = gtk.gtk_window_new(0)
            gtk.gtk_window_set_title(gwin, _kag_window_title().encode("utf-8"))
            icon_file = os.path.join(config.gamedir, "gui", "window_icon.png")
            if os.path.isfile(icon_file):
                err_icon = ctypes.c_void_p(None)
                gtk.gtk_window_set_icon_from_file(gwin, icon_file.encode("utf-8"), ctypes.byref(err_icon))
            if orig_pos and len(orig_pos) == 2:
                gtk.gtk_window_move(gwin, int(orig_pos[0]), int(orig_pos[1]))

            vbox = gtk.gtk_box_new(1, 0)
            gtk.gtk_container_add(gwin, vbox)

            mb = gtk.gtk_menu_bar_new()
            gtk.gtk_box_pack_start(vbox, mb, 0, 0, 0)

            ebox = gtk.gtk_event_box_new()
            gtk.gtk_event_box_set_visible_window(ebox, 1)
            gtk.gtk_widget_set_size_request(ebox, 800, 600)
            prov = gtk.gtk_css_provider_new()
            bg_css = b"* { background-color: #000000; }"
            err_css = ctypes.c_void_p(None)
            gtk.gtk_css_provider_load_from_data(prov, bg_css, len(bg_css), ctypes.byref(err_css))
            gtk.gtk_style_context_add_provider(gtk.gtk_widget_get_style_context(ebox), prov, 800)
            gtk.gtk_box_pack_start(vbox, ebox, 1, 1, 0)

            self.gtk_win = gwin
            self.menubar = mb
            self.ebox = ebox
            self._build_gtk_menus()

            ALLOC_CB = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(GtkAllocation), ctypes.c_void_p)

            def _on_ebox_alloc(_w, alloc_ptr, _d):
                if self._cleaned_up or not self.sdl_xid:
                    return
                al = alloc_ptr.contents
                if al.width > 1 and al.height > 1:
                    self.x11.XMoveResizeWindow(self.dpy, self.sdl_xid, 0, 0, al.width, al.height)
                    self.x11.XSync(self.dpy, 0)

            c_alloc = ALLOC_CB(_on_ebox_alloc)
            self._callbacks.append(c_alloc)
            gobj.g_signal_connect_data(ebox, b"size-allocate", ctypes.cast(c_alloc, ctypes.c_void_p), None, None, 0)

            EVT_BOOL_CB = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

            def _on_delete_event(_w, _ev, _d):
                if "quit" not in _kag_native_menu_queue:
                    _kag_native_menu_queue.append("quit")
                try:
                    renpy.restart_interaction()
                except Exception:
                    pass
                return 1

            c_del = EVT_BOOL_CB(_on_delete_event)
            self._callbacks.append(c_del)
            gobj.g_signal_connect_data(gwin, b"delete-event", ctypes.cast(c_del, ctypes.c_void_p), None, None, 0)

            def _on_win_focus_in(_w, _ev, _d):
                if not self._gtk_menu_open:
                    self._send_sdl_focus(True)
                return 0

            c_focin = EVT_BOOL_CB(_on_win_focus_in)
            self._callbacks.append(c_focin)
            gobj.g_signal_connect_data(gwin, b"focus-in-event", ctypes.cast(c_focin, ctypes.c_void_p), None, None, 0)

            def _on_win_focus_out(_w, _ev, _d):
                self._send_sdl_focus(False)
                return 0

            c_focout = EVT_BOOL_CB(_on_win_focus_out)
            self._callbacks.append(c_focout)
            gobj.g_signal_connect_data(gwin, b"focus-out-event", ctypes.cast(c_focout, ctypes.c_void_p), None, None, 0)

            def _on_win_state(_w, _ev, _d):
                if self.gdk_win:
                    st = self.gdk.gdk_window_get_state(self.gdk_win)
                    fs_now = bool(st & 16)
                    if fs_now != self.is_fullscreen:
                        self.is_fullscreen = fs_now
                        if fs_now:
                            self.gtk.gtk_widget_hide(self.menubar)
                        else:
                            self.gtk.gtk_widget_show(self.menubar)
                        self.sync_state(force=True)
                return 0

            c_wstate = EVT_BOOL_CB(_on_win_state)
            self._callbacks.append(c_wstate)
            gobj.g_signal_connect_data(gwin, b"window-state-event", ctypes.cast(c_wstate, ctypes.c_void_p), None, None, 0)

            SHELL_CB = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

            def _on_menu_closed(_ms, _d):
                self._gtk_menu_open = False
                if self.is_fullscreen and self._fs_autohide_shown:
                    self._fs_autohide_shown = False
                    self.gtk.gtk_widget_hide(self.menubar)
                if self.gtk.gtk_window_is_active(self.gtk_win):
                    self._send_sdl_focus(True)

            c_mclose = SHELL_CB(_on_menu_closed)
            self._callbacks.append(c_mclose)
            gobj.g_signal_connect_data(mb, b"deactivate", ctypes.cast(c_mclose, ctypes.c_void_p), None, None, 0)
            gobj.g_signal_connect_data(mb, b"selection-done", ctypes.cast(c_mclose, ctypes.c_void_p), None, None, 0)

            gtk.gtk_widget_show_all(gwin)
            while gtk.gtk_events_pending():
                gtk.gtk_main_iteration_do(0)

            mb_h = max(24, int(gtk.gtk_widget_get_allocated_height(mb)))
            gtk.gtk_window_resize(gwin, canvas_w, canvas_h + mb_h)
            gtk.gtk_window_present(gwin)
            while gtk.gtk_events_pending():
                gtk.gtk_main_iteration_do(0)

            gdk_win = gtk.gtk_widget_get_window(gwin)
            gtk_xid = gdk.gdk_x11_window_get_xid(gdk_win)
            ebox_gdk = gtk.gtk_widget_get_window(ebox)
            ebox_xid = gdk.gdk_x11_window_get_xid(ebox_gdk)
            self.gdk_win = gdk_win
            self.gtk_xid = gtk_xid
            self.ebox_xid = ebox_xid

            GDK_FILTER_CB = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

            def _on_gdk_xevent(xevent_ptr, _gev, _data):
                if self._cleaned_up or not xevent_ptr or not self.dpy or not self.sdl_xid:
                    return 0
                try:
                    xany = ctypes.cast(xevent_ptr, ctypes.POINTER(_X11AnyEvent)).contents
                    if xany.type in (2, 3) and not self._gtk_menu_open and xany.window != self.sdl_xid:
                        buf = (ctypes.c_long * 24)()
                        ctypes.memmove(buf, xevent_ptr, ctypes.sizeof(buf))
                        xkey = ctypes.cast(buf, ctypes.POINTER(_X11KeyEvent)).contents
                        xkey.window = self.sdl_xid
                        xkey.subwindow = 0
                        self.x11.XSendEvent(self.dpy, self.sdl_xid, 0, 0, ctypes.byref(buf))
                        self.x11.XFlush(self.dpy)
                        return 2
                except Exception:
                    pass
                return 0

            c_filter = GDK_FILTER_CB(_on_gdk_xevent)
            self._callbacks.append(c_filter)
            self._gdk_filter_cb = ctypes.cast(c_filter, ctypes.c_void_p)
            gdk.gdk_window_add_filter(gdk_win, self._gdk_filter_cb, None)

            alloc_w = max(800, int(gtk.gtk_widget_get_allocated_width(ebox)))
            alloc_h = max(600, int(gtk.gtk_widget_get_allocated_height(ebox)))
            x11.XReparentWindow(dpy, sdl_xid, ebox_xid, 0, 0)
            x11.XMoveResizeWindow(dpy, sdl_xid, 0, 0, alloc_w, alloc_h)
            x11.XMapRaised(dpy, sdl_xid)
            x11.XSync(dpy, 0)

            if preferences.fullscreen:
                self.set_display_mode("fullscreen")

            self.sync_state(force=True)
            while gtk.gtk_events_pending():
                gtk.gtk_main_iteration_do(0)
            self._send_sdl_focus(True)
            return True

        def cleanup(self):
            if self._cleaned_up:
                return
            self._cleaned_up = True
            if self.backend == "gtk3" and self.dpy:
                try:
                    if self.gdk and self.gdk_win and self._gdk_filter_cb:
                        self.gdk.gdk_window_remove_filter(self.gdk_win, self._gdk_filter_cb, None)
                        self._gdk_filter_cb = None
                    if self.sdl_xid and self.root_xid:
                        self.x11.XUnmapWindow(self.dpy, self.sdl_xid)
                        self.x11.XReparentWindow(self.dpy, self.sdl_xid, self.root_xid, 0, 0)
                        self.x11.XSync(self.dpy, 0)
                    if self.gtk_win:
                        self.gtk.gtk_widget_hide(self.gtk_win)
                        while self.gtk.gtk_events_pending():
                            self.gtk.gtk_main_iteration_do(0)
                except Exception:
                    pass

        def _connect_gtk_top_item(self, item_widget):
            ITEM_CB = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

            def _on_sel(_w, _d):
                self._gtk_menu_open = True

            c_sel = ITEM_CB(_on_sel)
            self._callbacks.append(c_sel)
            self.gobj.g_signal_connect_data(
                item_widget, b"select", ctypes.cast(c_sel, ctypes.c_void_p), None, None, 0
            )

        def _connect_gtk_action(self, widget, action_token):
            CB_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)

            def _cb(_w_ptr, _data):
                if self._updating:
                    return
                _kag_enqueue_native_action(action_token)

            c_cb = CB_TYPE(_cb)
            self._callbacks.append(c_cb)
            self.gobj.g_signal_connect_data(
                widget, b"activate", ctypes.cast(c_cb, ctypes.c_void_p), None, None, 0
            )

        def _make_gtk_item(self, key, raw_label, parent_shell, action_token=None, check=False, radio=False, sensitive=True):
            lbl_bytes = _kag_mnemonic_label(raw_label, "_").encode("utf-8")
            if check or radio:
                it = self.gtk.gtk_check_menu_item_new_with_mnemonic(lbl_bytes)
                if radio:
                    self.gtk.gtk_check_menu_item_set_draw_as_radio(it, 1)
            else:
                it = self.gtk.gtk_menu_item_new_with_mnemonic(lbl_bytes)
            if not sensitive:
                self.gtk.gtk_widget_set_sensitive(it, 0)
            self.gtk.gtk_menu_shell_append(parent_shell, it)
            if parent_shell == self.menubar:
                self._connect_gtk_top_item(it)
            if key:
                self.gtk_items[key] = (it, raw_label)
            if action_token:
                self._connect_gtk_action(it, action_token)
            return it

        def _build_gtk_menus(self):
            gtk = self.gtk
            mb = self.menubar

            # 1. System(S)
            m_sys_top = self._make_gtk_item("top_sys", "システム(S)", mb)
            m_sys = gtk.gtk_menu_new()
            gtk.gtk_menu_item_set_submenu(m_sys_top, m_sys)
            self._make_gtk_item("sys_save", "栞をはさむ (セーブ)", m_sys, "save")
            self._make_gtk_item("sys_load", "栞をたどる (ロード)", m_sys, "load")
            self._make_gtk_item("sys_hist", "メッセージ履歴を見る", m_sys, "history")
            self._make_gtk_item("sys_hide", "メッセージを消す", m_sys, "hide_msg")
            self._make_gtk_item("sys_skip", "次に進むまでスキップ", m_sys, "skip")
            gtk.gtk_menu_shell_append(m_sys, gtk.gtk_separator_menu_item_new())
            self._make_gtk_item("sys_shortcuts", "ショートカット設定(K)...", m_sys, "shortcuts")
            gtk.gtk_menu_shell_append(m_sys, gtk.gtk_separator_menu_item_new())
            self._make_gtk_item("sys_title", "最初に戻る (タイトル)", m_sys, "title")
            self._make_gtk_item("sys_quit", "終了", m_sys, "quit")
            gtk.gtk_widget_show_all(m_sys)

            # 2. Text(C)
            m_txt_top = self._make_gtk_item("top_text", "文字表示(C)", mb)
            m_txt = gtk.gtk_menu_new()
            gtk.gtk_menu_item_set_submenu(m_txt_top, m_txt)
            self._make_gtk_item("txt_hdr_spd", "文字表示速度", m_txt, sensitive=False)
            self._make_gtk_item("spd_fast", "速い (10ms)", m_txt, "speed:fast", radio=True)
            self._make_gtk_item("spd_normal", "普通 (30ms)", m_txt, "speed:normal", radio=True)
            self._make_gtk_item("spd_slow", "遅い (50ms)", m_txt, "speed:slow", radio=True)
            self._make_gtk_item("spd_instant", "ノーウェイト", m_txt, "speed:instant", radio=True)
            gtk.gtk_menu_shell_append(m_txt, gtk.gtk_separator_menu_item_new())
            self._make_gtk_item("txt_hdr_fnt", "フォント選択", m_txt, sensitive=False)
            self._make_gtk_item("fnt_mono", "等幅ゴシック (原作準拠)", m_txt, "font:mono", radio=True)
            self._make_gtk_item("fnt_prop", "プロポーショナルゴシック", m_txt, "font:prop", radio=True)
            gtk.gtk_widget_show_all(m_txt)

            # 3. Movie(M)
            m_mov_top = self._make_gtk_item("top_movie", "ムービー(M)", mb)
            m_mov = gtk.gtk_menu_new()
            gtk.gtk_menu_item_set_submenu(m_mov_top, m_mov)
            self._make_gtk_item("mov_watch", "ムービーを見る", m_mov, "movie_toggle", check=True)
            gtk.gtk_widget_show_all(m_mov)

            # 4. Volume(V)
            m_vol_top = self._make_gtk_item("top_vol", "音量(V)", mb)
            m_vol = gtk.gtk_menu_new()
            gtk.gtk_menu_item_set_submenu(m_vol_top, m_vol)
            for mix_key, mix_raw in [("music", "ＢＧＭ(B)"), ("voice", "ボイス(V)"), ("sfx", "効果音(S)")]:
                sub_top = self._make_gtk_item("vol_top_" + mix_key, mix_raw, m_vol)
                sub_menu = gtk.gtk_menu_new()
                gtk.gtk_menu_item_set_submenu(sub_top, sub_menu)
                it_mute = self._make_gtk_item(
                    "vol_%s_0" % mix_key, "ミュート (0%)", sub_menu, "vol:%s:0" % mix_key, radio=True
                )
                self.gtk_vol_items[(mix_key, 0)] = it_mute
                for pct in (100, 80, 60, 40, 20, 5):
                    it_p = self._make_gtk_item(
                        None, "%d%%" % pct, sub_menu, "vol:%s:%d" % (mix_key, pct), radio=True
                    )
                    self.gtk_vol_items[(mix_key, pct)] = it_p
                gtk.gtk_widget_show_all(sub_menu)
            gtk.gtk_widget_show_all(m_vol)

            # 5. Display(D)
            m_disp_top = self._make_gtk_item("top_disp", "表示(D)", mb)
            m_disp = gtk.gtk_menu_new()
            gtk.gtk_menu_item_set_submenu(m_disp_top, m_disp)
            self._make_gtk_item("disp_win", "ウィンドウ", m_disp, "disp:window", radio=True)
            self._make_gtk_item("disp_full", "フルスクリーン", m_disp, "disp:fullscreen", radio=True)
            gtk.gtk_widget_show_all(m_disp)

            # 6. Language(L)
            m_lang_top = self._make_gtk_item("top_lang", "言語(L)", mb)
            m_lang = gtk.gtk_menu_new()
            gtk.gtk_menu_item_set_submenu(m_lang_top, m_lang)
            it_ja = gtk.gtk_check_menu_item_new_with_mnemonic("日本語 (Original)".encode("utf-8"))
            gtk.gtk_check_menu_item_set_draw_as_radio(it_ja, 1)
            gtk.gtk_menu_shell_append(m_lang, it_ja)
            self._connect_gtk_action(it_ja, "lang:ja")
            self.gtk_items["lang_ja"] = (it_ja, None)

            it_zh = gtk.gtk_check_menu_item_new_with_mnemonic("简体中文 (Simplified Chinese)".encode("utf-8"))
            gtk.gtk_check_menu_item_set_draw_as_radio(it_zh, 1)
            gtk.gtk_menu_shell_append(m_lang, it_zh)
            self._connect_gtk_action(it_zh, "lang:zh_cn")
            self.gtk_items["lang_zh"] = (it_zh, None)
            gtk.gtk_widget_show_all(m_lang)

            # 7. Help(H)
            m_hlp_top = self._make_gtk_item("top_help", "ヘルプ(H)", mb)
            m_hlp = gtk.gtk_menu_new()
            gtk.gtk_menu_item_set_submenu(m_hlp_top, m_hlp)
            self._make_gtk_item("hlp_about", "このソフトについて(A)...", m_hlp, "about")
            gtk.gtk_widget_show_all(m_hlp)

        def _adjust_win32_client_size(self, target_w=800, target_h=600):
            if not self.hwnd or preferences.fullscreen:
                return
            user32 = self.user32

            class RECT(ctypes.Structure):
                _fields_ = [
                    ("left", ctypes.c_long), ("top", ctypes.c_long),
                    ("right", ctypes.c_long), ("bottom", ctypes.c_long),
                ]

            crect = RECT()
            if not user32.GetClientRect(self.hwnd, ctypes.byref(crect)):
                return
            cw = crect.right - crect.left
            ch = crect.bottom - crect.top
            if cw <= 0 or ch <= 0 or (cw == target_w and ch == target_h):
                return
            style = user32.GetWindowLongW(self.hwnd, -16)
            ex_style = user32.GetWindowLongW(self.hwnd, -20)
            adj = RECT(0, 0, target_w, target_h)
            if user32.AdjustWindowRectEx(ctypes.byref(adj), style, 1, ex_style):
                outer_w = adj.right - adj.left
                outer_h = adj.bottom - adj.top
                user32.SetWindowPos(self.hwnd, None, 0, 0, outer_w, outer_h, 0x0002 | 0x0004 | 0x0010)

        def _init_windows_win32(self):
            w = renpy.pygame.display.get_window()
            if w is None:
                return False
            user32 = ctypes.windll.user32
            kernel32 = ctypes.windll.kernel32
            self.user32 = user32
            self.kernel32 = kernel32

            user32.GetActiveWindow.argtypes = []
            user32.GetActiveWindow.restype = ctypes.c_void_p
            user32.IsWindowVisible.argtypes = [ctypes.c_void_p]
            user32.IsWindowVisible.restype = ctypes.c_int
            user32.GetClassNameW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int]
            user32.GetClassNameW.restype = ctypes.c_int
            user32.EnumThreadWindows.argtypes = [ctypes.c_uint, ctypes.c_void_p, ctypes.c_ssize_t]
            user32.EnumThreadWindows.restype = ctypes.c_int
            kernel32.GetCurrentThreadId.argtypes = []
            kernel32.GetCurrentThreadId.restype = ctypes.c_uint

            user32.CreateMenu.argtypes = []
            user32.CreateMenu.restype = ctypes.c_void_p
            user32.CreatePopupMenu.argtypes = []
            user32.CreatePopupMenu.restype = ctypes.c_void_p
            user32.AppendMenuW.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_size_t, ctypes.c_wchar_p]
            user32.AppendMenuW.restype = ctypes.c_int
            user32.SetMenu.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
            user32.SetMenu.restype = ctypes.c_int
            user32.DrawMenuBar.argtypes = [ctypes.c_void_p]
            user32.DrawMenuBar.restype = ctypes.c_int
            user32.DestroyMenu.argtypes = [ctypes.c_void_p]
            user32.DestroyMenu.restype = ctypes.c_int
            user32.EnableMenuItem.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint]
            user32.EnableMenuItem.restype = ctypes.c_int
            user32.CheckMenuItem.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint]
            user32.CheckMenuItem.restype = ctypes.c_uint
            user32.CheckMenuRadioItem.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
            user32.CheckMenuRadioItem.restype = ctypes.c_int
            user32.SetWindowTextW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p]
            user32.SetWindowTextW.restype = ctypes.c_int
            user32.GetClientRect.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
            user32.GetClientRect.restype = ctypes.c_int
            user32.GetWindowLongW.argtypes = [ctypes.c_void_p, ctypes.c_int]
            user32.GetWindowLongW.restype = ctypes.c_uint
            user32.AdjustWindowRectEx.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_int, ctypes.c_uint]
            user32.AdjustWindowRectEx.restype = ctypes.c_int
            user32.SetWindowPos.argtypes = [
                ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint
            ]
            user32.SetWindowPos.restype = ctypes.c_int

            wm_info = w.get_wm_info() or {}
            hwnd = wm_info.get("window", 0)
            if not hwnd:
                WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_ssize_t)
                sdl_found = []
                vis_found = []

                def _enum_cb(h, _lp):
                    if user32.IsWindowVisible(h):
                        buf = ctypes.create_unicode_buffer(64)
                        user32.GetClassNameW(h, buf, 64)
                        if buf.value == "SDL_app":
                            sdl_found.append(h)
                            return 0
                        vis_found.append(h)
                    return 1

                cb = WNDENUMPROC(_enum_cb)
                user32.EnumThreadWindows(kernel32.GetCurrentThreadId(), ctypes.cast(cb, ctypes.c_void_p), 0)
                hwnd = (sdl_found[0] if sdl_found else (vis_found[0] if vis_found else user32.GetActiveWindow()))
            if not hwnd:
                return False
            self.hwnd = hwnd

            self._build_win32_menus()
            self._adjust_win32_client_size(800, 600)

            # Subclass HWND to intercept WM_COMMAND (0x0111) from native Win32 menu bar
            WNDPROC = ctypes.WINFUNCTYPE(
                ctypes.c_ssize_t, ctypes.c_void_p, ctypes.c_uint, ctypes.c_size_t, ctypes.c_ssize_t
            )
            GWLP_WNDPROC = -4
            set_wndproc = getattr(user32, "SetWindowLongPtrW", user32.SetWindowLongW)
            call_wndproc = user32.CallWindowProcW
            set_wndproc.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
            set_wndproc.restype = ctypes.c_void_p
            call_wndproc.argtypes = [
                ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_size_t, ctypes.c_ssize_t
            ]
            call_wndproc.restype = ctypes.c_ssize_t

            def _wndproc(h, msg, wparam, lparam):
                if msg == 0x0111:  # WM_COMMAND
                    cmd_id = wparam & 0xFFFF
                    act = self.win_cmd_map.get(cmd_id)
                    if act:
                        _kag_enqueue_native_action(act)
                        return 0
                return call_wndproc(self._orig_wndproc, h, msg, wparam, lparam)

            self._wndproc_ref = WNDPROC(_wndproc)
            self._callbacks.append(self._wndproc_ref)
            self._orig_wndproc = set_wndproc(hwnd, GWLP_WNDPROC, ctypes.cast(self._wndproc_ref, ctypes.c_void_p))
            self.sync_state(force=True)
            return True

        def _build_win32_menus(self):
            user32 = self.user32
            MF_STRING = 0x0000
            MF_POPUP = 0x0010
            MF_SEPARATOR = 0x0800
            MF_GRAYED = 0x0001

            self.win_cmd_map.clear()
            self.win_id_by_action.clear()
            self.win_radio_groups.clear()
            next_id = [1001]

            def add_item(hmenu, raw_label, action_token=None, gray=False):
                cid = next_id[0]
                next_id[0] += 1
                lbl = _kag_mnemonic_label(raw_label, "&") if raw_label else ""
                flags = MF_STRING | (MF_GRAYED if gray else 0)
                user32.AppendMenuW(hmenu, flags, cid, ctypes.c_wchar_p(lbl))
                if action_token:
                    self.win_cmd_map[cid] = action_token
                    self.win_id_by_action[action_token] = (hmenu, cid)
                return cid

            menubar = user32.CreateMenu()

            # 1. System
            m_sys = user32.CreatePopupMenu()
            add_item(m_sys, "栞をはさむ (セーブ)", "save")
            add_item(m_sys, "栞をたどる (ロード)", "load")
            add_item(m_sys, "メッセージ履歴を見る", "history")
            add_item(m_sys, "メッセージを消す", "hide_msg")
            add_item(m_sys, "次に進むまでスキップ", "skip")
            user32.AppendMenuW(m_sys, MF_SEPARATOR, 0, None)
            add_item(m_sys, "ショートカット設定(K)...", "shortcuts")
            user32.AppendMenuW(m_sys, MF_SEPARATOR, 0, None)
            add_item(m_sys, "最初に戻る (タイトル)", "title")
            add_item(m_sys, "終了", "quit")
            user32.AppendMenuW(menubar, MF_POPUP, m_sys, ctypes.c_wchar_p(_kag_mnemonic_label("システム(S)", "&")))

            # 2. Text
            m_txt = user32.CreatePopupMenu()
            add_item(m_txt, "文字表示速度", None, gray=True)
            spd_first = add_item(m_txt, "速い (10ms)", "speed:fast")
            add_item(m_txt, "普通 (30ms)", "speed:normal")
            add_item(m_txt, "遅い (50ms)", "speed:slow")
            spd_last = add_item(m_txt, "ノーウェイト", "speed:instant")
            self.win_radio_groups["speed"] = (m_txt, spd_first, spd_last)
            user32.AppendMenuW(m_txt, MF_SEPARATOR, 0, None)
            add_item(m_txt, "フォント選択", None, gray=True)
            fnt_first = add_item(m_txt, "等幅ゴシック (原作準拠)", "font:mono")
            fnt_last = add_item(m_txt, "プロポーショナルゴシック", "font:prop")
            self.win_radio_groups["font"] = (m_txt, fnt_first, fnt_last)
            user32.AppendMenuW(menubar, MF_POPUP, m_txt, ctypes.c_wchar_p(_kag_mnemonic_label("文字表示(C)", "&")))

            # 3. Movie
            m_mov = user32.CreatePopupMenu()
            add_item(m_mov, "ムービーを見る", "movie_toggle")
            user32.AppendMenuW(menubar, MF_POPUP, m_mov, ctypes.c_wchar_p(_kag_mnemonic_label("ムービー(M)", "&")))

            # 4. Volume
            m_vol = user32.CreatePopupMenu()
            for mix_key, mix_raw in [("music", "ＢＧＭ(B)"), ("voice", "ボイス(V)"), ("sfx", "効果音(S)")]:
                sub = user32.CreatePopupMenu()
                v_first = add_item(sub, "ミュート (0%)", "vol:%s:0" % mix_key)
                v_last = v_first
                for pct in (100, 80, 60, 40, 20, 5):
                    cid = next_id[0]
                    next_id[0] += 1
                    act = "vol:%s:%d" % (mix_key, pct)
                    user32.AppendMenuW(sub, MF_STRING, cid, ctypes.c_wchar_p("%d%%" % pct))
                    self.win_cmd_map[cid] = act
                    self.win_id_by_action[act] = (sub, cid)
                    v_last = cid
                self.win_radio_groups["vol_" + mix_key] = (sub, v_first, v_last)
                user32.AppendMenuW(m_vol, MF_POPUP, sub, ctypes.c_wchar_p(_kag_mnemonic_label(mix_raw, "&")))
            user32.AppendMenuW(menubar, MF_POPUP, m_vol, ctypes.c_wchar_p(_kag_mnemonic_label("音量(V)", "&")))

            # 5. Display
            m_disp = user32.CreatePopupMenu()
            d_first = add_item(m_disp, "ウィンドウ", "disp:window")
            d_last = add_item(m_disp, "フルスクリーン", "disp:fullscreen")
            self.win_radio_groups["disp"] = (m_disp, d_first, d_last)
            user32.AppendMenuW(menubar, MF_POPUP, m_disp, ctypes.c_wchar_p(_kag_mnemonic_label("表示(D)", "&")))

            # 6. Language
            m_lang = user32.CreatePopupMenu()
            l_ids = []
            for lbl, act in [("日本語 (Original)", "lang:ja"), ("简体中文 (Simplified Chinese)", "lang:zh_cn")]:
                cid = next_id[0]
                next_id[0] += 1
                user32.AppendMenuW(m_lang, MF_STRING, cid, ctypes.c_wchar_p(lbl))
                self.win_cmd_map[cid] = act
                self.win_id_by_action[act] = (m_lang, cid)
                l_ids.append(cid)
            self.win_radio_groups["lang"] = (m_lang, l_ids[0], l_ids[-1])
            user32.AppendMenuW(menubar, MF_POPUP, m_lang, ctypes.c_wchar_p(_kag_mnemonic_label("言語(L)", "&")))

            # 7. Help
            m_hlp = user32.CreatePopupMenu()
            add_item(m_hlp, "このソフトについて(A)...", "about")
            user32.AppendMenuW(menubar, MF_POPUP, m_hlp, ctypes.c_wchar_p(_kag_mnemonic_label("ヘルプ(H)", "&")))

            old_menu = self.hmenu
            self.hmenu = menubar
            if not preferences.fullscreen:
                user32.SetMenu(self.hwnd, menubar)
                self._win_menu_attached = True
                user32.DrawMenuBar(self.hwnd)
            else:
                self._win_menu_attached = False
            user32.SetWindowTextW(self.hwnd, ctypes.c_wchar_p(_kag_window_title()))
            if old_menu:
                user32.DestroyMenu(old_menu)

        def _init_macos_cocoa(self):
            w = renpy.pygame.display.get_window()
            if w is None:
                return False
            objc = ctypes.CDLL("/usr/lib/libobjc.A.dylib")
            ctypes.CDLL("/System/Library/Frameworks/AppKit.framework/AppKit")

            objc.objc_getClass.argtypes = [ctypes.c_char_p]
            objc.objc_getClass.restype = ctypes.c_void_p
            objc.sel_registerName.argtypes = [ctypes.c_char_p]
            objc.sel_registerName.restype = ctypes.c_void_p
            objc.objc_allocateClassPair.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
            objc.objc_allocateClassPair.restype = ctypes.c_void_p
            objc.objc_registerClassPair.argtypes = [ctypes.c_void_p]
            objc.class_addMethod.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p]
            objc.class_addMethod.restype = ctypes.c_bool

            msg_id0 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(("objc_msgSend", objc))
            msg_id_cstr = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(("objc_msgSend", objc))
            msg_id_id = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(("objc_msgSend", objc))
            msg_v_id = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(("objc_msgSend", objc))
            msg_v_bool = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(("objc_msgSend", objc))
            msg_v_long = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ssize_t)(("objc_msgSend", objc))
            msg_long0 = ctypes.CFUNCTYPE(ctypes.c_ssize_t, ctypes.c_void_p, ctypes.c_void_p)(("objc_msgSend", objc))
            msg_init_item = ctypes.CFUNCTYPE(
                ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p
            )(("objc_msgSend", objc))

            self.objc = objc
            self._cocoa_fns = (msg_id0, msg_id_cstr, msg_id_id, msg_v_id, msg_v_bool, msg_v_long, msg_long0, msg_init_item)

            sel = objc.sel_registerName
            cls_NSObject = objc.objc_getClass(b"NSObject")
            cls_NSString = objc.objc_getClass(b"NSString")
            cls_NSApp = objc.objc_getClass(b"NSApplication")
            cls_NSMenu = objc.objc_getClass(b"NSMenu")
            cls_NSMenuItem = objc.objc_getClass(b"NSMenuItem")

            def nsstr(py_s):
                return msg_id_cstr(cls_NSString, sel(b"stringWithUTF8String:"), py_s.encode("utf-8"))

            self._nsstr = nsstr
            target_cls = objc.objc_getClass(b"KAGNativeMenuTarget")
            sel_action = sel(b"onKagMenuAction:")
            if not target_cls:
                target_cls = objc.objc_allocateClassPair(cls_NSObject, b"KAGNativeMenuTarget", 0)
                IMP_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

                def _on_cocoa_cmd(_self_ptr, _cmd_ptr, sender_ptr):
                    if not sender_ptr:
                        return
                    tag = int(msg_long0(sender_ptr, sel(b"tag")))
                    act = self.cocoa_tag_map.get(tag)
                    if act:
                        _kag_enqueue_native_action(act)

                c_imp = IMP_TYPE(_on_cocoa_cmd)
                self._callbacks.append(c_imp)
                objc.class_addMethod(target_cls, sel_action, ctypes.cast(c_imp, ctypes.c_void_p), b"v@:@")
                objc.objc_registerClassPair(target_cls)

            self.cocoa_target = msg_id0(msg_id0(target_cls, sel(b"alloc")), sel(b"init"))
            ns_app = msg_id0(cls_NSApp, sel(b"sharedApplication"))
            main_menu = msg_id0(ns_app, sel(b"mainMenu"))
            if not main_menu:
                main_menu = msg_id_id(msg_id0(cls_NSMenu, sel(b"alloc")), sel(b"initWithTitle:"), nsstr(""))
                msg_v_id(ns_app, sel(b"setMainMenu:"), main_menu)

            next_tag = [2001]
            empty_key = nsstr("")

            def make_menu(raw_title, key=None):
                m = msg_id_id(msg_id0(cls_NSMenu, sel(b"alloc")), sel(b"initWithTitle:"), nsstr(kag_tr(raw_title)))
                msg_v_bool(m, sel(b"setAutoenablesItems:"), False)
                top_it = msg_init_item(msg_id0(cls_NSMenuItem, sel(b"alloc")), sel(b"initWithTitle:action:keyEquivalent:"), nsstr(kag_tr(raw_title)), None, empty_key)
                msg_v_id(top_it, sel(b"setSubmenu:"), m)
                msg_v_id(main_menu, sel(b"addItem:"), top_it)
                if key:
                    self.cocoa_items[key] = (top_it, m, raw_title)
                return m

            def add_cocoa_item(menu_obj, key, raw_label, action_token=None, enabled=True, raw_override=None):
                disp = raw_override if raw_override is not None else kag_tr(raw_label)
                act_sel = sel_action if action_token else None
                it = msg_init_item(
                    msg_id0(cls_NSMenuItem, sel(b"alloc")),
                    sel(b"initWithTitle:action:keyEquivalent:"),
                    nsstr(disp), act_sel, empty_key
                )
                if action_token:
                    tval = next_tag[0]
                    next_tag[0] += 1
                    self.cocoa_tag_map[tval] = action_token
                    msg_v_long(it, sel(b"setTag:"), tval)
                    msg_v_id(it, sel(b"setTarget:"), self.cocoa_target)
                msg_v_bool(it, sel(b"setEnabled:"), bool(enabled))
                msg_v_id(menu_obj, sel(b"addItem:"), it)
                if key:
                    self.cocoa_items[key] = (it, None, raw_label)
                return it

            m_sys = make_menu("システム(S)", "top_sys")
            add_cocoa_item(m_sys, "sys_save", "栞をはさむ (セーブ)", "save")
            add_cocoa_item(m_sys, "sys_load", "栞をたどる (ロード)", "load")
            add_cocoa_item(m_sys, "sys_hist", "メッセージ履歴を見る", "history")
            add_cocoa_item(m_sys, "sys_hide", "メッセージを消す", "hide_msg")
            add_cocoa_item(m_sys, "sys_skip", "次に進むまでスキップ", "skip")
            msg_v_id(m_sys, sel(b"addItem:"), msg_id0(cls_NSMenuItem, sel(b"separatorItem")))
            add_cocoa_item(m_sys, "sys_shortcuts", "ショートカット設定(K)...", "shortcuts")
            msg_v_id(m_sys, sel(b"addItem:"), msg_id0(cls_NSMenuItem, sel(b"separatorItem")))
            add_cocoa_item(m_sys, "sys_title", "最初に戻る (タイトル)", "title")
            add_cocoa_item(m_sys, "sys_quit", "終了", "quit")

            m_txt = make_menu("文字表示(C)", "top_text")
            add_cocoa_item(m_txt, "txt_hdr_spd", "文字表示速度", None, enabled=False)
            add_cocoa_item(m_txt, "spd_fast", "速い (10ms)", "speed:fast")
            add_cocoa_item(m_txt, "spd_normal", "普通 (30ms)", "speed:normal")
            add_cocoa_item(m_txt, "spd_slow", "遅い (50ms)", "speed:slow")
            add_cocoa_item(m_txt, "spd_instant", "ノーウェイト", "speed:instant")
            msg_v_id(m_txt, sel(b"addItem:"), msg_id0(cls_NSMenuItem, sel(b"separatorItem")))
            add_cocoa_item(m_txt, "txt_hdr_fnt", "フォント選択", None, enabled=False)
            add_cocoa_item(m_txt, "fnt_mono", "等幅ゴシック (原作準拠)", "font:mono")
            add_cocoa_item(m_txt, "fnt_prop", "プロポーショナルゴシック", "font:prop")

            m_mov = make_menu("ムービー(M)", "top_movie")
            add_cocoa_item(m_mov, "mov_watch", "ムービーを見る", "movie_toggle")

            m_vol = make_menu("音量(V)", "top_vol")
            for mix_key, mix_raw in [("music", "ＢＧＭ(B)"), ("voice", "ボイス(V)"), ("sfx", "効果音(S)")]:
                sub_m = msg_id_id(msg_id0(cls_NSMenu, sel(b"alloc")), sel(b"initWithTitle:"), nsstr(kag_tr(mix_raw)))
                msg_v_bool(sub_m, sel(b"setAutoenablesItems:"), False)
                sub_it = add_cocoa_item(m_vol, "vol_top_" + mix_key, mix_raw, None, enabled=True)
                msg_v_id(sub_it, sel(b"setSubmenu:"), sub_m)
                self.cocoa_items["vol_top_" + mix_key] = (sub_it, sub_m, mix_raw)
                self.cocoa_vol_items[(mix_key, 0)] = add_cocoa_item(sub_m, "vol_%s_0" % mix_key, "ミュート (0%)", "vol:%s:0" % mix_key)
                for pct in (100, 80, 60, 40, 20, 5):
                    self.cocoa_vol_items[(mix_key, pct)] = add_cocoa_item(sub_m, None, None, "vol:%s:%d" % (mix_key, pct), raw_override="%d%%" % pct)

            m_disp = make_menu("表示(D)", "top_disp")
            add_cocoa_item(m_disp, "disp_win", "ウィンドウ", "disp:window")
            add_cocoa_item(m_disp, "disp_full", "フルスクリーン", "disp:fullscreen")

            m_lang = make_menu("言語(L)", "top_lang")
            add_cocoa_item(m_lang, "lang_ja", None, "lang:ja", raw_override="日本語 (Original)")
            add_cocoa_item(m_lang, "lang_zh", None, "lang:zh_cn", raw_override="简体中文 (Simplified Chinese)")

            m_hlp = make_menu("ヘルプ(H)", "top_help")
            add_cocoa_item(m_hlp, "hlp_about", "このソフトについて(A)...", "about")

            self.sync_state(force=True)
            return True

        def sync_state(self, force=False):
            if not self.active or self._cleaned_up:
                return
            cur_lang = persistent.kag_language or _preferences.language
            spd = persistent.kag_text_speed or "normal"
            fmode = persistent.kag_font_mode or "mono"
            mov_on = bool(persistent.movieSkip != 0)
            vol_m = kag_get_mixer_percent("music")
            vol_v = kag_get_mixer_percent("voice")
            vol_s = kag_get_mixer_percent("sfx")
            is_full = bool(self.is_fullscreen if self.backend == "gtk3" else preferences.fullscreen)
            in_title = bool(store.kag_in_title)
            rc_en = bool(store.kag_rclick_enabled)
            hist_en = bool(store.kag_history_enabled)
            skip_en = bool(store.kag_clickskip_enabled)

            sig = (cur_lang, spd, fmode, mov_on, vol_m, vol_v, vol_s, is_full, in_title, rc_en, hist_en, skip_en)
            if not force and sig == self._last_state_sig:
                return
            self._last_state_sig = sig

            if self.backend == "gtk3":
                self._updating_gtk_sync(
                    cur_lang, spd, fmode, mov_on, vol_m, vol_v, vol_s, is_full, in_title, rc_en, hist_en, skip_en
                )
            elif self.backend == "win32":
                self._updating_win32_sync(
                    cur_lang, spd, fmode, mov_on, vol_m, vol_v, vol_s, is_full, in_title, rc_en, hist_en, skip_en
                )
            elif self.backend == "cocoa":
                self._updating_cocoa_sync(
                    cur_lang, spd, fmode, mov_on, vol_m, vol_v, vol_s, is_full, in_title, rc_en, hist_en, skip_en
                )

        def _updating_gtk_sync(
            self, cur_lang, spd, fmode, mov_on, vol_m, vol_v, vol_s, is_full, in_title, rc_en, hist_en, skip_en
        ):
            gtk = self.gtk
            self._updating = True
            try:
                if cur_lang != self._last_lang:
                    self._last_lang = cur_lang
                    gtk.gtk_window_set_title(self.gtk_win, _kag_window_title().encode("utf-8"))
                    for key, (widget, raw_label) in self.gtk_items.items():
                        if raw_label:
                            gtk.gtk_menu_item_set_label(widget, _kag_mnemonic_label(raw_label, "_").encode("utf-8"))
                            gtk.gtk_menu_item_set_use_underline(widget, 1)

                gtk.gtk_widget_set_sensitive(self.gtk_items["sys_save"][0], 1 if (not in_title and rc_en) else 0)
                gtk.gtk_widget_set_sensitive(self.gtk_items["sys_hist"][0], 1 if (not in_title and hist_en) else 0)
                gtk.gtk_widget_set_sensitive(self.gtk_items["sys_hide"][0], 1 if (not in_title) else 0)
                gtk.gtk_widget_set_sensitive(self.gtk_items["sys_skip"][0], 1 if (not in_title and skip_en) else 0)
                gtk.gtk_widget_set_sensitive(self.gtk_items["sys_title"][0], 1 if (not in_title) else 0)

                for s_key, s_val in [("spd_fast", "fast"), ("spd_normal", "normal"), ("spd_slow", "slow"), ("spd_instant", "instant")]:
                    gtk.gtk_check_menu_item_set_active(self.gtk_items[s_key][0], 1 if spd == s_val else 0)
                gtk.gtk_check_menu_item_set_active(self.gtk_items["fnt_mono"][0], 1 if fmode == "mono" else 0)
                gtk.gtk_check_menu_item_set_active(self.gtk_items["fnt_prop"][0], 1 if fmode == "prop" else 0)
                gtk.gtk_check_menu_item_set_active(self.gtk_items["mov_watch"][0], 1 if mov_on else 0)

                for mix_key, cur_pct in [("music", vol_m), ("voice", vol_v), ("sfx", vol_s)]:
                    gtk.gtk_check_menu_item_set_active(self.gtk_vol_items[(mix_key, 0)], 1 if cur_pct == 0 else 0)
                    for step_pct in (100, 80, 60, 40, 20, 5):
                        active_step = (cur_pct > 0 and abs(cur_pct - step_pct) <= 3)
                        gtk.gtk_check_menu_item_set_active(self.gtk_vol_items[(mix_key, step_pct)], 1 if active_step else 0)

                gtk.gtk_check_menu_item_set_active(self.gtk_items["disp_win"][0], 0 if is_full else 1)
                gtk.gtk_check_menu_item_set_active(self.gtk_items["disp_full"][0], 1 if is_full else 0)
                gtk.gtk_check_menu_item_set_active(self.gtk_items["lang_ja"][0], 0 if cur_lang == "zh_cn" else 1)
                gtk.gtk_check_menu_item_set_active(self.gtk_items["lang_zh"][0], 1 if cur_lang == "zh_cn" else 0)
            finally:
                self._updating = False

        def _updating_win32_sync(
            self, cur_lang, spd, fmode, mov_on, vol_m, vol_v, vol_s, is_full, in_title, rc_en, hist_en, skip_en
        ):
            user32 = self.user32
            if cur_lang != self._last_lang:
                self._last_lang = cur_lang
                self._build_win32_menus()

            if is_full and self._win_menu_attached:
                user32.SetMenu(self.hwnd, None)
                self._win_menu_attached = False
            elif not is_full and not self._win_menu_attached and self.hmenu:
                user32.SetMenu(self.hwnd, self.hmenu)
                self._win_menu_attached = True
                self._adjust_win32_client_size(800, 600)

            MF_BYCOMMAND = 0x0000
            MF_ENABLED = 0x0000
            MF_GRAYED = 0x0001
            MF_CHECKED = 0x0008
            MF_UNCHECKED = 0x0000

            def set_en(act, en):
                info = self.win_id_by_action.get(act)
                if info:
                    user32.EnableMenuItem(info[0], info[1], MF_BYCOMMAND | (MF_ENABLED if en else MF_GRAYED))

            def set_chk(act, chk):
                info = self.win_id_by_action.get(act)
                if info:
                    user32.CheckMenuItem(info[0], info[1], MF_BYCOMMAND | (MF_CHECKED if chk else MF_UNCHECKED))

            def set_radio(grp_name, act):
                grp = self.win_radio_groups.get(grp_name)
                info = self.win_id_by_action.get(act)
                if grp and info:
                    user32.CheckMenuRadioItem(grp[0], grp[1], grp[2], info[1], MF_BYCOMMAND)

            set_en("save", not in_title and rc_en)
            set_en("history", not in_title and hist_en)
            set_en("hide_msg", not in_title)
            set_en("skip", not in_title and skip_en)
            set_en("title", not in_title)

            set_radio("speed", "speed:" + spd)
            set_radio("font", "font:" + ("prop" if fmode == "prop" else "mono"))
            set_chk("movie_toggle", mov_on)

            for mix_key, cur_pct in [("music", vol_m), ("voice", vol_v), ("sfx", vol_s)]:
                matched_act = None
                if cur_pct == 0:
                    matched_act = "vol:%s:0" % mix_key
                else:
                    for step_pct in (100, 80, 60, 40, 20, 5):
                        if abs(cur_pct - step_pct) <= 3:
                            matched_act = "vol:%s:%d" % (mix_key, step_pct)
                            break
                if matched_act:
                    set_radio("vol_" + mix_key, matched_act)
                else:
                    set_chk("vol:%s:0" % mix_key, False)
                    for step_pct in (100, 80, 60, 40, 20, 5):
                        set_chk("vol:%s:%d" % (mix_key, step_pct), False)

            set_radio("disp", "disp:fullscreen" if is_full else "disp:window")
            set_radio("lang", "lang:zh_cn" if cur_lang == "zh_cn" else "lang:ja")
            if self._win_menu_attached:
                user32.DrawMenuBar(self.hwnd)

        def _updating_cocoa_sync(
            self, cur_lang, spd, fmode, mov_on, vol_m, vol_v, vol_s, is_full, in_title, rc_en, hist_en, skip_en
        ):
            sel = self.objc.sel_registerName
            _, _, _, msg_v_id, msg_v_bool, msg_v_long, _, _ = self._cocoa_fns
            nsstr = self._nsstr

            if cur_lang != self._last_lang:
                self._last_lang = cur_lang
                for _k, (it_ptr, sub_ptr, raw_lbl) in self.cocoa_items.items():
                    if raw_lbl:
                        tr_s = nsstr(kag_tr(raw_lbl))
                        msg_v_id(it_ptr, sel(b"setTitle:"), tr_s)
                        if sub_ptr:
                            msg_v_id(sub_ptr, sel(b"setTitle:"), tr_s)

            def c_en(k, en):
                if k in self.cocoa_items:
                    msg_v_bool(self.cocoa_items[k][0], sel(b"setEnabled:"), bool(en))

            def c_st(k, on):
                if k in self.cocoa_items:
                    msg_v_long(self.cocoa_items[k][0], sel(b"setState:"), 1 if on else 0)

            c_en("sys_save", not in_title and rc_en)
            c_en("sys_hist", not in_title and hist_en)
            c_en("sys_hide", not in_title)
            c_en("sys_skip", not in_title and skip_en)
            c_en("sys_title", not in_title)

            for s_key, s_val in [("spd_fast", "fast"), ("spd_normal", "normal"), ("spd_slow", "slow"), ("spd_instant", "instant")]:
                c_st(s_key, spd == s_val)
            c_st("fnt_mono", fmode == "mono")
            c_st("fnt_prop", fmode == "prop")
            c_st("mov_watch", mov_on)

            for mix_key, cur_pct in [("music", vol_m), ("voice", vol_v), ("sfx", vol_s)]:
                msg_v_long(self.cocoa_vol_items[(mix_key, 0)], sel(b"setState:"), 1 if cur_pct == 0 else 0)
                for step_pct in (100, 80, 60, 40, 20, 5):
                    active_step = (cur_pct > 0 and abs(cur_pct - step_pct) <= 3)
                    msg_v_long(self.cocoa_vol_items[(mix_key, step_pct)], sel(b"setState:"), 1 if active_step else 0)

            c_st("disp_win", not is_full)
            c_st("disp_full", is_full)
            c_st("lang_ja", cur_lang != "zh_cn")
            c_st("lang_zh", cur_lang == "zh_cn")

        def pump_events(self):
            if self._cleaned_up or not self.ensure_initialized():
                return False
            self.sync_state(force=False)
            need_fast = False
            if self.backend == "gtk3":
                try:
                    while self.gtk.gtk_events_pending():
                        self.gtk.gtk_main_iteration_do(0)
                    if self._gtk_menu_open:
                        need_fast = True
                    elif self.gtk_xid and self.dpy:
                        rr = ctypes.c_ulong()
                        cr = ctypes.c_ulong()
                        rx = ctypes.c_int()
                        ry = ctypes.c_int()
                        wx = ctypes.c_int()
                        wy = ctypes.c_int()
                        mk = ctypes.c_uint()
                        if self.x11.XQueryPointer(
                            self.dpy, self.gtk_xid, ctypes.byref(rr), ctypes.byref(cr),
                            ctypes.byref(rx), ctypes.byref(ry), ctypes.byref(wx), ctypes.byref(wy),
                            ctypes.byref(mk)
                        ):
                            win_w = self.gtk.gtk_widget_get_allocated_width(self.gtk_win)
                            if 0 <= wx.value <= win_w and -8 <= wy.value <= 42:
                                need_fast = True
                            if self.is_fullscreen:
                                if wy.value <= 4 and not self._fs_autohide_shown:
                                    self._fs_autohide_shown = True
                                    self.gtk.gtk_widget_show(self.menubar)
                                elif wy.value > 44 and self._fs_autohide_shown and not self._gtk_menu_open:
                                    self._fs_autohide_shown = False
                                    self.gtk.gtk_widget_hide(self.menubar)
                except Exception:
                    pass
            _kag_drain_immediate_native_actions()
            return need_fast

        def periodic(self):
            self.pump_events()

    _kag_native_menubar = _KAGNativeMenuBar()

    def _kag_is_immediate_action(act):
        return act in _KAG_IMMEDIATE_MENU_EXACT or act.startswith(_KAG_IMMEDIATE_MENU_PREFIXES)

    def _kag_exec_single_native_action(act):
        if act == "save":
            if not store.kag_in_title and store.kag_rclick_enabled:
                kag_open_saveload_from_menubar("save")
        elif act == "load":
            kag_open_saveload_from_menubar("load")
        elif act == "history":
            kag_open_history()
        elif act == "hide_msg":
            if not store.kag_in_title:
                renpy.run(HideInterface())
        elif act == "skip":
            if not store.kag_in_title and store.kag_clickskip_enabled:
                kag_start_skip()
        elif act == "title":
            if not store.kag_in_title:
                kag_open_confirm(kag_tr("タイトルへ戻りますか？"), Function(kag_return_to_title))
        elif act == "quit":
            kag_open_confirm(kag_tr("終了しますか？"), Function(kag_quit_game))
        elif act.startswith("speed:"):
            kag_set_text_speed(act.split(":", 1)[1])
        elif act.startswith("font:"):
            kag_set_font_mode(act.split(":", 1)[1])
        elif act == "movie_toggle":
            persistent.movieSkip = 0 if persistent.movieSkip != 0 else 1
            renpy.restart_interaction()
        elif act.startswith("vol:"):
            _, mix_name, pct_str = act.split(":")
            kag_set_mixer_percent(mix_name, int(pct_str))
        elif act == "disp:window":
            _kag_native_menubar.set_display_mode("window")
        elif act == "disp:fullscreen":
            _kag_native_menubar.set_display_mode("fullscreen")
        elif act == "lang:ja":
            kag_set_language(None)
        elif act == "lang:zh_cn":
            kag_set_language("zh_cn")
        elif act == "about":
            kag_open_about_dialog()
        elif act == "shortcuts":
            kag_open_shortcuts_dialog()
        _kag_native_menubar.sync_state(force=True)

    def _kag_enqueue_native_action(act):
        _kag_native_menu_queue.append(act)
        _kag_native_menubar.sync_state(force=True)
        try:
            renpy.restart_interaction()
        except Exception:
            pass

    def _kag_drain_immediate_native_actions():
        if not _kag_native_menu_queue:
            return
        idx = 0
        while idx < len(_kag_native_menu_queue):
            act = _kag_native_menu_queue[idx]
            if _kag_is_immediate_action(act):
                _kag_native_menu_queue.pop(idx)
                try:
                    _kag_exec_single_native_action(act)
                except Exception as exc:
                    renpy.log("Native menu immediate action error (%r): %r" % (act, exc))
            else:
                idx += 1

    class _KAGNativeMenuPump(renpy.Displayable):
        def __init__(self, **kwargs):
            super(_KAGNativeMenuPump, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            fast = _kag_native_menubar.pump_events()
            if fast or _kag_native_menu_queue:
                renpy.redraw(self, 0.012)
            return renpy.Render(0, 0)

    _kag_native_menu_pump_disp = _KAGNativeMenuPump()

    def kag_periodic_native_menubar():
        was_active = bool(getattr(store, "_kag_native_menubar_active", False))
        _kag_native_menubar.ensure_initialized()
        _kag_native_menubar.periodic()
        if getattr(store, "_kag_native_menubar_active", False):
            if renpy.get_screen("kag_menubar"):
                renpy.hide_screen("kag_menubar")
            if not was_active:
                try:
                    renpy.restart_interaction()
                except Exception:
                    pass

    def _kag_cleanup_native_menubar():
        _kag_native_menubar.cleanup()

    if kag_periodic_native_menubar not in config.periodic_callbacks:
        config.periodic_callbacks.append(kag_periodic_native_menubar)
    if _kag_cleanup_native_menubar not in config.quit_callbacks:
        config.quit_callbacks.append(_kag_cleanup_native_menubar)

    def kag_dispatch_native_menu_action():
        if not _kag_native_menu_queue:
            return
        act = _kag_native_menu_queue.pop(0)
        _kag_exec_single_native_action(act)

default _kag_active_dropdown = None
default _kag_editing_comment_slot = None
default _kag_editing_comment_text = ""

transform kag_mesframe_fadein:
    alpha 0.0
    linear 0.65 alpha 1.0

transform kag_mesframe_instant:
    alpha 1.0

# Overlay keeping mesFrame & hold-box text seamless across {nw} -> [ws]/[wait] and extra.ks headers
screen kag_mesframe_overlay():
    zorder 50
    if not _windows_hidden and not kag_in_title:
        if kag_mesframe_visible:
            if kag_mesframe_fade:
                add "images/bg/mesFrame.png" xpos 0 ypos 0 at kag_mesframe_fadein
                timer 0.7 action SetVariable("kag_mesframe_fade", False)
            else:
                add "images/bg/mesFrame.png" xpos 0 ypos 0
        if not renpy.get_screen("say") and kag_hold_box_active and kag_hold_box_text:
            $ _hb_tr = (not kag_mesframe_visible or kag_hold_box_text == "ＭＯＶＩＥを見ますか？")
            $ _hb_txt = kag_tr(kag_hold_box_text) if _hb_tr else kag_hold_box_text
            $ _hb_font = kag_get_dialogue_font(_hb_txt)
            $ _hb_rect = kag_get_msg_inner_rect()
            fixed xpos _hb_rect[0] ypos _hb_rect[1] xsize _hb_rect[2] ysize _hb_rect[3]:
                text _hb_txt:
                    style "say_dialogue"
                    font _hb_font
                    rest_indent kag_hold_box_indent

# KAG3 Say Screen matching MessageLayer 0 + Layer 3 mesFrame
screen say(who, what):
    zorder 60
    on "show" action Function(kag_on_say_display, what)

    $ _say_tr = (not kag_mesframe_visible or what == "ＭＯＶＩＥを見ますか？")
    $ _say_txt = kag_tr(what) if _say_tr else what
    $ _say_font = kag_get_dialogue_font(_say_txt)
    $ _cur_indent = kag_measure_indent_from_what(_say_txt)
    $ _say_rect = kag_get_msg_inner_rect()
    fixed xpos _say_rect[0] ypos _say_rect[1] xsize _say_rect[2] ysize _say_rect[3]:
        if who is not None:
            text who id "who" xpos 0 ypos 0 style "say_label" font kag_get_dialogue_font(who)
        text _say_txt id "what":
            style "say_dialogue"
            font _say_font
            rest_indent _cur_indent

# Interactive Buttons & Located/Choices Links (menu.ks, option.ks, extra.ks, [choices])
screen kag_interactive_menu(buttons, links):
    zorder 70
    fixed xysize (800, 600):
        # 1. Positioned 3-state image buttons
        for b in buttons:
            $ _states = kag_resolve_button_states(b["graphic"])
            $ _btn_act = Return((b["graphic_stem"] if "graphic_stem" in b else b["storage"], b["target"], b["exp"], b["current_stem"])) if False else Return((b["storage"], b["target"], b["exp"], b["current_stem"]))
            if _states and len(_states) >= 3:
                imagebutton:
                    xpos b["x"]
                    ypos b["y"]
                    idle _states[0]
                    hover _states[2]
                    selected_idle _states[1]
                    action _btn_act
            elif _states:
                imagebutton:
                    xpos b["x"]
                    ypos b["y"]
                    idle _states[0]
                    hover _states[-1]
                    action _btn_act
            else:
                $ _img = kag_resolve_image(b["graphic"]) or "images/ui/thm_no.png"
                imagebutton:
                    xpos b["x"]
                    ypos b["y"]
                    idle _img
                    action _btn_act

        # 2. Located links (e.g., extra.ks memorial chapter lists & "戻る")
        for lnk in links:
            if lnk["x"] is not None or lnk["y"] is not None:
                $ _lx = lnk["x"] if lnk["x"] is not None else 20
                $ _ly = lnk["y"] if lnk["y"] is not None else 20
                $ _lc = lnk["color"] or "#ffffff"
                $ _ls = lnk["size"] or 24
                $ _ltxt = kag_tr(lnk["caption"])
                textbutton _ltxt:
                    xpos _lx
                    ypos _ly
                    background None
                    hover_background None
                    padding (0, 0)
                    text_font kag_get_dialogue_font(_ltxt)
                    text_size _ls
                    text_color _lc
                    text_hover_color "#ff0099"
                    text_outlines []
                    action Return((lnk["storage"], lnk["target"], lnk["exp"], lnk["current_stem"]))

        # 3. Standard unlocated [choices] links inside bottom message box / card
        $ _unloc = [lnk for lnk in links if lnk["x"] is None and lnk["y"] is None]
        if _unloc:
            if kag_in_choices and not kag_mesframe_visible:
                add "images/bg/mesFrame.png" xpos 0 ypos 0
            $ _shift_prompt = (kag_hold_box_active and bool(kag_hold_box_text) and kag_mesframe_visible)
            if len(_unloc) <= 3:
                $ _c_y = 508 if _shift_prompt else 480
                $ _c_h = 58 if _shift_prompt else 85
                $ _c_sp = 2 if (_shift_prompt or len(_unloc) == 3) else 6
                $ _c_bg = None
                $ _c_pad = (0, 0)
            else:
                $ _c_y = max(30, 565 - len(_unloc) * 32)
                $ _c_h = min(520, len(_unloc) * 32 + 16)
                $ _c_sp = 6
                $ _c_bg = "#1a0a18cc"
                $ _c_pad = (12, 8)
            frame:
                xpos 36
                ypos _c_y
                xsize 732
                ysize _c_h
                background _c_bg
                padding _c_pad
                vbox spacing _c_sp:
                    for lnk in _unloc:
                        $ _utxt = kag_tr(lnk["caption"])
                        textbutton _utxt:
                            xfill True
                            background None
                            hover_background None
                            padding (0, 0)
                            text_style "say_dialogue"
                            text_font kag_get_dialogue_font(_utxt)
                            text_size 23
                            text_color "#ffffff"
                            text_hover_color "#ff99cc"
                            action Return((lnk["storage"], lnk["target"], lnk["exp"], lnk["current_stem"]))

# Fixed Top Menu Bar Controller (Native OS controls on Linux/Windows; fixed top bar in headless/fallback)
screen kag_menubar_hotspot():
    zorder 999
    $ _kag_nm_ok = _kag_native_menubar.ensure_initialized()
    add _kag_native_menu_pump_disp
    if not kag_in_text_input():
        key "kag_sc_menubar" action Function(kag_trigger_shortcut_action, "menubar")
        key "kag_sc_save" action Function(kag_trigger_shortcut_action, "save")
        key "kag_sc_load" action Function(kag_trigger_shortcut_action, "load")
        key "kag_sc_history" action Function(kag_trigger_shortcut_action, "history")
        key "kag_sc_hide_msg" action Function(kag_trigger_shortcut_action, "hide_msg")
        key "kag_sc_toggle_skip" action Function(kag_trigger_shortcut_action, "toggle_skip")
        key "kag_sc_fullscreen" action Function(kag_trigger_shortcut_action, "fullscreen")
        key "kag_sc_screenshot" action Function(kag_trigger_shortcut_action, "screenshot")
        key "kag_sc_shortcuts" action Function(kag_trigger_shortcut_action, "shortcuts")
        key "kag_sc_title" action Function(kag_trigger_shortcut_action, "title")
        key "kag_sc_quit" action Function(kag_trigger_shortcut_action, "quit")
        if _kag_native_menubar.backend == "gtk3":
            key "alt_K_s" action Function(_kag_native_menubar.open_gtk_menu, "top_sys")
            key "alt_K_c" action Function(_kag_native_menubar.open_gtk_menu, "top_text")
            key "alt_K_m" action Function(_kag_native_menubar.open_gtk_menu, "top_movie")
            key "alt_K_v" action Function(_kag_native_menubar.open_gtk_menu, "top_vol")
            key "alt_K_d" action Function(_kag_native_menubar.open_gtk_menu, "top_disp")
            key "alt_K_l" action Function(_kag_native_menubar.open_gtk_menu, "top_lang")
            key "alt_K_h" action Function(_kag_native_menubar.open_gtk_menu, "top_help")
        key "rollback" action If(kag_history_enabled and not kag_in_title and not kag_in_overlay_menu(), true=Function(kag_open_history), false=NullAction())
    timer 0.02 repeat True action If(_kag_native_menu_queue, true=Function(kag_dispatch_native_menu_action), false=NullAction())
    if not kag_is_android_ui() and not _kag_nm_ok and not _kag_native_menubar_active and not renpy.get_screen("kag_menubar"):
        use kag_menubar

screen kag_menubar():
    zorder 130
    key "K_ESCAPE" action Function(kag_close_menubar_dropdown)

    frame:
        xpos 0
        ypos 0
        xsize 800
        ysize 26
        background "#f4f0f5ee"
        padding (4, 2)
        hbox spacing 6:
            textbutton kag_tr("システム(S)"):
                background ("#ff0099" if _kag_active_dropdown == "sys" else "#00000000")
                hover_background "#ffcce6"
                padding (8, 2)
                text_size 14
                text_color ("#ffffff" if _kag_active_dropdown == "sys" else "#111111")
                action Function(kag_toggle_menubar_dropdown, "sys")
            textbutton kag_tr("文字表示(C)"):
                background ("#ff0099" if _kag_active_dropdown == "text" else "#00000000")
                hover_background "#ffcce6"
                padding (8, 2)
                text_size 14
                text_color ("#ffffff" if _kag_active_dropdown == "text" else "#111111")
                action Function(kag_toggle_menubar_dropdown, "text")
            textbutton kag_tr("ムービー(M)"):
                background ("#ff0099" if _kag_active_dropdown == "movie" else "#00000000")
                hover_background "#ffcce6"
                padding (8, 2)
                text_size 14
                text_color ("#ffffff" if _kag_active_dropdown == "movie" else "#111111")
                action Function(kag_toggle_menubar_dropdown, "movie")
            textbutton kag_tr("音量(V)"):
                background ("#ff0099" if _kag_active_dropdown == "vol" else "#00000000")
                hover_background "#ffcce6"
                padding (8, 2)
                text_size 14
                text_color ("#ffffff" if _kag_active_dropdown == "vol" else "#111111")
                action Function(kag_toggle_menubar_dropdown, "vol")
            textbutton kag_tr("表示(D)"):
                background ("#ff0099" if _kag_active_dropdown == "disp" else "#00000000")
                hover_background "#ffcce6"
                padding (8, 2)
                text_size 14
                text_color ("#ffffff" if _kag_active_dropdown == "disp" else "#111111")
                action Function(kag_toggle_menubar_dropdown, "disp")
            textbutton kag_tr("言語(L)"):
                background ("#ff0099" if _kag_active_dropdown == "lang" else "#00000000")
                hover_background "#ffcce6"
                padding (8, 2)
                text_size 14
                text_color ("#ffffff" if _kag_active_dropdown == "lang" else "#111111")
                action Function(kag_toggle_menubar_dropdown, "lang")
            textbutton kag_tr("ヘルプ(H)"):
                background ("#ff0099" if _kag_active_dropdown == "help" else "#00000000")
                hover_background "#ffcce6"
                padding (8, 2)
                text_size 14
                text_color ("#ffffff" if _kag_active_dropdown == "help" else "#111111")
                action Function(kag_toggle_menubar_dropdown, "help")

    # Dropdown Panels
    if _kag_active_dropdown is not None:
        button:
            xpos 0
            ypos 26
            xsize 800
            ysize 574
            background "#00000018"
            action Function(kag_close_menubar_dropdown)

    if _kag_active_dropdown == "sys":
        frame xpos 4 ypos 26 background "#faf6fbee" padding (6, 6):
            vbox spacing 2:
                textbutton kag_tr("栞をはさむ (セーブ)") style "kag_menu_item" sensitive (not kag_in_title and kag_rclick_enabled) action Function(kag_open_saveload_from_menubar, "save")
                textbutton kag_tr("栞をたどる (ロード)") style "kag_menu_item" action Function(kag_open_saveload_from_menubar, "load")
                textbutton kag_tr("メッセージ履歴を見る") style "kag_menu_item" sensitive (kag_history_enabled and not kag_in_title) action Function(kag_open_history)
                textbutton kag_tr("メッセージを消す") style "kag_menu_item" sensitive (not kag_in_title) action [Function(kag_close_menubar_dropdown), HideInterface()]
                textbutton kag_tr("次に進むまでスキップ") style "kag_menu_item" sensitive (not kag_in_title and kag_clickskip_enabled) action [Function(kag_close_menubar_dropdown), Function(kag_start_skip)]
                null height 4
                textbutton kag_tr("ショートカット設定(K)...") style "kag_menu_item" action Function(kag_open_shortcuts_dialog)
                null height 4
                textbutton kag_tr("最初に戻る (タイトル)") style "kag_menu_item" sensitive (not kag_in_title) action Function(kag_open_confirm, kag_tr("タイトルへ戻りますか？"), Function(kag_return_to_title))
                textbutton kag_tr("終了") style "kag_menu_item" action Function(kag_open_confirm, kag_tr("終了しますか？"), Function(kag_quit_game))

    elif _kag_active_dropdown == "text":
        frame xpos 92 ypos 26 background "#faf6fbee" padding (6, 6):
            vbox spacing 2:
                text kag_tr("文字表示速度") size 12 color "#666666"
                textbutton (("✓ " if persistent.kag_text_speed == "fast" else "   ") + kag_tr("速い (10ms)")) style "kag_menu_item" action Function(kag_set_text_speed, "fast")
                textbutton (("✓ " if persistent.kag_text_speed == "normal" else "   ") + kag_tr("普通 (30ms)")) style "kag_menu_item" action Function(kag_set_text_speed, "normal")
                textbutton (("✓ " if persistent.kag_text_speed == "slow" else "   ") + kag_tr("遅い (50ms)")) style "kag_menu_item" action Function(kag_set_text_speed, "slow")
                textbutton (("✓ " if persistent.kag_text_speed == "instant" else "   ") + kag_tr("ノーウェイト")) style "kag_menu_item" action Function(kag_set_text_speed, "instant")
                null height 4
                text kag_tr("フォント選択") size 12 color "#666666"
                textbutton (("✓ " if persistent.kag_font_mode == "mono" else "   ") + kag_tr("等幅ゴシック (原作準拠)")) style "kag_menu_item" action Function(kag_set_font_mode, "mono")
                textbutton (("✓ " if persistent.kag_font_mode == "prop" else "   ") + kag_tr("プロポーショナルゴシック")) style "kag_menu_item" action Function(kag_set_font_mode, "prop")

    elif _kag_active_dropdown == "movie":
        frame xpos 182 ypos 26 background "#faf6fbee" padding (6, 6):
            vbox spacing 2:
                textbutton (("✓ " if persistent.movieSkip != 0 else "   ") + kag_tr("ムービーを見る")) style "kag_menu_item" action SetField(persistent, "movieSkip", 0 if persistent.movieSkip != 0 else 1)

    elif _kag_active_dropdown == "vol":
        frame xpos 272 ypos 26 background "#faf6fbee" padding (8, 8):
            hbox spacing 12:
                for _m_label, _m_name in [(kag_tr("ＢＧＭ(B)"), "music"), (kag_tr("ボイス(V)"), "voice"), (kag_tr("効果音(S)"), "sfx")]:
                    $ _cur_pct = kag_get_mixer_percent(_m_name)
                    vbox spacing 2:
                        text _m_label size 13 bold True color "#cc0066"
                        textbutton (("✓ " if _cur_pct == 0 else "   ") + kag_tr("ミュート (0%)")) style "kag_menu_item" action Function(kag_set_mixer_percent, _m_name, 0)
                        for _step_pct in (100, 80, 60, 40, 20, 5):
                            textbutton (("✓ " if abs(_cur_pct - _step_pct) <= 3 else "   ") + "{}%".format(_step_pct)) style "kag_menu_item" action Function(kag_set_mixer_percent, _m_name, _step_pct)

    elif _kag_active_dropdown == "disp":
        frame xpos 332 ypos 26 background "#faf6fbee" padding (6, 6):
            vbox spacing 2:
                textbutton (("✓ " if not preferences.fullscreen else "   ") + kag_tr("ウィンドウ")) style "kag_menu_item" action Preference("display", "window")
                textbutton (("✓ " if preferences.fullscreen else "   ") + kag_tr("フルスクリーン")) style "kag_menu_item" action Preference("display", "fullscreen")

    elif _kag_active_dropdown == "lang":
        $ _kag_cur_lang = persistent.kag_language or _preferences.language
        frame xpos 402 ypos 26 background "#faf6fbee" padding (6, 6):
            vbox spacing 2:
                textbutton (("✓ " if _kag_cur_lang != "zh_cn" else "   ") + "日本語 (Original)") style "kag_menu_item" text_font kag_get_jp_font() action Function(kag_set_language, None)
                textbutton (("✓ " if _kag_cur_lang == "zh_cn" else "   ") + "简体中文 (Simplified Chinese)") style "kag_menu_item" text_font kag_get_sc_font() action Function(kag_set_language, "zh_cn")

    elif _kag_active_dropdown == "help":
        frame xpos 472 ypos 26 background "#faf6fbee" padding (6, 6):
            vbox spacing 2:
                textbutton kag_tr("このソフトについて(A)...") style "kag_menu_item" action Function(kag_open_about_dialog)

style kag_menu_item is button:
    background "#00000000"
    hover_background "#ff0099"
    padding (8, 3)

style kag_menu_item_text is text:
    font kag_get_active_font()
    size 13
    color "#111111"
    hover_color "#ffffff"
    insensitive_color "#999999"

# Right-Click Menu matching plug_rclick_tjs.ks exact button positions & 4-state slices
screen kag_rclick_menu():
    modal True
    zorder 100
    on "hide" action Function(kag_on_overlay_screen_hide, "kag_rclick_menu")
    key "game_menu" action Return("close")
    key "mouseup_3" action Return("close")

    add "images/ui/rclick_bg.png" xpos 0 ypos 0

    $ _rbtns = [
        ("btn_rclick_save", 325, 100, Return("save")),
        ("btn_rclick_load", 325, 160, Return("load")),
        ("btn_rclick_msgclr", 325, 220, Return("msgclr")),
        ("btn_rclick_msgskip", 325, 280, Return("msgskip")),
        ("btn_rclick_backtitle", 325, 340, Return("backtitle")),
        ("btn_rclick_gamestop", 325, 400, Return("quit")),
        ("btn_rclick_cancel", 325, 480, Return("close")),
    ]
    for _name, _bx, _by, _act in _rbtns:
        $ _st = kag_resolve_button_states(_name)
        imagebutton:
            xpos _bx
            ypos _by
            idle _st[0]
            hover _st[2]
            selected_idle _st[1]
            action _act

# 30-Slot Save / Load Screen matching plug_rclick_tjs.ks coordinates & colors
screen kag_save_load(mode="save", from_load_ks=False, from_rclick=False):
    modal True
    zorder 105
    on "hide" action Function(kag_on_overlay_screen_hide, "kag_save_load")
    key "game_menu" action Return("back")
    key "mouseup_3" action Return("back")

    add "images/ui/rclick_bg.png" xpos 0 ypos 0

    if mode == "load":
        add "images/ui/slices/title_load_idle.png" xpos 20 ypos 30
    else:
        add "images/ui/slices/title_save_idle.png" xpos 20 ypos 30

    # 6 Page tabs (5 slots per page)
    for _pg in range(6):
        $ _pg_label = kag_tr("データ {start}～{end}").format(start=_pg * 5 + 1, end=(_pg + 1) * 5)
        $ _active_pg = (kag_saveload_page == _pg)
        textbutton _pg_label:
            xpos 10
            ypos (100 + _pg * 30)
            xsize 100
            ysize 25
            background ("#ff0099" if _active_pg else "#000000")
            hover_background ("#ff0099" if _active_pg else "#550033")
            text_size 13
            text_color "#ffffff"
            text_align (0.5, 0.5)
            action SetVariable("kag_saveload_page", _pg)

    # Return button
    $ _back_st = kag_resolve_button_states("btn_saveload_back")
    imagebutton:
        xpos 10
        ypos 550
        idle _back_st[0]
        hover _back_st[2]
        selected_idle _back_st[1]
        action Return("back")

    # 5 Save Data Items (starting at ypos 28 below fixed top menu bar)
    for _row in range(5):
        $ _slot_idx = kag_saveload_page * 5 + _row
        $ _sname = kag_slot_name(_slot_idx)
        $ _is_loadable = renpy.can_load(_sname)
        $ _locked = persistent.kag_locks[_slot_idx]
        $ _bm = kag_tr(persistent.kag_bookmarks[_slot_idx]) if (_is_loadable and persistent.kag_bookmarks[_slot_idx]) else (FileSaveName(_sname, slot=True) or kag_tr("データなし"))
        $ _dt = persistent.kag_dates[_slot_idx] if (_is_loadable and persistent.kag_dates[_slot_idx]) else "----/--/-- --:--"
        $ _cmt = persistent.kag_comments[_slot_idx] or ""

        button:
            xpos 136
            ypos (_row * 114 + 28)
            xsize 656
            ysize 108
            background "#ff0099a0"
            hover_background "#ff22aaa0"
            padding (0, 0)
            if mode == "save":
                action If(_locked, true=Notify(kag_tr("ロックされているため上書きできません。")), false=If(_is_loadable, true=Confirm(kag_tr("上書きセーブしますか？"), Function(kag_save_to_slot, _slot_idx)), false=Function(kag_save_to_slot, _slot_idx)))
            else:
                action If(_is_loadable, true=Function(kag_load_from_slot, _slot_idx), false=NullAction())

            fixed xysize (656, 108):
                text "{}".format(_slot_idx + 1) xpos 6 ypos 40 size 20 color "#000000"
                if _is_loadable:
                    add FileScreenshot(_sname, empty="images/ui/thm_no.png", slot=True) xpos 32 ypos 4 xysize (133, 100)
                else:
                    add "images/ui/thm_no.png" xpos 32 ypos 4 xysize (133, 100)

                text _bm xpos 180 ypos 12 size 14 color "#ffffff" font kag_get_dialogue_font(_bm)
                text (kag_tr("日付 : ") + _dt) xpos 180 ypos 32 size 14 color "#ffffff"

                # Lock checkbox at (350, 22)
                textbutton (("[[✓] " if _locked else "[[ ] ") + kag_tr("ロック")):
                    xpos 350
                    ypos 22
                    xsize 120
                    ysize 30
                    background "#ffffff40"
                    hover_background "#ffffff80"
                    text_size 14
                    text_color "#ffffff"
                    action Function(kag_toggle_slot_lock, _slot_idx)

                text kag_tr("コメント :") xpos 180 ypos 59 size 14 color "#ffffff"
                textbutton _cmt:
                    xpos 180
                    ypos 78
                    xsize 460
                    ysize 22
                    background "#ffffff"
                    hover_background "#ffeef8"
                    padding (6, 2)
                    text_font kag_get_dialogue_font(_cmt)
                    text_size 13
                    text_color "#000000"
                    sensitive _is_loadable
                    action [SetVariable("_kag_editing_comment_slot", _slot_idx), SetVariable("_kag_editing_comment_text", _cmt), Show("kag_comment_editor")]

# Inline Comment Editor modal for Save Slots
screen kag_comment_editor():
    modal True
    zorder 140
    fixed xysize (800, 600):
        frame align (0.5, 0.5) xsize 500 padding (20, 16) background "#2d102aee":
            vbox spacing 12:
                text kag_tr("コメント編集 (データ {})").format((_kag_editing_comment_slot or 0) + 1) size 16 color "#ffffff"
                frame background "#ffffff" padding (6, 6) xfill True:
                    input value VariableInputValue("_kag_editing_comment_text") length 48 font kag_get_active_font() color "#000000" size 15
                hbox spacing 16 xalign 1.0:
                    textbutton kag_tr("キャンセル") action [SetVariable("_kag_editing_comment_slot", None), Hide("kag_comment_editor")]
                    textbutton kag_tr("決定") action [Function(kag_update_slot_comment, _kag_editing_comment_slot, _kag_editing_comment_text), SetVariable("_kag_editing_comment_slot", None), Hide("kag_comment_editor")]

# Scrollbar styles (explicit xsize/ysize prevents Side from collapsing viewport width to 0)
style vscrollbar:
    xsize 15
    base_bar Solid("#404040")
    thumb Solid("#888888")
    hover_thumb Solid("#ff0099")
    unscrollable "hide"

style scrollbar:
    ysize 15
    base_bar Solid("#404040")
    thumb Solid("#888888")
    hover_thumb Solid("#ff0099")
    unscrollable "hide"

# Scrollable 2,000-line Backlog matching ExHistoryLayer.ks
screen history():
    tag menu
    zorder 110
    on "hide" action Function(kag_on_overlay_screen_hide, "history")
    key "game_menu" action Return()
    key "mouseup_3" action Return()

    add Solid("#000000e0", xysize=(800, 600))

    # Top-right close button [×] placed below the 26px fixed top menu bar (larger tap target on Android)
    textbutton "×":
        xpos (744 if kag_is_android_ui() else 774)
        ypos (8 if kag_is_android_ui() else 28)
        xsize (48 if kag_is_android_ui() else 24)
        ysize (48 if kag_is_android_ui() else 24)
        background "#440033"
        hover_background "#ff0099"
        text_size (24 if kag_is_android_ui() else 16)
        text_color "#ffffff"
        text_align (0.5, 0.5)
        action Return()

    viewport id "history_vp":
        xpos 20
        ypos 54
        xsize 764
        ysize 530
        side_spacing 8
        scrollbars "vertical"
        mousewheel True
        draggable True
        yinitial 1.0

        vbox:
            xfill True
            spacing 6

            for h in _history_list:
                $ _h_line = kag_format_history_line(h)
                text _h_line:
                    font kag_get_dialogue_font(_h_line)
                    size 20
                    line_spacing 6
                    color "#ffffff"
                    drop_shadow (1, 1)
                    drop_shadow_color "#000000"
                    substitute False

# Spell Input Modal matching part_A.ks [input name=f.spell]
screen kag_input_dialog(prompt="", title="", default_val=""):
    modal True
    zorder 115
    default spell_buf = default_val or ""

    fixed xysize (800, 600):
        add Solid("#000000aa", xysize=(800, 600))
        frame align (0.5, 0.5) xsize 520 padding (24, 20) background "#fff5faee":
            vbox spacing 12:
                text (kag_tr(title) if title else kag_tr("文字入力")) size 18 bold True color "#cc0066"
                text (kag_tr(prompt) if prompt else kag_tr("※20文字以内で入力してください。")) size 14 color "#222222"
                frame background "#ffffff" padding (8, 6) xfill True:
                    input value ScreenVariableInputValue("spell_buf") length 24 font kag_get_active_font() color "#000000" size 18
                hbox spacing 16 xalign 1.0:
                    textbutton kag_tr("決定"):
                        background "#ff0099"
                        hover_background "#ff33aa"
                        padding (18, 6)
                        text_color "#ffffff"
                        text_size 16
                        action Return(spell_buf)

# About Modal matching others/about.ks
screen kag_about_dialog():
    modal True
    zorder 140
    on "hide" action Function(kag_on_overlay_screen_hide, "kag_about_dialog")
    key "K_ESCAPE" action Hide("kag_about_dialog")
    fixed xysize (800, 600):
        add Solid("#00000088", xysize=(800, 600))
        frame align (0.5, 0.5) xsize 460 padding (24, 20) background "#fff5faf5":
            vbox spacing 12 xfill True:
                text kag_tr("このソフトについて") size 20 bold True color "#cc0066"
                text kag_tr("おジャ魔女あどべんちゃ～「ないしょのまほう」") size 16 bold True color "#222222"
                text (kag_tr("Ren'Py 移植版") + "  Ver " + config.version) size 14 color "#555555"
                textbutton kag_tr("閉じる"):
                    xalign 1.0
                    background "#ff0099"
                    hover_background "#ff33aa"
                    padding (16, 6)
                    text_color "#ffffff"
                    action Hide("kag_about_dialog")

init python:
    class _KAGKeyCaptureDisplayable(renpy.Displayable):
        def __init__(self, **kwargs):
            super(_KAGKeyCaptureDisplayable, self).__init__(**kwargs)
            self._pending_mod_key = None
            self._rev_keys = None

        def _get_rev_keys(self):
            if self._rev_keys is not None:
                return self._rev_keys
            rev = {}
            consts = renpy.pygame.constants
            for name in dir(consts):
                if not name.startswith("K_") or name.startswith("K_AC_"):
                    continue
                val = getattr(consts, name, None)
                if isinstance(val, int):
                    if val not in rev or len(name) < len(rev[val]):
                        rev[val] = name
            self._rev_keys = rev
            return rev

        def render(self, width, height, st, at):
            return renpy.Render(0, 0)

        def event(self, ev, x, y, st):
            target_id = getattr(store, "_kag_capturing_shortcut", None)
            if not target_id:
                self._pending_mod_key = None
                return None
            pg = renpy.pygame
            if ev.type == pg.KEYDOWN:
                if getattr(ev, "repeat", False):
                    raise renpy.IgnoreEvent()
                rev = self._get_rev_keys()
                kname = rev.get(ev.key)
                if not kname:
                    raise renpy.IgnoreEvent()
                if kname in ("K_NUMLOCK", "K_CAPSLOCK", "K_SCROLLOCK", "K_SCROLLLOCK", "K_MODE"):
                    raise renpy.IgnoreEvent()
                mods = ev.mod
                no_mods = not (mods & (pg.KMOD_CTRL | pg.KMOD_ALT | pg.KMOD_SHIFT | pg.KMOD_META))
                if kname == "K_ESCAPE" and no_mods:
                    self._pending_mod_key = None
                    store._kag_capturing_shortcut = None
                    renpy.restart_interaction()
                    raise renpy.IgnoreEvent()
                if kname in _KAG_MODIFIER_KEYSYMS:
                    self._pending_mod_key = kname
                    raise renpy.IgnoreEvent()
                self._pending_mod_key = None
                prefixes = []
                if mods & pg.KMOD_CTRL:
                    prefixes.append("ctrl")
                if mods & pg.KMOD_ALT:
                    prefixes.append("alt")
                if mods & pg.KMOD_SHIFT:
                    prefixes.append("shift")
                if (mods & pg.KMOD_META) and not (mods & pg.KMOD_ALT):
                    prefixes.append("meta")
                key_str = "_".join(prefixes + [kname]) if prefixes else kname
                store._kag_capturing_shortcut = None
                kag_set_shortcut(target_id, key_str)
                raise renpy.IgnoreEvent()
            elif ev.type == pg.KEYUP:
                if self._pending_mod_key:
                    rev = self._get_rev_keys()
                    kname = rev.get(ev.key)
                    if kname == self._pending_mod_key:
                        self._pending_mod_key = None
                        store._kag_capturing_shortcut = None
                        kag_set_shortcut(target_id, kname)
                        raise renpy.IgnoreEvent()
                raise renpy.IgnoreEvent()
            return None

    _kag_key_capture_disp = _KAGKeyCaptureDisplayable()

screen kag_shortcuts_dialog():
    modal True
    zorder 145
    on "hide" action [SetVariable("_kag_capturing_shortcut", None), Function(kag_on_overlay_screen_hide, "kag_shortcuts_dialog")]
    key "K_ESCAPE" action If(_kag_capturing_shortcut, true=SetVariable("_kag_capturing_shortcut", None), false=[SetVariable("_kag_capturing_shortcut", None), Hide("kag_shortcuts_dialog")])
    fixed xysize (800, 600):
        add Solid("#00000088", xysize=(800, 600))
        frame align (0.5, 0.5) xsize 660 ysize 510 padding (20, 16) background "#fff5faf8":
            vbox spacing 10:
                text kag_tr("ショートカット設定") size 20 bold True color "#cc0066"
                if _kag_capturing_shortcut:
                    text kag_tr("新しいキーを押してください... (Escでキャンセル)") size 14 bold True color "#cc0066"
                else:
                    text kag_tr("各機能のショートカットキーを変更・解除できます。") size 13 color "#555555"

                $ _cur_shortcuts = kag_get_shortcuts()
                viewport xsize 620 ysize 360 scrollbars "vertical" mousewheel True draggable True:
                    vbox spacing 4:
                        for _row_i, (_sc_id, _sc_label, _sc_default) in enumerate(KAG_SHORTCUT_SPEC):
                            $ _cur_key = _cur_shortcuts.get(_sc_id)
                            $ _is_cap = (_kag_capturing_shortcut == _sc_id)
                            frame xsize 596 ysize 34 padding (10, 4) background ("#ffe0f0" if _is_cap else ("#ffffffdd" if _row_i % 2 == 0 else "#fff0f7dd")):
                                text kag_tr(_sc_label) xalign 0.0 yalign 0.5 size 14 color "#222222"
                                hbox xalign 1.0 yalign 0.5 spacing 6:
                                    frame xsize 128 ysize 26 padding (6, 2) background ("#ff009922" if _is_cap else "#f3e8f0"):
                                        text (kag_tr("入力待ち...") if _is_cap else kag_format_shortcut_key(_cur_key)) align (0.5, 0.5) size 13 bold True color ("#cc0066" if _is_cap else ("#222222" if _cur_key else "#888888"))
                                    textbutton (kag_tr("中止") if _is_cap else kag_tr("変更")):
                                        xsize 68
                                        ysize 26
                                        padding (4, 2)
                                        background ("#aa4477" if _is_cap else "#ff0099")
                                        hover_background ("#cc5599" if _is_cap else "#ff33aa")
                                        text_size 13
                                        text_color "#ffffff"
                                        text_align (0.5, 0.5)
                                        action SetVariable("_kag_capturing_shortcut", None if _is_cap else _sc_id)
                                    textbutton kag_tr("解除"):
                                        xsize 68
                                        ysize 26
                                        padding (4, 2)
                                        background "#777777"
                                        hover_background "#555555"
                                        insensitive_background "#cccccc"
                                        text_size 13
                                        text_color "#ffffff"
                                        text_align (0.5, 0.5)
                                        sensitive (_cur_key is not None)
                                        action [SetVariable("_kag_capturing_shortcut", None), Function(kag_clear_shortcut, _sc_id)]

                hbox xfill True:
                    textbutton kag_tr("初期設定に戻す"):
                        xalign 0.0
                        background "#888888"
                        hover_background "#666666"
                        padding (14, 6)
                        text_size 14
                        text_color "#ffffff"
                        action Function(kag_reset_shortcuts)
                    textbutton kag_tr("閉じる"):
                        xalign 1.0
                        background "#ff0099"
                        hover_background "#ff33aa"
                        padding (18, 6)
                        text_size 14
                        text_color "#ffffff"
                        action [SetVariable("_kag_capturing_shortcut", None), Hide("kag_shortcuts_dialog")]
        add _kag_key_capture_disp

# Standard Confirm & Notify screens styled cleanly at 800x600
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    on "hide" action Function(kag_on_overlay_screen_hide, "confirm")
    fixed xysize (800, 600):
        add Solid("#00000088", xysize=(800, 600))
        frame align (0.5, 0.5) xsize 440 padding (24, 20) background "#fff5faf8":
            vbox spacing 16 xalign 0.5:
                text _(message) text_align 0.5 size 16 color "#222222" xalign 0.5
                hbox spacing 24 xalign 0.5:
                    textbutton kag_tr("はい") background "#ff0099" hover_background "#ff33aa" padding (20, 6) text_color "#ffffff" action yes_action
                    textbutton kag_tr("いいえ") background "#888888" hover_background "#666666" padding (20, 6) text_color "#ffffff" action no_action

screen notify(message):
    zorder 250
    frame xpos 20 ypos (12 if kag_is_android_ui() else 32) padding (12, 6) background "#ff0099dd":
        text message size (16 if kag_is_android_ui() else 14) color "#ffffff"
    timer 2.5 action Hide("notify")
