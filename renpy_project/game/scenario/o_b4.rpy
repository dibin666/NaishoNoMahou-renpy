# Auto-generated from 04. onpu/o_B4.ks by tools/transpile_ks.py
label kag_o_b4:

label kag_o_b4_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_onpu.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_o_b4_op__dash__04_00:
    $ kag_set_bookmark('「４日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    "午後３時。"
    extend "ＭＡＨＯ堂はおやつの時間。"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0229.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「お待たせ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0771.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「わぁ～おいしそう～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0230.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「今日はわたしの特製クッキーだよ。{w=0.4}今朝うちで焼いてきたんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0265.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「いっただきま～す！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おいしいです～」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0767.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマや。{w=0.4}ももちゃん、また腕あげたんとちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0231.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「へへへ、ありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0530.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ももちゃんのお菓子は、おいしすぎてつい食べ過ぎちゃうのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「マジョバニラさんのお店で食べたクッキーに、ちょっと似てますね」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0232.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「本当？{w=0.4}そう言ってもらえるとうれしいなあ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0772.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや～この３時のおやつのために生きてるって感じだよね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0768.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃ～ん。{w=0.4}しあわせやって言いたいのはわかるけど、まだ今日の仕事残ってんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0773.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いいじゃん、{w=0.4}とりあえず今の休憩のひとときを楽しもうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0769.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それもそやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    "さっきからおんぷちゃんが、何やら小さなノートのような物をペラペラとめくりながら、"
    extend "ブツブツとつぶやいている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、どうしたの？」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0352.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えっ？{w=0.4}あ、りずむちゃん、何？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何、って……{w=0.5}おんぷちゃん、大丈夫？{w=0.4}何だか元気がないみたいだけど……{w=0.55}おんぷちゃん、それは？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0353.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、これ？{w=0.4}これは単語帳よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「単語帳？」"
    $ kag_cm()
    $ kag_playse('4-0354.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん。{w=0.4}\nわたしが英会話の勉強をしてるのは知ってたっけ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "単語帳にはていねいな字で英単語と、その裏には訳が書かれている。"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0355.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「その英会話の塾でテストがあるの。{w=0.4}でもわたしあんまり勉強してなくて、{w=0.4}昨日ちょっと徹夜しちゃったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0774.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「徹夜って……{w=0.55}おんぷちゃん、寝てないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0266.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「え？{w=0.35}おんぷ寝なくても平気なの？{w=0.4}い～な～。{w=0.4}ハナちゃんも１日中起きてたいな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0775.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃんそれはちがうでしょ。{w=0.4}眠らないと次の日１日中ぼうっとして、{w=0.4}元気がなくなっちゃうんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0267.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そうなの？{w=0.4}それじゃおんぷ、元気ないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0356.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「元気ないってほどじゃないけど、ちょっと眠いかも」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0531.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それにしても、徹夜までしなくたって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0233.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだよ！{w=0.4}もしテスト中に居眠りなんかしちゃったら大変だよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0770.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ももちゃんそんな、{w=0.4}どれみちゃんやないんやから……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0776.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃん、それどういう意味～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0771.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、いや、別に。{w=0.4}なははは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0357.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「心配してくれてありがとう。{w=0.4}でもわたしが好きでやってることだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、何だか顔色も悪いですよ……」"
    $ kag_cm()
    $ kag_playse('4-0358.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「このくらい平気よ。{w=0.4}あ、わたしもクッキーもらうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "クッキーをかじり、アイスティーをひと口飲む。"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0359.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん、おいしい。{w=0.4}これでもっとがんばれるわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "おんぷちゃんやっぱり無理してる……{w=0.6}\nそうだ！魔法でテストの問題を知っちゃえば……！"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「テストの問題よ、出ろ！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'white', time_ms=100, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', 'bg017_b', time_ms=100, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_o_b4_op__dash__04_01:
    $ kag_set_bookmark('「４日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0359.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「これ……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、おんぷちゃん。{w=0.4}これで今度のテストはバッチリです！」"
    $ kag_cm()
    $ kag_drawchar('o_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0360.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ダメよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ！？」"
    $ kag_cm()
    $ kag_playse('4-0361.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、それはダメ。{w=0.4}そんなのカンニングと同じよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0361.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「もしいい点を取れたって、わたしちっともうれしくない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「で、でも、{w=0.4}おとといだってとっても眠たそうだったし、昨日はライブだったし、{w=0.4}何もそんなに無理しなくたって、ちょっとくらいなら」"
    $ kag_cm()
    $ kag_drawchar('o_08.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_stopbgm()
    $ kag_sound_se('se-027.ogg', buf=1)
    $ kag_ws(buf=0, canskip=True)
    $ kag_wait(800, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '04おんぷ-04', time_ms=500, bgcolor='0x000000')
    $ persistent.cgo3=1
    $ kag_mesframe()

label kag_o_b4_op__dash__04_02:
    $ kag_set_bookmark('「４日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_playse('4-0362.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「平気だって言ってるでしょ！{w=0.4}りずむちゃんにわたしの何がわかるって言うのよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんな言い方って……」"
    $ kag_cm()
    "わたしはおんぷちゃんのためを思って……"
    $ kag_cm()
    $ kag_cm()
    $ kag_cm()
    $ kag_playse('4-0364.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「何が言いたいのよ？{w=0.4}言ってくれなきゃわからないじゃない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0777.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まあまあ、おんぷちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0365.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたし言ったよね。{w=0.4}まわりは大変に見えるかも知れないけど、{w=0.4}好きなことだから平気だって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、こういう時こそ魔法を使った方が……」"
    $ kag_cm()
    $ kag_playse('4-0366.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なんでも魔法で解決すればいいってものじゃないのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！」"
    $ kag_cm()

label kag_o_b4_op__dash__04_03:
    $ kag_set_bookmark('「４日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=100, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_drawchar('a_09.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('3-0772.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ストーップ！{w=0.4}おんぷちゃん、言い過ぎやで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0367.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あっ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0368.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしは、わたしの力を信じてるから。{w=0.4}絶対にズルはしない……{w=0.5}それだけは、わかってほしいの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0778.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ほ、ほら、おんぷちゃんがんばりたいって言ってるんだし。{w=0.4}ね？りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……{w=0.6}ごめんなさい」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0369.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんなごめんなさい、大きな声を出しちゃった。{w=0.55}{nw}"
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    extend "あっ、そろそろ時間よ。{w=0.4}みんな、お仕事に戻りましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-020.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0234.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「気にしなくていいよ。{w=0.4}おんぷちゃん、きっと寝不足で気が立ってたんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0773.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おんぷちゃんが、あんなに大声を出すなんてめずらしいねんけどなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0532.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「いくら寝てないにしても、ちょっと変よね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0779.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、どうしてだと思う？」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_o_b4_choices_op02:
    $ kag_set_bookmark('おんぷシナリオ選択肢02')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】ズルをしようとしたから', current_stem='o_b4', storage=None, target='*choices_op02-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】魔法で解決しようとしたから', current_stem='o_b4', storage=None, target='*choices_op02-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_o_b4_choices_op02__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag += 1
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}あ、あの、わたしがズルをしようとしたから……」"
    $ kag_cm()
    jump kag_o_b4_after_choices_op02
    call kag_s_wait

label kag_o_b4_choices_op02__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしが、魔法でテストを出しちゃったから……」"
    $ kag_cm()
    jump kag_o_b4_after_choices_op02
    call kag_s_wait
    "【分岐終わり】{nw}"

label kag_o_b4_after_choices_op02:
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0780.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あのね、おんぷちゃんって、将来は海外でも通じる女優をめざしてるんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「海外……？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0774.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「つまり外国やな。{w=0.4}他の国では、あたしらが今しゃべっている言葉とはちがうねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0781.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん。{w=0.4}そのために英会話のスクールに通って、勉強してるんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0781.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だから、魔法でテストがいい点取れても、意味がないんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし……{w=0.55}おんぷちゃんのこと、全然わかってなかったのに、勝手なことを……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0782.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなに気にしないでいいよ。{w=0.4}おんぷちゃんだってあやまってたじゃん」"
    $ kag_cm()
    $ kag_stopse(buf=0)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0782.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「本気で怒ってなんていないよ、きっと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    "それでも、何かわたしにできること、ないかな……"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_stopse(buf=0)

label kag_o_b4_op__dash__04_04:
    $ kag_set_bookmark('「４日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0783.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんな、おつかれ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0534.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「おつかれさま」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0775.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、また明日な～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0235.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「バイバ～イ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0370.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(800, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}おんぷちゃん、やっぱり元気なかったな」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしよう、気になるな……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よし！」"
    $ kag_cm()
    $ kag_sound_se('se-032.1.ogg', buf=1)
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'white', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg254', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b4_op__dash__04_05:
    $ kag_set_bookmark('「４日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}まだそんなに遠くには行ってないと思うんだけど……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっと、おんぷちゃんのおうちは確かあっちの方だって言ってたような……{w=0.65}あっ！いた！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg095', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「………………」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg254', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    "どうしたんだろう？少しフラフラしているけど。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうか。おんぷちゃん、単語帳を読みながら歩いてるんだ……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あぶないなあ……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ああっ！」"
    $ kag_cm()
    $ kag_stopbgm()
    "おんぷちゃんの行く先を見ると、狭い道を猛スピードで走っている１台の車が！"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、気づいてない！？\n{w=0.4}このままじゃ……{w=0.45}えい！」"
    $ kag_cm()
    $ kag_sound_se('se-032.1.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg095', time_ms=500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_stopse(buf=0)

label kag_o_b4_op__dash__04_06:
    $ kag_set_bookmark('「４日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0371.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えっ！？{w=0.4}何これ！{w=0.4}体が動かない……！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-041.ogg', buf=1)
    $ kag_playse('4-0372.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「きゃ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よかった……」"
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0373.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg048', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b4_op__dash__04_07:
    $ kag_set_bookmark('「４日目」がんばることの大切さ')
    $ kag_cm()
    "公園に着くまで、わたしもおんぷちゃんも、一言も話さなかった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、怒ってるのかな……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0374.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんも座って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ようやくおんぷちゃんが口を開く。"
    $ kag_cm()
    "言われたとおりに、おんぷちゃんのとなりに座る。"
    $ kag_cm()
    $ kag_playse('4-0375.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「さっきのって、りずむちゃんの魔法よね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}あの、ごめんなさい！」"
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あのままじゃ、{w=0.4}おんぷちゃんが車にぶつかっちゃうと思って……{w=0.6}だから……」"
    $ kag_cm()
    $ kag_playbgm('m413a', loop=True)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0376.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、ありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん……{w=0.65}怒って、ないの？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0377.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「もちろんよ、本当にありがとう。{w=0.4}単語帳を見ながら歩くのはあぶないわね。{w=0.4}気をつけなきゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、わたし魔法を使っちゃって、その……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0378.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「魔法を使っちゃダメなんて、わたし一言も言ってないわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0378.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ライブの時だって、りずむちゃんの魔法に助けてもらったし。{w=0.4}今日なんてあぶないところだったし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0378.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それって魔法じゃないとできないことでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_playse('4-0379.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「魔法って確かに便利なんだけど、{w=0.55}魔法を使っても意味がないってことだってあるって、わたしは思うの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='2', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('sepia', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_image('bg017_a', layer='1', page='back', left=0, top=0, visible=True, sepia=True)
    $ kag_trans(time_ms=50, method='', rule='trans01', vague=100)
    $ kag_wt(canskip=True)
    $ kag_image('c_frm', layer='2', page='back', left=0, top=0, visible=True, sepia=False)
    $ kag_trans(time_ms=600, method='crossfade', rule='', vague=64)
    $ kag_wt(canskip=True)
    $ kag_wait(500, canskip=True)
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('1-0785.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あのね、おんぷちゃんって、将来は海外でも通じる女優をめざすしてるんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「海外……？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('3-0774.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「つまり外国やな。{w=0.4}他の国では、あたしらが今しゃべっている言葉とは違うねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('1-0786.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん。{w=0.4}そのために英会話のスクールに通って、勉強してるんだよ。{w=0.4}だから、魔法でテストがいい点取れても、意味がないんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='2', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg087', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b4_op__dash__04_08:
    $ kag_set_bookmark('「４日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、わかります……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0380.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「けがを治す魔法とか、{w=0.4}人の心を変える魔法はもちろんなんだけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0381.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それだけじゃなくって、{w=0.4}チャイドルのお仕事もそうだし、英会話とかもなんだけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0381.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「もっと小さなことだって魔法じゃ解決できない時って、自分の力でどうにかしなくちゃいけないんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0382.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ＭＡＨＯ堂ではごめんね。{w=0.4}りずむちゃんが心配してくれてるのはわかってるんだけど、ついきつい言い方しちゃった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいえ、{w=0.4}わたしもおんぷちゃんのことを思っているつもりで、勝手なことをしちゃって……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0383.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「テストのことは別に気にしてないわ。{w=0.4}問題をみたわけじゃないし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よかった～」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0384.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも、わたしがこんな風に思えるようになったのって、{w=0.4}どれみちゃんたちのおかげなのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？{w=0.4}それってどういう……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0385.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「さ、そろそろ帰らなくちゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0386.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、今日は本当にありがとう。{w=0.4}助かったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0387.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「もう単語帳を見ながら歩いたりしないから、安心してね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0388.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃまた明日、ＭＡＨＯ堂で」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-020.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    "どれみちゃんたちのおかげって、どういうことなんだろう？"
    $ kag_cm()
    "おんぷちゃん、そのうち話してくれるかな……？"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.o4_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_o_b5_gamestart
    return
