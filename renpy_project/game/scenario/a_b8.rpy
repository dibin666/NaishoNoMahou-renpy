# Auto-generated from 03. ai/a_B8.ks by tools/transpile_ks.py
label kag_a_b8:

label kag_a_b8_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_ai.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg014', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_a_b8_ai__dash__08_00:
    $ kag_set_bookmark('「８日目」あいこの気持ち')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0716.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へえ～。{w=0.4}りずむちゃんのお花のアレンジ、そんなにきれいだったんだ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ＭＡＨＯ堂でのお仕事にもずいぶんなれた。{w=0.4}いつもの時間に、いつものようにみんなはやってきて、開店の準備を始める。"
    $ kag_cm()
    "わたしは、あいちゃんとどれみちゃんといっしょに、お店の前をそうじしていた。"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0635.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そらあもう、昔のガーデニングショップを思い出したわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「昔はガーデニングショップだったんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0717.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだよ。{w=0.4}去年はスイートハウスだったしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へええ……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0636.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もらった花は、枯れたらマズイからって花ビンに移してあるから、もうあのアレンジは見られへんけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0718.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そっか。{w=0.4}ちょっと見たかったけど、しょうがないね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「で、その、お父さんの調子はどうです？」"
    $ kag_cm()
    $ kag_drawchar('a_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0637.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「くあー！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ひええ！」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0719.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、あいちゃんどうどう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0638.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしは馬か！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0720.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お、落ちついてよ。{w=0.4}いったいどうしたのさ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0639.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それが聞いてーや。{w=0.4}お父ちゃんな『こんなええ花もろたらカゼなんて引いてられんわー』なんて言うて、朝ケロ\nッとしてんねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もうなおったんですか？{w=0.4}それならよかったじゃないですか」"
    $ kag_cm()
    $ kag_playse('3-0640.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ところが続きがあんねんて。{w=0.4}お父ちゃんの奴、どっから\nか旅行カバン出してきて『ほな行ってくるわ』って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0721.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？{w=0.4}ど、どこへ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0641.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「会社の慰安旅行やて。{w=0.4}温泉で一泊してくるって言うねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0722.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えええ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、まだ病み上がりなのにそんな……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0642.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしもそう言うたら『温泉が待ってるのにカゼなんか引いてられへん』なんて言って、もうピンピンしてんねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0723.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あの、さっきと言ってることがちがうんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ……」"
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0643.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「せやからあたし朝から、思いっきり『アホかー！』ってさけんでしもたわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0724.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あははは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、なおったんだからいいじゃないですか」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0644.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まあ、そやねんけどな。{w=0.4}それでな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0725.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まだあるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0645.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、今日うちに来てくれへん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_playse('3-0646.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「せめてお礼に、夕飯ごちそうしたいねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんな、お礼だなんて」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0647.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「んなことゆわんと、いっしょにご飯食べよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、わかりました！{w=0.4}それじゃあ、お言葉に甘えてお邪魔します」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0234.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみー！{w=0.4}あいこ、りずむー！{w=0.4}おそうじ終わった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0726.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「しまった！{w=0.4}まだ途中だった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0648.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「アカン。{w=0.4}はよやらな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_a_b8_ai__dash__08_01:
    $ kag_set_bookmark('「８日目」あいこの気持ち')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0185.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そっかぁ。{w=0.4}じゃあ楽しみだね、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0649.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん何食べたい？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うーん、そうですね～」"
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0727.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ステーキがいいよ！{w=0.4}おいしいよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0211.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それはどれみちゃんが食べたいんでしょ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0235.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんプリンがいい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0487.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それは３時のおやつでしょ、ハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0236.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「へへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、こっちの食べ物をあんまり知らないので、あいちゃんのおすすめでいいですよ」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0650.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そう？{w=0.4}ほな何にしようかな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0488.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お寿司とかどうかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0728.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はづきちゃん、それはいくらなんでもぜいたくなんじゃ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0651.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それええなあ。{w=0.4}ほんなら手巻き寿司にしよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お寿司というのはどういう……？」"
    $ kag_cm()
    $ kag_playse('3-0652.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それは見てからのお楽しみでええやん。{w=0.4}りずむちゃん生ものは平気？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0653.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「んなら問題ないわ。{w=0.4}なぁ仕事終わったら一緒に帰ろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わかりました」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0729.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ところでりずむちゃん、帰るのは明日なんだよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうです」"
    $ kag_cm()
    $ kag_playse('1-0730.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「何時ごろに帰るの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「夕方までには帰ろうかって思ってますけど」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0731.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあさ、明日のお昼は送別会にしない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0186.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Good idea！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0212.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いいわね、それ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0237.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やろうやろう～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな……{w=0.6}お世話になりっぱなしだったのに」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0489.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それは言いっこなしよ。{w=0.4}わたしたちだって手伝ってもらってたんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0187.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしケーキ焼いてくるね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0213.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ママがおいしいお茶をもらってたから、わたしはそれを持ってくるわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0490.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしは、ばあやといっしょにクッキーを焼いてくるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0732.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おおお～楽しみだよぉ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0654.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もう、どれみちゃんは～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg016', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b8_ai__dash__08_02:
    $ kag_set_bookmark('「８日目」あいこの気持ち')
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0655.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほなまたな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0733.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「バイバーイ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「さよならー」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0656.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「さ、行こかりずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg054', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b8_ai__dash__08_03:
    $ kag_set_bookmark('「８日目」あいこの気持ち')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0657.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「へぇ～。りずむちゃん、いろいろやったことあんねん\nなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、問屋魔女のお手伝いを１日だけやったこともあるんですよ」"
    $ kag_cm()
    $ kag_playse('3-0658.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ～あたしらも１回だけやった～。{w=0.4}ホンマヘトヘトやったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「まちがえておとなりさんに届けちゃったりして、{w=0.4}荷物が届かないって怒られたりして、大変でした」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0659.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あるある。{w=0.4}食べ物やったりしたらえらいことやで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ、それが通信販売のダイエット器具だったんですよ。{w=0.4}そのお家はおとなりと仲が悪くて、こっぴどく怒られちゃったんです」"
    $ kag_cm()
    $ kag_playse('3-0660.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっはっはっは！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「笑いごとじゃないですよ。{w=0.4}もうどうしようかと思ったんですから」"
    $ kag_cm()
    $ kag_playse('3-0661.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あはは、それでどうなったん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「困って舎監の先生に相談したら、{w=0.4}これを使ったらって昔先生が使ってたやつを貸してくれて」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0662.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それを貸したん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}そうしたら、本当にダイエットに成功したみたいで、後でものすごく感謝されちゃって」"
    $ kag_cm()
    $ kag_playse('3-0663.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そりゃよかったやん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でもないんですよ。{w=0.4}その舎監の先生はダイエットに成功してなくて、{w=0.4}何で成功したのか先生にしつこく聞かれるはめになっちゃったんです」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0664.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あははは！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もう～」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0665.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ゴメンゴメン。{w=0.4}でも、大変やったなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「結局その後、ずーっと毎朝先生のジョギングに付き合わされちゃいました」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0666.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしんとこは、お父ちゃんのお腹出てきたんが気になってな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか？」"
    $ kag_cm()
    $ kag_playse('3-0667.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうやねん。{w=0.4}毎日ジョギングでもして、やせたらどないやって言うてんねんけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「やってくれないんですか？」"
    $ kag_cm()
    $ kag_playse('3-0668.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「めんどくさがりやから、休みの日になったらゴロゴロしてばっかりやねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「困りましたねぇ」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0669.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そのくせ、お母ちゃんに会うときだけは、気合い入れんねんから、{w=0.4}ぜんぜんわからんわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「家のドアをせまくして、やせるまで入れないようにしたらどうですか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0670.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっはっはっはっは！{w=0.4}それええやん！{w=0.4}りずむちゃんもおもろいこと言うなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、そうですか……？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0671.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「仕事かてうまいこといかへんて言うてたけど、{w=0.4}さっきの話みたいに最後にお礼言われたんやったら、それでええんとちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「まあ、たしかに……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0672.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こんだけおもろいねんもん、まわりの人も放っとかへんと思うけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしはマジメに考えてるんですけど……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg095', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b8_ai__dash__08_04:
    $ kag_set_bookmark('「８日目」あいこの気持ち')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お風呂って、外にあるんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0673.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うちお風呂ないから、お風呂屋さんに行くねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おふろや……？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0674.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「広いお風呂やから、あったまんで～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「温泉みたいな感じですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0675.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなようなトコやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こっちにはいろんなお店があるんですね」"
    $ kag_cm()
    $ kag_playse('3-0676.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやろ。{w=0.4}んで、そこのお風呂屋さんは、ゆかりちゃんっていうクラスメートの家がやってんねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へええ～」"
    $ kag_cm()
    $ kag_playse('3-0677.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あの『梅の湯』ってのがそうや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0677.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お風呂屋さんで洗面器とタオルは借りられるから、{w=0.4}シャンプーと石けんはあたしのを貸したげる」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg036', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b8_ai__dash__08_05:
    $ kag_set_bookmark('「８日目」あいこの気持ち')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「こ、これがお寿司……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0678.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そう！海の幸いっぱいや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、おいしそうですね～」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0679.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そらもうたまらんで～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「い、いただいてもいいですか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0680.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どうぞ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg036', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b8_ai__dash__08_06:
    $ kag_set_bookmark('「８日目」あいこの気持ち')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「しあわせ……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0681.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おいしかったな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとうあいちゃん。{w=0.4}今日はサイコーの日です！」"
    $ kag_cm()
    $ kag_playse('3-0682.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや～喜んでもらってあたしもうれしいわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お風呂屋さんも広くてとっても気持ちよかったし」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0683.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もうあとは横になったら、わたしすぐにでも寝ちゃいますよ」"
    $ kag_cm()
    $ kag_playse('3-0684.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なんなら泊まってく？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、そんな、悪いですよ」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0685.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「気にせんでええって。{w=0.4}もうちょっとしたらお父ちゃんから電話来るから、{w=0.4}そんときにひとこと言うといたら問題ないし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか？」"
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_sound_se('se-046.ogg', buf=1)
    $ kag_resumebgm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0686.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほら来た」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('3-0687.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はい、妹尾です」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0687.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん、うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0687.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あんな、今日りずむちゃん泊めてもええかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0687.4.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん、そうそう。{w=0.4}ほなりずむちゃんにかわるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0688.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、お父ちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はじめまして、巻機山りずむです。{w=0.4}あいちゃんのお父さんですか？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい……{w=0.7}ええ……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか？あははは！{w=0.6}はい、わかりました」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、あいちゃん」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0689.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、ありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('3-0690.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お父ちゃん？うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0690.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん、わかった。{w=0.4}お父ちゃんもあんまハメはずしたらアカンで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0690.3', buf=0, loop=False)
    "あいこ「うん。ほな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ。あいちゃんのお父さんって、おもしろい人ですね」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0691.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お父ちゃん、なんか言うとった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ『あいちゃんはいびきがうるさいから、耳栓を用意しとけ』って」"
    $ kag_cm()
    $ kag_drawchar('a_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0692.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「オトメに向かって何ちゅうことさらすんや、あのアホ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0693.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「で、泊まってもええって。{w=0.4}どないする？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うーん。{w=0.4}じゃあ、お言葉に甘えて」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0694.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「よっしゃ！{w=0.4}決まり！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「とりあえず、片づけましょうか」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0695.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうやね。{w=0.4}あ、そうや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_playse('3-0696.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こないだりずむちゃんに貸してって言われてた本、あとで持ってくるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ああ！{w=0.4}そうだった」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '03あいこ-08', time_ms=1000, bgcolor='0x000000')
    $ persistent.cga5=1
    $ kag_mesframe()

label kag_a_b8_ai__dash__08_07:
    $ kag_set_bookmark('「８日目」あいこの気持ち')
    $ kag_cm()
    $ kag_playse('3-0697.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「う～ん。{w=0.4}どこいったんやろな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「見つからないですね」"
    $ kag_cm()
    $ kag_playse('3-0698.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「せまい家やから、すぐに見つかると思ててんけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ちょっと残念ですけど、{w=0.4}他の絵本が読めたから、わたしは大満足です」"
    $ kag_cm()
    $ kag_playse('3-0699.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ん～、そう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この『人魚姫』は初めて読んだんですけど、{w=0.4}グッときますね」"
    $ kag_cm()
    $ kag_playse('3-0700.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ん～あたしにはちょっと悲しい話なのがな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですよね。{w=0.4}わたしだったら、声とひきかえにしなくても足をつけてあげたのに」"
    $ kag_cm()
    $ kag_playse('3-0701.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そういうお話やから、{w=0.4}しゃあないっちゃーしゃあないねんけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg035', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('bgm-v04', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「しあわせになるために、どちらかを選ばなきゃいけないなんて悲しいですよね」"
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}あいちゃん？」"
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0702.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そういうこともあんねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}それって……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0703.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、何でもない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0703.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そろそろ寝よか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、あ、そうですね」"
    $ kag_cm()
    $ kag_playse('3-0704.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お父ちゃんのふとんはあたしが使うから、りずむちゃんあたしのふとんでええ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg034', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "はぐらかされちゃったけど、あいちゃんは何を言おうとしたんだろう。"
    $ kag_cm()
    "わたしは、あいちゃんの何とも言えない表情が気になっていた。"
    $ kag_cm()
    "あいちゃんのふとんの中で、わたしはだんだんとねむりに落ちていった。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.a8_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_a_c_gamestart
    return
