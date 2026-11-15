# Game options, channels, persistence metadata, and Linux/Windows build configuration

define config.name = _("おジャ魔女あどべんちゃ～「ないしょのまほう」")
define gui.show_name = False
define config.version = "1.0.0"
define gui.about = _p("""おジャ魔女あどべんちゃ～「ないしょのまほう」\nRen'Py 8 移植版 Ver 1.0.0""")

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.default_music_volume = 0.60
define config.default_sfx_volume = 1.0
define config.default_voice_volume = 1.0
define config.default_text_cps = 33
define config.default_afm_time = 10

define config.window_icon = "gui/window_icon.png"
# Store saves & persistent data inside the portable game directory (<game_root>/game/saves/)
define config.save_directory = None
define config.thumbnail_width = 133
define config.thumbnail_height = 100
define config.history_length = 2000
define config.allow_skipping = True
define config.skip_indicator = False
define config.has_autosave = True
define config.rollback_enabled = True
define config.hard_rollback_limit = 256

# Show KAG right-click menu on right-click / Escape when enabled
define config.game_menu_action = Function(kag_handle_game_menu_request)

init -10 python:
    # KAG3 has 1 BGM channel (music) + 3 SE buffers: buf 0 (voice), buf 1 (oneshot SE), buf 2 (looping SE)
    renpy.music.register_channel("se0", mixer="voice", loop=False, tight=True)
    renpy.music.register_channel("se1", mixer="sfx", loop=False, tight=True)
    renpy.music.register_channel("se2", mixer="sfx", loop=True, tight=True)

init python:
    build.name = "naisho_no_mahou"
    build.directory_name = "NaishoNoMahou-1.0.0"
    build.executable_name = "NaishoNoMahou"
    build.include_update = False
    build.include_i686 = False

    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")

    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("game/cache/**", None)

    # Keep GUI icons on disk (screens_kag.rpy reads gui/window_icon.png via os.path.isfile)
    # and keep video outside .rpa for direct streaming/seeking.
    build.classify("game/gui/**", "all")
    build.classify("game/video/**", "all")

    # Pack scripts, translations, images, audio, and fonts into .rpa archives
    # for fast archive extraction and clean directory layout on Windows and Linux.
    build.classify("game/tl/**/images/**", "images")
    build.classify("game/images/**", "images")
    build.classify("game/audio/**", "audio")
    build.classify("game/fonts/**", "fonts")
    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")
    build.classify("game/tl/**", "scripts")

    build.package("linux", "tar.bz2", "linux linux_arm renpy all", description="Linux x86_64")
    build.package("win", "zip", "windows renpy all", description="Windows x86_64")
    build.package("pc", "zip", "windows linux renpy all", description="Windows and Linux x86_64")
