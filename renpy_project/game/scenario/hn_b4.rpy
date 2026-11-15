# Auto-generated from 06. hana/hn_B4.ks by tools/transpile_ks.py
label kag_hn_b4:

label kag_hn_b4_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hana.tlg', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hn_b4_hn__dash__04_00:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0759.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんなに集まってもらったのは他でもないわ。{w=0.4}\n今日は何の日かわかるわね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0065.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0760.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃん？{w=0.4}何の日？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん。{w=0.4}今日はバトルレンジャーの放送日だね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.2.ogg', buf=1)
    $ kag_cm()
    $ kag_wait(1500, canskip=True)
    $ kag_resumebgm()
    $ kag_drawchar('o_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0761.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ど、どれみちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えっ？{w=0.4}ちがうの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0979.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ちゃうやろ！{w=0.4}今日は１ヶ月に１回の」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0675.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「新月の日よ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そっかぁ！{w=0.4}新月かぁ！{w=0.4}じゃ今日はハナちゃんが赤ちゃんに戻る日だよね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0980.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そや！{w=0.4}せやから、赤ちゃんに戻ったハナちゃんのお世話を、誰がするかを決めるんやろ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0762.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0561.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はいは～い！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0562.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん、りずむがいいなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええっ！」"
    $ kag_cm()
    $ kag_playse('6-0563.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「今日の夜は、りずむといっしょがいい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、ええと」"
    $ kag_cm()
    $ kag_playse('6-0564.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「じゃあ、きまり！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0066.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「え、ええぇ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_01:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "結局ハナちゃんの希望で、今夜のハナちゃんの世話はわたしに決まり、突然だけど、わたしのママ修行が始まろうとしていた。"
    $ kag_cm()
    "これも、女王様の言いつけ通りなのかなあ？"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1078.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあ、りずむちゃん。{w=0.4}今日はハナちゃんのお世話のやり方を教えるからね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0565.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はいはいは～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1079.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はい！{w=0.4}ハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0566.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんもりずむといっしょに、\n{w=0.4}お勉強したいで～す！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0981.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お世話される本人が、{w=0.4}お世話のやり方を勉強したいつってもなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0619.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「なんか不思議な感じがするよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0763.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも、ハナちゃんがあえて逆の立場を勉強することで、{w=0.4}りずむちゃんの負担がへるかもしれないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1080.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なるほど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0676.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「いい機会だから、ハナちゃんもいっしょに勉強してもらおうかしら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0567.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}ハナちゃん、がんばる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0983.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「とりあえず、りずむちゃんに何を教えるか考えよっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_02:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0620.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん！{w=0.4}まずはあたしが、ハナちゃんのママになる３つの心がまえを教えるよっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よろしくお願いします」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0568.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「もも～よろしく～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0621.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「コホン。{w=0.4}ひと～つ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0622.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ノォッ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0623.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Repeat after me！！{w=0.4}二人とも、わたしの言ったことをまねして言って！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい！」"
    $ kag_cm()
    $ kag_playse('5-0624.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「コホン！{w=0.4}ひと～つ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ひと～つ」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0569.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ひと～つ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0625.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ママには、{w=0.5}何ごとにも動じない、{w=0.5}強い根性が必要である！」{nw}"
    $ kag_history_opt(output=False, enabled=None)
    $ kag_waitclick()
    $ kag_history_opt(output=True, enabled=None)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0570.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「何ごとにも動じない、強い根性が必要である」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こ、根性……って？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0626.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ふた～つ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふた～つ」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0571.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ふた～つ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0627.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「いつも、{w=0.5}赤ちゃんの立場にたって行動することが大切である！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0572.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「いつも、赤ちゃんの立場にたって行動することが大切である」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0628.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「みぃ～っつ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みぃ～っつ！」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0573.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「みぃ～っつ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0629.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ハナちゃんを心から愛してあげること。{w=0.4}これがいちばん大事だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0574.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「てへへ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0630.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わかった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0575.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「は～い！{w=0.4}ハナちゃん、ハナちゃんのこと愛するね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0764.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それでは、次はわたしとはづきちゃんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0677.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「育児の基本的な知識について教えるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0576.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「は～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よろしくお願いします」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0765.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「まず、ハナちゃんの食事について！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    "忘れないように、わたしはメモを取り出した。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_03:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    "数分後……"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0678.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ということで、ハナちゃんには離乳食を作ってあげてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0766.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「食事の量と時間もきちんと決めて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0577.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「スゥ～スゥ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0679.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ハ、ハナちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0578.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「んあ？{w=0.4}ん～。ハナちゃんねむい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0767.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「寝ちゃダメよ、ハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0984.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「しゃあない。{w=0.4}ハナちゃんは寝かしといて次行こか。"
    $ kag_playse('3-0984.2', buf=0, loop=False)
    extend "次はあたしとどれみちゃんで……{w=0.55}ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-1081.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う～ん、う～ん。もう、たべられましぇ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.2.ogg', buf=1)
    $ kag_wait(1000, canskip=True)
    $ kag_resumebgm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0985.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃんも寝とったんか～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1082.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん、あれ？{w=0.4}どうしたのあいちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0986.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……{w=0.4}ほ、ほな気を取り直して、{w=0.4}あたしとどれみちゃんでみっちり、ハナちゃんについてお勉強や！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1083.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃんをあやす時の、とっておきの技を教えてあげるね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1084.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「これさあ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "バッ！"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-1085.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うに～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_playse('6-0579.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「むにゃむにゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1086.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、あれ。{w=0.4}ちがったかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1087.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「こ、こうだ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "バッ！"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-1088.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うにょ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんが人指し指で鼻を上に押し上げる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、ええと…………」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1089.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃ、じゃあこれだ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1090.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日の夕ご飯はステーキだって！{w=0.4}きゃ～ステキ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('2-0680.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「くっくっくっくっく……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0631.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「くっくっくっくっく……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0987.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もぅ～どれみちゃん、{w=0.4}アカンアカン！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1091.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え……{w=0.4}\nだって前はこれでハナちゃん、泣きやんだよ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0988.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お笑いは常に進歩してんねん！{w=0.4}いつまでも同じ芸で通用すると思ったら大まちがいやで！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0768.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お笑いって、ハナちゃんについてお勉強だったんじゃないの……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg015', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_04:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1092.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ということで、りずむちゃん。{w=0.4}いちおうあたしたちが教えられることは全部教えたけど、どう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。{w=0.4}たぶん……」"
    $ kag_cm()
    "う、う～ん。"
    $ kag_cm()
    "何だかわかったような、わからなかったような……"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0989.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ま、まあ、何か困ったことがあったらすぐ呼んでな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1093.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃんも、{w=0.4}あんまりりずむちゃんに迷惑かけちゃダメだよ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0580.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「は～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0769.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「今から心配しても始まらないわ。{w=0.4}今日はりずむちゃんを信じてまかせましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1094.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、そうだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0632.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それじゃあ、あたしたちはそろそろ帰るね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0681.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、がんばってね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}がんばります！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "ＭＡＨＯ堂から出て行くどれみちゃんたちに元気よく答えた。"
    extend "\nそしてお店は、ハナちゃんとわたしの二人だけになる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それではハナちゃん、{w=0.4}よろしくね」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0581.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg019', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_wait(1500, canskip=True)
    $ kag_changetype('cross', '06ハナ-04-1', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghn2=1
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_05:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_playse('6-0582.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わ～ん！{w=0.4}あ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「う、うぅ」"
    $ kag_cm()
    "困ったなぁ。"
    extend "とりあえずだっこしてみたけど……"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どどどどうしよう」"
    $ kag_cm()
    "ハナちゃんは赤ん坊に戻ったとたん、ずっと泣きっぱなしだ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんどうしたの？{w=0.4}何で泣いてるの？」"
    $ kag_cm()
    $ kag_playse('6-0583.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わぁ～ん。{w=0.4}マンマ、マンマ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「マンマ……？{w=0.4}そうか！{w=0.4}ご飯のことですね！」"
    $ kag_cm()
    $ kag_playse('6-0584.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うううぅ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "よかった。少し泣きやんでくれた。"
    $ kag_cm()
    "ちょっとはわたしの言葉がわかるみたい。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「やっぱり、そうなんですね！{w=0.4}それじゃあ」"
    $ kag_cm()
    "メモ帳を取り出し、はづきちゃんとおんぷちゃんから教わった離乳食のレシピを見る。"
    $ kag_cm()
    "ハナちゃん、お腹をすかせてるから、すぐに作れそうな物の方がいいよね。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれがいいかなぁ……」"
    $ kag_cm()
    $ kag_playse('6-0585.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「んん～！{w=0.4}ぶ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、な～に？」"
    $ kag_cm()
    $ kag_playse('6-0586.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「しゅて～き！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ス、ステーキは、まだ食べられないんじゃ……」"
    $ kag_cm()
    $ kag_playse('6-0587.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「しゅて～きっ！{w=0.4}うわ～ん！！{w=0.4}あああ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わわわっ！{w=0.4}ハナちゃん、泣かないでください～」"
    $ kag_cm()
    $ kag_playse('6-0588.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あぁぁあん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしたら……{w=0.6}あっ！{w=0.4}そうだ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、こっち見て」"
    $ kag_cm()
    $ kag_playse('6-0589.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わぁぁん……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'black', time_ms=500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_set_next_indent('りずむ「')
    "りずむ「バァ！」"
    $ kag_cm()
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「や、やりました！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', '06ハナ-04-1', time_ms=500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_playse('6-0590.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「う……{w=0.55}うわぁぁぁぁん！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ど、どれみちゃ～ん、{w=0.4}\nぜんぜんうまくいかないじゃないですか～」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！{w=0.4}そうか！」"
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('sepia', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_frmdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('3-0988.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お笑いは常に進歩してんねん！{w=0.4}いつまでも同じ芸で通用すると思ったら大まちがいやで！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', '06ハナ-04-1', time_ms=500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_06:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_resumebgm()
    "お笑いは常に進歩してるのよね。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん？」"
    $ kag_cm()
    $ kag_playse('6-0590.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「カエルがころんでヒックリカエル！{w=0.4}そんなバナナ！？」"
    $ kag_cm()
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「な、なんでやねん、なんでやねん……」"
    $ kag_cm()
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「…………」"
    $ kag_cm()
    "つぶらな瞳でわたしを見つめるハナちゃん。"
    extend "顔から火が出そう。"
    $ kag_cm()
    "イヤな汗が出てきた。"
    $ kag_cm()
    "何だか耳まで熱くなってきた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、なんかすごくはずした気がする……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'white', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', '06ハナ-04-2', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('6-0591.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「きゃっきゃっ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふうぅ……{w=0.55}よ、よかったです……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それじゃあ、わたし。{w=0.4}食事作ってきますね！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_07:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すぐ作りますから、ここで待っていてください」"
    $ kag_cm()
    $ kag_playse('6-0592.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うふふっ」"
    $ kag_cm()
    $ kag_playse('6-0593.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ん～……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ？……{w=0.55}ハナちゃん？」"
    $ kag_cm()
    $ kag_set_next_indent('[[playbgm storage=m52\\"]りずむ「')
    "[[playbgm storage=m52\"]りずむ「ハナちゃん？ハナちゃんはどこ！？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_08:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃ～ん！{w=0.4}どこ～？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ど、どこに行っちゃったんだろう……」"
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('sepia', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_frmdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('2-0682.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ハナちゃんからは、目をはなさないこと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('4-0770.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ハナちゃんは歩けるから、{w=0.4}ちょっと目をはなすとすぐにいなくなっちゃうの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0770.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「だから、なるべくいっしょにいてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_resumebgm()
    "せっかくはづきちゃんやおんぷちゃんが注意してくれたのに。"
    $ kag_cm()
    "せっかく、みんながわたしを信じてまかせてくれたのに。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんに何かあったら……」"
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_sound_se('se-005.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('6-0594.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「きゃっきゃっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ハナちゃんが、お店に置いてあるアクセサリーで遊んでいる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……{w=0.6}よかったあ～」"
    $ kag_cm()
    $ kag_playse('6-0595.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よかった」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あは……{w=0.6}何でもないですよ」"
    $ kag_cm()
    "安心して、わたしは思わず涙ぐんでしまった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もう勝手にいなくなっちゃダメですよ？」"
    $ kag_cm()
    $ kag_playse('6-0596.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg010', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_09:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_playbgm('m413a', loop=True)
    $ kag_playse('6-0597.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「すぅ～すぅ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふう、つかれた……」"
    $ kag_cm()
    "さっきまでハナちゃんに読んであげていた絵本を、本棚へと戻す。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「赤ちゃんのお世話がこんなに大変なんて……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でもやっぱり、ハナちゃんってかわいいな。{w=0.4}ふふっ」"
    $ kag_cm()
    $ kag_playse('6-0598.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ん～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ……{w=0.6}すみません……{w=0.55}起こしてしまいましたか？」"
    $ kag_cm()
    $ kag_playse('6-0599.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ん～あう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「な～に？{w=0.4}ハナちゃん？」"
    $ kag_cm()
    $ kag_playse('6-0600.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あううぅ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ん？」"
    $ kag_cm()
    $ kag_playse('6-0601.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ～がと、ママ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '06ハナ-04-2', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghn3=1
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_10:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、{w=0.7}ママってなんか、うれしいです……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('sepia', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_frmdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('5-0633.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ハナちゃんを心から愛してあげること。{w=0.4}これがいちばん大事だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg010', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……」"
    $ kag_cm()
    "わたしは、しばらくハナちゃんの寝顔を見つめていた。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b4_hn__dash__04_11:
    $ kag_set_bookmark('「４日目」りずむママのかつやく')
    $ kag_cm()
    $ kag_sound_se('se-024', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "誰？こんな時間に……"
    $ kag_cm()
    $ kag_playse('1-1095.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ちーす」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ、どれみちゃん。{w=0.4}\n……みなさんまでどうしたんです？」"
    $ kag_cm()
    $ kag_drawchar('d_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1096.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ちょっと様子を見たくなっちゃってさ。{w=0.4}どうだった？りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「大変でしたけど、なんとかなりました」"
    $ kag_cm()
    $ kag_drawchar('hz_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0683.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「よかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0634.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「でも半日教えただけで、しっかりハナちゃんのめんどうを見られるなんてすごいね～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0991.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0771.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、お世話の才能があるのかもね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんな。{w=0.4}わたしなんてまだまだです」"
    $ kag_cm()
    $ kag_drawchar('d_m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1097.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ううん！{w=0.4}きっとおんぷちゃんの言う通りだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0684.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんやさしくて、いつも一生懸命だもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1098.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん起きてきたら、りずむちゃんにお礼を言ってもらわなきゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん。{w=0.4}そんなことないです」"
    $ kag_cm()
    "わたしの方こそ、ありがとう。ハナちゃん。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hn4_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hn_b5_gamestart
    return
