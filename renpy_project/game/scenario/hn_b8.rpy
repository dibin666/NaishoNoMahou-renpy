# Auto-generated from 06. hana/hn_B8.ks by tools/transpile_ks.py
label kag_hn_b8:

label kag_hn_b8_gamestart:
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
    $ kag_history_opt(output=True, enabled=None)

label kag_hn_b8_hn__dash__08_00:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    "お店の中では、みんながいつものように持ち場を決めて作業をしている。"
    $ kag_cm()
    "わたしはみんなにお願いして、ハナちゃんとビーズメーカーでアクセサリー作りをしていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('hn_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0742.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わ、わぁぁ～！{w=0.4}りずむ～すとっぷすとっぷ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？{w=0.4}……{w=0.5}あああぁ！」"
    $ kag_cm()
    "床の上には、とてつもなく長いアクセサリーが広がっていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「す、すみません」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0743.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_playse('6-0743.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「今日のりずむ、なんか変だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('6-0744.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんなことないですよ！あ、あああっ！」"
    $ kag_cm()
    $ kag_drawchar('hn_05.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいた！」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0745.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、やっぱり変だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「な、何でもないんです」"
    $ kag_cm()
    $ kag_drawchar('hn_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0746.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「む～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ただ……」"
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0747.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ。{w=0.4}何でもないです」"
    $ kag_cm()
    $ kag_drawchar('hn_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0748.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「むう～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_hn_b8_hn__dash__08_01:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1145.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや～やっぱり楽しみと言えば、ひと仕事終わった後の、おんぷちゃんに入れてもらったお茶だよねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0692.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「なんといってもこのひとときが一番よね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0646.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そのために仕事してるっちゅうても、{w=0.4}言いすぎやないな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0693.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう、あいちゃんったら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1011.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なはははは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0694.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ふふふふふ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……{w=0.55}で、あの二人、何かあったんやろか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0695.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「二人とも元気ないわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1146.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やっぱり、明日りずむちゃん帰っちゃうから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0647.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「落ちこんでるのかなぁ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0780.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんな、紅茶入れてきたわよ～{w=0.4}はい、どれみちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1147.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おんぷちゃん、ありがとう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0781.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はい、ももちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0648.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Thank you」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0782.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんとハナちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1148.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「二人とも自分の部屋にいるんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0783.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう。{w=0.4}じゃあわたし、りずむちゃんにお茶とお菓子を持っていくわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b8_hn__dash__08_02:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、何やってるんだろう」"
    $ kag_cm()
    "さっきのハナちゃんとのことを思い返した。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「考えたって何も変わらないのに……」"
    $ kag_cm()
    $ kag_sound_se('se-024', buf=1)
    $ kag_playse('4-0784.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、いる？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん？{w=0.4}はい……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0785.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お茶とお菓子、持ってきたわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうございます」"
    $ kag_cm()
    $ kag_playse('4-0786.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ねぇ、りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_playse('4-0787.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「明日、魔女界に帰っちゃうのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ……{w=0.65}そうですね」"
    $ kag_cm()
    $ kag_playse('4-0788.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんは、どう思ってるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どう、って？」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0789.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「今日になって、りずむちゃん元気なさそうだから。{w=0.4}とても帰りたいって感じに見えないのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')

label kag_hn_b8_choices_hn03:
    $ kag_set_bookmark('はなシナリオ選択肢03')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】帰りたくないです', current_stem='hn_b8', storage=None, target='*choices_hn03-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】そんなことはないです', current_stem='hn_b8', storage=None, target='*choices_hn03-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_hn_b8_choices_hn03__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag += 1
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}ホントは帰りたくないです。{w=0.4}わたし、ハナちゃんやみなさんと、ずっといっしょにいたいです」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0790.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあ、帰らなくてもいいんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ！？」"
    $ kag_cm()
    $ kag_playse('4-0791.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「きっと女王様に事情を説明すれば、ムリな話じゃないと思うけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そうでしょうか？」"
    $ kag_cm()
    $ kag_playse('4-0792.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんは、どうして人間界にいたいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは、ずっといっしょに……」"
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0793.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それだけ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_hn_b8_after_choices_hn03
    call kag_s_wait

label kag_hn_b8_choices_hn03__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんなことは……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0794.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあ、どうして元気がないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0795.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ハナちゃんも心配してたわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}わたし、帰りたくないです」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0796.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあ、帰らなくてもいいんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ！？」"
    $ kag_cm()
    $ kag_playse('4-0797.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「きっと女王様に事情を説明すれば、ムリな話じゃないと思うけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そうでしょうか？」"
    $ kag_cm()
    $ kag_playse('4-0798.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんは、どうして人間界にいたいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんやみなさんと、{w=0.4}ずっといっしょにいたいから……{w=0.55}です」"
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0799.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ふ～ん、本当にそれでいいんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_hn_b8_after_choices_hn03
    call kag_s_wait
    "【分岐終わり】{nw}"

label kag_hn_b8_after_choices_hn03:
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0800.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあ魔女界のみんなは、{w=0.4}りずむちゃんが魔女界から逃げ出したって思わない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんな」"
    $ kag_cm()
    $ kag_playse('4-0801.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ゴメンね、変なこと言っちゃって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ……」"
    $ kag_cm()
    $ kag_playse('4-0802.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でもね、{w=0.4}これだけはわかってほしいんだけど、{w=0.4}ハナちゃんもわたしもみんなも、{w=0.4}りずむちゃんにいつまでも笑顔でいてもらいたいの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0803.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ハナちゃんは、{w=0.4}りずむちゃんが笑顔じゃないと、{w=0.4}悲しむんじゃないかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そうかも、しれないですけど」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0804.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「元気出して。{w=0.4}今のままじゃ、来たときのりずむちゃんと何も変わらないわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何も……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0805.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それだけ言いたかったの。{w=0.4}それじゃあわたし、行くね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-031.1', buf=1)
    "確かに、おんぷちゃんの言ったとおりかも……。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_hn_b8_hn__dash__08_03:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1149.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おんぷちゃん、どうだった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0806.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、魔女界に帰りたくないって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「やっぱしな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1150.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0807.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でもね、相談には乗ったのはいいんだけど、{w=0.4}結局はりずむちゃんの問題だから、答えは自分で出してもらうしかないのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0696.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしたちはそれでいいかもしれないけど、{w=0.4}ハナちゃんはそうは思わないんじゃないかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1151.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ\t「')
    "どれみ	「そうだよね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0808.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ええ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg010', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b8_hn__dash__08_04:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん！」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0749.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何をしてるんですか？」"
    $ kag_cm()
    $ kag_playse('6-0750.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「アクセサリー作ってるの……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、ビーズ、長すぎじゃあないですか？」"
    $ kag_cm()
    $ kag_drawchar('hn_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0751.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えっ？{w=0.4}わわっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、手伝います！」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0752.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、元気出た？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}すみませんでした」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0753.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ううん！{w=0.4}えへへ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はりきってますね」"
    $ kag_cm()
    $ kag_playse('6-0754.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへへ～！{w=0.4}だってうれしいんだもん！{w=0.4}りずむが笑ってくれて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、そんなに暗かったですか？」"
    $ kag_cm()
    $ kag_drawchar('hn_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0755.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ん～こんな顔してたよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんが、ハナちゃんをあやす時の顔みたいだ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ！{w=0.4}そんな顔してましたか！？」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0756.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}あははは～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0757.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、そうだ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('6-0758.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あのね、今日、{w=0.4}りずむの部屋で寝てもいい？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_playse('6-0759.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「今日は、ずっとりずむのそばにいたいんだもん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0760.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ダメぇ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん！{w=0.4}とってもうれしいです！」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0761.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やったぁ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふふ」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_hn_b8_hn__dash__08_05:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0809.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃん、あいちゃん。{w=0.4}様子はどうだった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1152.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「声を聞いてると、どうやら解決したみたいだね！{w=0.35}二人とも」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1014.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0810.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう。{w=0.4}よかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0649.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「めでたしめでたし～だね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0697.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ふふふ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b8_hn__dash__08_06:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    $ kag_sound_se('se-024', buf=1)
    $ kag_stopse(buf=0)
    $ kag_set_next_indent('りずむ「')
    "りずむ「は～い！」"
    $ kag_cm()
    $ kag_playse('6-0762.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんだよ～{w=0.35}入っていい～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいですよ～」"
    $ kag_cm()
    $ kag_sound_se('se-006.1', buf=1)
    $ kag_stopse(buf=0)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、いらっしゃい」"
    $ kag_cm()
    $ kag_drawchar('hn_p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0763.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうぞ、今ハナちゃん用のふとんを出しますから」"
    $ kag_cm()
    $ kag_drawchar('hn_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0764.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ありがとう～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '06ハナ-08', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghn6=1
    $ kag_mesframe()

label kag_hn_b8_hn__dash__08_07:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    $ kag_playse('6-0765.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なあに？{w=0.4}ハナちゃん」"
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_playse('6-0766.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむは明日、魔女界に帰っちゃうんだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('6-0767.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そしたらハナちゃん、さみしくなっちゃうな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……{w=0.6}わたしもさみしいです」"
    $ kag_cm()
    $ kag_playse('6-0768.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「じゃあさ！{w=0.45}りずむ人間界に残ろうよ！{w=0.4}そうしたら、ずっとずっといっしょだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}ありがとう。{w=0.4}でも、でもね。{w=0.4}やっぱりわたし帰ります」"
    $ kag_cm()
    $ kag_playse('6-0769.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしもね、{w=0.4}ずっと人間界にいられたら、{w=0.65}ずっとハナちゃんたちといられたらって思ってたんです」"
    $ kag_cm()
    $ kag_playse('6-0770.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「じゃあ、どうして？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、わたしが笑ってうれしいって言ってくれましたよね」"
    $ kag_cm()
    $ kag_playse('6-0771.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いつでもハナちゃんの前では、{w=0.4}笑顔でいられるわたしになりたいから。{w=0.4}わたしは魔女界に帰ります」"
    $ kag_cm()
    $ kag_playse('6-0772.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむがそうしたいんなら……わかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも！{w=0.4}かならずまた会いに来ます。{w=0.4}きっとかならず」"
    $ kag_cm()
    $ kag_playse('6-0773.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.35}ハナちゃんたちも魔女界に行った時は、かならず会いに行くよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b8_hn__dash__08_08:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    $ kag_playbgm('m413a', loop=True)
    $ kag_drawchar('hn_p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0774.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('6-0775.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんね……{w=0.65}覚えてるんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_drawchar('hn_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0776.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんが、赤ちゃんになった時のこと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そうなんですか？」"
    $ kag_cm()
    $ kag_drawchar('hn_p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0777.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}ハッキリとは覚えてないけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0777.2', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「でも、りずむがハナちゃんをだっこしてくれた時、{w=0.4}すっごくあったかかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0777.3', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それだけは、はっきり覚えてるんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……」"
    $ kag_cm()
    $ kag_drawchar('hn_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0778.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん、すごくうれしかったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ハナちゃんがわたしをだきしめる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_playse('6-0779.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「だから、ありがとう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}ううぅ」"
    $ kag_cm()
    "ハナちゃんの前では、笑顔でいようって決めてたのに。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}んくっ」"
    $ kag_cm()
    "涙をこらえようとするけど、止まってくれない。"
    $ kag_cm()
    "どうしてこんなに、ハナちゃんはやさしくなれるんだろう"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしも病気になった時、{w=0.4}ハナちゃんが看病してくれて、すごくうれしかった。{w=0.4}だから、ありがとう……」"
    $ kag_cm()
    $ kag_drawchar('hn_p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0780.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、人間界に来てハナちゃんたちと出会えて、本当によかった」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg019', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b8_hn__dash__08_09:
    $ kag_set_bookmark('「８日目」ないしょのまほう')
    $ kag_cm()
    "雲ひとつない夜空。"
    $ kag_cm()
    "星たちの光は、やさしくＭＡＨＯ堂を照らしていた。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('bgm-v04', loop=True)
    $ kag_drawchar('hn_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0781.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへ。{w=0.4}泣いちゃったね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}でも、胸の中が、すごくあったかいです」"
    $ kag_cm()
    $ kag_drawchar('hn_p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0782.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}ハナちゃんも！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あのね、ハナちゃん」"
    $ kag_cm()
    $ kag_drawchar('hn_p_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0782.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「大好きです」"
    $ kag_cm()
    $ kag_drawchar('hn_p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0783.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えっ？{w=0.4}よく聞こえなかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何でもないです」"
    $ kag_cm()
    $ kag_drawchar('hn_p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0784.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「え～っ何て言ったの～？{w=0.4}もっかい言って～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ないしょです……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hn8_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hn_c_gamestart
    return
