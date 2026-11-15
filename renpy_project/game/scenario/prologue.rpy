# Auto-generated from 00. part_A/prologue.ks by tools/transpile_ks.py
label kag_prologue:

label kag_prologue_gamestart:
    $ kag_set_bookmark('プロローグ\u3000\u3000魔女界編')
    $ kag_history_opt(output=False, enabled=None)
    $ kag_set_rclick(False)
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'black', time_ms=500, bgcolor='0x000000')
    $ kag_set_clickskip(True)
    $ kag_changetype('cross', 'prologue1', time_ms=1000, bgcolor='0x000000')
    $ kag_wait(1000, canskip=True)
    $ kag_changetype('cross', 'black', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('cross', 'prologue2', time_ms=1000, bgcolor='0x000000')
    $ kag_wait(1000, canskip=True)
    $ kag_changetype('cross', 'prologue3', time_ms=2000, bgcolor='0x000000')
    $ kag_wait(2500, canskip=True)
    $ kag_changetype('cross', 'bg065', time_ms=2000, bgcolor='0x000000')
    $ kag_wait(1000, canskip=True)
    $ kag_ct()
    $ kag_freeimage(layer='1', page='fore')
    $ kag_mesframe()
    $ kag_wait(1000, canskip=True)
    $ kag_history_opt(output=True, enabled=True)

label kag_prologue_prologue:
    if kag_f.re_scenario==0:
        $ kag_set_rclick(True)
        $ kag_set_clickskip(True)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ａ\u3000「')
    "魔女Ａ　「ほらそこ、しっかりしなさい！」{nw}"
    $ kag_wait(2000, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「すみませんっ、しっかりやります……{w=0.55}ああっ！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｂ\u3000「')
    "魔女Ｂ　「はやくしてくれないと、こっちの仕事が遅れちゃうじゃない！」{nw}"
    $ kag_wait(3000, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「すみませんっ、はやくやります……{w=0.55}あらら？」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｃ\u3000「')
    "魔女Ｃ　「ちょっと～。\n頼んでおいたお使い、まだ行ってくれてないの？」{nw}"
    $ kag_wait(3000, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0003.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「すみませんっ、これが終わったらすぐに……\n{w=0.45}きゃあっ！」{nw}"
    $ kag_wait(1000, canskip=True)
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ａ\u3000「')
    "魔女Ａ　「ハァ。もういいわ。お使いはわたしが行ってくるから、\nあなたは今やってる仕事を片づけなさい」{nw}"
    $ kag_wait(3000, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「すみませんっ……{w=0.55}ホントにすみません……」{nw}"
    $ kag_wait(2000, canskip=True)
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('note', 'bg067', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｂ\u3000「')
    "魔女Ｂ　「まったくドジね、あの子は……」{nw}"
    $ kag_wait(2000, canskip=True)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｃ\u3000「')
    "魔女Ｃ　「ほんと、お仕事失敗ばかりしているわね。\nお使いに行っても道に迷うばっかりだし」{nw}"
    $ kag_wait(3000, canskip=True)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｂ\u3000「')
    "魔女Ｂ　「なんであんな子が仕事してるのかしら。\nさっさとクビにしちゃえばいいのに……」{nw}"
    $ kag_wait(3000, canskip=True)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｃ\u3000「')
    "魔女Ｃ　「なんかうわさでは友だちもいないって言うわよ……」{nw}"
    $ kag_wait(2000, canskip=True)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｂ\u3000「')
    "魔女Ｂ　「まぁ、そうですの。でもそんな感じしますわね。\nいっつもグズグズしてますしね」{nw}"
    $ kag_wait(3000, canskip=True)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｃ\u3000「')
    "魔女Ｃ　「あんなに失敗ばかりしていたら、わたしたちまでいっしょに怒られちゃうわよ。まったく……」{nw}"
    $ kag_wait(3000, canskip=True)
    $ kag_cm()
    "少し離れた場所から、魔女たちのうわさ話が聞こえてくる。{nw}"
    $ kag_wait(2000, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0005.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「またわたしのこと、うわさしてる」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_wait(1000, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0005.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「どうしていつも悪口言われちゃうのかな？」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_wait(1000, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0005.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「やっぱり、わたしがドジなせいかな……」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_wait(1000, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたしは、涙をこらえるのがせいいっぱいだった。{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    $ kag_set_next_indent('マジョリン「')
    "マジョリン「あなた方、そこでなにを話しているのですか。{w=0.45}ここは城内です。{w=0.45}静かにしなさい」{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｂ＆Ｃ「')
    "魔女Ｂ＆Ｃ「すみませ～ん！」{nw}"
    $ kag_wait(2000, canskip=True)
    $ kag_cm()
    $ kag_set_next_indent('マジョリン「')
    "マジョリン「そこで聞いているあなたも、はやく仕事にもどりなさい」{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子\u3000「')
    "魔女の子　「すみません！{w=0.3}あっ！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-005.ogg', buf=1)
    "つまずいてしまった。{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    "そこいらにちらばる荷物。{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    "マジョリンさんのあきれ顔。{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子\u3000「')
    "魔女の子　「すみません！すみませんっ！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('マジョリン「')
    "マジョリン「……」{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0008.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子\u3000「')
    "魔女の子　「ハァ、わたし、ダメだなぁ……」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_wait(2000, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('blind01', 'eyecatch.tlg', time_ms=1500, bgcolor='0x000000')
    $ kag_playbgm('m401a.ogg', loop=False)
    $ kag_wait(300, canskip=True)
    $ kag_changetype('note', 'bg066', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('9-0009.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「わたしって、どうしていつも失敗ばかりしちゃうんだろう」{w=1.2}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    "また涙がこぼれそうになるのをどうにかこらえ、空を見あげる。{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あれ……？」{w=1.5}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    "お城の外の、いつもの風景。{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    "１つちがう所は、お城の３階くらいの高さを、ほうきに乗ってポロンを振り回して飛んでいる子たちの姿だ。{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    "年は、ちょうどわたしと同じくらい。{nw}"
    $ kag_wait(2500, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0011.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あれ、なんだろう。あのにぎやかな人たち」{w=1.2}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0011.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「見習い服？魔女見習いさんかな……」{w=1.2}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_wl(canskip=True)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_playse('3-0001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女見習い「')
    "魔女見習い「どれみちゃん、ふざけて飛んでたらあかんて！」{w=0.6}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女見習い「')
    "魔女見習い「そうよ、あぶないわ」{w=0.6}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女見習い「')
    "魔女見習い「だいじょうぶだってぇぇぇぇぇ！おおぅぅぅ！」{w=0.6}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    $ kag_playse('5-0001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女見習い「')
    "魔女見習い「アハハハハハハ」{w=0.6}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('note', 'prologue4', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgot6=1
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('4-0001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女見習い「')
    "魔女見習い「さぁ、ふざけてないで、はやくＭＡＨＯ堂に戻りましょう」{w=1}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女見習い「')
    "魔女見習い「寄り道してるとまたマジョリカがうるさいで～」{w=1}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('cross', 'prologue5', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m42.ogg', loop=True)
    $ kag_playse('9-0012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子\u3000「')
    "魔女の子　「……あの魔女見習いさんたち、お仕事の途中なのかなぁ」{w=1}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子\u3000「')
    "魔女の子　「なんだかとっても楽しそうだったなぁ」{w=1}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0014.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子\u3000「')
    "魔女の子　「いいなぁ。{w=0.4}わたしもああいうふうに、お友だちといっしょにお仕事ができたらなぁ……」{w=1}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0015.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子\u3000「')
    "魔女の子　「ちょっとくらい失敗しても、がみがみ怒られないだろうし。{w=0.55}陰で悪口なんか言われないだろうし、楽しいだろうなぁ」{w=1}{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    "魔女見習いたちが去った空の向こうを、\nわたしはしばらくの間ながめ続けていた。{nw}"
    $ kag_wait(2000, canskip=True)
    $ kag_cm()
    $ kag_playse('9-0016.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子\u3000「')
    "魔女の子　「お友だち……{w=1}か……」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_waitclick()
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1000, bgcolor='0x000000')
    $ kag_fadeoutbgm(1000)
    $ kag_wait(1000, canskip=True)
    if kag_f.re_scenario==1:
        jump kag_extra_return_s

label kag_prologue_op_movie:
    if persistent.movieSkip!=0:
        $ kag_changetype('blind01', 'eyecatch', time_ms=1000, bgcolor='0x000000')
        $ kag_video_opt(visible=True)
        $ kag_noop()
        $ kag_playvideo('どれみ1015.mpg')
        if persistent.m_skip==0:
            $ kag_set_clickskip(True)
            $ kag_wv(canskip=True)
        if persistent.m_skip==1:
            $ kag_click_count = 0
            $ kag_set_clickskip(True)
            $ kag_wv(canskip=True)
            if kag_get_click_count()!=0:
                jump kag_prologue_quit

label kag_prologue_quit:
    $ kag_video_opt(visible=False)
    $ kag_stopvideo()
    $ persistent.m_skip=1
    $ kag_set_clickskip(True)
    $ kag_wait(2000, canskip=True)
    jump kag_part_a_gamestart
    call kag_s_wait
    return
