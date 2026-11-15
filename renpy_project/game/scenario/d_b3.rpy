# Auto-generated from 01. doremi/d_B3.ks by tools/transpile_ks.py
label kag_d_b3:

label kag_d_b3_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_doremi.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_d_b3_d__dash__03_00:
    $ kag_set_bookmark('「３日目」思い出と公園')
    $ kag_cm()
    $ kag_drawchar('hn_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0038.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おお～ぅ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0181.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「これ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0050.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんが……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ひとりで……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0056.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「作ったの……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0051.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Ｏｈ～ファンタスティック！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0013.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「すっごぉ～い！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いや……{w=0.6}それほどでも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0182.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「すごいよ！りずむちゃん！{w=0.4}一晩でこんなにステキなアクセサリー作っちゃうなんて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0051.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「すごいわね、りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「実はすごい才能のもちぬしとちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ほ、ほめすぎです……」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0039.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「もうどれみなんかよりすごいね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0183.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん！{w=0.35}ママに向かって『なんか』はないでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0057.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そんなことより、もうお店の始まる時間よ。{w=0.35}早く開店させましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0184.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなことよりって、おんぷちゃんヒドイ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おんぷちゃんらしいわ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0052.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ほらほらどれみちゃん、りずむちゃんといっしょにアクセサリーならべようよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0185.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハイ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_d_b3_d__dash__03_01:
    $ kag_set_bookmark('「３日目」思い出と公園')
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg002', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m60', loop=True)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0186.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いらっしゃいませ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「この名札、他の名前もあるのかしら？」"
    $ kag_cm()
    $ kag_playse('1-0187.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そりゃあもう！{w=0.35}自分の名前から、大好きなあの人の名前まで、お好きなお名前を入れますよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、お返しと、こちらが商品です。"
    extend "ありがとうございます」"
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「すいませーん」"
    $ kag_cm()
    $ kag_playse('1-0188.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はーい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('子ども「')
    "子ども「わ～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "昨日はまわれ右ばっかりだったけど、今日はお客さんの入りもいい感じ。"
    $ kag_cm()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん、はいお水」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0189.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ありがとう、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_stopbgm()
    $ kag_playse('se-021.ogg', buf=0, loop=False)
    $ kag_wait(1000, canskip=True)
    $ kag_cm()
    $ kag_stopse(buf=0)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('up', 'black', time_ms=100, bgcolor='0x000000')
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_mesframe()
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('up', 'bg002', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0190.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんっ、大丈夫！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いたたた……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('子ども「')
    "子ども「うあああああああ～～～ん」"
    $ kag_cm()
    $ kag_set_next_indent('親「')
    "親「まぁ、ぼうや～！」"
    $ kag_cm()
    $ kag_set_next_indent('親「')
    "親「ぼうや、大丈夫？痛いとこはない？」"
    $ kag_cm()
    "どうやら、どれみちゃんにお水をわたす時に、\n子どもが後ろからぶつかってきたようだ。"
    $ kag_cm()
    "近くにわたしのメガネと、コップが転がっていた。"
    $ kag_cm()
    $ kag_set_next_indent('親「')
    "親「ちょっと！"
    extend "あなたがボサっと立ってるからぼうやが転んじゃったじゃないの！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ご、ごめんなさい！"
    extend "\nでも、その子が……」"
    $ kag_cm()
    $ kag_set_next_indent('親「')
    "親「なによ、うちの子のせいだっていうの？」"
    $ kag_cm()
    $ kag_set_next_indent('子ども「')
    "子ども「おねえちゃんがぶつかってきたの……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんな……」"
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0191.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、ケガはない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、うん」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('親「')
    "親「客の心配をする方が先でしょ！"
    extend "そんな安っぽいメガネを落としたくらいでおおげさよ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「安っぽい……」"
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0192.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ちょっと！{w=0.4}そんな言い方って{w=0.4}{nw}"
    $ kag_freeimage(layer='0', page='fore')
    extend "モゴモゴ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0053.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃん、おさえて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('親「')
    "親「まったくドジね！"
    extend "こんな子さっさとクビにしなさいよ！！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ、ああ……」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0193.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('sepia', 'bg067', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b3_d__dash__03_02:
    $ kag_set_bookmark('「３日目」思い出と公園')
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｂ「')
    "魔女Ｂ「まったくドジね、あの子は……」"
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｃ「')
    "魔女Ｃ「ほんと、お仕事失敗ばかりしているわね。"
    extend "\nお使いに行っても道に迷うばっかりだし」"
    $ kag_cm()
    $ kag_set_next_indent('魔女Ｂ「')
    "魔女Ｂ「なんであんな子が仕事してるのかしら。"
    extend "\nさっさとクビにしちゃえばいいのに……」"
    $ kag_cm()
    $ kag_changetype('cross', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_cm()
    $ kag_mesframe()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし……{w=2}クビ……」"
    $ kag_cm()
    "魔女界でのイヤな思い出が、くり返し頭の中をよぎる。"
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0194.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、しっかりして！{w=0.3}りずむちゃん！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしっ、わたし……」"
    $ kag_cm()
    $ kag_playse('1-0195.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ごめんなさい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃん、ここはあたしらにまかせてりずむちゃんを！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0196.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、あいちゃん、わかった！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-021.ogg', buf=1, loop=False)
    $ kag_wait(1000, canskip=True)
    $ kag_cm()
    $ kag_set_next_indent('親「')
    "親「ちょっと？わたしたちは客よ？"
    extend "客より店員を大事にするなんてどういう店なのかしら？」"
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_drawchar('a_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「くぅ～！{w=0.4}もうアタマにきたでぇ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0052.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「だめ！{w=0.3}あいちゃんいけないわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやかて、このままやったら腹の虫がおさまらん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0058.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしにまかせて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0054.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おんぷちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0059.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お客さま、大変失礼いたしました。{w=0.45}お子さんにおけがはありませんか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('親「')
    "親「た、大したことはないわ」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0060.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうですか。{w=0.45}ところで、わたしずっと見てたんですけど、"
    $ kag_playse('4-0060.2', buf=0, loop=False)
    extend "りずむちゃんにぶつかってきたのは、お子さんの方でしたよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('親「')
    "親「何を言うの！"
    extend "あの子がつっ立ってるから……」"
    $ kag_cm()
    $ kag_playse('4-0061.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「こんなお店の中でかけまわったら、あぶないとは思いませんか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('親「')
    "親「でも子どもって、じっとしてないものでしょ！{w=0.3}だったら……」"
    $ kag_cm()
    $ kag_playse('4-0062.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「では、かけまわるお子さんのために、お店のたなも柱もどかせましょうか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('親「')
    "親「そこまで言ってないわよ！"
    extend "こんな店もう２度と来ないわよ！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-009.2.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_playse('se-031.2.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0063.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ありがとうございました」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('はづき「')
    "はづき「……」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……」"
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0040.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ほへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0055.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おんぷちゃん、カッコイイ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「しびれんな～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0064.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えへ！{w=0.45}こないだ見たドラマで、同じセリフを言ってたからマネしちゃった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0053.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃんとりずむちゃん、\nどこまで行ったのかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0041.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「よ～し、ハナちゃんも行く～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まって！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0042.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どぉして止めるの！{w=0.4}どれみたちのこと心配じゃないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0078.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「心配やけど、ここはどれみちゃんにまかせよう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0054.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「大丈夫よハナちゃん、どれみちゃんを信じてわたしたちは待ちましょう、{w=0.5}ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0043.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん……{w=0.6}わかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0056.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ねぇ～{w=0.45}ちょっとGood idea！があるんだけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0079.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なに？ももちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0057.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あのね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg096', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b3_d__dash__03_04:
    $ kag_set_bookmark('「３日目」思い出と公園')
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0197.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、どこ！？{w=0.4}どこに行ったの！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg061', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0198.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0199.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もしかしたら……」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_d_b3_d__dash__03_05:
    $ kag_set_bookmark('「３日目」思い出と公園')
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg087', time_ms=1500, bgcolor='0x000000')
    $ kag_cm()
    $ kag_cm()
    $ kag_playbgm('bgm-004', loop=True)
    $ kag_wait(2000, canskip=True)
    $ kag_mesframe()
    "り～ん、り～ん"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「虫さんは、ひとりでさみしくないの……？」"
    $ kag_cm()
    "り～ん、り～ん"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    "りんりん～"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そっか……虫さん、ひとりじゃないんだ。"
    extend "わたしは……」"
    $ kag_cm()
    "り～んり～ん"
    $ kag_cm()
    "…………"
    $ kag_cm()
    $ kag_playse('1-0200.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ここにいたんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '01どれみ-03.tlg', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgd2=1
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ど、どれみちゃ……{w=0.65}ん……」"
    $ kag_cm()
    $ kag_playse('1-0201.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どうしたの？{w=0.3}急に飛び出したりして」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし……{w=0.6}うっ……{w=0.6}ひっく」"
    $ kag_cm()
    $ kag_set_next_indent('どれみ「')
    "どれみ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううっ……{w=0.65}ごめんなさい……」"
    $ kag_cm()
    $ kag_playse('1-0202.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしでよければ、相談にのるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg087', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b3_d__dash__03_06:
    $ kag_set_bookmark('「３日目」思い出と公園')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしね、小さい頃よくこうしてブランコで遊んでいたの……」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0203.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ブランコで？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん、ブランコって、ひとりでも遊べたから……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0204.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「さっきはお店で取り乱しちゃって……{w=0.65}ごめんなさい」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0205.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんな、気にすることないよ！{w=0.4}誰だってあんなこと言われたらさぁ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「同じことを言われたの……」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0206.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔女界で仕事をしていた時なんだけど」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0207.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「『あんな子さっさとクビにしなさいよ』って、かげ口を言われたことがあったの」"
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0208.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしみたいな魔女、いらないって言ってるのといっしょですよね？それって」"
    $ kag_cm()
    $ kag_set_next_indent('どれみ「')
    "どれみ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、先輩魔女や、あのお客さんの言うこともわかります」"
    $ kag_cm()
    "りずむ「わたしが、魔法で何でもうまくできる子だったらよかったのに」"
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0209.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それはちがうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_d_b3_choices_d01:
    $ kag_set_bookmark('どれみシナリオ選択肢01')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】わたしがドジさえしなければ', current_stem='d_b3', storage=None, target='*choices_d01-01', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】わたしがいなければ', current_stem='d_b3', storage=None, target='*choices_d01-02', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_d_b3_choices_d01__dash__01:
    $ kag_cm()
    $ kag_f.judgeflag=1
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしがドジさえしなければ、みんな困らなくてすむのに」"
    $ kag_cm()
    jump kag_d_b3_after_choices_d01
    call kag_s_wait

label kag_d_b3_choices_d01__dash__02:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしがいなければ、みんなを巻き込むこともなかったのに」"
    jump kag_d_b3_after_choices_d01
    call kag_s_wait

label kag_d_b3_after_choices_d01:
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「今日だって、どれみちゃんにお水を持っていくだけで、こんな大さわぎになっちゃうし、"
    extend "ホントにドジばっかりで、自分がイヤになっちゃう」"
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0210.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなのちがう！{w=0.4}絶対にちがう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('1-0211.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなのドジとかじゃなくて、自分ひとりでかかえこんじゃってるだけじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは……」"
    $ kag_cm()
    $ kag_playbgm('m413a', loop=True)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0212.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしね、魔法でドジが直ったらいいのにって、思ってたことあるんだ。{w=0.4}りずむちゃんが言ったみたいに」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0213.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「道を歩いているだけでも、家でテレビを見ているだけでも、おかしなことになっちゃって、みんなに迷惑かけて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ……{w=0.6}それはすごい、かも」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0214.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でしょ？{w=0.4}それにくらべたら、りずむちゃんなんてあたしの足もとにもおよばないよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}そうですね」"
    $ kag_cm()
    $ kag_playse('1-0215.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「元気出しなよ。{w=0.4}人間だって魔女だって、ついてない時くらいあるんだからさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}使わなかったんですか？{w=0.4}魔法」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0216.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ドジが直る魔法は、使わなかったんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0217.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうして？」"
    $ kag_cm()
    $ kag_playse('1-0218.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんなが今でも友だちでいてくれるから、それでいいのかなって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}わたし、ずっと友だちがいなかったから、よくわからないです」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0219.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしたちがいるじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_playse('1-0220.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしたちと、イヤなことを全部忘れちゃうぐらい、楽しい思い出をた～くさん作ろうよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「楽しい思い出？」"
    $ kag_cm()
    $ kag_playse('1-0221.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そ！{w=0.45}これからも～っと！楽しいことをいっぱいして、楽しい思い出だらけにしちゃえばいいんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0222.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしはもうあるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0223.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「思い出。{w=0.45}りずむちゃんといっしょにアクセサリー作ったり、いっしょにクッキーを食べたり……{w=0.65}あたしは楽しかったよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.55}わたしも……{w=0.65}です」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0224.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「きっと明日は、いいことあるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0225.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃ、元気になったところで、ＭＡＨＯ堂にかえろう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、なんか、ちょっと照れくさいです……」"
    $ kag_cm()
    $ kag_playse('1-0226.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だ～いじょうぶだって！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)

label kag_d_b3_d__dash__03_07:
    $ kag_set_bookmark('「３日目」思い出と公園')
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0227.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「さぁ、入ろう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg021', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('se-009.2.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0228.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「たっだいまぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ、その……{w=0.65}ただいまです……」"
    $ kag_cm()
    $ kag_sound_se('se-034.ogg', buf=1)
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わっ」"
    $ kag_cm()
    $ kag_playse('1-0229.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おお！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「これは……」"
    $ kag_cm()
    $ kag_playbgm('m14', loop=True)
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0080.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おかえり！{w=0.4}りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0058.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あのね！{w=0.3}遅くなっちゃったけどね、\nこれからりずむちゃんの『ようこそ！ＭＡＨＯ堂へ！』歓迎会ひらくんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0055.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「本当は、来てすぐやりたかったんだけど、なんかあわただしかったから……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0065.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「今日開くことにみんなで決めたの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0044.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんとぽっぷが、もものお手伝いをしてケーキつくったんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0009.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えへへ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0230.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ほら、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.7}はい……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('sepia', 'bg087', time_ms=1500, bgcolor='0x000000')
    $ kag_frmdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('1-0231.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんなが今でも友だちでいてくれるから、それでもいいのかなって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg021', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしも、そう思いました」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0232.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何でもないです」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0233.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃ、りずむちゃん、ＭＡＨＯ堂へようこそ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('A-0014.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「かんぱーい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.d3_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_d_b4_gamestart
    return
