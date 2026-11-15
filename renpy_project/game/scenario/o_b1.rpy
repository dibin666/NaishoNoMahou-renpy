# Auto-generated from 04. onpu/o_B1.ks by tools/transpile_ks.py
label kag_o_b1:

label kag_o_b1_gamestart:
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

label kag_o_b1_op__dash__01_00:
    $ kag_set_bookmark('「１日目」おんぷちゃんってすごい！')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0741.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあ、今日からりずむちゃんにもＭＡＨＯ堂のお仕事を手伝ってもらうってことで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0494.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、よろしくね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！{w=0.4}よろしくお願いします！」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0219.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「まずはどうしようか？{w=0.4}いきなりお仕事ってのは無理があるわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0729.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやなぁ～。{w=0.4}道具の使い方も分からへんやろうし……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、えっと……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0191.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「まずは、お仕事の説明だね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0240.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はいは～い！{w=0.4}ハナちゃんがりずむに説明してあげる！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0742.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え、それは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0495.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ちょっと不安って言うか……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0192.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ハ、ハナちゃんには、ちょっと難しいかも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0241.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ぶう～！{w=0.4}ハナちゃんできるもん！{w=0.4}ね、りずむ行こ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ……」"
    $ kag_cm()
    "い、いいのかなあ。"
    extend "みんなの様子からすると、ちょっと不安な……"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0220.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あら、ハナちゃんは昨日からやりかけのお仕事があったんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0242.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、そうだった……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0496.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ハナちゃん、そっちを先にやらなくちゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0743.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0243.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「む～{w=0.6}わかった。{w=0.4}ハナちゃんお仕事する」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ハナちゃん、ちょっと不満そう。"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0730.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、あらためてどないしよっか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0193.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「誰がりずむちゃんに説明する？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0221.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お店の案内もしなきゃね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの……{w=0.65}悪いですから、みなさんはお仕事をしていてください」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしはお店の中を見学しながら、{w=0.4}みなさんのお仕事を見させてもらいますから……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0222.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。{w=0.4}それが手っ取り早いかも」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0497.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「その方が、りずむちゃんも気楽かもしれないわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0744.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしはハナちゃんを手伝ってくるから。{w=0.4}りずむちゃん、あたしたちの所にも来てね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0244.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「来てね～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0731.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、あたしらも仕事しよか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0498.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうしましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0194.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「今日も１日ガンバロー！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_pausebgm()
    $ kag_sound_se('se-045.ogg', buf=1)
    "おんぷちゃんのポケットから音がする。"
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0223.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「もしもし？{w=0.6}うん、{w=0.6}うん、{w=0.6}うん……{w=0.65}えええ～っ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0732.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なんやろ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0195.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「何かあったのかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "何だろう？"
    extend "時おり「そんな、いきなり……」とか「だったらもう少しだけ……」といった声が聞こえてくる。"
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0224.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……{w=0.7}うん、わかった。{w=0.4}待ってるから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-035.ogg', buf=1)
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0225.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_resumebgm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0745.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0226.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「カメラマンの先生の都合で、急に撮影が決まっちゃったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0226.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「すぐに帰ってこいって言われたんだけど、１時間だけ待ってもらうことにしたわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0499.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そう……{w=0.55}それじゃしかたがないわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0733.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「て言うか、急ぐんやったらすぐ帰った方がええんちゃう？{w=0.4}おんぷちゃんが抜けたぶんは、あたしらがフォローするから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0227.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ううん。{w=0.4}お仕事も大事だけど、今日はＭＡＨＯ堂のお手伝いをするって最初からママには言ってあったから、{w=0.4}こっちの方もやらなきゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0227.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「１時間しかないけど、がんばれば今日やろうとしていた所くらいなら終わると思うから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0746.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしたちも手伝うから大急ぎで終わらせちゃおう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0228.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ありがとうどれみちゃん。{w=0.4}そうと決まったら急がなきゃ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0196.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「オッケー！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0734.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「よっしゃ！{w=0.4}ほなやるか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0229.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしのことは気にしないで。{w=0.4}りずむちゃんもがんばってね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0245.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～！{w=0.4}こっちこっち～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "おんぷちゃんって、ＭＡＨＯ堂以外に仕事をしてるのかな？"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('left', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg003', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b1_op__dash__01_01:
    $ kag_set_bookmark('「１日目」おんぷちゃんってすごい！')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0246.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇりずむ！{w=0.4}これ見て～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわぁ……{w=0.65}きれ～い」"
    $ kag_cm()
    "ビーズのアクセサリーを見せてもらう。{w=0.4}作りかけだけど、とってもきれいだ。"
    $ kag_cm()
    $ kag_playse('6-0247.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「でしょ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0747.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん、がんばったもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「本当にきれい……{w=0.6}これってどうやって作るんですか？」"
    $ kag_cm()
    "ビーズの束を手に取りながら、どれみちゃんにたずねてみた。"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0748.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、これはね、このビーズメーカーを使ってるんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんは、ビーズメーカー見せながら説明してくれる。"
    $ kag_cm()
    $ kag_playse('1-0749.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ここからビーズを入れてね……{w=0.55}糸をここにセットして……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0248.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「このハンドルを回すと、つながったビーズが出てくるんだよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0249.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ほら、りずむもやってみて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ハナちゃんにそう言われ、わたしはビーズメーカーのハンドルを回してみた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ！{w=0.4}すごいですね～！」"
    $ kag_cm()
    "ふと、そばを見ると、できあがったビーズの束がちょっとした山になっている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ずいぶんたくさん作ってるんですね。{w=0.4}これって、どうなるんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0230.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃん、ハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0250.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、おんぷ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0750.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ビーズの束ならもうできてるから、このへんのを適当に持っていって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0231.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わかった。{w=0.4}りずむちゃん、どう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}あ、今どれみちゃんたちにビーズメーカーの使い方を教えてもらっていました」"
    $ kag_cm()
    $ kag_playse('4-0232.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃんは、あの、はかどってますか？」"
    $ kag_cm()
    $ kag_playse('4-0233.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「平気よ。{w=0.4}それじゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0751.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「さてと……{w=0.55}{nw}"
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    extend "あ、{w=0.4}ハナちゃんビーズもうなくなりそうだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0251.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あや、ホントだ……{w=0.6}って、どれみ。\n{w=0.4}そこにビーズあるよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "すみっこに、いつの間にかビーズの筒が置かれている。"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0752.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あれ？{w=0.4}いつのまに……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0752.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そっか、さっきおんぷちゃんが持ってきてくれたんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ」"
    $ kag_cm()
    "確かにさっきまでは、そこにビーズの筒なんてなかったはず。"
    extend "\nおんぷちゃん、ずいぶん急いでいる様に見えて、\n気がきくんだなあ。"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0753.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあハナちゃん、続きがんばろっか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0252.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0754.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、お店の中はもう見て回ったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}えっと……{w=0.5}まだここだけですけど」"
    $ kag_cm()
    $ kag_playse('1-0755.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあ、色々と見て回るといいよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0253.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、がんばれ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい、……{w=0.6}それじゃ」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b1_op__dash__01_02:
    $ kag_set_bookmark('「１日目」おんぷちゃんってすごい！')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0197.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あ、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "商品棚の前にくると、ももちゃんが商品の整理をしている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん、おつかれさまです」"
    $ kag_cm()
    "わたしは、ももちゃんのところに歩み寄った。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「商品の整理ですか？」"
    $ kag_cm()
    "見ると、ももちゃんの足元にはバケツとぞうきんが置かれている。"
    $ kag_cm()
    $ kag_playse('5-0198.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん。{w=0.4}それにお掃除も」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "商品棚は、半分くらい整理と掃除が終わっているようだ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「大変ですね……{w=0.6}あ、ここに置いてある商品って、どれもみなさんで作ったものなんですか？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0199.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん。{w=0.4}そうだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0200.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ほら、これはわたしが作ったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ももちゃんは、棚から布製のブレスレットを取り、わたしに見せてくれた。"
    extend "ブレスレットは、シンプルな中にビーズのワンポイントがある物だった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ、オシャレですね～」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0201.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「えへへ。{w=0.4}ありがと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「他の商品も、どれもみんなステキですね～」"
    $ kag_cm()
    $ kag_playse('5-0202.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「カワイイアクセサリーがい～っぱいだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "うれしそうに言うももちゃん。"
    extend "確かにカワイイなあ。"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0203.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あ、お仕事しなきゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、わたしもお手伝いします」"
    $ kag_cm()
    "わたしは足元のバケツからぞうきんを取った。"
    $ kag_cm()
    $ kag_playse('5-0204.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「えっと、それじゃあわたしはアクセサリーを整理するから、りずむちゃんはお掃除お願いできるかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}がんばります！」"
    $ kag_cm()
    "そう言うとわたしたちは、整理と掃除をはじめた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お客さんに気持ちよくお買い物してもらえるよう、きれいにしますね！」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0205.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「お客さん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしたんですか？」"
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0206.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「お客さん……{w=0.65}あんまり来ないんだけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？{w=0.4}……{w=0.65}えっと……{w=0.6}そ、そうなんですか？」"
    $ kag_cm()
    $ kag_playse('5-0207.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あ、全然来ないってワケじゃないよ！{w=0.4}ほ、ほら、ここのアクセサリーとかなくなってるし……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ももちゃんが整理している棚には、空いたスペースがある。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ここには、何が入るんですか？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0208.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おんぷちゃんが作ってるアクセサリーが入るんだよ。{w=0.4}今日作ってるはずなんだけど、間に合うかなあ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0209.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おんぷちゃんのアクセサリーは、ファンの人たちにすっごく人気があるんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ファン……？{w=0.4}\nおんぷちゃんには、ファンがいるんですか？」"
    $ kag_cm()
    $ kag_playse('5-0210.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだよ。{w=0.4}何せおんぷちゃんはチャイドルだからね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ちゃいどる……？」"
    $ kag_cm()
    "なんだろう、チャイドルって。"
    extend "聞きなれない単語に、わたしは首をひねる。"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0234.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ももちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0211.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あ、おんぷちゃん。{w=0.4}できた？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0235.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ううん、ちょっと参考にしたいアクセサリーがないかなって、見に来たの。{w=0.4}もう少し待っててくれるかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0212.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「まだ時間があるから、あせらなくていいよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0236.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('4-0237.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「確かこれ、このへんだったと思ったんだけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そう言って、お客さんがほしい物をさがしているようなそぶりでおんぷちゃんはアクセサリーたちをながめる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0238.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「何？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃんのお仕事って……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('4-0239.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ！{w=0.4}あった！{w=0.4}そっか、こうなってるんだ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0240.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ごめんなさい。{w=0.4}急いでるから、また後でね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "間に合うのかなあ……？"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0213.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「よし。{w=0.4}これで整理はＯＫっと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "アクセサリーを並べ終わって、満足そうにしている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、おんぷちゃん、本当に間に合うんでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0214.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「んあ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「さっきおんぷちゃんが手に取っていたアクセサリー、{w=0.4}すごく複雑そうで、とても１時間ではできそうになかったんですけど……」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0215.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うーん……{w=0.4}おんぷちゃんは、１度やるって決めたら絶対に曲げないから、{w=0.4}どうにかなっちゃうんじゃないかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もしも、うまくいかなかったら、どうするんでしょうか……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0216.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「その時はその時。{w=0.4}そうならないためにがんばってるんだから、わたしたちはおんぷちゃんを応援しなくちゃ。{w=0.4}\nね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そっか……{w=0.65}そうですね」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何かわたしにも手伝えることないかな？」"
    $ kag_cm()
    $ kag_playse('5-0217.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おんぷちゃん、集中してるみたいだから、そっとしておいた方がいいよ。」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0218.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それより、はづきちゃんとあいちゃんが糸つむぎしてるから、{w=0.4}よかったらそっちを手伝ってあげて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。{w=0.4}わかりました」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg004', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b1_op__dash__01_03:
    $ kag_set_bookmark('「１日目」おんぷちゃんってすごい！')
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0500.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あら、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すごい立派な機械ですね……{w=0.6}えっと、糸つむぎ機、ですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0736.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そう。{w=0.4}その名の通り、糸をつむぐ機械やね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0501.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「これで綿から糸をつむいで、あっちのはた織り機で布にするのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「糸つむぎ機に、はた織り機……{w=0.55}何だか難しそうですね」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0737.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「確かに、簡単とは言われへんかもな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0502.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そんなに心配しなくても大丈夫よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0503.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、まだはた織り機は見てないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ、まだです」"
    $ kag_cm()
    $ kag_playse('2-0504.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「なら、まずはこの糸つむぎ機の使い方から説明しましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0738.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな。{w=0.4}それにはた織り機は……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0505.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしたちもまだ、ちゃんと使いこなせてないのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}そ、そうなんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0739.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「実はそやねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0506.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「マジョクロスさんに教わって、少しくらいなら使えるんだけど、{w=0.4}まだあんまり上手にできないのよね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0740.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ま、はた織り機に関しては、あたしらもりずむちゃんといっしょに勉強ってトコやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい！{w=0.4}がんばります！」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0741.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「よっしゃ！{w=0.4}ほなさっそく糸つむぎ機を使ってみよか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.6}でもえっと……{w=0.55}どうすればいいんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0742.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こういうのは習うよりなれろっちゅうやっちゃ。{w=0.4}ほら、ココ座って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0507.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃあ、わたしはこっちをやるわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    "はづきちゃんはなにするんだろう？"
    $ kag_cm()
    $ kag_playse('2-0508.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あ、わたしはこっちで、糸がからまないようにするの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0743.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ひとりで糸つむぎ機を使うのは難しいから、２人で協力してやんねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あいちゃんが説明してくれる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そうなんですね……{w=0.65}えっと、はづきちゃん、よろしくお願いします」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0509.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「はい、よろしくお願いします」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃんも、よろしくお願いします」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0744.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まかせとき！{w=0.4}ほなりずむちゃん、そのペダル踏んでみて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっと……{w=0.55}これ？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0745.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そや。{w=0.4}そのペダルを踏むと、あっちのホイールに糸がつむがれるから。{w=0.4}最初はゆっくり、テンポよく踏んでみて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「う、うん」"
    $ kag_cm()
    $ kag_playse('se-008.1.ogg', buf=1, loop=False)
    $ kag_playse('3-0746.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう、ええ感じや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あいちゃんの言葉通りペダルを踏み始める。"
    extend "糸つむぎ機はカラカラと回り始め、糸をつむいでいく。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうございます！」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0510.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ、上手よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よ～し、この調子で……」"
    $ kag_cm()
    "なれてきたのと、うまくいってうれしいのが合わさって、わたしはペダルを踏む足をつい早くしてしまう。"
    extend "糸つむぎ機が勢いを増して回る。"
    $ kag_cm()
    $ kag_playse('se-008.2.ogg', buf=1, loop=False)
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0511.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あ、りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0747.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、あかん、ちょっと早すぎや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-008.2.ogg', buf=1, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！」"
    $ kag_cm()
    "あわててペダルから足を離したけど、勢いのついたホイールはすぐには止まらない。"
    $ kag_cm()
    "ホイールがずれて、糸がからまりだしてしまう。"
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0512.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「キャッ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0748.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あちゃあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ご……{w=0.6}ごめんなさい！！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし……{w=0.7}また失敗しちゃって……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0749.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そ、そんな気にせんでもええって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「で、でも……{w=0.7}わたし、こんなにしてしまって……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0241.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あれ、何やってるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "たまたま横を走っていたおんぷちゃんが立ち止まる。"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0513.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ちょっと糸がからまっちゃったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0242.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうなんだ、しかたがないから切っちゃいましょうよ。{w=0.4}はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……」"
    $ kag_cm()
    $ kag_playse('4-0243.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「気にしないの。{w=0.4}からんじゃった糸もほんの少しだし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、でも……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0514.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうよ。{w=0.4}りずむちゃん。{w=0.4}あんまり気にしないで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0750.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「最初は失敗なんてつきもんやて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい……{w=0.65}本当にすみませんでした」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0244.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうそう。{w=0.4}それに失敗と言えば……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('1-0756.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なになに？{w=0.4}どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0245.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんにはかなわないわよ。{w=0.4}ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0751.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うんうん、ホンマや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0515.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフッ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0756.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0246.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ウフフッ、あ！{w=0.4}{nw}"
    $ kag_drawchar('o_05.tlg', time_ms=100, sepia=False, canskip=True)
    extend "いけない！{w=0.4}もう時間がないわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-021.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0247.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はい！{w=0.4}ももちゃんお待たせ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0219.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Wow！{w=0.4}おんぷちゃんこれすごくカワイイよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0248.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「もうママが来ちゃう！{w=0.4}\n{nw}"
    $ kag_drawchar('o_01.tlg', time_ms=100, sepia=False, canskip=True)
    extend "それじゃみんな、あとはよろしく！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0757.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そいじゃね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0254.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おんぷ、がんばってね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('sepia', 'bg005', time_ms=1000, bgcolor='0x000000')
    $ kag_frmdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('5-0220.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うーん……{w=0.4}おんぷちゃんは、１度やるって決めたら絶対に曲げないから、{w=0.4}どうにかなっちゃうんじゃないかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg004', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b1_op__dash__01_04:
    $ kag_set_bookmark('「１日目」おんぷちゃんってすごい！')
    $ kag_cm()
    "……本当に１時間で終わらせちゃったんだ、おんぷちゃん。"
    $ kag_cm()
    $ kag_cm()
    "おまけに、わたしも助けてもらっちゃった。"
    $ kag_cm()
    "どうしたらあんな風になれるのかな？"
    $ kag_cm()
    "おんぷちゃんみたいな人になれたら……"
    $ kag_cm()
    "ううん、なってみたい！"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}ようし、決めた」"
    $ kag_cm()
    "わたしは、糸つむぎ機のペダルを踏みながら、あることを思いついていた。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ persistent.o1_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_o_b2_gamestart
    return
