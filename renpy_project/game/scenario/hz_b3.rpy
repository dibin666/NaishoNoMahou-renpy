# Auto-generated from 02. hazuki/hz_B3.ks by tools/transpile_ks.py
label kag_hz_b3:

label kag_hz_b3_gamestart:
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

label kag_hz_b3_hz__dash__03_00:
    $ kag_set_bookmark('「3日目」りずむの習い事－ＭＡＨＯ堂（中２Ｆ）')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0202.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん。{w=0.4}そのビーズとって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('2-0203.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うん。{w=0.3}こんな感じかしら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「キレイですね～」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0204.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「最初のうちは、あまり色をふやさない方がキレイにできるのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わかりました。ところではづきちゃんは、マジョリカさんにアクセサリーの作り方を習ったんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0205.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ううん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、それじゃ他の人に習ったんですか？」"
    $ kag_cm()
    $ kag_playse('2-0206.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「はた織りだけはマジョクロスの所へ教わりに行ったけど」{nw}"
    $ kag_wait(350, canskip=True)
    $ kag_waitclick()
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0206.2', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「だいたいはとりあえずやってみてからコツをつかんだりって感じだから、誰かに習ったってわけじゃないのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すごいですね。わたしはてっきり誰かに習うものだって思ってました」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b3_hz__dash__03_01:
    $ kag_set_bookmark('「3日目」りずむの習い事－ＭＡＨＯ堂（１Ｆ）')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "お昼過ぎになり、３時のおやつにはまだ早いんだけど、みんなちょっとだけ休憩モード。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん。{w=0.4}今日持ってきたそれは何ですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0207.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？ああ、これはバイオリンよ。{w=0.4}ほら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントだ」"
    $ kag_cm()
    $ kag_playse('2-0208.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「夕方にレッスンがあるから、持ってきたのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「バイオリンを習ってるんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0209.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいなあ。{w=0.4}楽器が演奏できるって、ちょっとうらやましいです」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0210.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そ、そんなに大したことじゃないわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なにか弾いてみてもらえませんか？」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0132.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はづきやってやって～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0211.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え、そう？じゃあ、ちょっとだけ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-001.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_resumebgm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0133.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おお～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「す、すごーい！」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0212.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それほどでも……{w=0.55}りずむちゃんもやってみる？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、わたし、バイオリンどころか、小さい頃に幼稚園のおゆうぎでカスタネットを叩いたくらいで……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0213.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「何ごともチャレンジよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はあ。それでは」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっと、こんな感じですか？」"
    $ kag_cm()
    $ kag_playse('2-0214.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もうちょっとバイオリンを持ち上げて、あごをつけて……{w=0.45}そうそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こ、こうですか？」"
    $ kag_cm()
    $ kag_playse('2-0215.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もっと左足を前に出して」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('2-0216.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「弓の持ち方は……{w=0.55}そう、そんな感じ。{w=0.4}弓を引くようにして音を出すのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！では……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_pausebgm()
    $ kag_sound_se('se-011.1.ogg', buf=1)
    $ kag_ws(buf=0, canskip=True)
    $ kag_resumebgm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0134.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うえ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ああ……」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0217.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフ。{w=0.4}初めはみんな失敗するものよ。{w=0.4}ちょっといいかしら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "はづきちゃんはわたしの後ろにきて、そっと手を回す。"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0218.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「弦と弓を直角にして、力を入れずに……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-001.ogg', buf=1)
    $ kag_ws(buf=0, canskip=True)
    $ kag_resumebgm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0219.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ほら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントだ！」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0220.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0135.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～。つぎハナちゃんにやらせて～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい。いいですよ」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0136.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やった！{w=0.4}ね～はづき、こう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0221.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もうちょっと首を……{w=0.55}そうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0137.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「よ～し。{w=0.4}いっくよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-002.ogg', buf=1)
    $ kag_ws(buf=0, canskip=True)
    $ kag_resumebgm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わあ～」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0222.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ハナちゃん上手上手」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0138.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんは飲み込みが早いんですね～」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0223.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ホントよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_sound_se('se-011.2.ogg', buf=1)
    $ kag_ws(buf=0, canskip=True)
    $ kag_resumebgm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0139.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0224.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ま、まあこんなこともあるわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_hz_b3_hz__dash__03_02:
    $ kag_set_bookmark('「3日目」りずむの習い事－ＭＡＨＯ堂（１Ｆ）')
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0551.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「バイオリン教えてるの？{w=0.4}はづきちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0225.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「教えてるって言うか、弾き方だけよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「バイオリンはいつから習ってるんですか？」"
    $ kag_cm()
    $ kag_playse('2-0226.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「幼稚園の頃からよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0552.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はづきちゃんはバイオリンだけじゃなくて、勉強も得意だし、{w=0.4}スイミングスクールにも通ってるし、{w=0.4}日本舞踊だって踊れちゃうんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「す、すご～い！」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0227.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そんな大したことじゃ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんなにいろいろできるなんて、ソンケーしちゃいます！」"
    $ kag_cm()
    $ kag_playse('2-0228.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんは習いごととかしてないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「特には……{w=0.55}みなさんも習いごとをしてるんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0553.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしは昔ピアノを習ってたけど、今は何もやってないよ。{w=0.4}おんぷちゃんは英会話とか習ってるけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なるほど……{w=0.6}\nわたしも何か、習いごとやってみたいです！」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0229.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お願いします、はづきちゃん！」"
    $ kag_cm()
    $ kag_playse('2-0230.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「きゅ、急に言われても……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0554.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんはどんなのを習いたいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですねぇ。{w=0.4}あ！魔女界の本で見た、座ってお茶を飲むのをやってみたいです」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0231.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「茶道のことね。それなら、ばあやに習ってるから、少しくらいなら教えられるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0140.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おもしろそう！{w=0.4}ハナちゃんもやる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0555.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「茶道って正座でしょ？……{w=0.55}苦手なんだよね～、正座」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0232.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でもお茶菓子とかも出てくるわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0556.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お菓子！？やるやる～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0233.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「じゃあ、ちょっと待ってね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_playbgm('m408b', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg402.tlg', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('2-0234.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「パイパイポンポイ　プワプワプー」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0235.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お着物とお茶室よ、出てきて！」"
    $ kag_stopse(buf=0)
    $ kag_fadeoutbgm(1000)
    $ kag_cm()
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '02はづき-03', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghz2=1
    $ kag_mesframe()

label kag_hz_b3_hz__dash__03_03:
    $ kag_set_bookmark('「3日目」りずむの習い事－ＭＡＨＯ堂（１Ｆ）')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わあ～」"
    $ kag_cm()
    $ kag_playse('6-0141.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「きものきもの～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0236.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0557.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うわあ、床の間だあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0237.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「床の間は、お茶会の最初の入り口で、亭主さんの心を表すものなの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「本格的ですね～」"
    $ kag_cm()
    $ kag_playse('2-0238.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃあ、よろしくお願いします」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_bookmark('「3日目」りずむの習い事－お茶会')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0558.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お、お茶菓子、まだ～？{w=0.4}げ、限界、近いんですけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0142.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみぃ～ハナちゃん、足痛いよぉ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "はづきちゃんがお茶を入れ始める……{w=0.5}といっても「お手前」とかいってお茶碗に緑色の粉を入れてお湯で溶いているのでちょっと不思議な感じがする。"
    $ kag_cm()
    $ kag_drawchar('d_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0559.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「がまんがまん、お茶菓子にありつくまではひたすら忍耐あるのみだよ、ハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0143.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ぶっぶのぶ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_k_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0239.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お茶菓子をどうぞ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0560.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やったあ！{w=0.4}{nw}"
    $ kag_drawchar('d_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    extend "って、あれ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0144.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「こ、こんだけ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_k_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0240.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「栗きんとんよ。{w=0.4}お茶会のお菓子って必ず和菓子だから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0561.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや、和菓子は好きなんですけど、量がその、ちょっと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0145.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ちょっぴり」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ですね」"
    $ kag_cm()
    $ kag_drawchar('hz_k_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0241.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でも、お茶が主役で、お菓子を食べにきてるわけじゃないから、こんなものよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0562.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん、日ごろの苦労に免じてここはママに少し分けて……{w=0.45}くれない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0146.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ダメだよどれみ。{w=0.4}ハナちゃんだって食べたいよぉ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0563.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなこと言わずにさあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0147.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やっ！そんなこというどれみにはぁ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0563.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「っ！」"
    $ kag_cm()
    "ハナちゃんがどれみちゃんの足をつっつく。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0564.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「むひょおおおお～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0148.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ふふ～んだ。{w=0.4}これはハナちゃんのお菓子だもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0565.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「！」"
    $ kag_cm()
    "今度はハナちゃんの足をどれみちゃんが指でつっつく。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0149.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ひょわわわわ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_k_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0242.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「２人とも。静かにして！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0566.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はーい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0150.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はーい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……………………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「………………………………………………」"
    $ kag_cm()
    $ kag_drawchar('hz_k_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0243.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、どうしたの？なんか様子がおかしいわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「べべべべ、別に平気です！」"
    $ kag_cm()
    "まずい、こんな感覚って初めてだ。足が自分のものじゃないみたい。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ、わあ！」"
    $ kag_cm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    "ビリビリビリ"
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('hz_k_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0244.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0567.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「す、すみませんすみません……{w=0.65}ああっ！！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "掛け軸がまっぷたつになってしまった。\nよろけた時に、その辺の何かをつかんだ気はしたんだけど……。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すすす、すみませんすみませんすみませんすみませんすみませんすみませんすみませんすみませんすみませんすみませんすみませんすみません」"
    $ kag_cm()
    $ kag_drawchar('hz_k_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0245.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「だ、大丈夫よ。{w=0.4}魔法で出した掛け軸だから。それより、りずむちゃんこそ大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「た、立ちあがれないです……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()

label kag_hz_b3_hz__dash__03_04:
    $ kag_set_bookmark('「3日目」りずむの習い事－お茶会')
    $ kag_cm()
    $ kag_drawchar('hn_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0151.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、足がしびれたぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0570.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしもだぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「た、大変でしたぁ」"
    $ kag_cm()
    $ kag_drawchar('hz_k_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0246.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「今回は初めってことで基本的なお手前をやったけど、{w=0.4}本当は茶道って、形式にとらわれずお茶を楽しむってことが大事なの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0571.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へー。そうなんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_k_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0246.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「いすに座ってお手前をいただくっていうのもあるくらいよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_k_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0152.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんそっちがよかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('A-0025.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「アハハハハ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b3_hz__dash__03_05:
    $ kag_set_bookmark('「3日目」りずむの習い事－ＭＡＨＯ堂（外観・夕方）')
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0247.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「じゃあ、わたしはバイオリンのレッスンだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん。今日はありがとうございました。{w=0.4}とっても楽しかったです」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0248.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そんな、お礼なんて言われるようなことはしてないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、よかったら他にも教えてください」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0249.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ。よろこんで。{w=0.4}それじゃまた」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「また明日」"
    $ kag_cm()
    "はづきちゃんっていろんなことができるのに、それを少しも自慢したりしない。"
    extend "何て言うか、ちょっとあこがれちゃうな。"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0217.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、ちょっと来て～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん。{w=0.4}今来たんですか？」"
    $ kag_cm()
    $ kag_playse('3-0218.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。ついさっき、ももちゃんとな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだ、茶室すぐに片づけますね」"
    $ kag_cm()
    $ kag_playse('3-0219.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、茶室をももちゃんがえらい気に入ってもうて、りずむちゃんにお茶を点ててくれって言うてな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええっ？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0220.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まーまー。はづきちゃんがいてへんかったら、できるのはあとりずむちゃんだけやから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0220.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もうバッチリ着物のカッコして待ってんねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_drawchar('m_y_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0134.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ワサビのココロ！イェーイ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0221.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ももちゃん、それを言うならワビサビや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ、形式にとらわれず、お茶を楽しむことが大事なんですよ」"
    $ kag_cm()
    $ kag_drawchar('m_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0134.6.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「んあ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おけいこ事は、楽しくなくっちゃね！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hz3_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hz_b4_gamestart
    return
