# Auto-generated from 05. momo/m_B3.ks by tools/transpile_ks.py
label kag_m_b3:

label kag_m_b3_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_momo.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg012', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_m_b3_mo__dash__03_00:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ん……{w=0.65}ん～」"
    $ kag_cm()
    "わたしはいつもよりも早く目が覚めた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「朝……{w=0.55}こんなに早くに目が覚めちゃった……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「静か……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ……{w=0.45}これ、あいちゃんのアクセサリー。{w=0.4}こっちはおんぷちゃんのアクセサリーだ。{w=0.4}そしてこれはももちゃんの……{w=0.55}何だかすごく温かい感じがする」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、このキバツなアクセサリーは……{w=0.6}ふふふ」"
    $ kag_cm()
    "どれみちゃんのアクセサリーだ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あは……{w=0.6}わたしも人のことは言えないかな。{w=0.55}……あっ、そうだ！」"
    $ kag_cm()
    "そしてそのとなりにある、はじめて自分ひとりで作ったビーズのアクセサリーに目をやる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔法できれいに作り直せばいいのよね」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしの作ったアクセサリーをきれいにして！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'white', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_fadeoutbgm(1000)
    $ kag_changetype('cross', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b3_mo__dash__03_01:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ねぇ、ももちゃんは……？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0841.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おやつの準備してるんとちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0864.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だあああぁ～！{w=0.4}つかれたよぉ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0299.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんも～！{w=0.4}ちょっと休憩しようよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0338.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「はい！{w=0.4}みんなお待たせ～。お菓子作ってきたよぉ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0865.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おおぉ～！{w=0.4}待ってました！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0300.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おやつ～おやつ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0645.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ほらグッドタイミング」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0578.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うふふふ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_m_b3_mo__dash__03_02:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0866.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はぁぁ～{w=0.6}生き返ったよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0842.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「しゃあないなぁ～。{w=0.4}でもまだ仕事残ってんで？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0301.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えええ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0843.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃん、『えええ～』やあらへんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0302.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「へへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0646.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも、いいんじゃない？{w=0.4}休憩は必要だし、ももちゃんの新作もおいしいし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0579.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ホントよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0339.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「へへへ、ありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0867.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もう今から、お菓子屋さん開いても大丈夫なくらいおいしいよね～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0844.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「さっすが本物のパティシエのタマゴってとこやね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0340.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そんなにほめられると照れちゃうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃんて……{w=0.65}パティシエのタマゴなんですか？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0341.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うーん。{w=0.4}タマゴって言うか、将来は、お菓子屋でパティシエもいいかな～って思ってるんだけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0868.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうそう！{w=0.4}それで、あたしの夢が、そのももちゃんのお店でいっぱいお菓子を食べることなんだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0845.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「食べるのが専門かい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こんなにおいしいお菓子、{w=0.4}どうやったら作れるんだろ……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()

label kag_m_b3_mo__dash__03_03:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0580.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そろそろ……{w=0.65}お仕事始めない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0846.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「しゃべってたら、時間たつの早いな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0647.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ほら、どれみちゃんにハナちゃん、{w=0.4}元気出して！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0870.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お～……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0303.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「お～……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ねぇ、ももちゃん！」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0342.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの、お菓子作り、わたしに教えてくれませんか？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0343.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！{w=0.4}いいよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとう！」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0871.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ええ！{w=0.4}じゃあ、あたしもお菓子作り……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0847.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃんは、去年いっぱいやったやろ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0872.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0304.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんは初めてだから、ハナちゃんもお菓子作りしたいな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0581.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ハナちゃんは食べるのが専門でしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0305.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「え、えへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b3_mo__dash__03_04:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0344.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうそう、生地はやさしい気持ちでたくさん混ぜれば、{w=0.4}その分だけふんわりしたスポンジが出来るんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_playse('5-0345.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それで……{w=0.55}できた生地を型に流し込んで……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_playse('5-0346.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それをオーブンで焼くんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0347.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ん？……{w=0.8}りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0348.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そ、そんなにいっぱいがんばらなくても……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え！{w=0.4}ま、まずいでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0349.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うううん、{w=0.4}まずくはないけど、もっとリラックスしようよ。{w=0.4}まずお菓子づくりは楽しくないとね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}なるほど」"
    $ kag_cm()
    "わたしはメモ帳に『◎お菓子づくりは楽しく』と書いた。"
    $ kag_cm()
    $ kag_playse('5-0350.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあこのスポンジの生地をオーブンに入れてみて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    "わたしは小走りになってスポンジの生地をオーブンへと運ぼうとした。"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0351.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん！{w=0.4}そこ、段になってるから気をつけて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？{w=0.4}わ、わ、わあぁっ」"
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_stopbgm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('down', 'black', time_ms=800, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「い……{w=0.55}いたた」"
    $ kag_cm()
    $ kag_playse('5-0352.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b3_mo__dash__03_05:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。大丈夫です……{w=0.65}ああっ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、スポンジが！」"
    $ kag_cm()
    "わたしが転んだ少し先。床に落ちてグチャグチャになったスポンジの生地が……。"
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0353.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「だ、大丈夫だよ！{w=0.4}また作ればいいよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ……{w=0.55}わたし……{w=0.5}直します！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「落としたスポンジの生地を直して！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'white', time_ms=500, bgcolor='0x000000')
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    "床に落ちてぐしゃぐしゃになったスポンジが元通りになる。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだ！{w=0.4}どうせなら魔法で焼いちゃいましょう」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0354.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「スポンジの生地よ、焼き上がれ！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'white', time_ms=500, bgcolor='0x000000')
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    "さらに、液体だったスポンジがふっくらと焼きあがった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「これで、オーブンで焼く手間がはぶけましたね」"
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん？」"
    $ kag_cm()
    $ kag_set_next_indent('ももこ「')
    "ももこ「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    "どうしたんだろ？\nわたし何かまずいことしたかな？"
    $ kag_cm()
    $ kag_playse('5-0355.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……{w=0.55}さっき、わたしのお菓子おいしいって言ってくれたよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0356.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「魔法もいいんだけどね。{w=0.4}使わないで作ったお菓子だっておいしいんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、{w=0.4}それって、どういうことでしょうか？」"
    $ kag_cm()
    $ kag_playse('5-0357.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「お菓子作りで大事なことって、{w=0.4}食べてくれる人に、おいしく食べてもらいたいって思う気持ちなんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「気持ち……？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0358.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん。{w=0.4}だから、ただ魔法を使ってケーキは作れても、{w=0.4}気持ちがこもってないとおいしさはぜんぜんちがうんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか……？」"
    $ kag_cm()
    $ kag_playse('5-0359.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ためしに、今からもう１回ケーキを作ろうよ。{w=0.4}きっとりずむちゃんにもわかるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_cm()

label kag_m_b3_mo__dash__03_06:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0848.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「２人とも、おつかれさ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0648.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お菓子作りどうだった、りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「う……{w=0.6}うん」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0873.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「い、いや～{w=0.45}失敗は誰にでもつきものさ～！{w=0.4}気にすることないって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0307.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみは、失敗しすぎだけどね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0582.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ふふふっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_12.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0874.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぶっぶのぶ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0360.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「失敗なんてしてないよ？……{w=0.4}りずむちゃんと一緒に色々ためしながらケーキ作ってたんだ。"
    $ kag_playse('5-0360.2', buf=0, loop=False)
    extend "それで、これからみんなに試食してもらって意見を聞かせてもらいたいんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0308.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わぁ～い！わぁ～い！{w=0.4}ししょく、ししょく～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0309.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「で、ししょくってなに？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0649.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「た、ためしに食べてみることよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0310.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おおお！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、お願いできますか……？」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0583.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もちろん、ＯＫよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0875.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まっかせといて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「で、ではこっちの方から……」"
    $ kag_cm()
    "わたしの持ってきたケーキをみんなが試食する。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(800, canskip=True)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0650.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「おいしい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0850.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん！なかなかいけんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0311.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おいしい～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0361.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それでね、今度は……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0362.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「こっちのケーキも食べてほしいの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0312.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ケーキたくさん！{w=0.4}うっれしいな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0876.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「こっちのも食べていいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0363.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうでしょうか……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(800, canskip=True)
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0876.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お、おいしい～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え！？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0650.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「さっきのもおいしかったけど、{w=0.4}こっちの方がもっとおいしいわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0850.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0583.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「口ではうまく伝えられないけど、{w=0.4}後の方がおいしいのはたしかよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0312.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんはどっちも好き！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0651.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それで、この２つを食べくらべてどうするの……{w=0.5}って、あれ？{w=0.4}りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0877.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ねぇ、ももちゃん。{w=0.4}これって……{w=0.55}あ、あれ？{w=0.4}いない？？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b3_mo__dash__03_07:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「作り方は同じだったのに……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0364.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「最初にみんなに食べてもらったのがさっき、わたしが魔法で作ったケーキ。{w=0.4}後に食べてもらったのが一から作った手作りのケーキ……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「材料もすべていっしょだったのに……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0365.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしがお菓子作りで一番気をつけてること」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それって……」"
    $ kag_cm()

label kag_m_b3_choices_momo01:
    $ kag_set_bookmark('ももこシナリオ選択肢01')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】気持ちをこめること', current_stem='m_b3', storage=None, target='*choices_momo01-01', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】魔法を使わないこと', current_stem='m_b3', storage=None, target='*choices_momo01-02', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_m_b3_choices_momo01__dash__01:
    $ kag_cm()
    $ kag_f.judgeflag=1
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0366.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「YES！{w=0.4}その通り！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_m_b3_after_choices_momo01
    call kag_s_wait

label kag_m_b3_choices_momo01__dash__02:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0367.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うーん、ちょっとちがうかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ……」"
    $ kag_cm()
    jump kag_m_b3_after_choices_momo01
    call kag_s_wait
    "【分岐終わり】{nw}"

label kag_m_b3_after_choices_momo01:
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0368.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「マジョモンローに言われたんだ、『お菓子にこめた気持ちは、必ず食べた人の心に伝わる』」"
    $ kag_cm()
    $ kag_playse('5-0368.2', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「『たとえ形が悪くても、気持ちがこもっていればどんなお菓子もおいしいよ』って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('5-0369.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あたしは思うんだ。魔法でお菓子はかんたんに作れるけど、気持ちをこめたお菓子は、もっとおいしくなれるんじゃないかって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん……」"
    $ kag_cm()
    $ kag_playse('5-0370.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うまく言えないんだけど、わかってもらえた？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ここで初めて、ももちゃんが言いたいことがわかった。"
    $ kag_cm()
    "わたし、せっかくももちゃんにお菓子作りを教えてもらっていたのに、一番大事なことをやろうとしてなかったんだって。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん。{w=0.4}ごめんなさい」"
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0371.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あっ！{w=0.4}あやまらなくてもいいよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん、{w=0.4}せっかくももちゃんと作ったケーキ、ダメにしちゃったから」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0372.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そんなことないよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_cm()
    $ kag_playse('5-0373.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「作り直した方のケーキだって、みんなよろこんでたじゃない。"
    $ kag_playse('5-0373.2', buf=0, loop=False)
    extend "そうだ！今から、もっともっといろんなお菓子の作り方教えるね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_playse('5-0374.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あっ！{w=0.4}でも、やっぱり明日からにしよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ。{w=0.4}ど、どうして？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0375.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「だって、今日はみんないっぱいお菓子を食べたから、おなかいっぱいだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ……{w=0.55}そうですね！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)

label kag_m_b3_mo__dash__03_08:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg237', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m413a', loop=True)
    "わたしが今朝、魔法で直した自分の作ったアクセサリーが置いてあるケースの前に立つ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「このアクセサリーだって、もっときれいになるよね」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「アクセサリーを元に戻して！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん。もう一回さいしょからやってみようっと」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg237', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b3_mo__dash__03_09:
    $ kag_set_bookmark('「３日目」心をこめて・・・')
    $ kag_cm()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「心をこめて……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「大切に思う心……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……わたしの気持ちが伝わりますように」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.m3_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_m_b4_gamestart
    return
