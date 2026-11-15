# Auto-generated from 08. other/load.ks by tools/transpile_ks.py
label kag_load:

label kag_load_gamestart:
    $ kag_cm()
    $ kag_f.loadmode=1
    call kag_open_rclick_menu
    $ kag_f.loadmode=0
    jump kag_load_back
    call kag_s_wait

label kag_load_back:
    jump kag_menu_mainmenu
    call kag_s_wait
    return
