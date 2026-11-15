# Auto-generated from 04. onpu/o_B6.ks by tools/transpile_ks.py
label kag_o_b6:

label kag_o_b6_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_onpu.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg025', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_o_b6_op__dash__06_00:
    $ kag_set_bookmark('「６日目」りずむの見習いマネージャー')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    "今日は、おんぷちゃんの付きそいでいっしょに録音スタジオまでやってきた。"
    $ kag_cm()
    "どうしてそうなったかって言うと、"
    extend "海岸からＭＡＨＯ堂に戻ってきた後、おんぷちゃんに声をかけられた。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_frmdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0433.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん。{w=0.4}明日時間ある？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}いつもどおり、ＭＡＨＯ堂のお手伝いをしようかなと思ってますけど？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0434.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「よかったら、わたしのお仕事のお手伝いをたのみたいんだけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えええ？{w=0.4}そんな、わたしでできるかどうか……」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0435.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「平気よ。{w=0.4}待ち時間の間、話し相手になってくれればいいの。{w=0.4}……{w=0.55}ダメ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな、上目づかいで言わなくっても……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0789.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どうせ明日もヒマやし、行ってきたらええやん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0541.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あいちゃん、それってちょっと悲しいかも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0436.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「決まりね。{w=0.4}明日、迎えに行くから。{w=0.4}それじゃあね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.55}あ、はい。{w=0.4}また明日……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-020.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0810.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おんぷちゃん、どうしたんだろうね？{w=0.4}急に」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0790.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ～さっきもなんや２人でええ雰囲気やったみたいやしな～。{w=0.4}なんかあったん？りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "横目であいちゃんに言われて、ついさっきのことを思い出し、また顔から火が出てしまう。"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0243.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「なに？なに？{w=0.4}何かあったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0791.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はっは～ん。{w=0.4}\nその様子、さてはドラマごっこでもしてたんやろ～。{w=0.4}なんか歯の浮くキザなセリフでも言われたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ボボボボッ"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いやあの、おんぷちゃんじゃなくて、わたしが……」"
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0811.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「わたしが～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0244.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「なんて言ったの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あああの、わたし、お先に寝ます！{w=0.4}おやすみなさい！」"
    $ kag_cm()
    $ kag_playse('se-021.ogg', buf=0, loop=False)
    $ kag_wait(500, canskip=True)
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0812.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、逃げた」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0792.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こら待て～。{w=0.4}何言うたか白状せい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「きゃああああ～」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg025', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b6_op__dash__06_01:
    $ kag_set_bookmark('「６日目」りずむの見習いマネージャー')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もうちょっとで白状させられるところだった……」"
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0437.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ねぇ、今日はラジオの収録からだったよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「ええ。{w=0.4}それからＣＭの撮影と、あわせてスチール撮り、それからドラマの収録ね。{w=0.4}今日はいそがしいけどがんばってね、おんぷちゃん」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0438.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0439.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どうしたの？りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}ううん、おんぷちゃん、{w=0.4}とてもいそがしそうなのに、やっぱりわたしがお仕事についていったらおジャマじゃないかな、{w=0.4}と思って……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0440.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「気にしないで。{w=0.4}確かに今日はスケジュールがたくさんだけど、どうしても待ち時間とかは出てくるの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0440.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そんな時に話し相手になってくれればって、そう思ったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「前に、ももこちゃんがお手伝いしてくれたこともあったわね」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだったんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0441.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん。{w=0.4}もっと前には、どれみちゃんがいっしょのオーディションを受けたことだってあったのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へぇ～」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「りずむちゃんは、気楽にしていればいいから。{w=0.4}誰かに聞かれたら『おんぷちゃんの付きそいで来ました』\nって言えばいいのよ」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_playse('4-0442.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、リラックスリラックス」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}あ、えへへ……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0443.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ふふふ。{w=0.4}それじゃ中に入りましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg024', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b6_op__dash__06_02:
    $ kag_set_bookmark('「６日目」りずむの見習いマネージャー－')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "ブースの中では、おんぷちゃんがラジオの収録中。"
    $ kag_cm()
    $ kag_set_next_indent('ＤＪ\u3000「')
    "ＤＪ　「それでは、今日のゲスト、{w=0.4}大人気チャイドルの瀬川おんぷちゃんで～す」"
    $ kag_cm()
    $ kag_playse('4-0444.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「こんばんは、瀬川おんぷです♪」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('ＤＪ\u3000「')
    "ＤＪ　「いや～、今日もかわいいですねぇ、{w=0.4}おんぷちゃん」"
    $ kag_cm()
    $ kag_playse('4-0445.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ありがとうございます♪」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "その様子を、わたしはガラス越しに見ている。"
    extend "となりにはおんぷちゃんのママもいる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ？{w=0.4}さっきおんぷちゃん、『こんばんは』って……」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「ああ、この番組は生放送じゃなくて、収録なのよ。{w=0.4}じっさいは夜に流れる番組なの」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なるほど、そうなんですか～」"
    $ kag_cm()
    $ kag_set_next_indent('ＤＪ\u3000「')
    "ＤＪ　「おんぷちゃんは、小さい頃から芸能活動をしていたそうで……」"
    $ kag_cm()
    "ブースの中では、ＤＪの人とおんぷちゃんの会話が進んでいる。"
    extend "収録は順調に進んでいるみたい。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「小さい頃から、ずっとこのお仕事をしてたんですか？」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「そうよ。{w=0.4}始めはドラマのチョイ役とかだったけど、歌とかラジオの仕事とかがだんだん増えてきてね」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すごいなあ……。{w=0.4}わたしなんか、あのガラス張りの部屋に入っただけでもドキドキして倒れちゃいそうです」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「フフフ。{w=0.4}始めの頃はおんぷちゃんだって緊張してたのよ」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今はとてもそう見えないですね……」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「それでね、おんぷちゃんったらその時……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}え！{w=0.4}そ、そうなんですか！」"
    $ kag_cm()
    $ kag_set_next_indent('ＤＪ\u3000「')
    "ＤＪ　「それでは、\n今日のゲストは瀬川おんぷちゃんでした～！」"
    $ kag_cm()
    $ kag_playse('4-0446.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ありがとうございました♪」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そうこうしているうちに、\nおんぷちゃんの収録が終わったみたいだ。"
    extend "\nブースから出て、わたしとおんぷママの元へと歩いてくる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、おつかれさま」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0447.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん。{w=0.4}ありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0448.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうそう。{w=0.4}ブースからちらっと見えたんだけど、２人で楽しそうに何のお話してたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、うん。{w=0.4}いろいろおんぷちゃんのお話を聞かせてもらってました！」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0449.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしの？{w=0.4}何の話？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「さあさあおんぷちゃん、{w=0.4}押してるから次の現場に行きましょう。ほら、りずむちゃんも早く」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、あああ、そ、そうでしたね。早くいきましょう、おんぷちゃん」"
    $ kag_cm()
    $ kag_drawchar('o_06.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('4-0450.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じろっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「（ギクッ）」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "変なウワサしてたわね！って表情をされた。"
    extend "\n誰にでも、小さい頃の思い出ってあるよね。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg022', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b6_op__dash__06_03:
    $ kag_set_bookmark('「６日目」りずむの見習いマネージャー')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0451.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「おはようございま～す！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「おはようございます」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、お、おはようございま～す！」"
    $ kag_cm()
    $ kag_set_next_indent('スタッフＡ「')
    "スタッフＡ「すみません、{w=0.4}ちょっと前の撮影が押してしまいまして、ひかえ室の方でしばらくお待ちいただけますか？」"
    $ kag_cm()
    $ kag_playse('4-0452.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「は～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「それじゃ２人とも、こっちの部屋で待っててね。{w=0.4}わたしは、なにか飲み物を買ってくるから」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、わたし、行ってきましょうか？」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「あ、いいわよ。{w=0.4}迷子にでもなったら大変だもの」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0453.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん。{w=0.4}先に入って待ってようよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}わかりました」"
    $ kag_cm()
    $ kag_set_next_indent('スタッフＡ「')
    "スタッフＡ「お待たせしました。{w=0.4}お願いします！」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0454.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「は～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "スタッフのかけ声とともに、ＣＭの撮影が始まる。"
    extend "ＣＭの撮影も順調に終わり、次の現場へと向かう。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg026', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b6_op__dash__06_04:
    $ kag_set_bookmark('「６日目」りずむの見習いマネージャー')
    $ kag_cm()
    "外はそろそろ夕方になろうとしている。"
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「次の撮影で今日はおしまいだから、がんばってね」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0455.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん平気？{w=0.4}つかれてない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！大丈夫です！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg023', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b6_op__dash__06_05:
    $ kag_set_bookmark('「６日目」りずむの見習いマネージャー')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "わたしは壁にもたれて、撮影現場をボーっとながめている。"
    $ kag_cm()
    "おんぷちゃんのママは、スタッフの人に呼ばれて席をはずしている。"
    $ kag_cm()
    "撮影現場をボーっと見ながら、別のことを考えていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、何の役にも立ってないなぁ……{w=0.6}魔女界にいた時も、こんな感じだったっけ……」"
    $ kag_cm()
    "他のみんながいそがしそうにお仕事している時に、声どころか仕事ももらえなくて、"
    extend "何か特別なことができるわけじゃないから、こんな風にずっと立ってて……。"
    $ kag_cm()
    "やっと声をかけてもらったと思ったら『あなたそこで何つっ立ってるの！』だったし……"
    $ kag_cm()
    $ kag_set_next_indent('監督\u3000「')
    "監督　「カーット！！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！」"
    $ kag_cm()
    "スタジオにひびき渡る声にハッとして、わたしは撮影現場の方に視線を移す。"
    $ kag_cm()
    $ kag_set_next_indent('監督\u3000「')
    "監督　「おんぷちゃんそこはちがう！{w=0.4}もっと感情をぶつけて！」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0456.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「すみません！{w=0.4}もう１度お願いします！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "撮影現場では、おんぷちゃんがＮＧを出されていた。"
    $ kag_cm()
    "きびしい口調の監督に、真剣な表情のおんぷちゃん。"
    $ kag_cm()
    "はりつめた現場の空気が、さらに引きしまるような感じすらした。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん……{w=0.55}がんばって」"
    $ kag_cm()
    $ kag_set_next_indent('監督\u3000「')
    "監督　「ちがう！{w=0.4}そうじゃなくて、もっとわかりやすく感情を表して！」"
    $ kag_cm()
    $ kag_playse('4-0457.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はい、すみません」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('監督\u3000「')
    "監督　「う～ん、だんだん近づいてはいるんだけどねぇ。{w=0.4}ここは後にしようか？」"
    $ kag_cm()
    $ kag_drawchar('o_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0458.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いいえ、もう少しで何とかなりそうなんです。{w=0.4}もう１度お願いします！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('監督\u3000「')
    "監督　「わかった！{w=0.4}できるまでやってみよう！」"
    $ kag_cm()
    $ kag_playse('4-0459.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    "ふだんはクールで、なんでも軽くこなせちゃうって思ってた。"
    $ kag_cm()
    "そうじゃないんだ。"
    $ kag_cm()
    "おんぷちゃんだってうまくいかないことはあるんだ。"
    $ kag_cm()
    "その時は……"
    $ kag_cm()
    $ kag_set_next_indent('監督「')
    "監督「カーットー！{w=0.4}だいぶよくなってきた。{w=0.4}後半もう少していねいにね」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0460.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はい！{w=0.4}お願いします！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}できるまでやるんだよね。{w=0.4}やっぱり」"
    $ kag_cm()
    "わたし……何を落ち込んでたんだろう？"
    extend "\n失敗したって、やり直せることなら、何度だってやり直せばいい。"
    $ kag_cm()
    "自分にできるかできないかなんて、やってみなくちゃわからないんだ。"
    $ kag_cm()
    $ kag_set_next_indent('監督\u3000「')
    "監督　「おんぷちゃん、今のよかったよ！{w=0.4}それじゃあ、あと少しがんばろうか！」"
    $ kag_cm()
    $ kag_playbgm('m14', loop=True)
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0461.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はい！{w=0.4}ありがとうございます！{w=0.4}\nよろしくお願いします！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よかった……」"
    $ kag_cm()
    "ふと、入り口の方を見ると、スタッフの人が飲み物の準備をしていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}そうだ！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg023', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b6_op__dash__06_06:
    $ kag_set_bookmark('「６日目」りずむの見習いマネージャー')
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0462.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あれ？{w=0.4}りずむちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おんぷママ「')
    "おんぷママ「それが、さっきどこかへ行っちゃったのよ。{w=0.4}すぐ戻るって言ってたけど……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、おんぷちゃんおつかれさま。{w=0.4}はい、どうぞ」"
    $ kag_cm()
    "ジュースが入ったコップをおんぷちゃんにわたす。"
    $ kag_cm()
    $ kag_playse('4-0463.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ありがとう。{w=0.4}これ、どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あそこに用意してあったのを、コップに入れて持ってきました」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('監督\u3000「')
    "監督　「ほう、今日はずいぶんとジュースの種類が多いな」"
    $ kag_cm()
    $ kag_set_next_indent('スタッフＢ「')
    "スタッフＢ「いつもは俺たちの仕事なのに、誰がやってくれたんだ？」"
    $ kag_cm()
    $ kag_set_next_indent('スタッフＡ「')
    "スタッフＡ「ああ、おんぷちゃんの付きそいの子がやってくれたんすよ」"
    $ kag_cm()
    $ kag_set_next_indent('スタッフＢ「')
    "スタッフＢ「お前がやると、同じのしか入れないから、いいんじゃねーの？」"
    $ kag_cm()
    $ kag_set_next_indent('スタッフＡ「')
    "スタッフＡ「あ、ヒドイっすね。{w=0.4}先輩だって、自分が好きなのしか入れないじゃないすか」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0464.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんが入れてくれたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}ちょっとがんばりすぎて、全部のジュース開けちゃいましたけど……」"
    $ kag_cm()
    $ kag_playse('4-0465.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いいんじゃない？{w=0.4}ほら、みるみるうちにへっていってるし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、本当だ……{w=0.6}よかった」"
    $ kag_cm()
    "わたしにだって、誰かの力になれるのかもしれない。"
    extend "\n少しずつさがしていけばいいんだ。ほんの少しずつ……"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg006', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b6_op__dash__06_07:
    $ kag_set_bookmark('「６日目」りずむの見習いマネージャー')
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0466.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「今日はありがとね。{w=0.4}さっきのシーン、自分でも感じつかめないなって思ってたの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0467.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それで、きのう海岸でりずむちゃんとお芝居したでしょ？{w=0.4}そんな感じにできたらって思って、今日１日つきあってもらったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そうだったんですか。{w=0.4}わたしは、本当に近くにいただけなんだけど……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0468.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いいのよ、それで。{w=0.4}わたしがそうしてもらいたかったんだし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_drawchar('a_02.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('3-0793.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お２人さん、お取り込み中のところすんませんな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わ！」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0469.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あいちゃん。{w=0.4}どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0813.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いやね、{w=0.4}昨日の海岸のお芝居ってのをちょ～っと聞かせてもらいたいのさ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あきらめてなかったんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0794.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あったり前やん！{w=0.4}しかも、おんぷちゃんの今日のお仕事に役だったなんて聞いたら、{w=0.4}こりゃますます迫真の演技っちゅーことやんか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0814.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ちょっとやって見せてよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0275.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハイハイ！{w=0.4}ハナちゃん特等席で見る！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0245.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあ、わたしそのとなり！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0542.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「せっかくだから、わたしも見たいわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いやあの、すぐにできるってわけじゃないです……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0039.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「みたい～みたい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0470.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ！{w=0.4}思い出した！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0795.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おんぷちゃん、どないしたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0471.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん。{w=0.4}ラジオの収録の時、ママと何話してたの？{w=0.4}さっきは急いでたから聞けなかったけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、あ、別に何でもないです……」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0472.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「『わたしに隠しこと？{w=0.4}ひどいわりずむちゃん』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0815.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おお！{w=0.4}昨日の続きからだね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0796.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「やんややんや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、ええ？{w=0.4}あ！{w=0.4}わたしもう寝……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-021.ogg', buf=0, loop=False)
    $ kag_wait(500, canskip=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0797.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうはいかんで！{w=0.4}こうなったら昨日の続きやるまで帰さへん！{w=0.4}いや、あたしら帰らんからな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg019', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんな～」"
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.o6_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_o_b7_gamestart
    return
