# Auto-generated from 01. doremi/d_B2.ks by tools/transpile_ks.py
label kag_d_b2:
    "r;================================================================================================================================={nw}"

label kag_d_b2_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_doremi.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg214', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_d_b2_d__dash__02_00:
    $ kag_set_bookmark('「２日目」一生懸命少しずつ・・・')
    $ kag_cm()
    $ kag_playbgm('bgm-001', loop=True)
    "青い空。"
    extend "\n照りつける太陽。"
    extend "\nセミの鳴き声。"
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()

label kag_d_b2_d__dash__02_01:
    $ kag_set_bookmark('「２日目」一生懸命少しずつ・・・')
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('どれみ「')
    "どれみ「………………」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('「')
    "「…………………………」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0136.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日もあついねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0005.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「そうだねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0137.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日も平和だねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0006.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「そうだねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('どれみ「')
    "どれみ「………………」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('「')
    "「…………………………」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0138.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日もお客こないねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0007.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「こないねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg003', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('se-009.2.ogg', buf=1, loop=False)
    $ kag_set_next_indent('お客さん「')
    "お客さん「ごめんください……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-022.ogg', buf=1)
    $ kag_playse('A-0008.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「いらっしゃいませ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「あ、ご、ごめんなさい！"
    extend "ちょっと用事を思い出したわ！"
    extend "またくるわね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-031.2.ogg', buf=1)
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0139.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「また、帰っちゃった……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0036.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「これで３人目ね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "昨日みんなで片づけをした後、どれみちゃんとわたしがつくった商品で在庫をそろえたんだけど。"
    $ kag_cm()
    "お店に入ろうとしたお客さんみんなが同じく、商品を見てまわれ右をする。"
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_drawchar('d_12.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0140.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「何も帰らなくてもいいじゃんね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0047.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そや、ちょっとくらい不細工やからって、帰ることないやんか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0141.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃん、それどういう意味？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0048.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「え、いやいや、{w=0.5}まあ、その、あはは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0037.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「普通のお客さんには、インパクトが強すぎるのかも」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_12.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0142.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうかなあ？{w=0.45}あたしはこれくらい刺激があった方が、おもしろいかなって思うんだけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0049.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あった方がっちゅーか、刺激だらけやんか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0050.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほら、これなんか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0143.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？{w=0.35}それはりずむちゃんが作ったんだよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0051.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「え」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0037.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「っ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0144.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃんひどいな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0052.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ……、あたしはてっきりどれみちゃんが作ったのかと思って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0038.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あいちゃん、フォローになってないわ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ひょっとして、わたしのつくった商品がいけないんでしょうか……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0053.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いやあ、気にすることないって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0045.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうよ。{w=0.35}昨日みたいにたくさん売れる日もあれば、こういう日もあるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お客さんが、回れ右してしまう日があるんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0046.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0054.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それは……{w=0.4}ないな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「やっぱり……{w=0.35}わたしがみなさんにご迷惑をおかけしてるんですね」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0145.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんがあやまることないよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0146.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「たぶん、あたしの教え方がまずかったんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('1-0147.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「何度も練習すればきっとうまくなるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0039.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうだわ、今度はちがう人がりずむちゃんに教えるっていうのはどうかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0055.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、それええなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0047.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあ今日は変わりばんこで教えることにしましょうか？{w=0.4}りずむちゃん、それでいい？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。"
    extend "みなさんのアクセサリーの作り方、教えてください」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0056.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まかしとき！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b2_d__dash__02_02:
    $ kag_set_bookmark('「２日目」一生懸命少しずつ・・・')
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0033.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Very good！{w=0.35}だいぶうまくなったね！りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0040.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ホント！{w=0.35}これなんかとてもかわいいし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0057.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「バンバン売れそうやで！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0048.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんて、実はかなり器用なのね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ……{w=0.6}そんなことないです……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0034.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おせじじゃないよ。{w=0.45}ほら、昨日作ったのよりずっと上手だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0148.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0058.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃん、そんなにおちこまんでもええやん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0149.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「娘よ、大きくなったね～。{w=0.45}あたしに教えられることはもう何もないさぁ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんなことないですよ！"
    extend "どれみちゃんといっしょに作っているとき、とても楽しかったし……」"
    $ kag_cm()
    $ kag_playse('1-0150.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、ありがと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0035.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そろそろお茶にしよっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0151.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え！{w=0.35}ももちゃん、もしかして今日は……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0036.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃんがこの間食べそこなったクッキーと、同じの作ってきたよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0152.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やったああ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんなに大事なクッキーなんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0041.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ちがうのよ。{w=0.4}この間、最後の１個をハナちゃんに食べられちゃっただけなのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はあ……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0059.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「も～どれみちゃんゲンキンやから～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0037.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあ、わたしクッキーにクリームのっけてくる」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0153.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしやる！{w=0.35}やらせて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0038.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それじゃあ、お願い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、わたしも手伝います！」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0154.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「さんきゅ～。{w=0.4}じゃあみんな、テラスでまってて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg009', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m67', loop=True)

label kag_d_b2_d__dash__02_03:
    $ kag_set_bookmark('「２日目」一生懸命少しずつ・・・')
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('はづき「')
    "はづき「……」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0039.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃんたち、遅いねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0042.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どうしたのかしら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0060.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ちょっとみてこよか～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-005.ogg', buf=1)
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0155.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うわ～ごめん、転んじゃった！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃんだいじょうぶ！」"
    $ kag_cm()
    $ kag_playse('1-0156.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、そこ、すべるから気をつけて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、えっ！きゃっ！」"
    $ kag_cm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0061.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なーんか、似たもの同士やな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0043.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ホントね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0049.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんが２人いるみたいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0040.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「アンビリーバボー！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg009', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b2_d__dash__02_04:
    $ kag_set_bookmark('「２日目」一生懸命少しずつ・・・')
    $ kag_cm()
    "数分後……"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0157.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんな！お待たせ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0158.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんがクリームを泡立てて、２人でデコレーションしました～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "テーブルの上には、形がくずれたクリームののった、欠けたクッキー。"
    $ kag_cm()
    "わたしとどれみちゃんで、どうにかテーブルまで運べたものの……"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0044.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あははは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0062.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「やっぱ２人になるとちがうな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0159.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0050.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「何でもないのよ、さ、頂きましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "みんながクッキーに手を伸ばす。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0030.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おいしいおいしい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0063.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん、おいしいやん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0045.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ホント」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ごめんなさい。"
    extend "ちょっとかざりつけに失敗しちゃいました」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0064.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなん気にすることあらへんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0160.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうそう。{w=0.4}大切なのは、まごころだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0051.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんの場合、ちょっと失敗が多すぎるけどね！」{nw}"
    $ kag_history_opt(output=False, enabled=None)
    $ kag_waitclick()
    $ kag_history_opt(output=True, enabled=None)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0161.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなぁ～おんぷちゃ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0052.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ、冗談よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0046.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ももちゃんどうしたの？{w=0.4}さっきからだまっちゃって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0041.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「う～ん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あのぉ、お口にあわなかったでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おいしいおいしい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0042.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「この味……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0043.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「この舌ざわり……{w=0.4}すごい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0044.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「このクリーム、りずむちゃんが泡立てたんだよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0045.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、\nひょっとしてお菓子作りの才能あるかも！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0065.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんな、ホイップぐらいで大げさな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0046.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ＮＯ！{w=0.25}『千里の道も一刀両断！』{w=0.4}基本を守ることは、とっても大事だよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0047.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「『千里の道も一歩から』よ。{w=0.35}ももちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0066.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「う～ん、たしかにお好み焼きも生地が命やしなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0053.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なんだか、クリームのあと味が軽いのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0162.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんすごい！{w=0.4}ももちゃんがココまで言うんだから、才能あるんだよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ、は、はい、ありがとうございます！」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0047.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん。{w=0.4}今度のティータイムのときに、わたしとお菓子作ろうよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おいしいおいしい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0163.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃ、さっそくあたしも１つ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ひょい"
    extend "ぱく"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0164.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0033.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ごちそうさま」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0165.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、{w=0.5}あ、{w=0.5}あ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0034.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「は～おいしかった。{w=0.4}ハナちゃんしあわせ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0166.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしのクッキ～～～～～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg020', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b2_d__dash__02_05:
    $ kag_set_bookmark('「２日目」一生懸命少しずつ・・・')
    $ kag_cm()
    "そろそろ閉店の時間だ。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0167.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日はさっぱり売れなかったねぇ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0009.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「そうだねぇ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0054.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたし、そろそろ、ドラマのお仕事があるから出かけなきゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0048.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしもそろそろバイオリンのおけいこがあるから、今日はここらへんで閉店にしましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0067.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0035.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「よ～し、ハナちゃんがんばって後片づけしちゃうもんね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0168.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ～あ、お腹へったなぁ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0048.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「また作るから、落ち込まないの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今度はもっとたくさん作った方がいいですよね」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0049.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0169.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんてったって、あたしは２回分食べるんだからね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふっ」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b2_d__dash__02_06:
    $ kag_set_bookmark('「２日目」一生懸命少しずつ・・・')
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0055.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0010.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「バイバ～イ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0049.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「みんなまた明日ね～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0011.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「バイバ～イ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0068.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、あたしとももちゃん、もう帰るけど、どれみちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0170.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、あたしはもう少ししたら帰る」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0069.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、また～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0050.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「シ～ユ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0012.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「バイバ～イ、また明日～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0036.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんちょっと眠いから、先に部屋に戻ってるね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0171.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おやすみ、ハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0037.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おやすみ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おやすみなさい、ハナちゃん」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0172.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、今日はごめんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？ごめんって……」"
    $ kag_cm()
    $ kag_playse('1-0173.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ＭＡＨＯ堂のお仕事のこと。{w=0.4}あたしの教え方が悪くて、なんかかえって足ひっぱっちゃったみたいで……{w=0.55}ごめん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん、そんなことないです。"
    extend "みなさんにも教えてもらったけど、どれみちゃんの教え方が悪かったわけじゃなくて、ちょっとしたコツがいるってだけだったから」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0174.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうなんだ……{w=0.65}よかった～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だから……{w=0.6}また教えてください」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0175.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、わかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それと……{w=0.6}今日は１ついいことがありました」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0176.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いいこと？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、ももちゃんにホイップが上手だって言われて、すごくうれしかったんです」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんか、自分がやったことをほめられたのって、久しぶりかなって」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0177.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だから、どれみちゃんはわたしにあやまることなんてないです！"
    extend "むしろ、わたしがどれみちゃんにお礼を言わなきゃ。{w=0.5}ありがとう……」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0178.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんな、へへへ、照れちゃうな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0179.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃ、あたしも帰るね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、また明日」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0180.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「バイバイ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "さあ、今日教えてもらったことのおさらいをしなくちゃね。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.d2_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_d_b3_gamestart
    return
