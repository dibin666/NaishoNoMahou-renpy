# Auto-generated from 03. ai/a_B7.ks by tools/transpile_ks.py
label kag_a_b7:

label kag_a_b7_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_ai.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg001', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_a_b7_ai__dash__07_00:
    $ kag_set_bookmark('「７日目」りずむとリボン')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0479.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「おはよう、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おはようございます」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0701.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おはよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0184.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はづき、おはよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0480.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あら？{w=0.4}もうお店開けてるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}朝早く小さい子がきて」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「病気で入院しているお友だちにおくる、{w=0.4}おみまいのお花につけるリボンを選びたいって言われて、早めに開けたんです」"
    $ kag_cm()
    $ kag_playse('2-0481.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうだったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0702.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どうせなら、リボンを結んであげればよかったんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}そう思って結んであげようか？って言ったんですけど、{w=0.4}自分でむすぶからいい、って言われちゃいました」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0482.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「きっとそういう年頃なのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0181.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「友だちのおみまいだったら、なおさらだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「せっかくきれいな結び方をおぼえたのに、ちょっと残念でした」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0703.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「きのうの午前中、ずっとあいちゃんに教わってたもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0209.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんなおはよう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0704.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、おんぷちゃんおはよう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おはようございます」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0483.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「おはよう。{w=0.4}あいちゃんは午後からだから、みんなそろったわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0705.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃさっそくお仕事に……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0185.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、なんでしょう？」"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0186.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「遊びに行こ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0706.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おいおい……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0187.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あのね、\nすっごくきれいな海が見える公園があるんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「海！{w=0.4}行きた……{w=0.55}でも、お仕事が」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0182.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「朝早くから仕事してたんだから、りずむちゃんはお昼くらいまで休みなよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな、いいんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0484.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「おそうじまでひとりでやってくれたんだから、オッケーよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0707.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、そうだね。{w=0.4}ハナちゃん、お昼までには帰ってきなよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0188.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わかってる！{w=0.4}行こ、りずむ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、待ってください」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg090', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b7_ai__dash__07_01:
    $ kag_set_bookmark('「７日目」りずむとリボン')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0189.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ふんふふ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんは、海、好きですか？」"
    $ kag_cm()
    $ kag_playse('6-0190.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「きのうあいちゃんといっしょに見た海、すごくキレイだったな～」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0191.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「公園から見える海も、キラキラ光っててとってもキレイだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「楽しみですね」"
    $ kag_cm()
    $ kag_playse('6-0192.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あれ、あいこ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(1000, canskip=True)
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0193.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ありゃ？{w=0.4}行っちゃったよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「聞こえなかったのかな？{w=0.4}あいちゃーん！」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0606.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あれ、２人ともどしたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0194.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あいこも、そんなに急いでどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0607.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ああ、ゆうべお父ちゃんがカゼひいてしもうてな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ！」"
    $ kag_cm()
    $ kag_playse('3-0608.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いつもみたいにお腹出して寝てるのがアカンのやけど、{w=0.4}熱もあるから薬買いにひとっ走り行ってこようと思ってな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0195.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そうなんだ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お父さん、大丈夫なんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0609.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「カゼは大したことはあれへんねんけど、お父ちゃんがやるはずやったそうじとか洗濯とかの方がな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「全部あいちゃんがやらなきゃいけないんですか？」"
    $ kag_cm()
    $ kag_playse('3-0610.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まあ、しゃーないな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.5}手伝いましょうか」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0611.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんな、ええって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0612.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「気持ちだけもろとくわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0196.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「お父さん早くよくなるといいね。{w=0.4}あいこ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0613.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ありがとな、ハナちゃん。{w=0.4}ほなりずむちゃんも、また」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだ！」"
    $ kag_cm()
    $ kag_playse('3-0613.5.ogg', buf=0, loop=False)
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん、ママに来てもらったらどうですか？」"
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0614.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それはムリや。{w=0.4}お母ちゃん遠いところに住んではるから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だったら、魔法で……」"
    $ kag_cm()
    $ kag_playse('3-0615.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それはアカン。{w=0.4}お母ちゃんのつごうも考えんと、それはできへん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「つごうって……{w=0.55}あいちゃんもお父さんも大変なのに、つごうも何もないじゃないですか！」"
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0616.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「よう知らんのにそんなこと言わんといてよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！」"
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0617.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしは、お母ちゃんを困らせるのが\n１番イヤやねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ご、ごめんなさい」"
    $ kag_cm()
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0618.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もうあたし行くわ。{w=0.4}ハナちゃん、今日のＭＡＨＯ堂はお休みするってみんなに言うといて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0197.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん、わかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0619.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、またな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg086', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b7_ai__dash__07_02:
    $ kag_set_bookmark('「７日目」りずむとリボン')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0198.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「きれいな海でしょ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントですね～」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('6-0199.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、元気ないね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_playse('6-0200.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あいこのこと、気にしてるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}悪いこと言っちゃったかなって思って」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0201.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あいこは怒ってないよ、平気だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃんのこともそうなんですけど、ちょっとなやんでることがあって、{w=0.4}それを思い出しちゃったのもあって……」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0202.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「なやみごと？{w=0.4}どんな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんは、魔女ですよね？」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0203.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「今は見習いだけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔女は魔法が使えるのに、人間界では喜ばれないこともあるって思いませんか？」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0204.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ほえ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「さっきみたく、あいちゃんのママを魔法で遠い所から呼び出しても、あいちゃんは喜ばない。{w=0.4}わたしはあいちゃんのために何ができるんでしょう？」"
    $ kag_cm()
    $ kag_playse('6-0205.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「う～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんはどう思いますか？」"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0206.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わかんない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0207.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「だって最初から魔法が使えるんだもん。{w=0.4}ハナちゃんそんなのわかんない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それはわたしもそうですけど……」"
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0208.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「う～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「う～ん」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0209.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そうだ。{w=0.4}ちょっと待ってて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(1000, canskip=True)
    $ kag_drawchar('hn_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0210.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「お待たせ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしたんですか？{w=0.4}見習い服に着がえたりして」"
    $ kag_cm()
    $ kag_playbgm('m407', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg413', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('6-0211.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ポロリンピュアリン　ハナハナピ！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('circle02', 'bg414', time_ms=600, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('6-0212.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「看護婦のすがたに～なれ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg086', time_ms=500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、これは……」"
    $ kag_cm()
    "なぜかわたしだけ、看護婦のかっこうになっている。"
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('hn_m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0213.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「これで、あいこのお父さんの看病をすればいいんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、あいちゃんに手伝わなくていいって言われちゃったし……」"
    $ kag_cm()
    $ kag_drawchar('hn_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0214.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うーん、それじゃこうしよう！」"
    $ kag_stopse(buf=0)
    $ kag_stopbgm()
    $ kag_cm()
    $ kag_playbgm('m407', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg413', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('6-0215.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ポロリンピュアリン　ハナハナピ！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('circle02', 'bg414', time_ms=600, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('6-0216.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「忍者のすがたに～なれ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg086', time_ms=500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_wait(1000, canskip=True)
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('hn_n_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0217.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「これなら見つからないから、バッチリだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_playse('6-0218.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それじゃあ、あいこの家に行こう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「い、いいのかなあ」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg033', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_set_bookmark('「７日目」りずむとリボン')
    $ kag_cm()
    $ kag_drawchar('hn_n_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0219.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「コソコソコソ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハ、ハナちゃん、本当にこんなことをしてもいいんでしょうか？」"
    $ kag_cm()
    $ kag_playse('6-0220.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「コソコソ。大丈夫」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0220.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「コソコソ今、コソコソハナちゃんたちは、コソコソ忍者なんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0221.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「コソコソ、さありずむもしっかりコソコソして」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「コ、コソコソ……」"
    $ kag_cm()
    $ kag_playse('6-0222.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「さ、もうすぐあいこの家だよコソコソ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そうですねコソコソ」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0620.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、りずむちゃんにハナちゃん、何してんの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_n_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0223.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うっ、なぜバレた」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0621.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「バレたもなにも、目の前におんのにわからんわけないやん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_n_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_drawchar('hn_n_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0224.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「きょ、今日のところはこれで引き上げるぞ。{w=0.4}おぼえておれ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、おぼえておれ……」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0622.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「は？……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_a_b7_ai__dash__07_03:
    $ kag_set_bookmark('「７日目」りずむとリボン')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ただいま……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0708.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おかえり～。{w=0.4}ハナちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、もうちょっと遊んで行くって……」"
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0709.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もうハナちゃんったら～。{w=0.4}お昼までには帰ってきてって言ったのにさ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ、わたしがいけないんです」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0710.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どういうこと？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「実は……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(1000, canskip=True)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0711.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0485.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「たしかに、むずかしい問題よね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0210.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どうしてほしいかなんて人それぞれだから、簡単にはいかないわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、あいちゃんにもハナちゃんにも悪いことしちゃって……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0183.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「２人とも気にしてないよ。{w=0.4}大丈夫だって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだといいんですけど……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0712.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でもさ、あいちゃんのお母さんは連れてこられなくたって、{w=0.4}あいちゃんのためにできることってあると思うよ？」{nw}"
    $ kag_history_opt(output=False, enabled=None)
    $ kag_waitclick()
    $ kag_history_opt(output=True, enabled=None)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ。{w=0.4}それって……？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0486.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「魔法でなにかをしてあげるだけじゃなくて、あいちゃんにりずむちゃんの気持ちが伝われば、{w=0.4}それでいいんじゃないかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0225.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「たっだいま～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0713.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あっ帰って来た。{w=0.4}それじゃあお昼にしようか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0184.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたし、したくしてくる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0226.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0227.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あげる」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お花……？」"
    $ kag_cm()
    $ kag_playse('6-0228.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あのね、おみまいをあげたらいいかなって、ハナちゃん思ったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……」"
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0229.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ダメ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それですよハナちゃん！{w=0.4}ナイスアイディアです！」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0230.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ホント？{w=0.4}よかった！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こんなことに気づかなかったなんて……{w=0.55}ありがとうハナちゃん！」"
    $ kag_cm()
    $ kag_playse('6-0231.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg015', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b7_ai__dash__07_04:
    $ kag_set_bookmark('「７日目」りずむとリボン')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それじゃ、行ってきます」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0714.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「気をつけてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0232.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、うまくいくといいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg034', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b7_ai__dash__07_05:
    $ kag_set_bookmark('「７日目」りずむとリボン')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううう、ちょっとドキドキする……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「やっぱり断られたらどうしよう……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それに、お花だけって言うのも……{w=0.55}何かほかにないかな……」"
    $ kag_cm()
    "わたしは、ごそごそとポケットに手をやる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだ！{w=0.4}朝のあの子の……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれを使おう！」"
    $ kag_cm()

label kag_a_b7_choices_ai03:
    $ kag_set_bookmark('あいこシナリオ選択肢03')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】レースペーパー', current_stem='a_b7', storage=None, target='*choices_ai03-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】リボン', current_stem='a_b7', storage=None, target='*choices_ai03-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_a_b7_choices_ai03__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}なんかちがうような？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うーん……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ！{w=0.4}そうだった！」"
    $ kag_cm()
    jump kag_a_b7_after_choices_ai03
    call kag_s_wait
    "【分岐終わり】{nw}"

label kag_a_b7_choices_ai03__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag += 1
    jump kag_a_b7_after_choices_ai03
    call kag_s_wait
    "【分岐終わり】{nw}"

label kag_a_b7_after_choices_ai03:
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「青いリボンよ、出て来い！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_sound_se('se-047.ogg', buf=1)
    "わたしは出て来たリボンを花に結んだ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よ～し」"
    $ kag_cm()
    $ kag_sound_se('se-024.ogg', buf=1)
    $ kag_playse('3-0623.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「は～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、りずむです」"
    $ kag_cm()
    $ kag_playse('3-0624.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん？{w=0.4}ちょっと待って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0625.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どしたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、これ……」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0626.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お花？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お父さんのおみまいに」"
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_playse('3-0627.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「え……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いろいろ考えたんですけど、{w=0.4}結局わたしができるのって、こんなことしかなくって」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0628.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……{w=0.6}ううん、ありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0629.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「メッチャうれしいわ。{w=0.4}ホンマありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よかった……」"
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0630.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「昼間はゴメンな。{w=0.4}りずむちゃん、せっかくいろいろ考えて言ってくれてんのに、{w=0.4}あたし自分のことばっかり考えて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいえ。{w=0.4}わたしがあいちゃんのこと、よく知りもしないで勝手なことを言ってたから、{w=0.4}わたしだっていけないんです」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0631.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんは、やさしいねんな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0632.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。{w=0.4}やさしいよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「な、なんか照れちゃいます……\n{w=0.55}明日も看病するんですか？」"
    $ kag_cm()
    $ kag_playse('3-0633.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もうお父ちゃんの熱も下がったから、明日はＭＡＨＯ堂行くわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか」"
    $ kag_cm()
    $ kag_playse('3-0634.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、また明日な」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}さようなら」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-031.1.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('sepia', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_image('bg017_a', layer='1', page='back', left=0, top=0, visible=True, sepia=True)
    $ kag_trans(time_ms=50, method='', rule='trans01', vague=100)
    $ kag_wt(canskip=True)
    $ kag_image('c_frm', layer='2', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=600, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    $ kag_mesframe()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('1-0715.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃんのためにできることってあると思うよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='2', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('sepia', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_image('bg017_a', layer='1', page='back', left=0, top=0, visible=True, sepia=True)
    $ kag_trans(time_ms=50, method='', rule='trans01', vague=100)
    $ kag_wt(canskip=True)
    $ kag_image('c_frm', layer='2', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=600, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    $ kag_mesframe()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('6-0233.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000\t「')
    "ハナ　	「あのね、おみまいをあげたらいいかなって、ハナちゃん思ったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='2', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg034', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みんながくれた、やさしさがあるからだよ。{w=0.4}あいちゃん」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ persistent.a7_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_a_b8_gamestart
    return
