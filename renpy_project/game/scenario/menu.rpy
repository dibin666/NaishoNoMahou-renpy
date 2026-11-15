# Auto-generated from 08. other/menu.ks by tools/transpile_ks.py
label kag_menu:

label kag_menu_gamestart:
    if kag_in_boot_splash:
        $ kag_in_boot_splash = False
        return
    $ kag_history_opt(output=False, enabled=False)
    $ kag_wait(200, canskip=True)
    $ kag_set_rclick(False)
    $ kag_cm()
    $ kag_changetype('left', 'maintitle', time_ms=500, bgcolor='0x000000')
    $ kag_fadeinbgm('bgm-v01', 100)
    $ kag_playse('タイトルコール.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_playse('タイトルコール2.ogg', buf=0, loop=False)
    if persistent.firstclear!=0:
        if persistent.clearChar==1:
            $ kag_stopse(buf=0)
            $ kag_playse('タイトルコール2-01.ogg', buf=0, loop=False)
        if persistent.clearChar==2:
            $ kag_stopse(buf=0)
            $ kag_playse('タイトルコール2-02.ogg', buf=0, loop=False)
        if persistent.clearChar==3:
            $ kag_stopse(buf=0)
            $ kag_playse('タイトルコール2-03.ogg', buf=0, loop=False)
        if persistent.clearChar==4:
            $ kag_stopse(buf=0)
            $ kag_playse('タイトルコール2-04.ogg', buf=0, loop=False)
        if persistent.clearChar==5:
            $ kag_stopse(buf=0)
            $ kag_playse('タイトルコール2-05.ogg', buf=0, loop=False)
        if persistent.clearChar==6:
            $ kag_stopse(buf=0)
            $ kag_playse('タイトルコール2-06.ogg', buf=0, loop=False)
        if persistent.NormalCnt==6 or persistent.TrueCnt>=3:
            $ kag_stopse(buf=0)
            $ kag_playse('タイトルコール2-08.ogg', buf=0, loop=False)
        if persistent.TrueCnt==6:
            $ kag_stopse(buf=0)
            $ kag_playse('タイトルコール2-07.ogg', buf=0, loop=False)
        if persistent.TrueCnt==6 and persistent.NormalCnt==6:
            $ kag_stopse(buf=0)
            $ kag_playse('タイトルコール2-09.ogg', buf=0, loop=False)
        $ kag_ws(buf=0, canskip=True)

label kag_menu_titlemenu:
    $ kag_startanchor()

label kag_menu_mainmenu:
    $ kag_history_opt(output=False, enabled=None)
    if kag_bgm_status()=='stop':
        $ kag_fadeinbgm('bgm-v01', 100)
    $ kag_f.re_scenario=0
    $ kag_cm()
    $ kag_add_button('main_btn_newgame', current_stem='menu', storage=None, target='*newgame', exp=None, x=478, y=390)
    $ kag_add_button('main_btn_gameload', current_stem='menu', storage=None, target='*loadgame', exp=None, x=478, y=418)
    $ kag_add_button('main_btn_option', current_stem='menu', storage=None, target='*omake', exp=None, x=478, y=446)
    $ kag_add_button('main_btn_end', current_stem='menu', storage=None, target=None, exp='kag_quit_game()', x=478, y=474)
    call kag_s_wait

label kag_menu_newgame:
    $ kag_fadeoutbgm(300)
    $ kag_set_clickskip(True)
    jump kag_prologue_gamestart
    call kag_s_wait

label kag_menu_loadgame:
    $ kag_ct()
    jump kag_load_gamestart
    call kag_s_wait

label kag_menu_settei:
    $ kag_fadeoutbgm(300)
    $ kag_ct()
    jump kag_option_gamestart
    call kag_s_wait

label kag_menu_omake:
    $ kag_fadeoutbgm(300)
    $ kag_ct()
    jump kag_extra_gamestart
    call kag_s_wait
    call kag_s_wait
    return
