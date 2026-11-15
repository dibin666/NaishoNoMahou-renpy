# Auto-generated from 04. onpu/o_B3.ks by tools/transpile_ks.py
label kag_o_b3:

label kag_o_b3_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_onpu.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg001', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_o_b3_op__dash__03_00:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    "今日のお仕事もそろそろ終わり。"
    extend "そんな中、不思議とみんなはそわそわしている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「まだかな、まだかな……{w=0.6}ふふっ」"
    $ kag_cm()
    "そんな中で、多分１番そわそわしているのは、きっとわたし。"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0757.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃ～ん、楽しみなんはわかるけど、{w=0.4}ちゃんと仕事も手伝ってな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！{w=0.4}は、はい！{w=0.4}ごめんなさい！」"
    $ kag_cm()
    "あいちゃんに注意されちゃった。まずいまずい。"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0758.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃ～ん、これ、しまうの忘れてるよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0758.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「えっ？{w=0.4}あ、ホンマや、ごめ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あいちゃんも、どこか気もそぞろな様子だ。"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0759.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なはは……{w=0.5}だって楽しみやもん、気になってしもて、{w=0.4}なぁりずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}もう何だか待ちきれなくって……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0759.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「実はあたしもだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_frmdraw()
    $ kag_mesframe()

label kag_o_b3_op__dash__03_01:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "午前中、みんなはいつものように、ＭＡＨＯ堂のお仕事をしていた。"
    extend "ちょうどお仕事が一段落ついたときに、"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0320.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんな。{w=0.4}悪いんだけど、今日はＭＡＨＯ堂のお手伝いを早くあがらせてもらっていいかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0221.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どうしたのおんぷちゃん？{w=0.4}チャイドルのお仕事？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0321.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん。{w=0.4}夕方から駅前でミニライブをするの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0522.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうなの？{w=0.4}知らなかったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "あとから聞いたんだけど、おんぷちゃんがライブをやるってことになれば、いろんなお知らせがあるそうで。"
    $ kag_cm()
    "町中で知らない人がいないくらいになるそうだから、はづきちゃんやみんなが知らないなんてことは、ちょっと不思議なことだったみたい。"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0322.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフフ。{w=0.4}実は今日のお昼に流れるラジオでだけ告知するの。{w=0.4}ちょっとしたシークレットライブってところかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか！？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0760.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあさ、お店、早めに閉めてみんなで……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「行きたいです行きたいです。{w=0.4}行きたいです！」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0761.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おっと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0760.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、なんかめっちゃ行きたいみたいやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ、すいません。{w=0.4}つい」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0222.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「いーのいーの。{w=0.4}わたしたちだって見に行きたいんだもん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0255.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんも行く行くー」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0523.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それなら、みんなで行きましょうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0323.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ウフフ、今日のライブは結構レアなイベントだから、{w=0.4}絶対みんなで見にきてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0036.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「もっちろん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、とっても楽しみです！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0324.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ふふっ、ありがとう。{w=0.4}がんばるね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b3_op__dash__03_02:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、そろそろ行かないと間に合わないんじゃないですか？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0762.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う～ん、そうだね。{w=0.4}駅前だから大して遠くはないけどちょっと早めに出ようか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0524.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ちょっと早いけど、お店を閉めちゃいましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0223.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん。{w=0.4}今日はお客さんも少なかったし、早めに閉めちゃっても大丈夫だよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0761.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「よっしゃ、ほな急いで片づけせな！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0256.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それじゃあ、おんぷのライブにしゅっぱ～つ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0037.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「お～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg078', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_stopse(buf=0)

label kag_o_b3_op__dash__03_03:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_playbgm('se-016.1.ogg', loop=True)
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0762.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何か……{w=0.55}めっちゃこんでんなぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0525.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、はぐれないように気をつけてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい……{w=0.65}大丈夫です……{w=0.6}きゃっ！」"
    $ kag_cm()
    "がんばってみんなについていこうとするけど、人波に押されて転びそうになってしまう。"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0763.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うわわっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうどれみちゃん……」"
    $ kag_cm()
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0224.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、気をつけてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、大丈夫です」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0257.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ！{w=0.4}ねぇねぇ、ステージってあれかな？」"
    $ kag_stopse(buf=0)
    $ kag_fadeoutbgm(1000)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg078', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_stopse(buf=0)

