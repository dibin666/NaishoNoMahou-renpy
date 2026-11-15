# Auto-generated from 03. ai/a_B6.ks by tools/transpile_ks.py
label kag_a_b6:

label kag_a_b6_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_ai.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_a_b6_ai__dash__06_00:
    $ kag_set_bookmark('「６日目」ステキな海！そしてステキな・・・')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_playse('se-017.ogg', buf=1, loop=True)
    "今日も美空町は猛暑。"
    extend "そんな中、ＭＡＨＯ堂ではジュウジュウと香ばしい音が聞こえてくる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どきどき……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0547.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、はよひっくり返さな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「むむむむむ……{w=0.8}えい！」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0548.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お！{w=0.4}うまい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふう～。{w=0.4}『お好み焼き』っていうのはとても緊張しますね」"
    $ kag_cm()
    $ kag_playse('3-0549.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もうひっくり返すだけでドキドキですよ～」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0550.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あはは。{w=0.4}まあ初めてやったらムリもないか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0688.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あの～。{w=0.4}こんなあつい日にお好み焼きッスか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0551.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「季節は関係ないやろ。{w=0.4}春夏秋冬いつでもお好み焼きはおいしいやん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0689.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そ、そうなの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0552.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃんのステーキといっしょやって。{w=0.4}あ、りずむちゃんソース取って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はいっ」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0553.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな食べよっか」"
    $ kag_stopse(buf=0)
    $ kag_stopse(buf=1)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1000, bgcolor='0x000000')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_a_b6_ai__dash__06_01:
    $ kag_set_bookmark('「６日目」ステキな海！そしてステキな・・・')
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0554.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ～食った食った～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ごちそうさまでした」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0690.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃんのお好み焼きは、サイコーだね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0555.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃんゲンキンやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0691.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へへへ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃんは、料理にくわしいんですね」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0556.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「単にタコ焼きとお好み焼きが、得意なだけやねんけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「２つも知ってるなんて、ソンケーしちゃいます」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0557.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「やめてそんなん。{w=0.4}照れるやん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そうそう。{w=0.4}聞きたかったことがあるんです」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0558.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「『タコ焼き』の『タコ』って、\nなんのことなんでしょう？」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0692.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0559.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、タコ知らんの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}はい」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0560.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「タコは、海の生き物やねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「海、ですか？」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0693.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、海知らないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「本で読んだことはあるんですけど、行ったことはないです」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0561.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そしたら、午後は海行こう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、仕事はいいんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0694.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「午後からはづきちゃん来るし、ヒマだから大丈夫。{w=0.4}行っといでよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0562.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ちゅーことで、決まりでええかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg080', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b6_ai__dash__06_02:
    $ kag_set_bookmark('「６日目」ステキな海！そしてステキな・・・')
    $ kag_cm()
    $ kag_playbgm('m14', loop=True)
    $ kag_playse('se-014.2.ogg', buf=1, loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ～～！{w=0.4}広いです～！」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0563.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやろ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「波の音が、すごいですね！」"
    $ kag_cm()
    $ kag_playse('3-0564.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわぁ～……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0565.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もうちょっと近くまで行こ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg211', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b6_ai__dash__06_03:
    $ kag_set_bookmark('「６日目」ステキな海！そしてステキな・・・')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「遠くから見たら青いのに、近くで見ると透明なんですね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg083', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0566.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんででしょう？」"
    $ kag_cm()
    $ kag_playse('3-0567.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「さあ……{w=0.5}あたしもくわしいことはよう知らんからな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この水の中に、タコさんが住んでいるんですか？」"
    $ kag_cm()
    $ kag_playse('3-0568.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「タコだけやのうて、今日お好み焼きで食べたイカとかエビもおんねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか？」"
    $ kag_cm()
    $ kag_playse('3-0569.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「青のりかてそうやし、カツオブシも元々は海の生き物やねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へええ……{w=0.55}海っておいしいものがいっぱいなんですね」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0570.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そ、そやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃあ、さっそくタコさんを……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「タコさんやってきて！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_wait(1000, canskip=True)
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0571.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あれ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「来ないですね」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それじゃ……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「イカさんやってきて！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_wait(1000, canskip=True)
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔法、失敗しちゃったかな？」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0572.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何もおこらんな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それなら！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「カツオブシさんやってきて！」"
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0573.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ちょ、ちょっとりずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0574.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「カツオブシは海にいてないて。\n{w=0.4}海にいるのはカツオや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、あのひらひらしたのが泳いでいるのかと……」"
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0575.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「んなわけあるかい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}それにしても、何もやってこないですね」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0576.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「海は広いから、タコやイカのおる所まで、魔法が届かんのかもな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんなに広いんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0577.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「広い広い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれくらいですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0578.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれくらいって……{w=0.65}うーん……{w=0.55}そや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('3-0579.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、行こ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、あ、どこへ？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0580.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ええからええから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', '03あいこ-06', time_ms=1000, bgcolor='0x000000')
    $ persistent.cga4=1
    $ kag_mesframe()

label kag_a_b6_ai__dash__06_04:
    $ kag_set_bookmark('「６日目」ステキな海！そしてステキな・・・')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわ……」"
    $ kag_cm()
    $ kag_playse('3-0581.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どや。{w=0.4}ごっつう広いやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}すごい……」"
    $ kag_cm()
    $ kag_playse('3-0582.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あの向こうに、よその国とかがあって、いろんな人がおんねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんだ……」"
    $ kag_cm()
    $ kag_playse('3-0583.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こうして見ると、海にとったらあたしらなんて、ちっぽけなモンやろな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん」"
    $ kag_cm()
    $ kag_playse('3-0584.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっ！{w=0.4}今魚がはねた！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、どこです？」"
    $ kag_cm()
    $ kag_playse('3-0585.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「岩場のすぐ近く」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ホントだ！」"
    $ kag_cm()
    $ kag_playse('3-0586.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「またはねた！{w=0.4}あのへんに集まってるんかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あははは。{w=0.4}おもしろ～い」"
    $ kag_cm()
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ……」"
    $ kag_cm()
    $ kag_playse('3-0587.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、よう笑うようになったね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、そうですか？」"
    $ kag_cm()
    $ kag_playse('3-0588.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。{w=0.4}会ったときはずーっとうつむいていて、元気なさそうやってんけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは……」"
    $ kag_cm()

label kag_a_b6_choices_ai02:
    $ kag_set_bookmark('あいこシナリオ選択肢02')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】みんなのおかげです。', current_stem='a_b6', storage=None, target='*choices_ai02-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】あいちゃんのおかげです。', current_stem='a_b6', storage=None, target='*choices_ai02-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_a_b6_choices_ai02__dash__1:
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg084', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_f.judgeflag += 1
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0589.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「自分ではよくわからないですけど、あいちゃんがそう思うなら、{w=0.4}わたしは出会ったときのわたしと、何かちがうのかも知れないです」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0590.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_a_b6_after_choices_ai02
    call kag_s_wait

label kag_a_b6_choices_ai02__dash__2:
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg084', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0591.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなことない。{w=0.4}りずむちゃん自身の力や」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_cm()
    $ kag_playse('3-0592.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もし、あたしが少しでもりずむちゃんの力になれてるんやったら、{w=0.4}めちゃうれしいことやけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしは、あいちゃんに会えてよかったって思います」"
    $ kag_cm()
    $ kag_playse('3-0593.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_a_b6_after_choices_ai02
    call kag_s_wait

label kag_a_b6_after_choices_ai02:
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん。あの……{w=0.8}よかったらだけど、{w=0.4}わたしの友だちになってください」"
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0594.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何を今さら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0595.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしらはもう友だちやで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}ありがとう……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg016', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b6_ai__dash__06_05:
    $ kag_set_bookmark('「６日目」ステキな海！そしてステキな・・・')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「イカとタコも魚屋で見れて、今日はとっても楽しかったです！」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0596.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そらあたしも連れてきたかいあったってもんやわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0173.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あいちゃん、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0597.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ももちゃん。{w=0.4}あれ、玉木もどしたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0061.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ぐうぜんそこでいっしょになったんですのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0174.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだ玉木さん！{w=0.4}この子は……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こんにちは。{w=0.4}玉木さん」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0175.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「へ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0062.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「こんにちは。{w=0.4}りずむさんたちはどこかへお出かけでしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。"
    extend "あいちゃんと海を見に行ってました」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0176.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「２人とも、いつ知り合ったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0063.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「この間、学校の近くでお会いしましたわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0177.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「なんだ。{w=0.4}そうだったんだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0598.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「やっぱり変わったな。{w=0.4}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0599.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ううん、ひとりごとや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0695.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ちょっとちょっとみんな～大変だよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0064.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あら、春風さん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0696.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、玉木……{w=0.45}ってそれどこじゃないよ！{w=0.4}りずむちゃん、あいちゃんテレビ見なかったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0600.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何が？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0697.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今ニュースでさ、海岸にイカとタコの大群が押し寄せてきて、{w=0.4}あたり一面イカタコだらけだって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ！」"
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0601.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっちゃ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、これって……」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0602.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「今さら魔法がきいてきたみたいやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0178.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「２人ともどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、いえ」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0603.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ～何でもない何でもない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0065.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「飛鳥さん。{w=0.4}そろそろ行きません？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0179.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0698.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どこへ行くの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0066.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「飛鳥さんを、我が家のディナーにご招待してるんですのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0180.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それじゃ、また明日ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0699.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ほんじゃね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0604.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん。{w=0.4}あたしらも、もっかい行ってこよか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0700.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「イカタコ見に行くんなら、あたしも行くよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0605.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、見に行くんやのうて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「実は……」"
    $ kag_cm()
    "こんな時ばっかり、わたしの魔法は効き目バツグンだ。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.a6_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_a_b7_gamestart
    return
