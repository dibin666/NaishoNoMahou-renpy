# Auto-generated from 08. other/extra.ks by tools/transpile_ks.py
label kag_extra:

label kag_extra_gamestart:
    $ kag_wait(200, canskip=True)
    $ kag_set_rclick(False)
    $ kag_history_opt(output=False, enabled=False)
    $ kag_changetype('circle02', 'option', time_ms=500, bgcolor='0x000000')
    $ kag_playbgm('m60', loop=True)

label kag_extra_extramenu:
    $ kag_cm()
    $ kag_add_button('option_btn_album', current_stem='extra', storage=None, target='*gallery', exp=None, x=350, y=100)
    $ kag_add_button('option_btn_memorial', current_stem='extra', storage=None, target='*return_s', exp=None, x=20, y=330)
    $ kag_add_button('option_btn_back', current_stem='extra', storage=None, target='*back', exp=None, x=4, y=470)
    call kag_s_wait

label kag_extra_gallery:
    $ kag_stoptrans()
    $ kag_cm()
    $ kag_changetype('cross', 'album', time_ms=1000, bgcolor='0x000000')

label kag_extra_selectcg:
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_add_button('album_btn_01', current_stem='extra', storage=None, target='*page00', exp=None, x=579, y=105)
    $ kag_add_button('album_btn_02', current_stem='extra', storage=None, target='*page01', exp=None, x=579, y=155)
    $ kag_add_button('album_btn_03', current_stem='extra', storage=None, target='*page02', exp=None, x=579, y=205)
    $ kag_add_button('album_btn_04', current_stem='extra', storage=None, target='*page03', exp=None, x=579, y=255)
    $ kag_add_button('album_btn_05', current_stem='extra', storage=None, target='*page04', exp=None, x=579, y=305)
    $ kag_add_button('album_btn_06', current_stem='extra', storage=None, target='*page05', exp=None, x=579, y=355)
    $ kag_add_button('album_btn_07', current_stem='extra', storage=None, target='*page06', exp=None, x=579, y=405)
    $ kag_add_button('album_btn_back', current_stem='extra', storage=None, target='*backselect', exp=None, x=-11, y=472)
    call kag_s_wait

label kag_extra_page00:
    $ kag_wt(canskip=True)
    $ kag_er()
    jump kag_extra_button1
    call kag_s_wait

label kag_extra_page01:
    $ kag_wt(canskip=True)
    $ kag_er()
    jump kag_extra_button2
    call kag_s_wait

label kag_extra_page02:
    $ kag_wt(canskip=True)
    $ kag_er()
    jump kag_extra_button3
    call kag_s_wait

label kag_extra_page03:
    $ kag_wt(canskip=True)
    $ kag_er()
    jump kag_extra_button4
    call kag_s_wait

label kag_extra_page04:
    $ kag_wt(canskip=True)
    $ kag_er()
    jump kag_extra_button5
    call kag_s_wait

label kag_extra_page05:
    $ kag_wt(canskip=True)
    $ kag_er()
    jump kag_extra_button6
    call kag_s_wait

label kag_extra_page06:
    $ kag_wt(canskip=True)
    $ kag_er()
    jump kag_extra_button7
    call kag_s_wait

label kag_extra_bgchange:
    if kag_f.cgPage==0:
        jump kag_extra_button1
    if kag_f.cgPage==1:
        jump kag_extra_button2
    if kag_f.cgPage==2:
        jump kag_extra_button3
    if kag_f.cgPage==3:
        jump kag_extra_button4
    if kag_f.cgPage==4:
        jump kag_extra_button5
    if kag_f.cgPage==5:
        jump kag_extra_button6
    if kag_f.cgPage==6:
        jump kag_extra_button7
    call kag_s_wait

label kag_extra_button1:
    $ kag_stoptrans()
    $ kag_f.cgPage=0
    $ kag_add_button('album_btn_01', current_stem='extra', storage=None, target='*page00', exp=None, x=579, y=105)
    $ kag_add_button('album_btn_02', current_stem='extra', storage=None, target='*page01', exp=None, x=579, y=155)
    $ kag_add_button('album_btn_03', current_stem='extra', storage=None, target='*page02', exp=None, x=579, y=205)
    $ kag_add_button('album_btn_04', current_stem='extra', storage=None, target='*page03', exp=None, x=579, y=255)
    $ kag_add_button('album_btn_05', current_stem='extra', storage=None, target='*page04', exp=None, x=579, y=305)
    $ kag_add_button('album_btn_06', current_stem='extra', storage=None, target='*page05', exp=None, x=579, y=355)
    $ kag_add_button('album_btn_07', current_stem='extra', storage=None, target='*page06', exp=None, x=579, y=405)
    $ kag_add_button('album_btn_back', current_stem='extra', storage=None, target='*backselect', exp=None, x=-11, y=472)
    if persistent.cgd1==1:
        $ kag_add_button('cgd1', current_stem='extra', storage=None, target='*cgd0', exp=None, x=73, y=119)
    if persistent.cgd2==1:
        $ kag_add_button('cgd2', current_stem='extra', storage=None, target='*cgd1', exp=None, x=243, y=170)
    if persistent.cgd3==1:
        $ kag_add_button('cgd3', current_stem='extra', storage=None, target='*cgd2', exp=None, x=413, y=220)
    if persistent.cgd4==1:
        $ kag_add_button('cgd4', current_stem='extra', storage=None, target='*cgd3', exp=None, x=73, y=252)
    if persistent.cgd5==1:
        $ kag_add_button('cgd5', current_stem='extra', storage=None, target='*cgd4', exp=None, x=243, y=303)
    if persistent.cgd6==1:
        $ kag_add_button('cgd6', current_stem='extra', storage=None, target='*cgd5', exp=None, x=413, y=353)
    $ kag_backlay()
    $ kag_image('album_06', layer='base', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=450, method='', rule='trans01', vague=64)
    $ kag_stoptrans()
    call kag_s_wait