label kag_o_b3_op__dash__03_04:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_se_loop('se-016.2.ogg')
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0764.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う、うわぁ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すごい人の多さですね。{w=0.4}これじゃ遠くからしかおんぷちゃんのライブが見れないですね」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0526.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それなら大丈夫よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0763.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おんぷちゃんから、ステージ裏に招待されてんねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そう言いながら、あいちゃんがポケットから何かカードのようなものを取りだす。"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0225.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「これを見せれば、ステージ裏に入れてもらえるんだって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0258.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「早くおんぷに会いに行こうよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}早く行きましょう！」"
    $ kag_cm()
    "人ごみを回りこんで、ステージ裏へと向かった。"
    $ kag_stopse(buf=2)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg071', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b3_op__dash__03_05:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "わたしたちは、パスを見せてステージ裏へ入れてもらう。"
    extend "\nスタッフの人たちはあわただしく動き回っている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ、すごくいそがしそうですね……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0764.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマやな。{w=0.4}ジャマにならんようにせな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0259.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、おんぷ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0325.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんな、わざわざ来てくれてありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0766.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いやいや、そんなこと～」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_05.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「こちらこそ招待してくれてありがとうございます！」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0766.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、今日ずっとはりきりっぱなしなんだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0326.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフフ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0527.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「おんぷちゃん、もう準備はすんだの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0327.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん。{w=0.4}もう打ち合わせは終わったから、あとは出番を待つだけよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん……すごくいそがしそうですよね」"
    $ kag_cm()
    $ kag_playse('4-0328.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、こういうのに興味あるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？……{w=0.65}興味がある、って言うか」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0226.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしたちは初めてじゃないけど、{w=0.4}りずむちゃんはステージ裏に来るのなんて初めてだもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。だからビックリしちゃって」"
    $ kag_cm()
    $ kag_drawchar('o_l_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0329.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そっか。{w=0.4}よかったらわたしが、スタッフさんたちのお仕事を説明しようか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0260.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、ハナちゃんも聞きた～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0330.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あそこにいるのが舞台監督さん。{w=0.4}ステージの責任者ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0767.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ほぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0331.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あれ、どれみちゃんには説明したことなかったっけ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0768.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ま、まあ、いつ聞いても新鮮っすよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0332.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「今マイクチェックしてるのが音響のスタッフさんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0261.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「『チェ』とか『ッカン』とかマイクでしゃべってるね。{w=0.4}変な音ぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0333.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「舞台の上でライトをチェックしてるのが照明さん。{w=0.4}今日は外だからちょっと大変そうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0333.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、外のライブって、屋内会場にくらべると結構大変なの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0333.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「トラブルとか起こりやすいから、スタッフさんたちも、いつもより念入りにチェックしてくれてるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へぇ～」"
    $ kag_cm()
    $ kag_playse('4-0334.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「大体こんな感じかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0262.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「いろんなお仕事の人がいるんだねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_l_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0335.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。{w=0.4}みんなで力を合わせて、ステージを作り上げるのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('スタッフＡ「')
    "スタッフＡ「おんぷちゃ～ん。{w=0.4}そろそろ時間です。{w=0.4}スタンバイお願いしま～す」"
    $ kag_cm()
    $ kag_drawchar('o_l_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0336.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はぁ～い！{w=0.55}……それじゃみんな、行ってくるね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ！{w=0.4}おんぷちゃん！」"
    $ kag_cm()
    $ kag_drawchar('o_l_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0337.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの……{w=0.55}その……{w=0.6}がんばってくださいね！」"
    $ kag_cm()
    $ kag_drawchar('o_l_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0338.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '04おんぷ-03', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgo2=1
    $ kag_mesframe()

label kag_o_b3_op__dash__03_06:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_seopt(buf=1, volume=80, gvolume=None)
    $ kag_playse('bgm-002.1.ogg', buf=1, loop=False)
    $ kag_playse('4-0339.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんな～！{w=0.4}今日はおんぷのミニライブに来てくれてありがと～！{w=0.4}短い間だけど、い～っぱい楽しんでいってねぇ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ……{w=0.65}すごい……」"
    $ kag_cm()
    $ kag_playse('4-0341.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃ、さっそく聴いてください。{w=0.4}『WE CAN DO！』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('ファン「')
    "ファン「おんぷちゃ～ん」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('blind01', 'eyecatch.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_fadeoutse(time_ms=800, buf=1)
    $ kag_seopt(buf=1, volume=100, gvolume=None)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', '04おんぷ-03', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('bgm-002.2.ogg', buf=1, loop=True)
    $ kag_playse('4-0343.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「最後になっちゃったけど、{w=0.4}わたしの大好きな曲です。{w=0.4}心を込めて歌います」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_fadeoutse(time_ms=800, buf=1)
    $ kag_playse('se-023.ogg', buf=2, loop=True)
    "ステージのスピーカーからは何も聞こえてこなくなった。"
    $ kag_cm()
    $ kag_playse('4-0344.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……{w=0.55}え？{w=0.4}あれっ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg071', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b3_op__dash__03_07:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0769.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えっ！？{w=0.35}なに？{w=0.4}どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0528.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「マイクの故障かしら？{w=0.4}どうしよう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0765.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おんぷちゃん、困ってる……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_stopse(buf=2)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', '04おんぷ-03', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('se-023.ogg', buf=2, loop=True)
    $ kag_playse('4-0345.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みなさん、ごめんなさい。{w=0.4}おちついて、ちょっと待ってください」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg071', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0227.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだ！{w=0.4}わたしたちが魔法でマイクを直せばいいんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしがやります！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', '04おんぷ-03', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「マイクよ、直れっ！！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'white', time_ms=500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', '04おんぷ-03', time_ms=500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b3_op__dash__03_08:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_playse('4-0346.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "おんぷちゃんは、舞台裏からのぞいているわたしたちの方を向いた。"
    $ kag_cm()
    "わたしと目が合うと、うなずいて再びマイクを握った。"
    $ kag_cm()
    $ kag_playse('4-0347.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんな～、ごめんなさーい。{w=0.4}\n久しぶりのお外のライブだから、マイクさんがカゼ引いちゃったみたいなの～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutse(time_ms=300, buf=2)
    $ kag_se_loop('se-049.ogg')
    "な、何とかなったみたい……"
    $ kag_cm()
    $ kag_playse('4-0348.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあ、お待たせしました。{w=0.4}聴いて下さい。{w=0.6}『ルピナスの子守唄』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('bgm-002.2.ogg', loop=True)
    $ kag_wait(800, canskip=True)
    $ kag_stopse(buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_fadeoutbgm(1000)
    $ kag_fadeoutse(time_ms=1000, buf=2)
    $ kag_changetype('cross', 'bg071', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b3_op__dash__03_09:
    $ kag_set_bookmark('「３日目」ライブってなに？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん！」"
    $ kag_cm()
    $ kag_drawchar('o_l_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0349.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん。{w=0.4}さっきはありがとう。{w=0.4}助かっちゃった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、い、いえ、そんな……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、おんぷちゃんのライブ、すごくステキでした」"
    $ kag_cm()
    $ kag_playse('4-0350.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うふっ。{w=0.4}ありがとう。{w=0.4}ちょっとトラブルもあったけど、{w=0.4}りずむちゃんのおかげでファンのみんなをがっかりさせなくてよかったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、自分が失敗しなくてよかったってことより、{w=0.4}まずファンの人たちのことを１番に考えてるんだ……」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0264.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おんぷ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0766.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おんぷちゃん、おつかれさん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0770.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やっぱおんぷちゃんの歌は最高だね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0529.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ホント、今日は楽しかったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0228.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「You did such a great job!　おつかれさま」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……またおんぷちゃんのすごいところを見つけちゃった」"
    $ kag_cm()
    $ kag_drawchar('o_l_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0351.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どうかした？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、いえ。何でもないです」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.o3_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_o_b4_gamestart
    return
