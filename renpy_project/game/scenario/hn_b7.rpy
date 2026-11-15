# Auto-generated from 06. hana/hn_B7.ks by tools/transpile_ks.py
label kag_hn_b7:

label kag_hn_b7_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hana.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_playbgm('m60', loop=True)
    $ kag_history_opt(output=True, enabled=None)

label kag_hn_b7_hn__dash__07_00:
    $ kag_set_bookmark('「７日目」気持ちがわからない！？～')
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0699.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うわぁ～りずむ上手～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "この日は、めずらしく午前中からお客さんがいっぱいだ。"
    $ kag_cm()
    "わたしとハナちゃんは、ビーズメーカーでアクセサリー作りをしていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとうございます」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0700.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむすごいね～{w=0.6}こんなにいろんなアクセサリー作れるようになるんだもん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんなことないです」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0701.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ううん！すごいよ～！{w=0.4}きのうだって、りずむすごかったし～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0702.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「『だ～つ』もすごかったし～{w=0.55}『きんぎょすくい』もすごかったし～{w=0.5}最後にやった『くじびき』だって、{w=0.4}りずむ１等賞だったよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あれはきっと、{w=0.4}たまたまですよ～」"
    $ kag_cm()
    $ kag_playse('6-0703.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん、うらやましいな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そういえば！」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0704.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ほえ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「前に、音楽室で楽器の練習をしていた時、{w=0.4}みなさんが鉄琴さんを『玉木さんに似ている』って言ってましたけど」"
    $ kag_cm()
    $ kag_playse('6-0705.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そうだっけ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「きのうお友だちになった、玉木さんのことだったんですね！」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0706.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、そうそう！{w=0.4}ちょっといじわるなところとかそっくり！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ。{w=0.4}それで、その鉄琴なんですけど」"
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0706.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「午後から二人で学校に行って、{w=0.4}\n楽器の練習しませんか？」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0707.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}そうしよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0708.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん、早く楽器、上手になりたーい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃんたちと、いっしょに演奏できるようになりたいですからね」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0709.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それじゃあ、どれみたちに言って来るね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b7_hn__dash__07_01:
    $ kag_set_bookmark('「７日目」気持ちがわからない！？～')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0710.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇどれみ～！{w=0.4}ハナちゃんとりずむ、午後から出かけるね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1131.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えっ？{w=0.4}午後から？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃんら、どこ行くの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0711.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむとね～学校で楽器の練習するの！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1132.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうなんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0712.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0775.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いいんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0638.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「でも、出かける時は声をかけてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0713.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わかってるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg014', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b7_hn__dash__07_02:
    $ kag_set_bookmark('「７日目」気持ちがわからない！？～')
    $ kag_cm()
    "太陽がちょうど真上になる頃。"
    $ kag_cm()
    "ＭＡＨＯ堂に、次から次へとお客さんがやって来る。"
    $ kag_cm()
    "午後になると、いそがしさはピークになった。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg002', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃん！{w=0.4}アクセサリーの追加たのむわ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0714.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「は～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、そろそろ……」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0715.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「これをあいこの所へ持っていくから、{w=0.4}ちょっと待ってて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1003.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おお～！{w=0.4}作んの早いな～！{w=0.4}さっすがハナちゃんや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0716.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、その調子でもっと作ってな！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0717.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん。{w=0.4}もう午後だから、楽器の練習を」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1133.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん！{w=0.4}そこにある箱持ってきて～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0718.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はぁぁ～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1134.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ありがとう～！{w=0.4}助かったよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0719.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1135.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「この箱こんな重いのに、{w=0.4}ハナちゃんも、『やる時は』やるんだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0720.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('6-0720.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ん？ハナちゃんいつもお手伝いしてるよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1136.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あはは！{w=0.4}冗談だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0721.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ぶぅ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「午後からは、いっしょに楽器を練習しようって言ってたのに……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('5-0639.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ねぇ～ハナちゃ～ん！{w=0.4}Please！こっちも手伝って～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0722.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はいは～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お店、いそがしいんだもんね。{w=0.4}仕方ないか」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg014', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はぁ……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_hn_b7_hn__dash__07_03:
    $ kag_set_bookmark('「７日目」気持ちがわからない！？～')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1137.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや～お客さん、いっぱいだったね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマやな～急にどないしたんやろな～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0688.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でも、時々こういうことってあるわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0776.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うんうん、なぜかお客さんがまとめて来ちゃう時」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0640.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「It's a mystery」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「…………」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1138.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん、おつかれさま」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマ今日は、ハナちゃんが手伝うてくれて助かったわ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0641.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだよね！{w=0.4}ハナちゃん、ありがとう～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「…………」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0689.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ハナちゃん……{w=0.55}どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0723.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ見なかった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1139.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ううん？{w=0.4}りずむちゃんいないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0777.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ハナちゃんと、ずっといっしょにいたんじゃないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0724.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0642.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あれ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0724.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0643.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ハナちゃん、午後はりずむちゃんと楽器の練習に行くんじゃなかった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「午前中、そんなこと言うてたな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0725.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あっ！{w=0.4}すっかり忘れてた……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0726.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん行ってくる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-021.ogg', buf=1)
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1140.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg061', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b7_hn__dash__07_04:
    $ kag_set_bookmark('「７日目」気持ちがわからない！？～')
    $ kag_cm()
    $ kag_playbgm('bgm-001', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「さすがに、勝手に入ってひとりで練習するわけにはいかないよね……」"
    $ kag_cm()
    "今日は校庭で行っているクラブもなく、門をくぐる児童もいない。"
    $ kag_cm()
    "聞こえる音といえば、セミの声だけ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしよう……」"
    $ kag_cm()
    $ kag_playse('se-021.ogg', buf=1, loop=False)
    $ kag_playse('6-0727.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハ、ハナちゃん！？」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0728.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ！{w=0.4}ごめんなさいっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……？」"
    $ kag_cm()
    $ kag_playse('6-0729.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん、りずむとの約束やぶっちゃった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0729.2', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「午後はりずむといっしょに楽器の練習するって言ったのに」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_playse('6-0730.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんが約束やぶっちゃったから、{w=0.4}怒ってるんだよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん、気にしないでください。{w=0.4}だって、今日はすごくいそがしかったし」"
    $ kag_cm()
    $ kag_playse('6-0731.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「でも！{w=0.4}りずむは楽器の練習をしたかったんだよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは確かに、そうですけど」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0732.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「じゃあ今から練習しようよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……」"
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ。{w=0.4}もう夕方だし、ＭＡＨＯ堂に戻りましょう」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0733.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「え～っ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「また明日でいいですよ」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0734.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うううぅ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「行きましょう。{w=0.4}ハナちゃん」"
    $ kag_cm()
    $ kag_playse('6-0735.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg221', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "高台にある美空第一小学校からの帰り道。"
    $ kag_cm()
    "下り坂から見える町なみは、赤くそまっていく。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg015', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b7_hn__dash__07_05:
    $ kag_set_bookmark('「７日目」気持ちがわからない！？～')
    $ kag_cm()
    "わたしたちがＭＡＨＯ堂へたどりつくころには、すっかり日も暮れていた。"
    $ kag_cm()
    "しかし、ＭＡＨＯ堂の明かりはついたままになっている。"
    $ kag_cm()
    "どうやらどれみちゃんたちはおうちに帰らず、ＭＡＨＯ堂にいるみたいだ。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_sound_se('se-009.1', buf=1)
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0736.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ただいま～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ただいま……{w=0.6}です」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1141.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あっ！{w=0.4}帰ってきた！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0778.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ハナちゃん、りずむちゃん。{w=0.4}おかえりなさい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0644.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おかえり～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0690.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お帰りなさい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1008.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんどこ行ってたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、学校へ……」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1142.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もしかして、ひとりで練習してたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「行ったのはいいんですけど、ただ校門の前をうろうろしてました」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1143.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ありゃ、そうだったんだ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0779.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあ練習はやらなかったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ……」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0737.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そうだ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_playbgm('m407', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg413', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('6-0738.ogg', buf=0, loop=False)
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
    $ kag_playse('6-0739.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「みんなの楽器よ～出ろ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_sound_se('se-047', buf=1)
    $ kag_stopse(buf=0)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '06ハナ-07', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghn5=1
    $ kag_mesframe()

label kag_hn_b7_hn__dash__07_06:
    $ kag_set_bookmark('「７日目」気持ちがわからない！？～')
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……{w=0.6}これは？」"
    $ kag_cm()
    $ kag_playse('6-0740.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「これで今から練習できるよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_cm()
    $ kag_playse('8-0204.ogg', buf=0, loop=False)
    $ kag_set_next_indent('鉄琴\u3000「')
    "鉄琴　「りずむさん？{w=0.4}ワタクシとの約束、忘れたワケじゃありませんわよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ！{w=0.4}玉木さん……じゃなくて鉄琴さん！？」"
    $ kag_cm()
    $ kag_playse('8-0205.ogg', buf=0, loop=False)
    $ kag_set_next_indent('鉄琴\u3000「')
    "鉄琴　「せっかく巻機山さんがこのワタクシを出してくれたんだから、{w=0.4}おとなしくワタクシのレッスンを受けるべきですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はあ……」"
    $ kag_cm()
    $ kag_playse('6-0741.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、いっしょに練習しようよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-1009.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしらもつきあうで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-1009.2', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「午後から二人が出かけること知っていたのに、{w=0.4}忙しくてついハナちゃんに仕事手伝わせてしもたんやから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0691.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしたちにも原因があるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん……」"
    $ kag_cm()
    $ kag_playse('1-1144.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「さ、あたしたちも準備しようよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0645.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「OK！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg015', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "ＭＡＨＯ堂からは、みんなの楽器の音が聞こえてくる。"
    $ kag_cm()
    "ときどき音をまちがえる時もあるけど、すきとおったその音色は、夏の夜の風へとまざり、そして周囲に消えていく。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、鉄琴さん、それにみなさん、ありがとう」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ persistent.hn7_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hn_b8_gamestart
    return
