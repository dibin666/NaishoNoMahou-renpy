# Auto-generated from 02. hazuki/hz_C.ks by tools/transpile_ks.py
label kag_hz_c:

label kag_hz_c_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hazuki.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg021', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hz_c_hz__dash__c_00:
    $ kag_set_bookmark('「エンディング」さよなら、そして始まり')
    $ kag_cm()
    "夕方、そろそろＭＡＨＯ堂も閉店の時間。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('A-0032.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「ありがとうございました～」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('1-0641.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや～、何だか今日はお客さんがたくさん来たね～」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('3-0257.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマやなぁ～{w=0.4}ぎょーさん売れたわ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "普段通りの会話。{w=0.8}お客さんが多くても少なくても、みんなは何も変わらない。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0188.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあ、そろそろお店を閉めましょうか」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('5-0156.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あ、そういえば今日のおやつが少し残ってるよ～」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('6-0179.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん食べる～」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "３時には、いつものようにみんなでおやつを食べていた。{w=0.8}いつもと何も変わらない１日だった。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "ちょっとだけいつもとちがったことといえば、朝、はづきちゃんといっしょにＭＡＨＯ堂にやって来たことくらい。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "２人でアクセサリーを作った。{w=0.8}２人で作ったアクセサリーが売れて、とってもうれしかった。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('2-0453.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃあわたし、戸じまりをしてくるわね」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0132.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、わたしも手伝います」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_fadeoutbgm(5000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=2000, bgcolor='0x000000')
    $ kag_wait(500, canskip=False)
    $ kag_mesframe()
    "わたしは、ＭＡＨＯ堂のドアプレートを『ＣＬＯＳＥＤ』にした。{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg020', time_ms=2000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_c_hz__dash__c_01:
    $ kag_set_bookmark('「エンディング」さよなら、そして始まり')
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0133.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、今日まで本当にありがとうございました」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "明日には、このＭＡＨＯ堂にわたしはいない。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('1-0642.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、そんなことないよ！{w=0.4}あたしたちの方こそ、ありがとうだよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0134.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん、そんな……」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('3-0258.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマやで。{w=0.4}仕事もバッチリ手伝うてもろたし」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0135.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん……」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('4-0189.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしたちも、りずむちゃんの助けになれたかな？」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0136.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん。{w=0.4}もちろんです……」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('5-0157.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「楽しかったよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0137.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん……{w=0.65}うん、わたしも楽しかったです」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('6-0180.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんも、とっても楽しかった♪」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0138.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('2-0454.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、はい」{nw}"
    $ kag_wait(1000, canskip=False)
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0139.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「これは？」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "はづきちゃんの手のひらに乗っているのは、ビーズを使ったきれいなブレスレットだ。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=False)
    $ kag_playse('2-0455.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「これ、みんなからのプレゼント」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '02はづき-09', time_ms=2000, bgcolor='0x000000')
    $ persistent.cghz7=1
    $ kag_mesframe()

label kag_hz_c_hz__dash__c_02:
    $ kag_set_bookmark('「エンディング」さよなら、そして始まり')
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0141.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ、きれいですね」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "夕日をうけたビーズが、キラキラと光る。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('3-0259.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんに気づかれへんように作るの、けっこう大変やってんで！」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('1-0643.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうそう、ハナちゃんが大きな声で『それがプレゼントなのぉ～』とか大きな声で言っちゃったときは、{w=0.4}もう心臓が止まるかと思ったよ～」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('4-0190.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんだって、最初はりずむちゃんの手首をはかろうとしてたじゃない」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('4-0190.2', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしはそっちの方がおどろいちゃったわよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_stopse(buf=0)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('1-0644.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、あれはついうっかりして……」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0033.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「あはははは」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0142.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、ありがとう」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('1-0645.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あのね、デザインは、はづきちゃんが考えたんだよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0143.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('3-0260.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はづきちゃんが言い出して、ほんならみんなで作ろかってことになってんな」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0457.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ゆうべに思いついたから、時間がなくって。{w=0.4}こんなことくらいしかできないんだけど」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0144.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな、こんなにしてもらって、ホントはわたしがお礼をしなくちゃいけないのに」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0458.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お礼じゃないのよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playbgm('m413a', loop=True)
    if kag_f.judgeflag==3:
        $ kag_playse('9-0145.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0459.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしたちの、わたしの気持ちをりずむちゃんに伝えたくって……{w=0.55}だから」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0146.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん……」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0147.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「きっと、きっとまたみなさんに会いにきます！」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "はづきちゃんと出会えて、みんなと出会えて、わたしはしあわせでいっぱいだった。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0460.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0148.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「そしたら、またＭＡＨＯ堂のお仕事も手伝います」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0461.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ、よろしくね」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0149.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いっしょにお出かけもしましょう」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0462.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「楽しみね」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0150.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「どこがいいかな？{w=0.4}今度は駅前の商店街とか？{w=0.4}海もいいかも」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0463.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフフ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0151.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「どこにしよう……{w=0.6}今から迷っちゃいます」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0464.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフ。{w=0.4}また来たときに決めましょうよ」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0152.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「そっか、そうですね」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0465.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「約束よ、りずむちゃん」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0153.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.8}また会いましょう」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_playse('2-0466.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うん、きっとね……」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_fadeoutbgm(5000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=2000, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg020', time_ms=2000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_c_hz__dash__c_03:
    $ kag_set_bookmark('「エンディング」さよなら、そして始まり')
    $ kag_cm()
    "もうちょっとで泣いてしまいそうだった。{nw}"
    $ kag_wait(800, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "でもこらえた。{w=0.8}だって、はづきちゃんは笑っていたから。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "それはきっと、また会えるって信じているんだって。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "わたしもそう信じていたい。{w=0.8}だから涙をこらえた。{nw}"
    $ kag_wait(1500, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg019', time_ms=2000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_c_hz__dash__c_04:
    $ kag_set_bookmark('「エンディング」さよなら、そして始まり')
    $ kag_cm()
    "ＭＡＨＯ堂の中庭には、魔女界への扉が開いていた。{w=0.8}ほうきに乗ったわたしは、扉の向こうを見つめている。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0154.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん本当に、本当にありがとう！」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    "みんなは、見上げながら手をふって、わたしを送ろうとしている。{nw}"
    $ kag_wait(1200, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0155.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「さようなら！」{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'white', time_ms=2000, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_mesframe()
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0156.ogg', buf=0, loop=False)
    "わたしのうでには、はづきちゃんからもらったブレスレットが揺れていた。{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(1500, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0157.ogg', buf=0, loop=False)
    "みんなの気持ち。{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0158.ogg', buf=0, loop=False)
    "わたしの気持ち。{nw}"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    if kag_f.judgeflag==3:
        $ kag_playse('9-0159.ogg', buf=0, loop=False)
    "ずっと、ずっと忘れない！"
    $ kag_ws(buf=0, canskip=False)
    $ kag_wait(2000, canskip=False)
    $ kag_wait(1000, canskip=False)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hzc_s=1
    $ layerposition_def()
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    $ persistent.clearChar=2
    if persistent.hz_n_end!=1:
        $ persistent.hz_n_end=1
        $ persistent.NormalCnt += 1
    if persistent.hz_t_end!=1:
        $ persistent.hz_t_end=1
        $ persistent.TrueCnt += 1
    $ kag_fadeinse('bgm-v02', time_ms=300, buf=0)
    if kag_f.judgeflag!=3:
        $ persistent.hz_t_end=0
        $ kag_stopse(buf=0)
        $ kag_fadeinse('bgm-v03', time_ms=300, buf=0)
    jump kag_endroll_hz_gamestart
    call kag_s_wait
    return
