# Auto-generated from 03. ai/a_B2.ks by tools/transpile_ks.py
label kag_a_b2:

label kag_a_b2_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_ai.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg004', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_a_b2_ai__dash__02_00:
    $ kag_set_bookmark('「２日目」思い出の絵本')
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0334.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ええ！{w=0.4}りずむちゃん寄宿舎暮らしなん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんなに珍しいですか？」"
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0335.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしらと大して年変われへんのに、大変やなぁ。"
    $ kag_playse('3-0335.2', buf=0, loop=False)
    extend "おまけにひとり部屋やったら退屈ちゃうの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そういうときはいつも本を読んでいるんで、そんなに退屈じゃないですよ」"
    $ kag_cm()
    $ kag_playse('3-0336.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんは本とか好きなん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}でも、むずかしい本とかじゃなくて、{w=0.4}小さいころに読んだ絵本を読み返すのが好きなんです」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0337.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ～それわかる。{w=0.4}ひさしぶりに読むと、ごっつうなつかしい感じするもんな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃんにもそんな絵本ってあるんですか？」"
    $ kag_cm()
    $ kag_playse('3-0338.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あるある！{w=0.4}それやったらどうせ午後は、りずむちゃんに学校を案内することになってるから、{w=0.4}図書室で絵本見したるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントですか！{w=0.4}やった！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg093', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b2_ai__dash__02_01:
    $ kag_set_bookmark('「２日目」思い出の絵本')
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0339.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ところで」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('3-0340.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、寄宿舎暮らししてるんやったら、{w=0.4}毎日家事とか大変やろ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、ええまあ」"
    $ kag_cm()
    $ kag_playse('3-0341.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしはお父ちゃんと２人でやってるから、{w=0.4}まだ楽な方やけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか？{w=0.4}だったら、あいちゃんの方が大変だと思うんですけど」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0342.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「え？{w=0.4}ってことは、料理は……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「決まった時間に食堂に行けば、食べられますから」"
    $ kag_cm()
    $ kag_playse('3-0343.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうなんや。{w=0.4}ほな、洗濯とかは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔法で」"
    $ kag_cm()
    $ kag_playse('3-0344.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうじは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ですから、魔法で……」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0345.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もしかして、部屋の片づけとかも？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もちろん、魔法でやりますよ」"
    $ kag_cm()
    $ kag_playse('3-0346.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なんか、魔法ばっかりやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そりゃまあ、魔女ですから」"
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0052.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「あら？{w=0.4}妹尾さん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0347.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「玉木。{w=0.4}学校行ってたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0053.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ええ。{w=0.4}大した用じゃないんだけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('8-0053.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ところで……{w=0.65}その妹尾さんの後ろにいらっしゃるのはどなたですの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、あ」"
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0054.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「このあたりじゃ見ないですけど……{w=0.5}\nどこの小学校かしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの……{w=0.6}わたし……」"
    $ kag_cm()
    "ううう、ちょっと苦手なタイプかも。"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0348.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「この子はりずむちゃんって言うて、\nえっと……{w=0.55}ハナちゃんのいとこや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0055.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「そうだったんですの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0349.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「玉木～。{w=0.4}いきなり『どこの小学校かしら？』はないやろ。{w=0.4}りずむちゃんビビってるやんか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0056.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ワ、ワタクシは別に、こわがらせるつもりはありませんわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううぅ……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0350.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0057.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ハア……{w=0.55}ちょっと、りずむさん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0058.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「申し遅れましたけど、ワタクシは玉木麗香。{w=0.4}美空第一小学校の児童会長ですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0058.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「こわがることなんて、な～んにもありませんのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。すみません」"
    $ kag_cm()
    $ kag_playse('8-0059.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「これでよくって？{w=0.4}妹尾さん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0351.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0060.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「それじゃあ、ワタクシはそろそろいきますわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0352.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。{w=0.4}またな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg064', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b2_ai__dash__02_02:
    $ kag_set_bookmark('「２日目」思い出の絵本')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0353.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ひととおり回ったから、図書室でも行こか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あいちゃんに連れられ、学校の中を案内してもらう。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}あ、はい。……{w=0.4}そうですね」"
    $ kag_cm()
    "へええ、人間界の学校は広いんだなあ。"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0354.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなにキョロキョロしてたら、迷子になるで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、あ、すみません」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0355.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こっちの学校は、やっぱし珍しい？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「その、ふだんって、ものすごくいっぱい人がいるんですか？」"
    $ kag_cm()
    $ kag_playse('3-0356.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。{w=0.4}入って来た、げた箱のトコなんて、朝は人でいっぱいやで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、ちょっと苦手かも……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0357.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「別に転校するわけちゃうねんから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そうですよね」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0358.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんがあっちで読んでた本って、どんなん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええと、魔女がひとりでいろんな所に旅をして、{w=0.4}いろんな人に助けられて、目指した場所にたどり着くお話とか」"
    $ kag_cm()
    $ kag_playse('3-0359.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ふーん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みにくい魔女ガエルが、呪いがとけたら実はとても美しいお姫さまだったとか」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0360.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こっちでも似たような話あるな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、苦労したり大変な目にあったりしたけど、{w=0.4}最後は幸せになれるお話ってとても好きなんです」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0361.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そら苦労したら、むくわれたいもんな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「逆に、うまくいってたのに、全部ダメになっちゃって、{w=0.4}それで終わっちゃうお話とか読むと、もう一晩中気になって眠れないんですよ」"
    $ kag_cm()
    $ kag_playse('3-0362.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あるある。{w=0.4}あれからどうなったか考えただけで寝られへんとかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「絵本に出てくるお菓子がすごくおいしそうで、ママにねだって作ってもらったり」"
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そのお菓子が似てなくて……{w=0.55}あれ？あいちゃん？」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0363.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ん、ああ、何でもない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「他には……{w=0.55}あ、そうそう」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0363.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ずっと気になってる本があったんですよ。{w=0.4}保育園においてあったんですけど、表紙しかなくって、中が全部やぶけてて読めなくって」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0364.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そら気になるなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もう題名もおぼえてなくって。{w=0.4}どんなお話だったんだろう」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '03あいこ-02', time_ms=1000, bgcolor='0x000000')
    $ persistent.cga1=1
    $ kag_mesframe()
    $ kag_cm()

label kag_a_b2_ai__dash__02_03:
    $ kag_set_bookmark('「２日目」思い出の絵本')
    $ kag_cm()
    $ kag_playse('3-0365.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あった！{w=0.4}これこれ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へえ……」"
    $ kag_cm()
    "題名は『白雪姫』。表紙にはお姫さまの絵と、意地の悪そうな魔女が描かれている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「これって……{w=0.6}魔女？」"
    $ kag_cm()
    $ kag_playse('3-0366.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('3-0367.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや～小さいころ、お父ちゃんに読んでもらったのを思い出すわ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "美しいお姫さま、みにくい魔女。\nラストで魔女は退治される。"
    extend "お姫さまは王子さまと結ばれる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「う～ん」"
    $ kag_cm()
    $ kag_playse('3-0368.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どないしたん？{w=0.4}真剣な顔して」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}ええ。{w=0.4}この魔女が気になって」"
    $ kag_cm()
    $ kag_playse('3-0369.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お話の魔女がどうかした？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔法が使えるんだったら、何も白雪姫に毒入りのリンゴを食べさせなくたって、{w=0.4}魔法でキレイになればいいのにって思って」"
    $ kag_cm()
    $ kag_playse('3-0370.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あーそっかー。{w=0.4}考えたことなかったなー」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それに、どっちかって言うと、白雪姫って女王様みたいで、{w=0.4}なんかそう考えたら白雪姫が魔女になって……{w=0.55}\nあれ？ってなっちゃって」"
    $ kag_cm()
    $ kag_playse('3-0371.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あはは。{w=0.4}りずむちゃんやったらそう思うのもムリないかもな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みんなから愛されて、白雪姫っていいですね」"
    $ kag_cm()
    $ kag_playse('3-0372.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしなんてまるっきり逆で……」"
    $ kag_cm()
    $ kag_playse('3-0373.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなことないやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうでしょうか？」"
    $ kag_cm()
    $ kag_playse('3-0374.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんは悪い方に考えすぎや。"
    $ kag_playse('3-0374.2', buf=0, loop=False)
    extend "学校来るときに会った玉木かて、別にりずむちゃんがキライやのうて、ふだんからあの調子なだけやで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「玉木さんは……{w=0.55}その……」"
    $ kag_cm()
    $ kag_playse('3-0375.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ～気にしてる気にしてる」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「まあ、はい……」"
    $ kag_cm()
    $ kag_playse('3-0376.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もっとええ方に考えな。{w=0.4}そや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('3-0377.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしが小さいころ読んだ本は他にもあんねん。{w=0.4}これとか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ちょっと楽しそうですね」"
    $ kag_cm()
    $ kag_playse('3-0378.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「これはおもろいで～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg224', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b2_ai__dash__02_04:
    $ kag_set_bookmark('「２日目」思い出の絵本')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0379.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こっちの本もなかなかおもろいやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}それに、魔女界の絵本と似てるのがあったりで、ちょっと意外でした」"
    $ kag_cm()
    $ kag_playse('3-0380.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「魔女界の絵本も読んでみたいな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ＭＡＨＯ堂のわたしの部屋にあるから、\n貸しましょうか？」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0381.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ～でもあたし魔法文字読まれへんしなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「絵本ですから、文字が読めなくてもわかりますよ」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0382.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、そうか。{w=0.4}ほんならなんかオススメ１冊頼むわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b2_ai__dash__02_05:
    $ kag_set_bookmark('「２日目」思い出の絵本')
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0652.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おかえり、学校はどうだった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「楽しかったです。{w=0.4}図書室で人間界のいろんな本を読んでました」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0383.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんと、小さいころに読んだ本でもりあがってな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0653.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そっか～。{w=0.4}あたしもあるよ。{w=0.4}ほら、おまんじゅうをいっぱいもらうやつ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0384.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「『まんじゅうこわい』か～。{w=0.4}昔話やな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11y.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0654.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「他にも、ステーキがいっぱい出てくる話とかがさあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0469.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃんヨダレ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0385.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんな本あったかな……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0160.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたし、アメリカの絵本なら持ってるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0194.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ももちゃんそれ貸してくれる？\n{w=0.4}英語の勉強に使えそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0161.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん、いいよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさんそれぞれに、昔読んだ絵本があるんですね」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0386.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな。{w=0.4}それもふしぎなことに、細かいとこまでよう覚えてるもんやしな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0655.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだ！{w=0.4}宿題の読書感想文、ステーキのやつにしよう！」{nw}"
    $ kag_history_opt(output=False, enabled=None)
    $ kag_waitclick()
    $ kag_history_opt(output=True, enabled=None)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0387.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃん、絵本はアカンやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0162.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「関先生に『幼稚園からやりなおすか？』とか言われちゃうよ？きっと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0656.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ああ……{w=0.55}それは、マズイ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0388.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「さて、午後ぬけたぶん、ちょっと仕事しよか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('3-0389.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、あのへんの棚の整理でもしよか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg015', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b2_ai__dash__02_06:
    $ kag_set_bookmark('「２日目」思い出の絵本')
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0391.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほんじゃ、これ借りてくわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}帰るときまでに返してくれればいいですから」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0392.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ありがと。{w=0.4}ほなまたな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「また明日」"
    $ kag_cm()
    $ kag_playse('3-0393.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、そや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('3-0394.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「学校で言ってた、りずむちゃんが昔読まれへんかったって本、どんな表紙やった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですね……{w=0.6}お姫さまと、変な形の馬車が描いてありました」"
    $ kag_cm()
    $ kag_playse('3-0395.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なるほどな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうかしたんですか？」"
    $ kag_cm()
    $ kag_playse('3-0396.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ちょっと心当たりがあってな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ！{w=0.4}こっちにも似たような本があるんですか？」"
    $ kag_cm()
    $ kag_playse('3-0397.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ん、まあ、自信はないけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それって、学校の図書室にあるんですか？」"
    $ kag_cm()
    $ kag_playse('3-0398.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「図書室にもあるし、あたしも持ってる」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントですか！{w=0.4}か、貸してください」"
    $ kag_cm()
    $ kag_playse('3-0399.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「押し入れの奥の方にしまってあるから、すぐには貸されへんけど、{w=0.4}りずむちゃんがいる間にもっていくわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0400.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほなまた！」"
    $ kag_stopse(buf=0)
    $ kag_playse('se-020.ogg', buf=0, loop=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「また明日」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.a2_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_a_b3_gamestart
    return
