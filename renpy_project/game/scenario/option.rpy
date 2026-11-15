# Auto-generated from 08. other/option.ks by tools/transpile_ks.py
label kag_option:

label kag_option_gamestart:
    $ kag_wait(200, canskip=True)
    $ kag_cm()
    $ kag_history_opt(output=False, enabled=False)
    $ kag_changetype('left', 'bg004', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_option_choices:
    $ kag_set_bookmark('選択肢')
    $ kag_cm()
    "ＭＯＶＩＥを見ますか？"
    $ kag_add_link('はい', current_stem='option', storage=None, target='*yes', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('いいえ', current_stem='option', storage=None, target='*no', exp=None, x=None, y=None, color=None, size=None)
    call kag_s_wait

label kag_option_yes:
    $ kag_cm()
    $ kag_f.movie=1
    jump kag_option_back
    call kag_s_wait

label kag_option_no:
    $ kag_f.movie=0
    jump kag_option_back
    call kag_s_wait

label kag_option_back:
    $ kag_history_opt(output=True, enabled=None)
    $ kag_changetype('left', 'bg001', time_ms=500, bgcolor='0x000000')
    jump kag_menu_mainmenu
    call kag_s_wait
    return
