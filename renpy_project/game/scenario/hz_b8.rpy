# Auto-generated from 02. hazuki/hz_B8.ks by tools/transpile_ks.py
label kag_hz_b8:

label kag_hz_b8_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hazuki.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg016', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hz_b8_hz__dash__08_00:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0178.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それじゃあ、また明日ね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0413.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、行きましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "今日わたしは、はづきちゃんの家にお泊りをする。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg097', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0638.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日のごはんはなんだろうな～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0255.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしんちはこれから決めんとな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0255.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうや！今日はお肉屋さんで鶏肉の特売やったから、それ買うて帰って、チキンライスや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0186.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんとはづきちゃん、お泊まりだなんて本当に仲がいいのね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0639.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホントだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0256.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、初めて会うたときにくらべて、えらい明るうなったしな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0187.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも、明日帰っちゃうのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0640.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん。{w=0.4}ちょっとさみしいかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg054', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b8_hz__dash__08_01:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃんのお家にお泊りかぁ……{w=0.55}何だかちょっとドキドキしちゃうな」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0414.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ふふっ。{w=0.4}りずむちゃんったら、緊張するってほどのことじゃないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0415.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「今日はパパがお仕事でいないし、気楽にしてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃんのパパって、映画監督さんでしたっけ？」"
    $ kag_cm()
    $ kag_playse('2-0416.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ、そうよ。{w=0.4}今はロケでしばらく帰ってこれないみたい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「人間界って、ママの他にパパもいるって聞いて、はづきちゃんのパパに会ってみたかったんだけど、{w=0.4}ちょっと残念かな」"
    $ kag_cm()
    "今日、はづきちゃんから、人間界の『家族』の話を聞いて、わたしがはづきちゃんの家族に会ってみたいってお願いしたら、{w=0.4}それじゃあってことで急にお泊まりが決まった。"
    extend "えっと『善は急げ』だっけ？"
    $ kag_cm()
    $ kag_playse('2-0417.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でもその分っていうわけじゃないけど、りずむちゃんがお泊りに来るってばあやに話したら、お夕飯ははりきっちゃうって言ってたわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はづきちゃんの家には『ばあや』さんって人がいるんでしたね。{w=0.4}楽しみだなぁ～」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0418.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ふふふ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今歩いている周りにある家それぞれに、ママがいて、パパがいて、子どもがいてばあやがいて……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0419.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん。{w=0.4}ばあやは珍しいと思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、そうなの？」"
    $ kag_cm()
    $ kag_playse('2-0420.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それだけじゃないわ。{w=0.4}４人家族だったり６人家族だったり、みんなひとつひとつちがっていて当たり前なのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そっか……」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0421.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「だって、全く同じ人なんていないでしょ？{w=0.4}その人たちが組み合わさっているんだから、同じ形の家族は１つもないのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なるほど……{w=0.5}魔女だって全く同じなんてことないから、その通りですね」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0422.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あ、そろそろお家に着くわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "はづきちゃんの言葉に、わたしは視線を前へと向ける。"
    extend "そこには、はづきちゃんの家の門が見える。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg030', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b8_hz__dash__08_02:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわぁ……{w=0.6}立派なお家……」"
    $ kag_cm()
    "元老院魔女だって、こんなに大きな家に住んでいる人はそうそういない。"
    extend "はづきちゃんの『家族』に会える上に、おまけが１つくっついてきた気分。"
    extend "ドキドキが、ワクワクへと変わっていく。"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0423.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「大したとこじゃないのよ、りずむちゃんったら。{w=0.4}ほら、早く早く」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、うん」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg031', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b8_hz__dash__08_03:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「び、びっくりした～」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0424.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そんなにおどろかなくても」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ばあやさんの声、迫力ありすぎですよ」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0425.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「なれれば平気よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうでしょうか……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg032', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b8_hz__dash__08_04:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ、おいしそう……」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0426.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ばあやったら、今日は張り切ってるわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('はづきママ「')
    "はづきママ「ばあや、これもう運んでいい？」"
    $ kag_cm()
    "別室のキッチンでは、ばあやさんとはづきちゃんのママが最後のしたくを整えている。"
    $ kag_cm()
    $ kag_set_next_indent('ばあや「')
    "ばあや「わたくしがやりますから、奥様がおやりにならなくてけっこうですよ」"
    $ kag_cm()
    $ kag_set_next_indent('はづきママ「')
    "はづきママ「でも～、せっかくはづきちゃんがお友だちのりずむちゃんを連れてきてくれたんだから、私も何かやらないと～」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0427.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ママまで張り切らなくてもいいのに……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_set_next_indent('はづきママ「')
    "はづきママ「ああ忙しいわ。{w=0.4}お風呂の用意と、おふとんの用意と、寝る前に読むご本と、そうだわ！{w=0.4}８時からとってもおもしろいテレビが……」"
    $ kag_cm()
    $ kag_set_next_indent('ばあや「')
    "ばあや「お風呂もおふとんも用意してますから、{w=0.4}奥様ははづきお嬢様とりずむ様のお相手をなさってくださいな」"
    $ kag_cm()
    $ kag_set_next_indent('はづきママ「')
    "はづきママ「はあ～い、シュン」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0428.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう、ママったら……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg032', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b8_hz__dash__08_05:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふぅ……{w=0.65}もうおなかいっぱいです。{w=0.4}ごちそうさまでした」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0429.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お口にあったかしら……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もちろん！{w=0.4}とってもおいしかったです」"
    $ kag_cm()
    $ kag_playse('2-0430.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「よかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "お夕食の間、はづきちゃんのママやばあやとたくさんお話をした。"
    $ kag_cm()
    "はづきちゃんの小さい頃の話。"
    $ kag_cm()
    "ＭＡＨＯ堂のお手伝いをするって言い出したときの話。"
    $ kag_cm()
    "はづきちゃんは照れくさそうに、そして時々は大げさな部分に訂正を入れていた。"
    $ kag_cm()
    "そんな食後のひとときにひたっているのもつかの間。"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0431.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃあ、わたしのお部屋に行きましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg031', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b8_hz__dash__08_06:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0432.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんも座って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('2-0433.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「何か飲み物でも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('はづきママ「')
    "はづきママ「はづきちゃ～ん、お風呂の準備ができてるわよ～」"
    $ kag_cm()
    $ kag_playse('2-0434.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「はぁ～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0435.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お風呂にしましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ、はい」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0436.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「今日もお仕事がんばったもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お客さんは、あんまり来なかったですけどね」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0437.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お客さんは少なくても疲れるのって不思議よね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ、そうですね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg031', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b8_hz__dash__08_07:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「寄宿舎だと、こんな夜ふかしできないからとっても楽しいです」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0438.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、寄宿舎に住んでるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ。{w=0.4}門限とか寝る時間とかが決まっているので、この８日間ってそれがないだけでちょっと気楽でした」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0439.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それは大変ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃんのおけいこやレッスンの話の方が大変だと思いますよ。{w=0.4}わたしは学校とお仕事だけですから」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0440.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お仕事は毎日なの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「学校のある日はだいたいですね。{w=0.4}たまにお城がいそがしいときは、お仕事だけって日もありますけど」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0441.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃあ遊ぶ時間がないんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんなことはないですけど、{w=0.4}わたしの場合、ドジってよけいにお仕事を増やしちゃったりしてばっかりだったから、終わったら日が暮れてたなんてこともありました」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0442.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もうちょっと、早く帰れるようになりたいんですけどね」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_playse('2-0443.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「８日間がんばれたんだもの。{w=0.4}きっと大丈夫よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだといいですけど……」"
    $ kag_cm()
    $ kag_playbgm('bgm-v04', loop=True)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0444.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしね、自分が言いたいって思うことがうまく言えなくて、そんな自分を何とかしたくて魔女見習いになったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……」"
    $ kag_cm()
    $ kag_playse('2-0445.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「魔女見習いになってから、いろんなことがあったけど、うまくいかないなって思うこともたくさんあったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃんがそんなことを思うなんて、ちょっと意外です」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0446.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ううん、本当のわたしは、そんな子なの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん……」"
    $ kag_cm()
    $ kag_playse('2-0446.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でもね、わたし、魔女見習いになってから、いろんなものをＭＡＨＯ堂のみんなからもらったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('2-0446.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うれしいこと、楽しいこと、悲しいこと。いろんなことがあったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0446.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「これからもうまくいかないことは、たくさんあると思うけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0446.4.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「みんながくれたものがあるから、きっと何とかできちゃうって思えるの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0446.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「だから、りずむちゃんもきっと大丈夫よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん……{w=0.4}はい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0446.6.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんが来てから、いろんなことがあったわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はじめてアクセサリーを作って……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0446.7.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「海に行って……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0446.8.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「扇風機が出たり、クーラーが出たりなんてのもあったわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ。とっても楽しかったです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('はづき「')
    "はづき「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_sound_se('se-057', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '02はづき-08', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghz6=1
    $ kag_mesframe()

label kag_hz_b8_hz__dash__08_08:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_playse('2-0447.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「星がきれいね。明日も晴れるかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "しばらくの間わたしたちは、だまって夜空を見つめていた。"
    $ kag_cm()
    "口に出さなくたっていいんだ。"
    $ kag_cm()
    "いいことも、悪いことも、全部わたしたちの思い出。"
    $ kag_cm()
    "時間だけは過ぎていって、遠ざかっても、今のこの気持ちだけは忘れない。"
    $ kag_cm()
    "同じものは何ひとつない、わたしたちだけの思い出があるから。"
    $ kag_cm()
    $ kag_playse('2-0448.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、そろそろ寝ましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('2-0449.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「電気、消すね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-058', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('2-0450.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「明日になったら、りずむちゃんは帰っちゃうのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}ちょっとさみしいですけど」"
    $ kag_cm()
    $ kag_playse('2-0451.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うん……{w=0.55}りずむちゃん、わたしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('2-0452.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「なんでもない。{w=0.4}おやすみなさい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_wait(500, canskip=True)
    "……はづきちゃんは何を言いかけたんだろう？"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hz8_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hz_c_gamestart
    return