label kag_extra_cgd0:
    $ kag_changetype('cross', '01どれみ-01.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgd1:
    $ kag_changetype('cross', '01どれみ-03.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgd2:
    $ kag_changetype('cross', '01どれみ-05.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgd3:
    $ kag_changetype('cross', '01どれみ-06.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgd4:
    $ kag_changetype('cross', '01どれみ-08.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgd5:
    $ kag_changetype('cross', '01どれみ-09.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_button2:
    $ kag_stoptrans()
    $ kag_f.cgPage=1
    $ kag_add_button('album_btn_01', current_stem='extra', storage=None, target='*page00', exp=None, x=579, y=105)
    $ kag_add_button('album_btn_02', current_stem='extra', storage=None, target='*page01', exp=None, x=579, y=155)
    $ kag_add_button('album_btn_03', current_stem='extra', storage=None, target='*page02', exp=None, x=579, y=205)
    $ kag_add_button('album_btn_04', current_stem='extra', storage=None, target='*page03', exp=None, x=579, y=255)
    $ kag_add_button('album_btn_05', current_stem='extra', storage=None, target='*page04', exp=None, x=579, y=305)
    $ kag_add_button('album_btn_06', current_stem='extra', storage=None, target='*page05', exp=None, x=579, y=355)
    $ kag_add_button('album_btn_07', current_stem='extra', storage=None, target='*page06', exp=None, x=579, y=405)
    $ kag_add_button('album_btn_back', current_stem='extra', storage=None, target='*backselect', exp=None, x=-11, y=472)
    if persistent.cghz1==1:
        $ kag_add_button('cghz1', current_stem='extra', storage=None, target='*cghz0', exp=None, x=73, y=119)
    if persistent.cghz2==1:
        $ kag_add_button('cghz2', current_stem='extra', storage=None, target='*cghz1', exp=None, x=243, y=170)
    if persistent.cghz3==1:
        $ kag_add_button('cghz3', current_stem='extra', storage=None, target='*cghz2', exp=None, x=413, y=220)
    if persistent.cghz4==1:
        $ kag_add_button('cghz4', current_stem='extra', storage=None, target='*cghz3', exp=None, x=73, y=252)
    if persistent.cghz5==1:
        $ kag_add_button('cghz5', current_stem='extra', storage=None, target='*cghz4', exp=None, x=243, y=303)
    if persistent.cghz6==1:
        $ kag_add_button('cghz6', current_stem='extra', storage=None, target='*cghz5', exp=None, x=413, y=353)
    if persistent.cghz7==1:
        $ kag_add_button('cghz7', current_stem='extra', storage=None, target='*cghz6', exp=None, x=73, y=385)
    $ kag_backlay()
    $ kag_image('album_07', layer='base', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=450, method='', rule='trans01', vague=64)
    $ kag_stoptrans()
    $ kag_set_clickskip(True)
    call kag_s_wait

label kag_extra_cghz0:
    $ kag_changetype('cross', '02はづき-02.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghz1:
    $ kag_changetype('cross', '02はづき-03.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghz2:
    $ kag_changetype('cross', '02はづき-05.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghz3:
    $ kag_changetype('cross', '02はづき-06.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghz4:
    $ kag_changetype('cross', '02はづき-07.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghz5:
    $ kag_changetype('cross', '02はづき-08.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghz6:
    $ kag_changetype('cross', '02はづき-09.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_button3:
    $ kag_stoptrans()
    $ kag_f.cgPage=2
    $ kag_add_button('album_btn_01', current_stem='extra', storage=None, target='*page00', exp=None, x=579, y=105)
    $ kag_add_button('album_btn_02', current_stem='extra', storage=None, target='*page01', exp=None, x=579, y=155)
    $ kag_add_button('album_btn_03', current_stem='extra', storage=None, target='*page02', exp=None, x=579, y=205)
    $ kag_add_button('album_btn_04', current_stem='extra', storage=None, target='*page03', exp=None, x=579, y=255)
    $ kag_add_button('album_btn_05', current_stem='extra', storage=None, target='*page04', exp=None, x=579, y=305)
    $ kag_add_button('album_btn_06', current_stem='extra', storage=None, target='*page05', exp=None, x=579, y=355)
    $ kag_add_button('album_btn_07', current_stem='extra', storage=None, target='*page06', exp=None, x=579, y=405)
    $ kag_add_button('album_btn_back', current_stem='extra', storage=None, target='*backselect', exp=None, x=-11, y=472)
    if persistent.cga1==1:
        $ kag_add_button('cga1', current_stem='extra', storage=None, target='*cga0', exp=None, x=73, y=119)
    if persistent.cga2==1:
        $ kag_add_button('cga2', current_stem='extra', storage=None, target='*cga1', exp=None, x=243, y=170)
    if persistent.cga3==1:
        $ kag_add_button('cga3', current_stem='extra', storage=None, target='*cga2', exp=None, x=413, y=220)
    if persistent.cga4==1:
        $ kag_add_button('cga4', current_stem='extra', storage=None, target='*cga3', exp=None, x=73, y=252)
    if persistent.cga5==1:
        $ kag_add_button('cga5', current_stem='extra', storage=None, target='*cga4', exp=None, x=243, y=303)
    if persistent.cga6==1:
        $ kag_add_button('cga6', current_stem='extra', storage=None, target='*cga5', exp=None, x=413, y=353)
    $ kag_backlay()
    $ kag_image('album_06', layer='base', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=450, method='', rule='trans01', vague=64)
    $ kag_stoptrans()
    $ kag_set_clickskip(True)
    call kag_s_wait

label kag_extra_cga0:
    $ kag_changetype('cross', '03あいこ-02.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cga1:
    $ kag_changetype('cross', '03あいこ-03.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cga2:
    $ kag_changetype('cross', '03あいこ-04.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cga3:
    $ kag_changetype('cross', '03あいこ-06.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cga4:
    $ kag_changetype('cross', '03あいこ-08.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cga5:
    $ kag_changetype('cross', '03あいこ-09.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_button4:
    $ kag_stoptrans()
    $ kag_f.cgPage=3
    $ kag_add_button('album_btn_01', current_stem='extra', storage=None, target='*page00', exp=None, x=579, y=105)
    $ kag_add_button('album_btn_02', current_stem='extra', storage=None, target='*page01', exp=None, x=579, y=155)
    $ kag_add_button('album_btn_03', current_stem='extra', storage=None, target='*page02', exp=None, x=579, y=205)
    $ kag_add_button('album_btn_04', current_stem='extra', storage=None, target='*page03', exp=None, x=579, y=255)
    $ kag_add_button('album_btn_05', current_stem='extra', storage=None, target='*page04', exp=None, x=579, y=305)
    $ kag_add_button('album_btn_06', current_stem='extra', storage=None, target='*page05', exp=None, x=579, y=355)
    $ kag_add_button('album_btn_07', current_stem='extra', storage=None, target='*page06', exp=None, x=579, y=405)
    $ kag_add_button('album_btn_back', current_stem='extra', storage=None, target='*backselect', exp=None, x=-11, y=472)
    if persistent.cgo1==1:
        $ kag_add_button('cgo1', current_stem='extra', storage=None, target='*cgo0', exp=None, x=73, y=119)
    if persistent.cgo2==1:
        $ kag_add_button('cgo2', current_stem='extra', storage=None, target='*cgo1', exp=None, x=243, y=170)
    if persistent.cgo3==1:
        $ kag_add_button('cgo3', current_stem='extra', storage=None, target='*cgo2', exp=None, x=413, y=220)
    if persistent.cgo4==1:
        $ kag_add_button('cgo4', current_stem='extra', storage=None, target='*cgo3', exp=None, x=73, y=252)
    if persistent.cgo5==1:
        $ kag_add_button('cgo5', current_stem='extra', storage=None, target='*cgo4', exp=None, x=243, y=303)
    if persistent.cgo6==1:
        $ kag_add_button('cgo6', current_stem='extra', storage=None, target='*cgo5', exp=None, x=413, y=353)
    $ kag_backlay()
    $ kag_image('album_06', layer='base', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=450, method='', rule='trans01', vague=64)
    $ kag_stoptrans()
    $ kag_set_clickskip(True)
    call kag_s_wait

label kag_extra_cgo0:
    $ kag_changetype('cross', '04おんぷ-02.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgo1:
    $ kag_changetype('cross', '04おんぷ-03.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgo2:
    $ kag_changetype('cross', '04おんぷ-04.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgo3:
    $ kag_changetype('cross', '04おんぷ-07.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgo4:
    $ kag_changetype('cross', '04おんぷ-08.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgo5:
    $ kag_changetype('cross', '04おんぷ-09.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_button5:
    $ kag_stoptrans()
    $ kag_f.cgPage=4
    $ kag_add_button('album_btn_01', current_stem='extra', storage=None, target='*page00', exp=None, x=579, y=105)
    $ kag_add_button('album_btn_02', current_stem='extra', storage=None, target='*page01', exp=None, x=579, y=155)
    $ kag_add_button('album_btn_03', current_stem='extra', storage=None, target='*page02', exp=None, x=579, y=205)
    $ kag_add_button('album_btn_04', current_stem='extra', storage=None, target='*page03', exp=None, x=579, y=255)
    $ kag_add_button('album_btn_05', current_stem='extra', storage=None, target='*page04', exp=None, x=579, y=305)
    $ kag_add_button('album_btn_06', current_stem='extra', storage=None, target='*page05', exp=None, x=579, y=355)
    $ kag_add_button('album_btn_07', current_stem='extra', storage=None, target='*page06', exp=None, x=579, y=405)
    $ kag_add_button('album_btn_back', current_stem='extra', storage=None, target='*backselect', exp=None, x=-11, y=472)
    if persistent.cgm1==1:
        $ kag_add_button('cgm1', current_stem='extra', storage=None, target='*cgm0', exp=None, x=73, y=119)
    if persistent.cgm2==1:
        $ kag_add_button('cgm2', current_stem='extra', storage=None, target='*cgm1', exp=None, x=243, y=170)
    if persistent.cgm3==1:
        $ kag_add_button('cgm3', current_stem='extra', storage=None, target='*cgm2', exp=None, x=413, y=220)
    if persistent.cgm4==1:
        $ kag_add_button('cgm4_1', current_stem='extra', storage=None, target='*cgm3', exp=None, x=73, y=252)
    if persistent.cgm5==1:
        $ kag_add_button('cgm5', current_stem='extra', storage=None, target='*cgm4', exp=None, x=243, y=303)
    if persistent.cgm6==1:
        $ kag_add_button('cgm6', current_stem='extra', storage=None, target='*cgm5', exp=None, x=413, y=353)
    $ kag_backlay()
    $ kag_image('album_06', layer='base', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=450, method='', rule='trans01', vague=64)
    $ kag_stoptrans()
    $ kag_set_clickskip(True)
    call kag_s_wait

label kag_extra_cgm0:
    $ kag_changetype('cross', '05ももこ-02.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgm1:
    $ kag_changetype('cross', '05ももこ-04.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgm2:
    $ kag_changetype('cross', '05ももこ-06.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgm3:
    $ kag_changetype('cross', '05ももこ-07-1.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click2
    call kag_s_wait

label kag_extra_cgm4:
    $ kag_changetype('cross', '05ももこ-08.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgm5:
    $ kag_changetype('cross', '05ももこ-09.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_click2:
    $ kag_click_count = 0
    $ kag_waitclick()
    if kag_get_click_count()!=0:
        $ kag_changetype('cross', '05ももこ-07-2.tlg', time_ms=400, bgcolor='0x000000')
        jump kag_extra_click3
    call kag_s_wait

label kag_extra_click3:
    $ kag_click_count = 0
    $ kag_waitclick()
    if kag_get_click_count()!=0:
        $ kag_changetype('cross', '05ももこ-07-3.tlg', time_ms=400, bgcolor='0x000000')
        jump kag_extra_click4
    call kag_s_wait

label kag_extra_click4:
    $ kag_click_count = 0
    $ kag_waitclick()
    if kag_get_click_count()!=0:
        $ kag_changetype('cross', '05ももこ-07-4.tlg', time_ms=400, bgcolor='0x000000')
        jump kag_extra_click
    call kag_s_wait

label kag_extra_button6:
    $ kag_stoptrans()
    $ kag_f.cgPage=5
    $ kag_add_button('album_btn_01', current_stem='extra', storage=None, target='*page00', exp=None, x=579, y=105)
    $ kag_add_button('album_btn_02', current_stem='extra', storage=None, target='*page01', exp=None, x=579, y=155)
    $ kag_add_button('album_btn_03', current_stem='extra', storage=None, target='*page02', exp=None, x=579, y=205)
    $ kag_add_button('album_btn_04', current_stem='extra', storage=None, target='*page03', exp=None, x=579, y=255)
    $ kag_add_button('album_btn_05', current_stem='extra', storage=None, target='*page04', exp=None, x=579, y=305)
    $ kag_add_button('album_btn_06', current_stem='extra', storage=None, target='*page05', exp=None, x=579, y=355)
    $ kag_add_button('album_btn_07', current_stem='extra', storage=None, target='*page06', exp=None, x=579, y=405)
    $ kag_add_button('album_btn_back', current_stem='extra', storage=None, target='*backselect', exp=None, x=-11, y=472)
    if persistent.cghn1==1:
        $ kag_add_button('cghn1', current_stem='extra', storage=None, target='*cghn0', exp=None, x=73, y=119)
    if persistent.cghn2==1:
        $ kag_add_button('cghn2', current_stem='extra', storage=None, target='*cghn1', exp=None, x=243, y=170)
    if persistent.cghn3==1:
        $ kag_add_button('cghn3', current_stem='extra', storage=None, target='*cghn2', exp=None, x=413, y=220)
    if persistent.cghn4==1:
        $ kag_add_button('cghn4', current_stem='extra', storage=None, target='*cghn3', exp=None, x=73, y=252)
    if persistent.cghn5==1:
        $ kag_add_button('cghn5', current_stem='extra', storage=None, target='*cghn4', exp=None, x=243, y=303)
    if persistent.cghn6==1:
        $ kag_add_button('cghn6', current_stem='extra', storage=None, target='*cghn5', exp=None, x=413, y=353)
    if persistent.cghn7==1:
        $ kag_add_button('cghn7', current_stem='extra', storage=None, target='*cghn6', exp=None, x=73, y=385)
    $ kag_backlay()
    $ kag_image('album_07', layer='base', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=450, method='', rule='trans01', vague=64)
    $ kag_stoptrans()
    $ kag_set_clickskip(True)
    call kag_s_wait

label kag_extra_cghn0:
    $ kag_changetype('cross', '06ハナ-02.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghn1:
    $ kag_changetype('cross', '06ハナ-04-1.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghn2:
    $ kag_changetype('cross', '06ハナ-04-2.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghn3:
    $ kag_changetype('cross', '06ハナ-05.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghn4:
    $ kag_changetype('cross', '06ハナ-07.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghn5:
    $ kag_changetype('cross', '06ハナ-08.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cghn6:
    $ kag_changetype('cross', '06ハナ-09.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_button7:
    $ kag_stoptrans()
    $ kag_f.cgPage=6
    $ kag_add_button('album_btn_01', current_stem='extra', storage=None, target='*page00', exp=None, x=579, y=105)
    $ kag_add_button('album_btn_02', current_stem='extra', storage=None, target='*page01', exp=None, x=579, y=155)
    $ kag_add_button('album_btn_03', current_stem='extra', storage=None, target='*page02', exp=None, x=579, y=205)
    $ kag_add_button('album_btn_04', current_stem='extra', storage=None, target='*page03', exp=None, x=579, y=255)
    $ kag_add_button('album_btn_05', current_stem='extra', storage=None, target='*page04', exp=None, x=579, y=305)
    $ kag_add_button('album_btn_06', current_stem='extra', storage=None, target='*page05', exp=None, x=579, y=355)
    $ kag_add_button('album_btn_07', current_stem='extra', storage=None, target='*page06', exp=None, x=579, y=405)
    $ kag_add_button('album_btn_back', current_stem='extra', storage=None, target='*backselect', exp=None, x=-11, y=472)
    if persistent.cgot1==1:
        $ kag_add_button('cgot1', current_stem='extra', storage=None, target='*cgoh0', exp=None, x=73, y=119)
    if persistent.cgot2==1:
        $ kag_add_button('cgot2', current_stem='extra', storage=None, target='*cgoh1', exp=None, x=243, y=170)
    if persistent.cgot3==1:
        $ kag_add_button('cgot3', current_stem='extra', storage=None, target='*cgoh2', exp=None, x=413, y=220)
    if persistent.cgot4==1:
        $ kag_add_button('cgot4', current_stem='extra', storage=None, target='*cgoh3', exp=None, x=73, y=252)
    if persistent.cgot5==1:
        $ kag_add_button('cgot5', current_stem='extra', storage=None, target='*cgoh4', exp=None, x=243, y=303)
    if persistent.cgot6==1:
        $ kag_add_button('cgot6', current_stem='extra', storage=None, target='*cgoh5', exp=None, x=413, y=353)
    $ kag_backlay()
    $ kag_image('album_06', layer='base', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=450, method='', rule='trans01', vague=64)
    $ kag_stoptrans()
    $ kag_set_clickskip(True)
    call kag_s_wait

label kag_extra_cgoh0:
    $ kag_changetype('cross', '07玉木-01.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgoh1:
    $ kag_changetype('cross', '08ぽっぷ-01.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgoh2:
    $ kag_changetype('cross', 'A-1.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgoh3:
    $ kag_changetype('cross', 'A-2.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgoh4:
    $ kag_changetype('cross', 'A-3.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_cgoh5:
    $ kag_changetype('cross', 'prologue4.tlg', time_ms=400, bgcolor='0x000000')
    jump kag_extra_click
    call kag_s_wait

label kag_extra_click:
    $ kag_click_count = 0
    $ kag_waitclick()
    if kag_get_click_count()!=0:
        jump kag_extra_bgchange
    call kag_s_wait

label kag_extra_backselect:
    $ kag_changetype('circle02', 'option', time_ms=500, bgcolor='0x000000')
    $ kag_f.cgPage=0
    jump kag_extra_extramenu
    call kag_s_wait

label kag_extra_re_movie:
    $ kag_changetype('down', 'bg096', time_ms=500, bgcolor='0x000000')
    $ kag_ct()
    $ kag_history_opt(output=False, enabled=None)
    $ kag_add_link('１．オープニング', current_stem='extra', storage=None, target='*op_movie', exp=None, x=30, y=30, color=None, size=None)
    $ kag_add_link('戻る', current_stem='extra', storage=None, target='*resetmenu', exp=None, x=30, y=80, color=None, size=None)
    $ kag_history_opt(output=True, enabled=None)
    call kag_s_wait

label kag_extra_op_movie:
    $ kag_ct()
    $ kag_video_opt(visible=True)
    $ kag_noop()
    $ kag_playvideo('どれみ1012.mpg')
    $ kag_set_clickskip(True)
    $ kag_click_count = 0
    $ kag_wv(canskip=True)
    if kag_get_click_count()!=0:
        jump kag_extra_quit

label kag_extra_quit:
    $ kag_video_opt(visible=False)
    $ kag_stopvideo()
    jump kag_extra_re_movie
    call kag_s_wait

label kag_extra_re_scenario:
    $ kag_cm()
    $ layerposition_def()
    $ kag_f.re_scenario=1
    $ kag_history_opt(output=False, enabled=False)
    $ kag_add_button('album_btn_01', current_stem='extra', storage=None, target='*s_doremi', exp=None, x=20, y=100)
    $ kag_add_button('album_btn_02', current_stem='extra', storage=None, target='*s_hazuki', exp=None, x=20, y=150)
    $ kag_add_button('album_btn_03', current_stem='extra', storage=None, target='*s_ai', exp=None, x=20, y=200)
    $ kag_add_button('album_btn_04', current_stem='extra', storage=None, target='*s_onpu', exp=None, x=20, y=250)
    $ kag_add_button('album_btn_05', current_stem='extra', storage=None, target='*s_momo', exp=None, x=20, y=300)
    $ kag_add_button('album_btn_06', current_stem='extra', storage=None, target='*s_hana', exp=None, x=20, y=350)
    $ kag_add_button('album_btn_07', current_stem='extra', storage=None, target='*s_etc', exp=None, x=20, y=400)
    $ kag_add_button('album_btn_back', current_stem='extra', storage=None, target='*resetmenu', exp=None, x=-11, y=472)
    call kag_s_wait

label kag_extra_s_doremi:
    $ kag_history_opt(output=False, enabled=False)
    $ kag_image('d_m_01', layer='0', page='back', left=200, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=500, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    "{color=#ff0066}春風どれみシナリオ{/color}{nw}"
    if persistent.d1_s==1:
        $ kag_add_link('「１日目」最初のお仕事！失敗してもがんばろう！', current_stem='extra', storage=None, target='*s_d1', exp=None, x=20, y=150, color='#ff0066', size=20)
    if persistent.d2_s==1:
        $ kag_add_link('「２日目」一生懸命少しずつ・・・', current_stem='extra', storage=None, target='*s_d2', exp=None, x=20, y=180, color='#ff0066', size=20)
    if persistent.d3_s==1:
        $ kag_add_link('「３日目」思い出と公園', current_stem='extra', storage=None, target='*s_d3', exp=None, x=20, y=210, color='#ff0066', size=20)
    if persistent.d4_s==1:
        $ kag_add_link('「４日目」みんなのまほう？', current_stem='extra', storage=None, target='*s_d4', exp=None, x=20, y=240, color='#ff0066', size=20)
    if persistent.d5_s==1:
        $ kag_add_link('「５日目」ステキないもうと', current_stem='extra', storage=None, target='*s_d5', exp=None, x=20, y=270, color='#ff0066', size=20)
    if persistent.d6_s==1:
        $ kag_add_link('「６日目」迷子とステーキ', current_stem='extra', storage=None, target='*s_d6', exp=None, x=20, y=300, color='#ff0066', size=20)
    if persistent.d7_s==1:
        $ kag_add_link('「７日目」おたがいの気持ち', current_stem='extra', storage=None, target='*s_d7', exp=None, x=20, y=330, color='#ff0066', size=20)
    if persistent.d8_s==1:
        $ kag_add_link('「８日目」最後の夜', current_stem='extra', storage=None, target='*s_d8', exp=None, x=20, y=360, color='#ff0066', size=20)
    if persistent.dc_s==1:
        $ kag_add_link('「エンディング」ないしょのまほう', current_stem='extra', storage=None, target='*s_d9', exp=None, x=20, y=390, color='#ff0066', size=20)
    $ kag_add_link('戻る', current_stem='extra', storage=None, target='*return_s0', exp=None, x=20, y=450, color='#ff0066', size=None)
    call kag_s_wait

label kag_extra_s_d1:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_d_b1_gamestart
    call kag_s_wait

label kag_extra_s_d2:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_d_b2_gamestart
    call kag_s_wait

label kag_extra_s_d3:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_d_b3_gamestart
    call kag_s_wait

label kag_extra_s_d4:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_d_b4_gamestart
    call kag_s_wait

label kag_extra_s_d5:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_d_b5_gamestart
    call kag_s_wait

label kag_extra_s_d6:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_d_b6_gamestart
    call kag_s_wait

label kag_extra_s_d7:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_d_b7_gamestart
    call kag_s_wait

label kag_extra_s_d8:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_d_b8_gamestart
    call kag_s_wait

label kag_extra_s_d9:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_d_c_gamestart
    call kag_s_wait

label kag_extra_s_hazuki:
    $ kag_history_opt(output=False, enabled=False)
    $ kag_image('hz_m_01', layer='0', page='back', left=200, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=500, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    "{color=#ff6600}藤原はづきシナリオ{/color}{nw}"
    if persistent.hz1_s==1:
        $ kag_add_link('「１日目」ＭＡＨＯ堂って大変！？', current_stem='extra', storage=None, target='*hz1', exp=None, x=20, y=150, color='#ff6600', size=20)
    if persistent.hz2_s==1:
        $ kag_add_link('「２日目」暑い！寒い！大混乱！！', current_stem='extra', storage=None, target='*hz2', exp=None, x=20, y=180, color='#ff6600', size=20)
    if persistent.hz3_s==1:
        $ kag_add_link('「３日目」りずむの習い事', current_stem='extra', storage=None, target='*hz3', exp=None, x=20, y=210, color='#ff6600', size=20)
    if persistent.hz4_s==1:
        $ kag_add_link('「４日目」美空小の怪談', current_stem='extra', storage=None, target='*hz4', exp=None, x=20, y=240, color='#ff6600', size=20)
    if persistent.hz5_s==1:
        $ kag_add_link('「５日目」思い出の砂浜', current_stem='extra', storage=None, target='*hz5', exp=None, x=20, y=270, color='#ff6600', size=20)
    if persistent.hz6_s==1:
        $ kag_add_link('「６日目」りずむと子犬', current_stem='extra', storage=None, target='*hz6', exp=None, x=20, y=300, color='#ff6600', size=20)
    if persistent.hz7_s==1:
        $ kag_add_link('「７日目」はづきとどれみ', current_stem='extra', storage=None, target='*hz7', exp=None, x=20, y=330, color='#ff6600', size=20)
    if persistent.hz8_s==1:
        $ kag_add_link('「８日目」最後の夜', current_stem='extra', storage=None, target='*hz8', exp=None, x=20, y=360, color='#ff6600', size=20)
    if persistent.hzc_s==1:
        $ kag_add_link('「エンディング」さよなら、そして始まり', current_stem='extra', storage=None, target='*hz9', exp=None, x=20, y=390, color='#ff6600', size=20)
    $ kag_add_link('戻る', current_stem='extra', storage=None, target='*return_s0', exp=None, x=20, y=450, color='#ff6600', size=None)
    call kag_s_wait

label kag_extra_hz1:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hz_b1_gamestart
    call kag_s_wait

label kag_extra_hz2:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hz_b2_gamestart
    call kag_s_wait

label kag_extra_hz3:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hz_b3_gamestart
    call kag_s_wait

label kag_extra_hz4:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hz_b4_gamestart
    call kag_s_wait

label kag_extra_hz5:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hz_b5_gamestart
    call kag_s_wait

label kag_extra_hz6:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hz_b6_gamestart
    call kag_s_wait

label kag_extra_hz7:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hz_b7_gamestart
    call kag_s_wait

label kag_extra_hz8:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hz_b8_gamestart
    call kag_s_wait

label kag_extra_hz9:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hz_c_gamestart
    call kag_s_wait

label kag_extra_s_ai:
    $ kag_history_opt(output=False, enabled=False)
    $ kag_image('a_m_01', layer='0', page='back', left=200, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=500, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    "{color=#3366ff}妹尾あいこシナリオ{/color}{nw}"
    if persistent.a1_s==1:
        $ kag_add_link('「１日目」がんばることの大切さ', current_stem='extra', storage=None, target='*a1', exp=None, x=20, y=150, color='#3366ff', size=20)
    if persistent.a2_s==1:
        $ kag_add_link('「２日目」思い出の絵本', current_stem='extra', storage=None, target='*a2', exp=None, x=20, y=180, color='#3366ff', size=20)
    if persistent.a3_s==1:
        $ kag_add_link('「３日目」平成足八本物語', current_stem='extra', storage=None, target='*a3', exp=None, x=20, y=210, color='#3366ff', size=20)
    if persistent.a4_s==1:
        $ kag_add_link('「４日目」ぽっぷのステキなお兄さん', current_stem='extra', storage=None, target='*a4', exp=None, x=20, y=240, color='#3366ff', size=20)
    if persistent.a5_s==1:
        $ kag_add_link('「５日目」お父さんってなに？', current_stem='extra', storage=None, target='*a5', exp=None, x=20, y=270, color='#3366ff', size=20)
    if persistent.a6_s==1:
        $ kag_add_link('「６日目」ステキな海！そしてステキな・・・', current_stem='extra', storage=None, target='*a6', exp=None, x=20, y=300, color='#3366ff', size=20)
    if persistent.a7_s==1:
        $ kag_add_link('「７日目」りずむとリボン', current_stem='extra', storage=None, target='*a7', exp=None, x=20, y=330, color='#3366ff', size=20)
    if persistent.a8_s==1:
        $ kag_add_link('「８日目」あいこの気持ち', current_stem='extra', storage=None, target='*a8', exp=None, x=20, y=360, color='#3366ff', size=20)
    if persistent.ac_s==1:
        $ kag_add_link('「エンディング」しあわせの魔法', current_stem='extra', storage=None, target='*a9', exp=None, x=20, y=390, color='#3366ff', size=20)
    $ kag_add_link('戻る', current_stem='extra', storage=None, target='*return_s0', exp=None, x=20, y=450, color='#3366ff', size=None)
    call kag_s_wait

label kag_extra_a1:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_a_b1_gamestart
    call kag_s_wait

label kag_extra_a2:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_a_b2_gamestart
    call kag_s_wait

label kag_extra_a3:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_a_b3_gamestart
    call kag_s_wait

label kag_extra_a4:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_a_b4_gamestart
    call kag_s_wait

label kag_extra_a5:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_a_b5_gamestart
    call kag_s_wait

label kag_extra_a6:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_a_b6_gamestart
    call kag_s_wait

label kag_extra_a7:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_a_b7_gamestart
    call kag_s_wait

label kag_extra_a8:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_a_b8_gamestart
    call kag_s_wait

label kag_extra_a9:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_a_c_gamestart
    call kag_s_wait

label kag_extra_s_onpu:
    $ kag_history_opt(output=False, enabled=False)
    $ kag_image('o_m_01', layer='0', page='back', left=200, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=500, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    "{color=#6633cc}瀬川おんぷシナリオ{/color}{nw}"
    if persistent.o1_s==1:
        $ kag_add_link('「１日目」おんぷちゃんってすごい！', current_stem='extra', storage=None, target='*o1', exp=None, x=20, y=150, color='#6633cc', size=20)
    if persistent.o2_s==1:
        $ kag_add_link('「２日目」わからない？チャイドルのお仕事', current_stem='extra', storage=None, target='*o2', exp=None, x=20, y=180, color='#6633cc', size=20)
    if persistent.o3_s==1:
        $ kag_add_link('「３日目」ライブってなに？', current_stem='extra', storage=None, target='*o3', exp=None, x=20, y=210, color='#6633cc', size=20)
    if persistent.o4_s==1:
        $ kag_add_link('「４日目」がんばることの大切さ', current_stem='extra', storage=None, target='*o4', exp=None, x=20, y=240, color='#6633cc', size=20)
    if persistent.o5_s==1:
        $ kag_add_link('「５日目」仕事とおんぷ\u3000りずむの気持ち', current_stem='extra', storage=None, target='*o5', exp=None, x=20, y=270, color='#6633cc', size=20)
    if persistent.o6_s==1:
        $ kag_add_link('「６日目」りずむの見習いマネージャー', current_stem='extra', storage=None, target='*o6', exp=None, x=20, y=300, color='#6633cc', size=20)
    if persistent.o7_s==1:
        $ kag_add_link('「７日目」おんぷと魔法', current_stem='extra', storage=None, target='*o7', exp=None, x=20, y=330, color='#6633cc', size=20)
    if persistent.o8_s==1:
        $ kag_add_link('「８日目」りずむ', current_stem='extra', storage=None, target='*o8', exp=None, x=20, y=360, color='#6633cc', size=20)
    if persistent.oc_s==1:
        $ kag_add_link('「エンディング」笑顔のにらめっこ', current_stem='extra', storage=None, target='*o9', exp=None, x=20, y=390, color='#6633cc', size=20)
    $ kag_add_link('戻る', current_stem='extra', storage=None, target='*return_s0', exp=None, x=20, y=450, color='#6633cc', size=None)
    call kag_s_wait

label kag_extra_o1:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_o_b1_gamestart
    call kag_s_wait

label kag_extra_o2:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_o_b2_gamestart
    call kag_s_wait

label kag_extra_o3:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_o_b3_gamestart
    call kag_s_wait

label kag_extra_o4:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_o_b4_gamestart
    call kag_s_wait

label kag_extra_o5:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_o_b5_gamestart
    call kag_s_wait

label kag_extra_o6:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_o_b6_gamestart
    call kag_s_wait

label kag_extra_o7:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_o_b7_gamestart
    call kag_s_wait

label kag_extra_o8:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_o_b8_gamestart
    call kag_s_wait

label kag_extra_o9:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_o_c_gamestart
    call kag_s_wait

label kag_extra_s_momo:
    $ kag_history_opt(output=False, enabled=False)
    $ kag_image('m_m_01', layer='0', page='back', left=200, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=500, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    "{color=#33cc00}飛鳥ももこシナリオ{/color}{nw}"
    if persistent.m1_s==1:
        $ kag_add_link('「１日目」今日も元気にＭＡＨＯ堂？', current_stem='extra', storage=None, target='*mm1', exp=None, x=20, y=150, color='#33cc00', size=20)
    if persistent.m2_s==1:
        $ kag_add_link('「２日目」ももこ先生の体験入学！？', current_stem='extra', storage=None, target='*mm2', exp=None, x=20, y=180, color='#33cc00', size=20)
    if persistent.m3_s==1:
        $ kag_add_link('「３日目」心をこめて・・・', current_stem='extra', storage=None, target='*mm3', exp=None, x=20, y=210, color='#33cc00', size=20)
    if persistent.m4_s==1:
        $ kag_add_link('「４日目」りずむのねがいごと', current_stem='extra', storage=None, target='*mm4', exp=None, x=20, y=240, color='#33cc00', size=20)
    if persistent.m5_s==1:
        $ kag_add_link('「５日目」夕日の砂浜', current_stem='extra', storage=None, target='*mm5', exp=None, x=20, y=270, color='#33cc00', size=20)
    if persistent.m6_s==1:
        $ kag_add_link('「６日目」人間界のおともだち', current_stem='extra', storage=None, target='*mm6', exp=None, x=20, y=300, color='#33cc00', size=20)
    if persistent.m7_s==1:
        $ kag_add_link('「７日目」楽しさはおいしさの隠し味', current_stem='extra', storage=None, target='*mm7', exp=None, x=20, y=330, color='#33cc00', size=20)
    if persistent.m8_s==1:
        $ kag_add_link('「８日目」友だちとわたし', current_stem='extra', storage=None, target='*mm8', exp=None, x=20, y=360, color='#33cc00', size=20)
    if persistent.mc_s==1:
        $ kag_add_link('「エンディング」～伝わる気持ち～', current_stem='extra', storage=None, target='*mm9', exp=None, x=20, y=390, color='#33cc00', size=20)
    $ kag_add_link('戻る', current_stem='extra', storage=None, target='*return_s0', exp=None, x=20, y=450, color='#33cc00', size=None)
    call kag_s_wait

label kag_extra_mm1:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_m_b1_gamestart
    call kag_s_wait

label kag_extra_mm2:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_m_b2_gamestart
    call kag_s_wait

label kag_extra_mm3:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_m_b3_gamestart
    call kag_s_wait

label kag_extra_mm4:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_m_b4_gamestart
    call kag_s_wait

label kag_extra_mm5:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_m_b5_gamestart
    call kag_s_wait

label kag_extra_mm6:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_m_b6_gamestart
    call kag_s_wait

label kag_extra_mm7:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_m_b7_gamestart
    call kag_s_wait

label kag_extra_mm8:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_m_b8_gamestart
    call kag_s_wait

label kag_extra_mm9:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_m_c_gamestart
    call kag_s_wait

label kag_extra_s_hana:
    $ kag_history_opt(output=False, enabled=False)
    $ kag_image('hn_m_02', layer='0', page='back', left=200, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=500, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    "{color=#ff9900}ハナちゃんシナリオ{/color}{nw}"
    if persistent.hn1_s==1:
        $ kag_add_link('「１日目」りずむショック！ハナのいたずら！？', current_stem='extra', storage=None, target='*hn1', exp=None, x=20, y=150, color='#ff9900', size=20)
    if persistent.hn2_s==1:
        $ kag_add_link('「２日目」音楽と魔法', current_stem='extra', storage=None, target='*hn2', exp=None, x=20, y=180, color='#ff9900', size=20)
    if persistent.hn3_s==1:
        $ kag_add_link('「３日目」みんなで遊ぼう！１日おねぇさん', current_stem='extra', storage=None, target='*hn3', exp=None, x=20, y=210, color='#ff9900', size=20)
    if persistent.hn4_s==1:
        $ kag_add_link('「４日目」りずむママのかつやく', current_stem='extra', storage=None, target='*hn4', exp=None, x=20, y=240, color='#ff9900', size=20)
    if persistent.hn5_s==1:
        $ kag_add_link('「５日目」ひとりぼっちのＭＡＨＯ堂', current_stem='extra', storage=None, target='*hn5', exp=None, x=20, y=270, color='#ff9900', size=20)
    if persistent.hn6_s==1:
        $ kag_add_link('「６日目」～お祭り勝負！りずむと玉木？～', current_stem='extra', storage=None, target='*hn6', exp=None, x=20, y=300, color='#ff9900', size=20)
    if persistent.hn7_s==1:
        $ kag_add_link('「７日目」気持ちがわからない！？', current_stem='extra', storage=None, target='*hn7', exp=None, x=20, y=330, color='#ff9900', size=20)
    if persistent.hn8_s==1:
        $ kag_add_link('「８日目」ないしょのまほう', current_stem='extra', storage=None, target='*hn8', exp=None, x=20, y=360, color='#ff9900', size=20)
    if persistent.hnc_s==1:
        $ kag_add_link('「エンディング」思い出は、音色とともに', current_stem='extra', storage=None, target='*hn9', exp=None, x=20, y=390, color='#ff9900', size=20)
    $ kag_add_link('戻る', current_stem='extra', storage=None, target='*return_s0', exp=None, x=20, y=450, color='#ff9900', size=None)
    call kag_s_wait

label kag_extra_hn1:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hn_b1_gamestart
    call kag_s_wait

label kag_extra_hn2:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hn_b2_gamestart
    call kag_s_wait

label kag_extra_hn3:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hn_b3_gamestart
    call kag_s_wait

label kag_extra_hn4:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hn_b4_gamestart
    call kag_s_wait

label kag_extra_hn5:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hn_b5_gamestart
    call kag_s_wait

label kag_extra_hn6:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hn_b6_gamestart
    call kag_s_wait

label kag_extra_hn7:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hn_b7_gamestart
    call kag_s_wait

label kag_extra_hn8:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hn_b8_gamestart
    call kag_s_wait

label kag_extra_hn9:
    $ kag_freeimage(layer='0', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_hn_c_gamestart
    call kag_s_wait

label kag_extra_s_etc:
    $ kag_history_opt(output=False, enabled=False)
    $ kag_image('memorial_all.png', layer='base', page='back', left=0, top=0, visible=True, sepia=False)
    if persistent.NormalCnt==6 or persistent.TrueCnt>=3:
        $ kag_image('t_02', layer='0', page='back', left=200, top=0, visible=True, sepia=False)
    if persistent.TrueCnt==6:
        $ kag_image('t_02', layer='0', page='back', left=100, top=0, visible=True, sepia=False)
        $ kag_image('p_m_02', layer='1', page='back', left=280, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=500, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    $ kag_add_link('プロローグ\u3000\u3000魔女界編', current_stem='extra', storage=None, target='*s_ps', exp=None, x=20, y=150, color='#009966', size=20)
    if persistent.firstclear==1:
        $ kag_add_link('共通シナリオ\u3000ＭＡＨＯ堂へようこそ', current_stem='extra', storage=None, target='*s_ap', exp=None, x=20, y=190, color='#009966', size=20)
    if persistent.NormalCnt==6 or persistent.TrueCnt>=3:
        $ kag_add_link('玉木麗香\u3000\u3000\u3000見えないやさしさ', current_stem='extra', storage=None, target='*s_tm', exp=None, x=20, y=230, color='#ff6600', size=20)
    if persistent.TrueCnt==6:
        $ kag_add_link('春風ぽっぷ\u3000\u3000ぽっぷちゃんとお店番', current_stem='extra', storage=None, target='*s_pp', exp=None, x=20, y=270, color='#ff0033', size=20)
    $ kag_add_link('戻る', current_stem='extra', storage=None, target='*return_s0', exp=None, x=20, y=450, color='#009966', size=None)
    call kag_s_wait

label kag_extra_s_ps:
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_prologue_gamestart
    call kag_s_wait

label kag_extra_s_ap:
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_part_a_gamestart
    call kag_s_wait

label kag_extra_s_tm:
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_omake_tm_gamestart
    call kag_s_wait

label kag_extra_s_pp:
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_fadeoutbgm(1000)
    jump kag_omake_p_gamestart
    call kag_s_wait

label kag_extra_return_s0:
    jump kag_extra_return_s
    call kag_s_wait

label kag_extra_return_s:
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ layerposition_def()
    $ kag_changetype('cross', 'memorial_all.png', time_ms=1000, bgcolor='0x000000')
    jump kag_extra_re_scenario
    call kag_s_wait

label kag_extra_resetmenu:
    $ kag_f.page=0
    $ kag_position(left='16', top='16', width='768', height='568', opacity='0')
    $ kag_changetype('left', 'option', time_ms=500, bgcolor='0x000000')
    jump kag_extra_extramenu
    call kag_s_wait

label kag_extra_back:
    $ kag_ct()
    $ kag_playbgm('bgm-v01', loop=True)
    $ kag_changetype('left', 'maintitle', time_ms=500, bgcolor='0x000000')
    jump kag_menu_mainmenu
    call kag_s_wait
    return
