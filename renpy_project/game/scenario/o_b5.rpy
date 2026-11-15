# Auto-generated from 04. onpu/o_B5.ks by tools/transpile_ks.py
label kag_o_b5:

label kag_o_b5_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_onpu.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg001', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_o_b5_op__dash__05_00:
    $ kag_set_bookmark('「５日目」仕事とおんぷ\u3000りずむの気持ち')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0787.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それでさぁ～、あの告白のシーンがもう最高で……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんが熱っぽく語っている。"
    extend "\nどうやら、昨日の夜に見たドラマの話をしているようだ。"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0777.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「へぇ、そうなんや～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0777.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「しかしめずらしいなぁ、どれみちゃんがバトルレンジャー以外のＴＶでこんなに熱く語るなんてな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_12.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0788.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もう～！{w=0.4}あいちゃんたら失礼しちゃう！{w=0.4}あたしだって夢見るオトメなんだよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0789.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「夕焼けの海岸で、ヒロインに告白する主人公。{w=0.4}そして抱きしめあう２人……"
    $ kag_playse('1-0789.2', buf=0, loop=False)
    extend "あぁ～もう最高だよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あははははは……」"
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0535.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「またどれみちゃんのテレビ病が出ちゃったわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0790.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「『わたし、あなたががんばってるのずっと見てた』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0791.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「『僕……{w=0.55}今までずっと失敗ばかりで……{w=0.5}そんな自分がいやで、ずっとウジウジしてた』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0792.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「『でも、君のおかげで、やっと前に進むことができそうなんだ』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0793.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「『君が支えてくれたおかげで、いろんなことを教えてくれたおかげで……』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0794.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そして２人はあつい口づけを……{w=0.6}あああ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0778.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ちょ、ちょっとどれみちゃん。{w=0.4}あたしに口づけしてどないすんの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0795.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいこ！{w=0.4}もうお前をはなさない！{w=0.4}あいこおおお！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0779.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ぎゃああ～！{w=0.4}どれみちゃんタンマタンマ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-022.ogg', buf=1, loop=False)
    $ kag_drawchar('hn_03.tlg', time_ms=300, sepia=False, canskip=True)
    $ kag_playse('6-0268.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみとあいこ、おっかけっこしてる～。{w=0.4}ハナちゃんもやる～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-022.ogg', buf=1)
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0796.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「僕たちの前に道はない！{w=0.4}さあ、共に目指そう！{w=0.4}あの正義の星に向かって！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0780.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなセリフあるわけないやろ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃんすごい。{w=0.4}迫真の演技ですね……」"
    $ kag_cm()
    $ kag_drawchar('a_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0781.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「演技やない、本気やっちゅ～ねん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0536.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう～みんな、仕事してよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg005', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b5_op__dash__05_01:
    $ kag_set_bookmark('「５日目」仕事とおんぷ\u3000りずむの気持ち')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0797.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はあ～。{w=0.4}やっぱり女の子ならさ、１度はあんな風に告白されたいよねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0236.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「はいはい……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0782.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃ～ん、そろそろ現実に戻ってきいや～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0389.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ふふっ。{w=0.4}どれみちゃん、知ってる？{w=0.4}あのシーンって、実はこの美空市の海岸で撮影したのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0798.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ええっ！{w=0.4}本当！？{w=0.4}美空市の海岸って、あの海岸？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0390.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0799.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そっか～……{w=0.55}あんな壮大なラブロマンスが、この美空市で……{w=0.5}じゃあじゃあじゃあ、あの海岸に行けば、{w=0.4}あたしもラブロマンスに出会えるってことだよね！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0783.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、ドラマやし……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0237.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「海岸だけじゃなくて、町のいろんなところがロケ地になってるみたいだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0391.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「プロデューサーの奥さんとのなれそめが、その海岸だったんだって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0800.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おおお～！{w=0.4}それを聞くと毎日通っちゃいそうだよあたし～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0537.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「おんぷちゃん、よくそんなこと知ってたわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0392.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えっ？{w=0.4}うん、まぁね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、美空市の海岸って、{w=0.4}この近くに、海があるんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0784.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0238.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「近くって言うほどすぐそばじゃないけど、ほうきならすぐだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだったんですか……{w=0.6}へぇ、海かぁ……」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0269.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、海行きたいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？{w=0.4}えっと、その……」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0270.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんは行きたいな～{w=0.4}海うみ、う～み～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしも、行ってみたいな……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0801.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあさ、これからみんなで行こうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0538.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0802.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そろそろ今日のお仕事も終わりだしさ。{w=0.4}この時間からじゃ泳げないだろうけど、遊ぶだけならできるじゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0785.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「とか何とか言うて。{w=0.4}ホンマはカッコイイ男の子探したいだけちゃうん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0803.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もちろん！{w=0.4}夕日の海岸で見つめ合う２人……{w=0.55}ああ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0239.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしも見てみた～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0786.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まあ、あたしも興味ないことないけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0804.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それにほら、あのプロデューサーにあやかるためにも……！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0787.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あまり、あてにならへんと思うけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0539.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃ、みんなで行ってみましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0393.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いいんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0240.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「賛成！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0271.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「さんせ～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それじゃ……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0805.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「海に向けて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0038.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「しゅっぱ～つ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg081', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b5_op__dash__05_02:
    $ kag_set_bookmark('「５日目」仕事とおんぷ\u3000りずむの気持ち')
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('se-014.2.ogg', loop=True)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0272.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「海だ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ……{w=0.65}広～い！{w=0.4}それにきれい……」"
    $ kag_cm()
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0540.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ほんと、波がきらきらしてきれいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0806.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やっぱ海はきれいだねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0241.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ロケをやってたのってあの辺かな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0807.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え、どこどこ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0273.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あははは～どれみ～もも～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-029.1.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0242.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ひゃあ！{w=0.4}ハナちゃん、冷たいよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0808.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハ～ナ～ちゃ～ん。{w=0.4}それぇ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0274.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あはははは、それそれ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-029.3.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0788.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もう、ハナちゃん、どれみちゃん、びしょぬれやんか～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ、おんぷちゃん、どこへ行くんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0394.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ちょっとその辺りを散歩しようかと思って……{w=0.55}りずむちゃんも来ない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、行きます」"
    $ kag_cm()
    "わたしたちとおんぷちゃんは、海岸線を歩き出す。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg212', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b5_op__dash__05_03:
    $ kag_set_bookmark('「５日目」仕事とおんぷ\u3000りずむの気持ち')
    $ kag_cm()
    $ kag_playbgm('se-014.1.ogg', loop=True)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0395.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「気持ちいい……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「風が涼しいですね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('4-0396.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんの話してたドラマね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0397.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんの話してたドラマね、{w=0.4}主人公は、仕事で失敗を続けてて、{w=0.4}ヒロインがそんな主人公を支え続けて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ」"
    $ kag_cm()
    $ kag_playse('4-0398.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「主人公は、そんな自分をなさけなく思いながらも、{w=0.4}ヒロインのおかげでがんばることができて、{w=0.4}思い出の砂浜で告白するの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "仕事で失敗続きの主人公……何だかわたしみたい。"
    $ kag_cm()
    $ kag_playse('4-0399.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「実はね。{w=0.4}ヒロイン役のオーディション、わたしも受けたんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0400.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「だけど、{w=0.4}年齢が若すぎるからって、落ちちゃったの……{w=0.6}こればっかりはどうしようもないことなんだけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだったんだ……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃんたちは、{w=0.4}オーディションに落ちちゃったことって、知ってるんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0401.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ううん。話してない。{w=0.4}みんなの中で知ってるのは、りずむちゃんだけ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('4-0402.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ステキなお話だったし、{w=0.4}やってみたかったんだけどな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0403.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「『わたし、あなたががんばってるのをずっと見てた』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、えっ！？」"
    $ kag_cm()
    "な、なんの話？\nわたしががんばってたの見てたって？"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0404.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ふふっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0405.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「これ、ドラマのヒロインのセリフなの。{w=0.4}オーディションのときしゃべったのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そ、そうだったんだ……」"
    $ kag_cm()
    $ kag_playse('4-0406.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「この後、主人公は自分の気持ちをヒロインにぶつけて、{w=0.4}過去を振り返って、そしてヒロインに告白するの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0407.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、アドリブでいいから、{w=0.4}主人公役やってみてよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、ええっ！？」"
    $ kag_cm()
    "突然そんなことを言われても……"
    $ kag_cm()
    $ kag_playse('4-0408.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ほら、こっちに来て」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0409.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いい？{w=0.4}主人公はまず、過去に失敗してきたことを振り返るの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0410.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも、これからは前向きになると決めて、{w=0.4}今まで支えてくれたヒロインに告白をする」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0411.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「こんな流れね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0412.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあいくわよ……{w=0.55}{nw}"
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    extend "『わたし、あなたががんばってるのをずっと見てた』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "さっきと同じセリフだ。"
    extend "\nじっと主人公を、わたしを見つめながら……"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの、わたし……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0413.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はい、カーット」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0414.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、これはお芝居だってば」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0414.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんは主人公……{w=0.5}男の人の役なんだから、{w=0.4}ちゃんと『僕』とか『俺』とかって言わなきゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0415.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあもう一回ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0415.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「『わたし、あなたががんばってるのをずっと見てた』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「『僕……{w=0.6}今までずっと失敗ばかりで……{w=0.55}そんな自分がいやで、{w=0.4}ずっとウジウジしてた』」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('りずむ「')
    "りずむ「『でも、君のおかげで、やっと前に進むことができそうなんだ。{w=0.4}君が支えてくれたおかげで……{w=0.6}いろんなことを教えてくれたおかげで……』」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だから、だからわたし、{w=0.4}もっとがんばってみたいの……」"
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0415.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えっ！？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今までお仕事とかで失敗すると、すぐ落ち込んじゃって。{w=0.4}どうしていいかわからなくなっちゃって」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、時間は待ってくれない。{w=0.4}お仕事は自分の気持ちと関係なく進めなくっちゃいけない」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0416.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ドラマのように、うまくできるかわからないけど……{w=0.65}わたし、{w=0.4}がんばっていこうって思ってます。{w=0.4}少しでもおんぷちゃんに、みんなに近づいて……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg209', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "今なら、今だけなら、言えるかもしれない。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みんなと、友だちになりたい……」"
    $ kag_cm()
    $ kag_wait(1000, canskip=True)
    $ kag_playse('4-0417.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「『わたしでよければ、そばにいるよ』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg212', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0418.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「クス、ちがうでしょ。{w=0.4}わたしはヒロイン役なんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0419.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そっか～。{w=0.4}りずむちゃん、ずっとそんなこと考えてたんだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、お、お、おんぷちゃん！」"
    $ kag_cm()
    "我に返ったわたしは、耳まで赤くなってしまった。"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0420.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ、それじゃあこの間言ってた『弟子入り』は、取り消しでいいよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0421.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「だって『師匠』と『弟子』じゃ、友だちになれないじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.6}はい、そうですね」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0422.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあ、決まりね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "もう言ってしまった後なんだけど、心臓はドキドキしているまんまだった。"
    $ kag_cm()
    "みんなに自己紹介する時と、ううん、それ以上ドキドキしている。"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0423.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしがオーディションに落ちたのって、年齢だけじゃないのかもね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}それって……？」"
    $ kag_cm()
    $ kag_playse('4-0424.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんの目。{w=0.4}まっすぐわたしに向けられてた。"
    $ kag_playse('4-0424.2', buf=0, loop=False)
    extend "こんな風に告白されるってこと、今までなかったから、びっくりしちゃった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ああああ、あの、その、か、からかわないでください。わたし……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0425.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わかってるわ。{w=0.4}誰かから、本気の気持ちを聞くことって、めったにないじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0425.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「オーディションの時には、ちょっと忘れてたかなって思ったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.5}わたし、こんなこと誰かに言ったの、初めてです」"
    $ kag_cm()
    $ kag_playse('4-0426.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしたちは、最初からりずむちゃんのこと、友だちだと思ってたけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0427.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「もちろんよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとう……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0809.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おお～い！{w=0.4}おんぷちゃ～ん！りずむちゃ～ん！{w=0.4}こっちにおいでよ！{w=0.45}いっしょにあそぼぉ～よ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0429.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いこっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}あ、そうだ」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0430.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なに？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃんが最後に言ったセリフ、あれも台本通りなんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0431.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なんて言ったかしら？{w=0.4}わたし覚えてな～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ず、ずるいです！」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0432.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたし知～らない。{w=0.4}先に行ってるわよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「ま、待ってくださ～い」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.o5_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_o_b6_gamestart
    return
