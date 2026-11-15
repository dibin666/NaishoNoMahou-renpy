# Auto-generated from 02. hazuki/hz_B7.ks by tools/transpile_ks.py
label kag_hz_b7:

label kag_hz_b7_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hazuki.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hz_b7_hz__dash__07_00:
    $ kag_set_bookmark('「７日目」はづきとどれみ')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0254.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おんぷちゃん、これはこっちでええの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0185.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あいちゃんとおんぷちゃんは商品の整理をしている。"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0154.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「はづきちゃん、そこのビーズとって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0354.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「えっと、これ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ももちゃんとはづきちゃんはアクセサリー作りをしている。"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0617.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナ隊員！{w=0.4}きみも仕事をしたまえ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0173.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ隊長もであります！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんとハナちゃんは……２人でサボっている。"
    $ kag_cm()
    "……昨日の夜にそんな映画でも見たのかな？"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0174.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「てやぁ！{w=0.4}たあ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0618.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やったな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0356.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう、どれみちゃんったらいつまでサボってるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0619.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ゴメンゴメン。{w=0.4}今やるよ……{w=0.55}"
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0619.2', buf=0, loop=False)
    extend "うわわわっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0357.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃんあぶない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_stopbgm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg013', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b7_hz__dash__07_01:
    $ kag_set_bookmark('「７日目」はづきとどれみ')
    $ kag_cm()
    $ kag_playse('1-0620.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいたたた……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0358.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0621.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へーきだよ。{w=0.4}ちょっとひじをすりむいただけだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0359.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「待ってて。{w=0.4}すぐに救急箱持ってくるから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0175.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ、いたい？……{w=0.6}ごめんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0622.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃんは悪くないよ。{w=0.4}あたしが足もとをよく見てなかったから。{w=0.4}あいたあ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「思いっきりおしりをぶつけて転んだから、しばらくそのままでいた方がいいですよ」"
    $ kag_cm()
    $ kag_playse('1-0623.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いたた……{w=0.55}うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしもひと月くらい前に、お城の掃除中に階段から落ちて、しばらく動けなかったですから」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0624.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}ついでにバケツの水をこぼしてお掃除がさらに大変で……」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0176.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「なんか、どれみみたいだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0625.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん、それどういう意味～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0177.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへ、あははは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふふ」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0626.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ふふふふ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0360.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「困ったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしたんですか？{w=0.4}はづきちゃん」"
    $ kag_cm()
    $ kag_playse('2-0361.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「救急箱なんだけど、マジョリカの部屋にあったみたいで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0627.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？{w=0.4}じゃあ、今お部屋変わってるから、救急箱ってないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それじゃあ、わたしが魔法で出します」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「救急箱よ、出てきて！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。はづきちゃん」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0362.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ありがとうりずむちゃん。{w=0.4}どれみちゃん見せて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0628.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0363.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう。{w=0.4}階段でよそ見なんてしちゃダメじゃない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0629.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「めんぼくないッス」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0364.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん。{w=0.4}消毒薬ってこれでいいのかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうです。{w=0.4}でも……」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0630.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぎいやああ～～～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}それ、とってもしみるんです」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b7_hz__dash__07_02:
    $ kag_set_bookmark('「７日目」はづきとどれみ')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0365.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「大したケガじゃなくてよかったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0631.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はづきちゃんは大げさだなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0366.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そんなことないわ。{w=0.4}キズ口からバイキンが入ったら大変よ？{w=0.4}昔からしょっちゅう転んでたし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0632.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうかなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0367.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん、幼稚園のころはよく顔から転んでたじゃない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0633.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う、そんな昔のことを……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんなことがあったんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0368.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うん。{w=0.4}小学校にあがってもしばらくはそうだったし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0634.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はづきちゃんだって学年が変わったのに、新学期になって１学年下のクラスにまちがえて登校したことあったじゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え！{w=0.4}はづきちゃんがですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0369.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どどど、どれみちゃん！{w=0.4}その……ことは……もう忘れてって言ったじゃない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「２人はいつから友だちなんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0635.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「幼稚園からだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0370.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、それで仲がいいんですね」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0636.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん、まあ幼なじみだからね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0371.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ。{w=0.4}あ、いけない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0372.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「学校の花壇にお水をやりにいかなくちゃいけないんだったわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0637.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それって、\nまりなちゃんがいつもやってるんじゃないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0373.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「家族で旅行に行くからって、今日だけ頼まれてたのよ。{w=0.4}ちょっと行ってくるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしも行きます」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg093', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b7_hz__dash__07_03:
    $ kag_set_bookmark('「７日目」はづきとどれみ')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいですね。{w=0.4}幼なじみって」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0374.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ。{w=0.4}わたし、幼稚園の知り合いって近くにいないんです」"
    $ kag_cm()
    $ kag_playse('2-0375.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃんとはずっといっしょだから、いつも近くに必ずいるって感じなのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「昔から自分のことをよく知っている人がいるって、ちょっとうらやましいです」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0376.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ふふふ、そう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg057', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b7_hz__dash__07_04:
    $ kag_set_bookmark('「７日目」はづきとどれみ')
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0377.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「このじょうろで花壇全部にお水をまくのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "校庭の真ん中では、男の子たちがサッカーをやっている。{w=0.4}この日ざしで、みんな元気だなあ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0378.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんがいてくれたから、思ったより早く終わりそうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それじゃ、始めましょうか」"
    $ kag_cm()
    $ kag_playse('2-0379.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "毎日毎日この暑さだから、さすがにお花さんたちもちょっとバテぎみのようすだ。{w=0.4}\nわたしもＭＡＨＯ堂に帰ったら冷たい麦茶が飲みたいなあ。"
    $ kag_cm()
    "ポーン"
    extend "\nポン"
    extend "\nポン"
    $ kag_cm()
    $ kag_set_next_indent('サッカー部員「')
    "サッカー部員「ごめーん！{w=0.4}ボールとってくれる～？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はーい！」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0380.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「今日もあついわね。{w=0.4}これじゃ毎日お花のお世話をするまりなちゃんだって大変よね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「まりなちゃん？{w=0.4}あ、クラスメートの方ですか」"
    $ kag_cm()
    $ kag_playse('2-0381.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ。{w=0.4}お花がとっても好きな子なのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「たしかに、毎日お世話するのは大変ですね」"
    $ kag_cm()
    "ポーン"
    extend "\nポン"
    extend "\nポン"
    $ kag_cm()
    $ kag_set_next_indent('サッカー部員「')
    "サッカー部員「わりいわりい～！{w=0.4}こっちにパスしてくれ～！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はーい！」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0382.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もうちょっと、はなれて練習した方がいいんじゃないかしら。{w=0.4}花壇にボールが入ったりしたら、お花が折れちゃうわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg057', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0383.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう終わっちゃった。{w=0.4}りずむちゃんまで手伝わせちゃってごめんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「これくらい、どうってことないですよ」"
    $ kag_cm()
    $ kag_playse('2-0384.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「じょうろを戻してくるわ。{w=0.4}りずむちゃん貸して」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_freeimage(layer='0', page='fore')
    "はづきちゃんが用具入れに足を向けたそのときだった。"
    extend "\n校庭からサッカーボールが飛んできた。"
    extend "\nボールの行き先には……"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃんあぶない！」"
    $ kag_cm()
    $ kag_playse('2-0385.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？{w=0.4}キャア！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'white', time_ms=500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_mesframe()
    $ kag_cm()
    "わたしは、考えるより先に、はづきちゃんのいた方へかけだしていった所までは覚えていた。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', 'black', time_ms=2500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('2-0386.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、りずむちゃん！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('サッカー部員「')
    "サッカー部員「大丈夫か！？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'white', time_ms=2500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('2-0387.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづき、ちゃん？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg251', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b7_hz__dash__07_05:
    $ kag_set_bookmark('「７日目」はづきとどれみ')
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0388.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「気がついたのね。{w=0.4}よかったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ、たしかボールが飛んできて……」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0389.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしのかわりに、りずむちゃんがボールにぶつかったのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そうか。{w=0.4}それでわたし気を失ってたんですね」"
    $ kag_cm()
    $ kag_playse('2-0390.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「サッカー部のみんなに、保健室までりずむちゃんを運んできてもらったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうでしたか……」"
    $ kag_cm()
    $ kag_drawchar('hz_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0391.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう！{w=0.4}無茶しないでよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……？」"
    $ kag_cm()
    $ kag_playbgm('m413a', loop=True)
    $ kag_playse('2-0392.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんが、りずむちゃんがこのまま目を開けなかったら、ホントにどうしようかと思ったんだから！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……すみません」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0393.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ごめんなさい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_playse('2-0394.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしを助けようとして、りずむちゃんがボールにぶつかっちゃったんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('2-0395.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ホントはお礼を言わなくちゃいけないのに、怒ったりしてごめんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんなこと」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0396.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ううん。{w=0.4}それにしても、飛び出すなんてあぶないわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_hz_b7_choices_hz03:
    $ kag_set_bookmark('はづきシナリオ選択肢03')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】とっさのことだったので', current_stem='hz_b7', storage=None, target='*choices_hz03-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】思わず飛び出しちゃったんです', current_stem='hz_b7', storage=None, target='*choices_hz03-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_hz_b7_choices_hz03__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、とっさのことだったから、魔法を使うヒマがなくって……」"
    $ kag_cm()
    jump kag_hz_b7_after_choices_hz03
    call kag_s_wait

label kag_hz_b7_choices_hz03__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag += 1
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0397.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「だからって何も、顔で受けなくってもよかったのに」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}実は、ぶつかる瞬間とかをぜんぜん覚えてなくって」"
    $ kag_cm()
    jump kag_hz_b7_after_choices_hz03
    call kag_s_wait

label kag_hz_b7_after_choices_hz03:
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0398.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そう……{w=0.55}フフ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0399.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフ……{w=0.6}りずむちゃんって、どれみちゃんみたい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わ、わたしってどれみちゃんに似てます？」"
    $ kag_cm()
    $ kag_playse('2-0400.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「幼稚園のころ、わたしがいじめっ子にからまれているときに、{w=0.4}どれみちゃんに助けてもらったことがあったの。{w=0.4}それを思い出しちゃったのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0401.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんの、やさしくってちょっぴりドジな所は、ホントどれみちゃんにそっくりね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「その、ドジって所はちょっと……」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0402.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ウフ、フフフフ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「も、もう～！{w=0.4}はづきちゃんったら」"
    $ kag_cm()
    $ kag_playse('2-0403.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフフ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg094', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b7_hz__dash__07_06:
    $ kag_set_bookmark('「７日目」はづきとどれみ')
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0404.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう平気？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}ぜ～んぜん平気です」"
    $ kag_cm()
    $ kag_playse('2-0405.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ホントに大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「大丈夫ですって。{w=0.4}そんなに心配しないでください」"
    $ kag_cm()
    $ kag_playse('2-0406.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ならいいんだけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どっちかって言うと、保健室を出た後の方が……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0407.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「サッカー部の子たち、すごく反省してたみたいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あんなにあやまってもらって、逆にわたしがびっくりしちゃいましたよ」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0408.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、よそ見して歩くと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}はうっ！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '02はづき-07', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghz5=1
    $ kag_mesframe()

label kag_hz_b7_hz__dash__07_07:
    $ kag_set_bookmark('「７日目」はづきとどれみ')
    $ kag_cm()
    $ kag_playbgm('m14', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いたたた……」"
    $ kag_cm()
    $ kag_playse('2-0409.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あぶないって言おうとしたんだけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "知らないうちに電柱が近づいてきて……{w=0.55}なわけはなく、わたしはよそ見をしていたせいでおでこを電柱にぶつけてしまった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「も、もう少し早く言ってくれるとよかったかも……」"
    $ kag_cm()
    $ kag_playse('2-0410.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ウフフフフ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、恥ずかしいです」"
    $ kag_cm()
    $ kag_playse('2-0411.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ウフフ……{w=0.5}ね、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_playse('2-0412.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ありがとう。{w=0.4}これからもよろしくね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}は、はいっ！」"
    $ kag_cm()
    "わたしとはづきちゃんは、\nＭＡＨＯ堂に戻るまでずっと、手をつないでいた。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hz7_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hz_b8_gamestart
    return
