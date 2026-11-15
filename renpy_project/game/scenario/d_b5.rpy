# Auto-generated from 01. doremi/d_B5.ks by tools/transpile_ks.py
label kag_d_b5:

label kag_d_b5_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_doremi.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg014', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_d_b5_d__dash__05_00:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "今日はわたしとぽっぷちゃんの２人でお店番。"
    extend "\nどれみちゃんたちは学校の登校日だそうで、そのあとクラブ活動もあるそうだ。"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0299.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあ行ってくるから、りずむちゃん、ぽっぷ、あとよろしくね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「だ～いじょうぶだって！まっかせなさい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0300.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホントに～？{w=0.4}りずむちゃん、まだなれてないんだから、アンタがしっかりしなきゃダメだよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0011.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねえちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0301.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「何よ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「はいこれ、うわばき」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0302.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へ{w=0.3}？{nw}"
    $ kag_drawchar('d_05.tlg', time_ms=100, sepia=False, canskip=True)
    extend "あああ～！忘れてた～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あたしが気づいたからよかったけど、学校で大恥かくところだったよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0303.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ありがとうぽっぷ～\n{nw}"
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    extend "あ、いや、ぽっぷ様～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0014.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「もう、調子いいんだから～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0304.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へへへ、それじゃ行ってくるね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いってらっしゃい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "わたしとぽっぷちゃんに見送られて、どれみちゃんは学校へ向かった。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0015.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「まったく、いつもこんなだから、やんなっちゃうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「気がきくんですね。ぽっぷちゃんは」"
    $ kag_cm()
    $ kag_playse('7-0016.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねえちゃんがおっちょこちょいなだけだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0017.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そんじゃ、お店開けようか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b5_d__dash__05_01:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_playbgm('m60', loop=True)
    $ kag_cm()
    $ kag_sound_se('se-009.1.ogg', buf=1)
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0018.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「は～い、いらっしゃいませ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いらっしゃいませ～！」"
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「これはなに？」"
    $ kag_cm()
    $ kag_playse('7-0019.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あっ、それはですね！{w=0.4}虹のイメージで作ったブレスレットです！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「へぇ～、なかなかステキね」"
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「うん、じゃあこれをください」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0020.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「はい、毎度ありがとうございます！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうございます！」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「１０００円お預かりします！{w=0.4}はい、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0022.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「お会計。{w=0.4}レジに行っておつり持ってきて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    "ぽっぷちゃん、なんかベテラン店員って感じだ。"
    extend "\nわたしは小走りでレジに向かい、会計をすませた。"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0023.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ありがとうございました～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとうございました！」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0024.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「さ、上に行こ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_d_b5_d__dash__05_02:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぽっぷちゃん、なんかもうベテランって感じですね」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0025.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「まあね～。{w=0.4}なにせおねえちゃんたちとＭＡＨＯ堂でお手伝いして、もう４年目だもん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すごい！なんか尊敬しちゃいます！」"
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0026.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あはは、なんか照れくさいな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-009.1', buf=1)
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0027.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あっ、お客さんだ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0028.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「いらっしゃいませ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたしもがんばらなくっちゃね。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いらっしゃ……」"
    $ kag_cm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いたぁ～！」"
    $ kag_cm()
    $ kag_playse('7-0029.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「り、りずむちゃんだいじょ～ぶ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいたた……」"
    $ kag_cm()
    "な、何もないところで転ぶなんて、まるで……"
    $ kag_cm()
    "…………"
    $ kag_cm()
    "……どれみちゃんみたい。"
    $ kag_cm()
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('note', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_sound_se('se-009.1', buf=1)
    $ kag_set_next_indent('お客さんＡ「')
    "お客さんＡ「こんにちは～」"
    $ kag_cm()
    $ kag_sound_se('se-009.1', buf=1)
    $ kag_sound_se('se-009.2', buf=1)
    $ kag_set_next_indent('お客さんＢ「')
    "お客さんＢ「ごめんください」"
    $ kag_cm()
    $ kag_set_next_indent('お客さんＣ「')
    "お客さんＣ「すみませ～ん」"
    $ kag_cm()
    $ kag_playse('7-0030.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_sound_se('se-009.1', buf=1)
    $ kag_set_next_indent('お客さんＤ「')
    "お客さんＤ「こんにちは～」"
    $ kag_cm()
    $ kag_set_next_indent('お客さんＥ「')
    "お客さんＥ「すみませ～ん、これいくらですか？」"
    $ kag_cm()
    $ kag_set_next_indent('お客さんＦ「')
    "お客さんＦ「ちょっとこの商品みていいかしら」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.7}あの……」"
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃん！{w=0.4}ぼうっとしてる場合じゃないよ！ほら早く！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0032.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「少々おまちください！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええと、こちらの商品は……」"
    $ kag_cm()
    "今日はものすごいお客さんの入りだ。"
    $ kag_cm()
    "わたしとぽっぷちゃんは、お店を所せましとかけずりまわった。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b5_d__dash__05_03:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0033.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ありがとうございました～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとうございました！」"
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0034.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「はあ、終わった……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ようやくひと息ですね」"
    $ kag_cm()
    $ kag_playse('7-0035.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「よりによって、あたしとりずむちゃんしかいないのに、あんなにお客さんくるんだもんなぁ～……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あはは、でも、たくさん売れたから良かったですね！」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0036.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そうだね！{w=0.45}きっとみんなびっくりするよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ところでぽっぷちゃん、これからどうします？"
    extend "\nそろそろ閉店にしますか？」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0037.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「う～ん、もういい時間だし、閉めよっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃあわたし、ホウキ取ってきますね」"
    $ kag_cm()
    $ kag_playse('7-0038.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()

label kag_d_b5_d__dash__05_04:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃんたち、遅いですね～」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0039.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「たぶん、クラブの練習をしてるんだと思うよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「けっこう、遅くまでやるんでしょうか」"
    $ kag_cm()
    $ kag_playse('7-0040.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「どうかなぁ？{w=0.4}でも、このまま待ってるのももったいないし、公園に行こうよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？公園ですか？」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0041.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うん、外もすずしくなってきたしさ。行こ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃあ、ちょっとお出かけしましょうか」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg087', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b5_d__dash__05_05:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0042.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃ～ん、はやくはやく～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんなに急がなくても……」"
    $ kag_cm()
    $ kag_playse('7-0043.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「日がくれちゃうよ～？{w=0.4}{nw}"
    $ kag_drawchar('p_06.tlg', time_ms=100, sepia=False, canskip=True)
    extend "あっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぽっぷちゃん！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '01どれみ-05.tlg', time_ms=1000, bgcolor='0x000000')
    $ persistent.cgd3=1
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('7-0044.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「いたたた……{w=0.65}転んじゃった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「大丈夫？」"
    $ kag_cm()
    $ kag_playse('7-0045.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あっ、だ、大丈夫だよこんなの、かすりキズだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「大変！血が出てる！」"
    $ kag_cm()
    "わたしは、ぽっぷちゃんを抱きかかえるようにして水飲み場まで運んでいった。"
    $ kag_cm()
    $ kag_playse('7-0046.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「り、りずむちゃん。そんな、大げさすぎだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「バイキンが入ったら大変ですよ！」"
    $ kag_cm()
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「……」"
    $ kag_cm()
    "水でキズ口を洗ってから、ハンカチを取り出し、ぽっぷちゃんのひざに当てる。"
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_playse('7-0047.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ありがとう、りずむちゃん{w=0.55}\n……へへへ。{w=0.5}なんか、おねえさんみたいだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？どれみちゃんみたいですか？」"
    $ kag_cm()
    $ kag_playse('7-0048.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ううん、そうじゃなくって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('7-0049.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うーん……{w=0.6}何となくそう思っただけ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか」"
    $ kag_cm()
    $ kag_playse('7-0050.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ホントにありがと。{w=0.4}もう平気だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg087', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b5_d__dash__05_05b:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0051.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お仕事はすごくてきぱきしてたのに、ぽっぷちゃんも、そそっかしいところがあるんですね」"
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0052.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そんなことないよ。{w=0.4}おねえちゃんよりましだもん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは、どれみちゃんのことですか？」"
    $ kag_cm()
    $ kag_playse('7-0053.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そう！{w=0.45}今日はうわばきだったけど、学校があるときって、だいたい週に１度は、忘れ物をあたしが届けてるんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは……{w=0.45}たしかにそそっかしいというか」"
    $ kag_cm()
    $ kag_playse('7-0054.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そのくせお弁当だけは絶対に忘れないしさ～。{w=0.4}ホント、やんなっちゃうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あははは」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0055.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あたしとちがってぜーんぜんモテないしさ、もう妹としてはずかしいよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「う～ん、でも、どれみちゃんってやさしいし、いいところはいっぱいあると思うんですけど」"
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0056.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ええ～？そうかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん。{w=0.55}わたし、ＭＡＨＯ堂に来たときって、すごく落ち込んでたんだけど」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0057.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今はそうでもない、っていうか、失敗してもへこたれないどれみちゃんを見てて、わたしもあんな風になれれば、\nって思ったの」"
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0058.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「う～ん。{w=0.45}よくわからないけど、めざすほどの物じゃないと思うよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0059.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねえちゃんは明るいだけがとりえだもん。"
    $ kag_playse('7-0059.2', buf=0, loop=False)
    extend "りずむちゃんなら、アクセサリー作りも上手だし、食い意地もはってないから、おねえちゃんなんてすぐに追いこせるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あはは、ありがとう」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg015', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b5_d__dash__05_06:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0060.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あれ、明かりがついてる。{w=0.4}みんな帰ってきたんだ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ぽっぷちゃん！まだ走らない方が……」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0061.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「へーきへーき。{w=0.45}もういたくも何ともないもん！{w=0.45}いこ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b5_d__dash__05_07:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0062.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「たっだいま～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0305.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、ぽっぷ。りずむちゃんも。{w=0.5}どこ行ってたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、いっしょに公園に行ってました」"
    $ kag_cm()
    $ kag_playse('1-0306.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうなんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0111.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お、２人とも帰ってきたで～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「おかえりなさい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0078.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「おかえり」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おかえり～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0057.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おかえり！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ただいま、です」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0063.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「今日さ～いっぱいお客さんがきて大変だったんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0307.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あれ、ぽっぷ。{w=0.35}そのハンカチどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0064.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ちょっと公園で転んじゃって。{w=0.4}りずむちゃんに手当てしてもらったの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0308.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え、そうなの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「大したケガじゃないんで、心配いりませんよ」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0309.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ありがとう。{w=0.55}ハンカチ、ちゃんと洗って返すからね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな、気にしないでください」"
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0310.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぽっぷ！{w=0.4}ちゃんとお礼言った？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0065.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「もう言ったよ！{w=0.4}幼稚園児じゃないんだから、よけいなお世話焼かないでよね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0311.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まったく生意気なんだから……{w=0.5}ほら、バンソーコー」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0066.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「……うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0112.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「今日はえらいいそがしかったんちゃう？{w=0.55}品物がかなりへってるみたいやけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}でもぽっぷちゃんがいてくれたから、とても助かりました」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0079.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ぽっぷちゃんは、お店番上手だもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お客さんの相手とか、すごくしっかりしてますよね。{w=0.55}わたしなんか、もうしどろもどろで……」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0067.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そんなことないよ。{w=0.4}りずむちゃんだって、お客さんとすごく楽しそうに話してたよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？そう……{w=0.5}ですか？」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0068.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うん！{w=0.4}言葉づかいもていねいだったし、あたしが見習いたいくらいだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ほ、ホメすぎですよ」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0113.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、ひょっとして、{w=0.4}マジョリカがいてない間、あたしらのこと監視するように女王様に言われて来たんちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「まさか……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「と、とんでもないです！」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0114.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ウソウソ。{w=0.4}冗談やって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0312.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんに追いつかれないように、あたしたちもがんばらないとね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0080.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。{w=0.4}りずむちゃん、明日もよろしくね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「その前に、どれみちゃん明日は……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0313.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ギク！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0058.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「がっこ～だよね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0314.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「明日も登校日なんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0081.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうじゃないのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん、実は……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0069.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「なになに？{w=0.4}何かあったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0315.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぽ、ぽっぷ、あたしの芋ようかんあげるから、早くかえろ？{w=0.55}ね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「芋ようかんはもらうけど、あたしは続きを聞いてから帰る」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0316.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0082.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そりゃあぽっぷちゃんには、今日提出する宿題のプリントを忘れたなんて、言えないわよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ええ！ホント？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0317.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おんぷちゃ～ん、ヒドイよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「もう～！{w=0.4}せっかくうわばき届けてあげたのに～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0318.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「面目ない……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あははは……」"
    $ kag_cm()
    $ kag_drawchar('d_12.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0319.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でもさ、関先生だってヒドイんだよ？{w=0.55}持ってくるのを忘れただけなのに、『それはやってないのといっしょだ～』\nって言って、あたしだけ宿題追加だよ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「先生、宿題出したのすっかり忘れてたのにね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_12.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0320.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだよ！{w=0.4}あのまま忘れてくれればよかったのにさ、玉木がよけいなこと聞くからさあ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは……{w=0.55}ちょっと運が悪いかも」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0321.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でしょ？あたしって世界一不幸な美少女だよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだ！」"
    $ kag_cm()

label kag_d_b5_choices_d02:
    $ kag_set_bookmark('どれみシナリオ選択肢02')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】手伝いましょうか？', current_stem='d_b5', storage=None, target='*choices_d02-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】魔法で……', current_stem='d_b5', storage=None, target='*choices_d02-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_d_b5_choices_d02__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「よかったらわたし、手伝いましょうか？」"
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0322.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホント？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_d_b5_after_choices_d02
    call kag_s_wait

label kag_d_b5_choices_d02__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag += 1
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ダメだよ！魔法で宿題なんてやっちゃ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}集中できるお勉強部屋をと、思ったんですけど」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0323.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ありがとう。{w=0.4}気持ちだけもらっておくよ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よかったらわたし、手伝いましょうか？」"
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0324.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホント？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_d_b5_after_choices_d02
    call kag_s_wait

label kag_d_b5_after_choices_d02:
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「とか言っておねえちゃん、りずむちゃんに全部やってもらおうとしてるんじゃないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0325.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そそそ、そんなことないよ！ないない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「それに、こっちの科目と魔女界の科目って、いっしょなのかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.6}どうなんでしょう？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0326.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、魔女界の科目ってどんなのがあるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええと、魔女の歴史とか、魔法文字書き取りとか……」"
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「それじゃぜんぜんちがうじゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0327.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ええ～？算数とかはないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「算数……{w=0.6}ですか？魔法電卓を使ってますけど」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0328.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「電卓？それだ！{w=0.4}りずむちゃんそれ貸して！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「算数の宿題で電卓使うなんてズルいよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0329.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぽっぷ～おねえちゃんの危機だよ？{w=0.4}ここは見逃してよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0078.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「スイカ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0330.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0079.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねえちゃん、いつも切ったスイカの大きい方を先に取るでしょ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0331.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ああ、よく見てるね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0080.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「今日から３日間、あたしに大きい方のスイカをくれたら、見逃してあげてもいいかな～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0332.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うぬぬ……{w=0.5}じゃあ、それで手を打とうじゃないの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0081.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「やったあ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0333.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なに？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「電卓なんですけど、家においてきちゃったので、持ってないんです」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0334.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えええ～！やっぱりダメか\n{w=0.6}……ガク」"
    $ kag_freeimage(layer='0', page='fore')
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ごめんなさい。"
    extend "お役に立てなくて」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0082.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「いいのいいの。{w=0.4}あ！{w=0.6}そろそろ晩ごはんの時間だ。{w=0.4}おねえちゃん帰ろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0335.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うう……{w=0.6}それじゃみんな、また明日……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0083.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ほらほら、急がなきゃ！{w=0.45}じゃあね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0336.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ああ……{w=0.6}ゆううつだよ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、さようなら」"
    $ kag_cm()
    $ kag_wait(350, canskip=True)
    $ kag_sound_se('se-031.1.ogg', buf=1)
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg015', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b5_d__dash__05_08:
    $ kag_set_bookmark('「５日目」ステキないもうと')
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「相変わらず仲いいわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃんとぽっぷちゃんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0115.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「やっぱり妹がおると楽しそうやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、それもぽっぷちゃんなら、なおさらですね」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0083.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたし、ぽっぷちゃんみたいな妹がいたらいいなって、思ったことある」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それわたしも」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしもある！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「思ったんですけど、どれみちゃんとぽっぷちゃんって似てませんか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0116.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あはは、似てる似てる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0084.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「２人とも食いしんぼだしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ぽっぷちゃんも意外にそそっかしいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふ、そうですね」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0117.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、あたしらも帰るわ。{w=0.4}またな、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0085.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「また明日ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「さようなら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「バーイ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。さようなら」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……」"
    $ kag_cm()
    "みんなが帰り道に向かう後ろ姿を見て、ふと思い出した。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('sepia', 'bg087', time_ms=1500, bgcolor='0x000000')
    $ kag_frmdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=True, canskip=True)
    $ kag_playse('7-0084.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ありがとう、りずむちゃん……{w=0.55}へへへ。{w=0.5}なんか、おねえさんみたいだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg015', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そっか。"
    extend "ぽっぷちゃんには、ステキなおねえさんがたくさんいるんだね」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.d5_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_d_b6_gamestart
    return
