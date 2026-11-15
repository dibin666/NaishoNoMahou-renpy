# Minimal Ren'Py GUI config tuned to exact KiriKiri2 / KAG3 800x600 metrics

init offset = -2

init python:
    gui.init(800, 600)

# Fonts (Noto Sans Mono CJK JP default = MS Gothic fixed-pitch metrics)
define gui.text_font = "fonts/NotoSansMonoCJKjp-Regular.otf"
define gui.name_text_font = "fonts/NotoSansMonoCJKjp-Regular.otf"
define gui.interface_text_font = "fonts/NotoSansMonoCJKjp-Regular.otf"
define gui.button_text_font = "fonts/NotoSansMonoCJKjp-Regular.otf"
define gui.choice_button_text_font = "fonts/NotoSansMonoCJKjp-Regular.otf"
define gui.system_font = "fonts/NotoSansMonoCJKjp-Regular.otf"

# Typography matching Config.tjs (24px white with black shadow, lineSpacing=6)
define gui.text_size = 24
define gui.name_text_size = 24
define gui.interface_text_size = 18
define gui.label_text_size = 22
define gui.notify_text_size = 16
define gui.title_text_size = 32

define gui.accent_color = "#ff0099"
define gui.idle_color = "#ffffff"
define gui.idle_small_color = "#e0e0e0"
define gui.hover_color = "#ff88cc"
define gui.selected_color = "#ff0099"
define gui.insensitive_color = "#888888"
define gui.muted_color = "#aa5588"
define gui.hover_muted_color = "#ff66aa"
define gui.text_color = "#ffffff"
define gui.interface_text_color = "#ffffff"

define gui.textbox_height = 150
define gui.textbox_yalign = 1.0
define gui.dialogue_xpos = 20
define gui.dialogue_ypos = 15
define gui.dialogue_width = 768
define gui.dialogue_text_xalign = 0.0

define gui.history_length = 2000
define gui.history_height = 26
define gui.history_name_xpos = 0
define gui.history_name_ypos = 0
define gui.history_name_width = 0
define gui.history_text_xpos = 16
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0
