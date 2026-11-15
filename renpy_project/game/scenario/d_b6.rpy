# Auto-generated from 01. doremi/d_B6.ks by tools/transpile_ks.py
label kag_d_b6:

label kag_d_b6_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_doremi.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg007', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_d_b6_d__dash__06_00:
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0337.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はいはい！あたしが行く！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃあ、わたしも行きます！」"
    $ kag_cm()
    "午後になって、ＭＡＨＯ堂に来たどれみちゃんといっしょに、商店街に行くことになった。"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0118.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃん珍しいなあ。いつもやったら麦茶飲んで『しあわせ～』とか言ってる時間やのに」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0338.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そ、そんなことないよ。{w=0.3}あたしはいつもどおりさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0078.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「昨日の宿題が間に合って、お買い物気分なんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そんなものなのかしら……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0339.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうそう。午前中出られなかった分、みんなの役に立ちたいって、せめてもの心づかいってヤツ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0086.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なんかひっかかるんだけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0340.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「気にしない気にしない。{w=0.4}それじゃ、いってくるね！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いってきます」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0119.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「気ぃつけてな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0079.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「いってらっしゃ～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0087.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いってらっしゃい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0078.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん、くれぐれも寄り道しちゃだめよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0341.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いやだなぁ～はづきちゃん。そんなのわかってるさぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg088', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b6_d__dash__06_01:
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「商店街って、人やお店がいっぱいですね」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0342.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「特にこの時間は、お母さんたちが多いんだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この時間って決まってるんですか？」"
    $ kag_cm()
    $ kag_playse('1-0343.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「晩ごはんの支度があるからね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、なるほど」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0344.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ささ、ちゃっちゃと買い物をすませて、福引きしよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「福引き……{w=0.5}って、なんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0345.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今ここの商店街でやってるくじのことだよ。{w=0.55}買い物した金額が多ければ多いほど、いっぱいくじが引けるんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なにか、景品とかがもらえるんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0346.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうそう、その景品がね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0346.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「む！このニオイは！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あのガラガラと音がするのが福引きですね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0347.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ステーキだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしもやってみたいな～{w=1}\n……あれ？"
    extend "どれみちゃん？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ひとりになっちゃった……」"
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg089', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b6_d__dash__06_02:
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん、どこ行っちゃったんだろう」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0085.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あれ？{w=0.4}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！ぽっぷちゃん」"
    $ kag_cm()
    $ kag_playse('7-0086.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「こんなところでどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、どれみちゃんとはぐれてしまって」"
    $ kag_cm()
    $ kag_playse('7-0087.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねえちゃんと？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。"
    extend "たくさん人がいたところでその、見失ってしまって……」"
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0088.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「しょうがないなあ。{w=0.5}どうせおねえちゃんのことだから、勝手にはぐれちゃったんだよ、きっと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな、わたしが福引きに見とれちゃってたから」"
    $ kag_cm()
    $ kag_playse('7-0089.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ううん、悪いのはおねえちゃんだって！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はあ」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0090.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ちょっとだけなら時間あるから、いっしょにさがすの手伝ってあげるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみません……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg090', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b6_d__dash__06_03:
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0091.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「いないねぇ～、おねえちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どこに行ったんでしょうか……」"
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0092.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あっ！！りずむちゃんごめん！{w=0.3}もうデートに行かなくっちゃ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「で、デート？」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0093.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そう！みさき君とね。{w=0.4}それじゃ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ、ぽっぷちゃん？」"
    $ kag_cm()
    $ kag_playse('7-0094.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねぇちゃんなら大丈夫だよ～！{w=0.45}おなかがすいたら帰ってくるって！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな、おなかがすいたらって……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg045', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b6_d__dash__06_04:
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「困ったなぁ。どうしよう？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「『ステーキだー！』って言ってた気がするけど……」"
    $ kag_cm()
    $ kag_set_next_indent('おやじ「')
    "おやじ「おめでとうございまーす！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんだろう？」"
    $ kag_cm()
    $ kag_drawchar('t_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0025.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「オーッホッホッホッホッホ！当然の結果ですわ！{w=0.45}それで、なにが当たったんですの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おやじ「')
    "おやじ「はい、お嬢ちゃん」"
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0026.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「……お食事券？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おやじ「')
    "おやじ「そう！３等ステーキハウスお食事券！"
    extend "１回限り４名様までご招待！」"
    $ kag_cm()
    $ kag_drawchar('t_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0027.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ってこのお店、ワタクシの叔父さまの店じゃありませんの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ、玉木さん？」"
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0028.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あら？{w=0.4}あなたはたしか……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「りずむです」"
    $ kag_cm()
    $ kag_playse('8-0029.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「そうそう、そのりずむさん、こんなところでお会いするなんて、奇遇ですわね。{w=0.3}お買い物かしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですけど、あの、実は……」"
    $ kag_cm()
    "…"
    extend "\n…"
    extend "\n…"
    extend "\n{nw}"
    $ kag_cm()
    $ kag_drawchar('t_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0030.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「まったく春風さんときたら、仕方ないですわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「玉木さん、どれみちゃんが行きそうな所って、知ってますか？」"
    $ kag_cm()
    $ kag_playse('8-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「う～ん。{w=0.6}春風さんのことですから、どうせステーキのにおいにでもつられて……{w=0.5}{nw}"
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    extend "あ！そうですわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('8-0032.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「りずむさん、あなたステーキは好き？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「す、ステーキですか？」"
    $ kag_cm()
    $ kag_playse('8-0033.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「さっき当たったこのお食事券で、ステーキハウスに行って春風さんをさがしますわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ？」"
    $ kag_cm()
    $ kag_playse('8-0034.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ほら、行きますわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ、玉木さん！まってくださ～い！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg046', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b6_d__dash__06_05:
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0035.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「こんにちは。おじ様」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('マスター「')
    "マスター「おや麗香ちゃん。"
    extend "いらっしゃい」"
    $ kag_cm()
    $ kag_playse('8-0036.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「商店街の福引きでこれが当たりましたの。{w=0.4}せっかくだから、お友だちとごちそうになりに来ましたわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('マスター「')
    "マスター「そうかそうか。"
    extend "じゃあすぐに用意するからね」"
    $ kag_cm()
    $ kag_playse('8-0037.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「さ、りずむさん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。"
    extend "失礼します」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg046', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b6_d__dash__06_06:
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_drawchar('t_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0038.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「そこでこのワタクシの登場ですわ！{w=0.4}困ってる方を見過ごすわけにはまいりませんから～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あは、そうですねぇ～」"
    $ kag_cm()
    $ kag_playse('8-0039.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「もういろんな所からのお誘いを断るだけで、大変なんですのよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええと、その、どれみちゃんは……？」"
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0040.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「りずむさん。{w=0.45}心配しなくても、こうしてここで張り込んでいれば、きっと春風さんはやって来ますわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なるほど……{w=0.65}さすが玉木さんですね！」"
    $ kag_cm()
    $ kag_drawchar('t_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0041.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「それほどでもありますわよ。{w=0.55}オーッホッホッホ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('店員\u3000「')
    "店員　「お待たせしました」"
    $ kag_cm()
    $ kag_playse('se-017.ogg', buf=1, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわぁ、おいしそう～！」"
    $ kag_cm()
    $ kag_playse('8-0042.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「今焼いたステーキのにおいをかぎつければ、春風さんはいても立ってもいられませんわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「においってそんな、犬みたいな……」"
    $ kag_stopse(buf=1)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '01どれみ-06', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgd4=1
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_playse('1-0348.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「くんくんくん……{w=0.55}ああ、シアワセ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0349.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はっ！そうだ、りずむちゃん探さなきゃ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0350.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それにしても、ステーキはやっぱりいいにおいだな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0351.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いやいや！りずむちゃんが先！{w=0.4}がまんがまん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg046', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_playse('se-017.ogg', buf=1, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.7}どれみちゃん、来ませんね」"
    $ kag_cm()
    $ kag_drawchar('t_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0043.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「おかしいですわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-012.1.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ……」"
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0044.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「気合いが足りませんわよ。{w=0.5}これは、あくまでも春風さんを呼び寄せるためにやってるんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ごめんなさい……{w=0.65}ステーキってはじめて見たんですけど、とってもおいしそうで」"
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0045.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「まあ、そうでしたの？ワタクシはもうあきあきしてるくらい食べてますわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいなあ～」"
    $ kag_cm()
    $ kag_drawchar('t_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0046.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「そりゃあもう小さい頃から……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-012.2.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('t_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あのぉ……{w=0.65}玉木さん？」"
    $ kag_cm()
    $ kag_wait(1500, canskip=True)
    $ kag_drawchar('t_04.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('8-0047.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「いただきますわよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、ええ？"
    extend "どれみちゃんは？」"
    $ kag_cm()
    $ kag_playse('8-0048.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「これだけ待っても来ないんだから、食べながら別の作戦を考えますわよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ\t「')
    "りずむ	「は、はあ」"
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0049.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「さあ、早く食べないと、せっかくのレアが台なしですわ」"
    $ kag_stopse(buf=0)
    $ kag_stopse(buf=1)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '01どれみ-06', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_playse('1-0352.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はあ～{w=0.35}ひとくちだけでも食べたいな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0353.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ダメダメ！まだりずむちゃんが見つかってないじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0354.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でもこの香り……{w=0.5}はあ～シアワセ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0355.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ああ～困ったあ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg090', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、おいしかった……{w=0.5}しあわせ……」"
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0050.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「それではりずむさん、失礼いたしますわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、ごちそうさまでした」"
    $ kag_cm()
    $ kag_drawchar('t_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0051.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「いいってことですのよ！それではまた」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「人間界に、こんなにおいしい食べ物があったなんて……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はっ！{w=0.3}どれみちゃん、さがしてたんだっけ」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「別の作戦なんて、ぜんぜん考えてなかった……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg202', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b6_d__dash__06_07:
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「やっぱり見つからないな……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「しょうがない、１度ＭＡＨＯ堂に戻ろう……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('se-009.1.ogg', buf=1, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ただいま……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0088.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あっ、おかえり」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0080.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おかえり」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0120.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あれ？りずむちゃんひとり？{w=0.35}どれみちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それがその、はぐれちゃって……」"
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0121.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はぐれた～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0079.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どこではぐれたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それが……」"
    $ kag_cm()
    "…"
    extend "\n…"
    extend "\n…"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}というわけなんです」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0122.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なるほど、だいたい事情はつかめたけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0080.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でも、なんで突然どれみちゃんいなくなっちゃったのかしら？」"
    $ kag_cm()
    $ kag_playse('2-0080.2', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「玉木さんの言うとおり、ステーキのにおいに誘われて、なんてちょっと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0081.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「いくらなんでも～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0089.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうよ、ねぇ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0123.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほんまや～いくらなんでもそれは～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0082.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「犬じゃないんだしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0090.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あははは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-006.2.ogg', buf=1)
    $ kag_playbgm('m39', loop=True)
    $ kag_drawchar('d_05.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('1-0356.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハア、ハア、りずむちゃんいる！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん！」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0357.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「よかった～。\nりずむちゃん、ごめん！ホントにごめん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、いえ。{w=0.4}わたしもあちこち歩いてしまったから」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0358.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんな、あたしがついうっかり、{w=1}{nw}"
    $ kag_drawchar('d_05.tlg', time_ms=100, sepia=False, canskip=True)
    extend "ス……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0083.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ス？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0359.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ス、ステーキのにおいにつられて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0126.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うっは！やっぱりか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0082.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん！\n寄り道しちゃダメって言ったじゃない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0360.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「すいません……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん、そんなに怒らなくても……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0127.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なんにせよ、りずむちゃんが無事帰ってこれたんやからええやん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0084.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0092.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ところでどれみちゃん、お買い物は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0361.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まだ……{w=0.55}してません」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……」"
    $ kag_cm()
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('はづき「')
    "はづき「……」"
    $ kag_cm()
    $ kag_drawchar('a_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0128.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それやったら、ひとっ走り行ってこんかい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0362.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はい～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしも行きます！」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0083.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「今度ははぐれないようにね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b6_d__dash__06_08:
    $ kag_set_bookmark('「６日目」迷子とステーキと')
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0363.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホントにごめんね、りずむちゃん。けっこう探しまわった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん。{w=0.35}途中で玉木さんに会って、どれみちゃんを見つけるために、張り込みをしてたから」"
    $ kag_cm()
    $ kag_drawchar('d_07', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0364.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「張り込み？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ。それでステーキハウスで……」"
    $ kag_cm()
    "…"
    extend "\n…"
    extend "\n…"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0365.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えええ～？そうだったの？……{w=0.5}で、まさか食べたの？ステーキ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はじめて食べたけど、とってもおいしかったです！」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0366.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いいなあ～。{w=0.5}な～んだ～お店の中にいたんだあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でもそれって、玉木さんが当てた福引きの景品なんですよ。無料お食事券」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0367.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「玉木が当てたの！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0368.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「くうう～こうしちゃいられない！りずむちゃん、もう１回当てるよ！{w=0.5}そのための買い物なんだから！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、そんなに当たるものなんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0369.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしのラッキーとりずむちゃんのラッキーを合わせたら、絶対当たるって！{w=0.35}さ、行こ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0370.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今度こそ、ステーキ食べるぞ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.d6_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_d_b7_gamestart
    return
