# Auto-generated from 04. onpu/o_C.ks by tools/transpile_ks.py
label kag_o_c:

label kag_o_c_gamestart:
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

label kag_o_c_op__dash__c_00:
    $ kag_set_bookmark('「エンディング」笑顔のにらめっこ')
    $ kag_cm()
    "お昼過ぎ。{w=0.8}いつものようにお仕事をしている。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "そんな中、わたしはひとりで片づけをしながら、{w=0.8}ちょっとだけ物思いにふけっていた。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "朝、目が覚めたのはおんぷちゃんの部屋だった。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "ようやく住みなれたＭＡＨＯ堂の自分の部屋ではなく、{w=0.8}初めてお泊まりしたおんぷちゃんの部屋。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "でもそれだけ。{w=0.8}他はいつもといっしょ。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "ＭＡＨＯ堂のお仕事も、いつも通り。{w=0.8}お客さんはあんまり来なかった。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "みんなも、いつものようにふざけっあったりしながらお仕事をしていた。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "おんぷちゃんはチャイドルのお仕事で少しだけお店をぬけると言って、{w=0.8}まだ戻って来ていない。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "でもそれもいつもといっしょ。{w=0.8}何もかも、いつもと変わらない時間。{w=0.8}短い間だったけど、すっかり日常になった時間。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('se-009.2.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0592.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ただいま～」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0196.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、お帰り～」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0593.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんごめんね。{w=0.4}ママったら夕べ遅くなるって言って、{w=0.4}なんの打ち合わせかと思ったらいきなり今日のお仕事だって言うもんだから」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0197.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、いつものことなんですよね」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0594.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「まあね。{w=0.4}ＭＡＨＯ堂までの道、わかった？」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0198.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}迷いました」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0595.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「え？」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0199.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、ちゃんとたどり着いたんで、問題ナシです」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0596.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ、そうね」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg020', time_ms=2000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_c_op__dash__c_01:
    $ kag_set_bookmark('「エンディング」笑顔のにらめっこ')
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0200.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、お世話になりました」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "みんなの前に立ち、ゆっくりとその顔を見回す。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('1-0823.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、今日までおつかれさま」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0201.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('1-0824.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お仕事も手伝ってもらったし、楽しかったよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0202.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとう」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('2-0549.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしたちのこと、忘れないでね」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0203.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん。{w=0.4}もちろんです……」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('3-0806.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「楽しかったわ。{w=0.6}ありがとうな」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0204.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん、わたしこそ、ありがとう」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('5-0248.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「魔女界に帰っても、元気でね」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0205.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}ももちゃんも、お元気で」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('6-0278.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「また会おうね、りずむ！」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0206.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}ハナちゃん」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "わたしは、かえす言葉がなくて、ずっとオウム返しだった。{w=0.8}ハナちゃんが魔女界の次期女王様候補だったのを聞いたのは、ついさっき。{nw}"
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "とってもおどろいたけど、ハナちゃんはハナちゃんだから。{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0597.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0598.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……{w=0.2}はい、これ。{w=0.4}わたしからのプレゼント」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "おんぷちゃんの手のひらに乗っていたのは、ＣＤだった。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('4-0599.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「何をプレゼントしようかなやんだんだけど。{w=0.4}りずむちゃん、わたしの歌をステキだって言ってくれたから」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0207.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとう、おんぷちゃん」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "そっとＣＤを受け取る。{w=0.8}ジャケットに写るおんぷちゃんは、とびきりの笑顔を浮かべている。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0600.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「魔女界に帰ったら、時々きいてね」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "目の前のおんぷちゃんは、ジャケットの笑顔とはちがう。{w=0.8}もっと親しいような、そんな笑顔だった。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0208.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、でも、これ魔女界じゃきけないかも。{w=0.4}ラジカセとかないし……」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0601.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、もう忘れちゃったの？」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0209.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}何を？」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0602.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ラジカセくらい、魔法で出しちゃってよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0210.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そっか、そうですね」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('4-0603.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフフ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0211.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふふ……」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()

label kag_o_c_op__dash__c_02:
    $ kag_set_bookmark('「エンディング」笑顔のにらめっこ')
    $ kag_cm()
    if kag_f.event_04==1:
        $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=False)
        $ kag_playse('4-0604.ogg', buf=0, loop=False)
        $ kag_set_next_indent('おんぷ「')
        "おんぷ「それと……」{nw}"
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        if kag_f.judgeflag==3:
            $ kag_playse('9-0212.ogg', buf=0, loop=False)
        $ kag_set_next_indent('りずむ「')
        "りずむ「え？」{nw}"
        $ kag_wait(1500, canskip=False)
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
        $ kag_playse('4-0605.ogg', buf=0, loop=False)
        $ kag_set_next_indent('おんぷ「')
        "おんぷ「実はマジョリカあての手紙に、{w=0.4}もう１通手紙が入ってたの」{nw}"
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        if kag_f.judgeflag==3:
            $ kag_playse('9-0213.ogg', buf=0, loop=False)
        $ kag_set_next_indent('りずむ「')
        "りずむ「それって……？」{nw}"
        $ kag_wait(1500, canskip=False)
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_playse('4-0606.ogg', buf=0, loop=False)
        $ kag_set_next_indent('おんぷ「')
        "おんぷ「りずむちゃんあてじゃないから、{w=0.4}見せようかどうか迷ったんだけど……{w=0.55}はい」{nw}"
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        "おんぷちゃんから手紙を受け取る。{nw}"
        $ kag_wait(1500, canskip=False)
        $ kag_sound_se('se-056.ogg', buf=1)
        $ kag_wait(3000, canskip=False)
        $ kag_cm()
        if kag_f.judgeflag==3:
            $ kag_playse('9-0214.ogg', buf=0, loop=False)
        $ kag_set_next_indent('りずむ「')
        "りずむ「……{w=0.6}ママ……」{nw}"
        $ kag_wait(1500, canskip=False)
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_playse('4-0607.ogg', buf=0, loop=False)
        $ kag_set_next_indent('おんぷ「')
        "おんぷ「うん」{nw}"
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        "手紙には、わたしのことが書かれていた。{nw}"
        $ kag_wait(800, canskip=False)
        $ kag_cm()
        "得意なこと、苦手なこと。{nw}"
        $ kag_wait(800, canskip=False)
        $ kag_cm()
        "好きな食べ物、きらいな食べ物。{nw}"
        $ kag_wait(800, canskip=False)
        $ kag_cm()
        "同じ魔女幼稚園のお友だちのこと。{nw}"
        $ kag_wait(1000, canskip=False)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_cm()
        "ママは遠くにいて、ずっと会ってない。それなのに。{nw}"
        $ kag_wait(1000, canskip=False)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        if kag_f.judgeflag==3:
            $ kag_playse('9-0215.ogg', buf=0, loop=False)
        $ kag_set_next_indent('りずむ「')
        "りずむ「……{w=0.65}ママ」{nw}"
        $ kag_wait(1500, canskip=False)
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
        $ kag_playse('4-0608.ogg', buf=0, loop=False)
        $ kag_set_next_indent('おんぷ「')
        "おんぷ「ちゃんと心配してくれている人がいるんだから、大丈夫よ」{nw}"
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        if kag_f.judgeflag==3:
            $ kag_playse('9-0216.ogg', buf=0, loop=False)
        $ kag_set_next_indent('りずむ「')
        "りずむ「うん……{w=0.6}うん……」{nw}"
        $ kag_wait(1500, canskip=False)
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
        $ kag_playse('4-0609.ogg', buf=0, loop=False)
        $ kag_set_next_indent('おんぷ「')
        "おんぷ「ほら、もう泣かないで」{nw}"
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        if kag_f.judgeflag==3:
            $ kag_playse('9-0217.ogg', buf=0, loop=False)
        $ kag_set_next_indent('りずむ「')
        "りずむ「うん、ありがとう……{w=0.6}おんぷちゃんは、この手紙、読んだんですか？」{nw}"
        $ kag_wait(1000, canskip=False)
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=False)
        $ kag_playse('4-0610.ogg', buf=0, loop=False)
        $ kag_set_next_indent('おんぷ「')
        "おんぷ「……{w=0.2}悪いかなって思ったんだけどね」{nw}"
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        if kag_f.judgeflag==3:
            $ kag_playse('9-0218.ogg', buf=0, loop=False)
        $ kag_set_next_indent('りずむ「')
        "りずむ「ううん。{w=0.4}手紙を見てたから、わたしのことを、{w=0.4}気づかってくれたんですよね？」{nw}"
        $ kag_wait(1000, canskip=False)
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
        $ kag_playse('4-0611.ogg', buf=0, loop=False)
        $ kag_set_next_indent('おんぷ「')
        "おんぷ「そうでもなかったわ。{w=0.4}読んでも読まなくても同じだったと思う。{w=0.4}だって……」{nw}"
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_set_next_indent('りずむ「')
        "りずむ「？」{nw}"
        $ kag_wait(1500, canskip=False)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=False)
        $ kag_playse('4-0612.ogg', buf=0, loop=False)
        $ kag_set_next_indent('おんぷ「')
        "おんぷ「手紙に書いてあるりずむちゃんと、目の前にいるりずむちゃんは、{w=0.4}同じだったから」{nw}"
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
        if kag_f.judgeflag==3:
            $ kag_playse('9-0219.ogg', buf=0, loop=False)
        $ kag_set_next_indent('りずむ「')
        "りずむ「おんぷちゃん……」{nw}"
        $ kag_wait(1500, canskip=False)
        $ kag_ws(buf=0, canskip=False)
        $ kag_stopse(buf=0)
        $ kag_wait(1000, canskip=False)
        $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0613.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「帰ったら、りずむちゃんは何をするの？」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0220.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「まずママに会って、いっぱいお話をして、{w=0.4}それからラジカセを出しておんぷちゃんのＣＤをきいて……」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0220.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ！{w=0.4}お城の仕事場の改装もしないと！それから……」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0614.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ、帰ったらいそがしいわよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0221.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「１つずつなら、きっとなんとかなります」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0615.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。{w=0.4}でも、もしつらいことや、かなしいことがあったら……」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0616.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「その時は、またこっちにおいでよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0222.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}そうでなくても、またみんなに会いたいですから」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0223.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、最後に１つだけ、聞きたいことがあるんですけど」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0617.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なぁに？」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0224.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしと……{w=0.6}わたしとおんぷちゃんは、友だちになれたのかな？」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「…………」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '04おんぷ-09', time_ms=2000, bgcolor='0x000000')
    $ persistent.cgo6=1
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('4-0618.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしでよければ、そばにいるよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0225.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……」{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0226.ogg', buf=0, loop=False)
    "その先は、もう言葉にならなかった。{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0227.ogg', buf=0, loop=False)
    "みんなに会えて、本当によかった。{nw}"
    $ kag_wait(2000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_wait(1000, canskip=False)
    if kag_f.judgeflag==3:
        $ kag_playse('9-0228.ogg', buf=0, loop=False)
    "お別れなのに、わたしは涙で顔がぐしゃぐしゃなのに、{nw}"
    $ kag_wait(5600, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_cm()
    "不思議とかなしいとは思わなかった。{nw}"
    $ kag_wait(2000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', 'white', time_ms=2000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_wait(2000, canskip=False)
    $ kag_playse('4-0619.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「がんばれ！{w=0.5}りずむちゃん」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0229.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.oc_s=1
    $ layerposition_def()
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    $ persistent.clearChar=4
    $ kag_bgmopt(volume=100, gvolume=None)
    if persistent.o_n_end!=1:
        $ persistent.o_n_end=1
        $ persistent.NormalCnt += 1
    if persistent.o_t_end!=1:
        $ persistent.o_t_end=1
        $ persistent.TrueCnt += 1
    $ kag_fadeinse('bgm-v02', time_ms=300, buf=0)
    if kag_f.judgeflag!=3:
        $ persistent.o_t_end=0
        $ kag_stopse(buf=0)
        $ kag_fadeinse('bgm-v03', time_ms=300, buf=0)
    jump kag_endroll_o_gamestart
    call kag_s_wait
    return
