# Auto-generated from 05. momo/m_B1.ks by tools/transpile_ks.py
label kag_m_b1:

label kag_m_b1_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_momo.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_m_b1_mo__dash__01_00:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0825.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあさっそく、今日はりずむちゃんとの出会いを祝しまして！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0279.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむのカンゲーカイをしよう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええっ！{w=0.4}歓迎会……{w=0.65}ですか？」"
    $ kag_cm()
    "わたしのために、歓迎会を開いてくれるなんて。"
    $ kag_cm()
    "そういえば、魔女界で歓迎会を開いてもらったことはなかったっけ。"
    $ kag_cm()
    "ちょっと感動……"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0807.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そらええ考えやけど、{w=0.4}仕事はどないするん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0826.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うっ……{w=0.55}い、いやほら、りずむちゃん人間界にきたばっかだしさ。{w=0.4}いきなり仕事よりかは、歓迎会でうちとけあってからの方がいいんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0550.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃんの言いたいことはわかるけど、{w=0.4}今からすぐにっていうのはちょっと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0620.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「午前中に終わらせちゃって、{w=0.4}歓迎会はその後にしましょうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0807.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。それやったらええな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0827.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあ、そうしよっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0249.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あっ！{w=0.4}でも、その前にＭＡＨＯ堂の案内はしておいた方がいいよね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっはい。{w=0.4}そうしていただくと助かります」"
    $ kag_cm()
    "これから８日間お世話になる場所なんだから、"
    extend "わたしはももちゃんの提案を、ありがたくうけることにした。"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0551.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「じゃあ、ＭＡＨＯ堂の案内は」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0250.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あたしがやるよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0552.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ももちゃんにまかせるとして、わたしたちは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0808.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「午後の歓迎会のためにちゃっちゃと仕事、{w=0.4}終わらせよっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0621.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0251.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあ、行こ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg006', time_ms=1500, bgcolor='0x000000')
    $ kag_cm()
    $ kag_wait(1500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg009', time_ms=1500, bgcolor='0x000000')
    $ kag_cm()
    $ kag_wait(1500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg010', time_ms=1500, bgcolor='0x000000')
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_01:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ここは？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0252.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「キッチンだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へええ……」"
    $ kag_cm()
    $ kag_playse('5-0253.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どうしたの、りずむちゃん？{w=0.4}キッチン珍しい？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え！{w=0.4}あっ、その……{w=0.6}すごいな……{w=0.5}と思って」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0253.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だって、こんなにりっぱな台所なんで、{w=0.4}びっくりしちゃいました！」"
    $ kag_cm()
    "なんか、ごはんを作るところと言うより、食べ物屋さんの台所みたい。"
    $ kag_cm()
    $ kag_playse('5-0254.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ここのキッチンはね……{w=0.55}思い出の場所なの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「思い出の……{w=0.55}場所？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0255.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「イエス。{w=0.4}あたしたち、前にここでお菓子屋さんをしてたの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんだ」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0256.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「去年、{w=0.4}あたしがアメリカから日本のＭＡＨＯ堂に来て、{w=0.4}今はアクセサリーのお店だけど、どれみちゃんたちと去年１年間、{w=0.4}ここでお菓子屋さんをしてたんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だから、こんなに本格的なんですね」"
    $ kag_cm()
    $ kag_playse('5-0257.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あっ！{w=0.4}でも、今のお店になる時に、その頃のキッチン自体全部消えちゃったから、{w=0.4}今はその時のキッチンとはちがうけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃあ……{w=0.65}何で思い出の場所なんですか？{w=0.4}その時の場所は消えちゃったんですよね？」"
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0258.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ん～、うまく言えないんだけど……{w=0.55}ええと、その時と同じじゃなくてもいいんだ」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0258.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じっさいは変わっちゃったけど、{w=0.4}その時の楽しかったりがんばったりした思い出は変わらないから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "思い出の場所は変わっちゃったけど、思い出は変わらない……"
    $ kag_cm()
    "なんか、こんがらがっちゃいそうな、そうでもないような、変な感じ。"
    $ kag_cm()
    $ kag_playse('5-0259.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「今はね、お菓子を作るのはほとんどあたしなんだけどね。{w=0.4}みんなもお菓子作り上手なんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか～」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0260.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「その、お菓子屋さんをしていた頃って、{w=0.4}どんなお菓子を作っていたんですか？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0261.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「う～ん、クッキーとかシュークリーム。{w=0.4}あとはパティシエ試験でいろんなお菓子を作ったんだよ！{w=0.4}それでね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    "わたしはそのひとつひとつの思い出に聞き入っていた。"
    $ kag_cm()
    "…"
    extend "\n…"
    extend "\n…"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0262.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それでね、この魔女が……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0263.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Oh my god！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ど、どうしたの？」"
    $ kag_cm()
    $ kag_playse('5-0264.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「大変、もうお昼だよ！{w=0.4}みんなの所に戻らないと！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！{w=0.4}そういえば、ずいぶん長話しちゃったみたい」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0265.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ＭＡＨＯ堂を案内するだけだったんだけど、つい去年の話がもりあがっちゃったね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}そろそろ戻った方がいいですよね」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_02:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0266.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Sorry！{w=0.4}みんな、遅くなってごめんなさい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0828.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どうしたの？{w=0.4}キッチンにずっといたみたいだけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0281.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん、もう待ちくたびれちゃった～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0267.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃんと色々お話してたら、遅くなっちゃった。{w=0.4}ハイ、これ差し入れ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'bg239', time_ms=300, bgcolor='0x000000')
    $ kag_wait(1600, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', 'bg017_b', time_ms=300, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0282.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「クッキ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0829.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「さっすが、ももちゃん！{w=0.4}気がきくよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0809.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃんとハナちゃん、ゲンキンやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふっ」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0622.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあ、お言葉に甘えて、ひとやすみしましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0810.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「休憩入れて、もうひとがんばりやな！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0553.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ええ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「（これって……なんだろう？）」"
    $ kag_cm()
    "わたしはどれみちゃんが作っていたアクセサリーが気になっていた。"
    $ kag_cm()
    "小さい頃、魔女博物館でみた呪いのアイテムそっくりなんだけど。"
    $ kag_cm()
    "人間界では何に使うのかな？後で聞いてみよう。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg018', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_03:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    "午後になって、仕事をひと段落させたみんなが中庭にテーブルやイスを運ぶ。"
    $ kag_cm()
    "テーブルにはももちゃんが作ったお菓子がたくさんならべられている。"
    $ kag_cm()
    "そしてジュースでの乾杯も終わり、お菓子をつまみながら話をしている。"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0830.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はぁ～、\nやっぱりももちゃんの作るお菓子はサイコーだね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしは、はじめてたべたんですけど、とってもおいしいです」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0268.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ありがとう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、いいんですか？{w=0.4}お店開けたままなんですよね」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0269.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お客さんが来ても、ここじゃ気づかないんじゃないですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0811.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あぁ大丈夫やて！{w=0.4}こんくらいの時間は、ほとんどお客さんけえへんから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0554.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そういう問題かしら……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0624.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あんまり自信持って言えない話だけど、{w=0.4}そうよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "どうやらＭＡＨＯ堂は開店から閉店まで大はんじょうの大忙し！{w=0.45}ってわけじゃないみたい。"
    $ kag_cm()
    "あれ？"
    extend "みんなの顔がちょっと暗くなった？"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0831.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はぁ～{w=0.55}もっとお店がはんじょうすればいいんだけどね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ＭＡＨＯ堂は、はんじょうしてないんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0832.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うわ、{w=0.4}りずむちゃん、そんな本当のことを！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0812.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お客さけえへんのは今日だけやないからな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0555.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「夏休みに入ってから、毎日こんな感じかも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0625.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「この調子じゃマジョリカが帰ってきたら怒られちゃうわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0833.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でも、{w=0.4}来ないものは来ないんだし、しょうがないじゃんねぇ」"
    $ kag_cm()
    $ kag_playse('1-0833.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おんぷちゃんに宣伝してもらっても、そのときだけしかお客さん来ないしさあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0556.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん……{w=0.6}マジョリカにはそんな理屈は通用しないわ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0270.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「みんな暗いよ！{w=0.4}もっと前向きに考えようよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0813.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0834.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日来たお客さん、{w=0.4}まだひとりだよ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0626.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「さすがにマジョリカが留守の間、ずっとこのまんまじゃまずいわね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0271.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うーん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたしにできることないかな……？"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お店をはんじょう……{w=0.65}そうだ！」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0271.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お客さんがいっぱい来るといいんですよね？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0835.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そりゃあね……{w=0.5}もう、ドバァ～ッとお客さんが来たらうれしいっすけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0284.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ドバァ～ッと！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0557.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「なにかいいアイディアはないかしら……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしにいい考えがあります！！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0042.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたしは水晶玉を取り出し、さっき決めた呪文を唱える。"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ＭＡＨＯ堂を飾り付けして！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_playse('se-047.ogg', buf=1, loop=False)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'bg216', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_04:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_cm()
    $ kag_playse('5-0272.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ケホッケホッケホッ、なんにも見えないよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0836.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どこ～{w=0.6}みんなどこ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0814.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっ！{w=0.45}どれみちゃん！{w=0.4}こんな時は動き回ったら危ないって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0837.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「わぁ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_playse('4-0627.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃん大丈夫……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0838.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いてててて……。{w=0.6}{w=0.4}何かにぶつかった……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', 'bg018', time_ms=3000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_05:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0839.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お、おおぉ～！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0628.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「これは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0840.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「か……{w=0.55}看板？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "煙がほとんどなくなり、さっきどれみちゃんがつまずいた物にみんなが注目する。"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0558.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「……{w=0.65}よね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0273.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「この看板『只今、アクセサリー全品２割引セール開催中』\nって書いてあるよ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0285.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あっ……{w=0.5}こっちは『本日、お買い上げの方にもれなく、ケーキをプレゼント』だって～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0559.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ど、どういうこと……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('4-0629.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「み、みんな外に来て！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg014', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0815.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ま、ＭＡＨＯ堂が……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0286.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おおおお～！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0560.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あ……{w=0.65}あ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ＭＡＨＯ堂の入り口には花輪や『セール中』なんて書いてある看板が。"
    $ kag_cm()
    "屋根とか壁とかも派手な飾り付けがされている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「きっと、これでお客さんがたくさんきます！」"
    $ kag_cm()
    "そう。やっぱり見た目はハデじゃなきゃ！"
    $ kag_cm()
    "わたしは以前に魔女界で見た、魔女がたくさんの行列を作っているお店の見た目を、ＭＡＨＯ堂にあわせてアレンジしてみた。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg006', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_se_loop('se-023.ogg')

label kag_m_b1_mo__dash__01_06:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0841.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お客さんが……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0287.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「いっぱい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0630.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そ、そうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0561.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「すごい……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playbgm('m52', loop=True)
    $ kag_playse('3-0816.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっ、お、お客さんの相手せな！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0274.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わ！{w=0.4}わぁぁ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0562.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「た、大変！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg002', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_07:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('3-0817.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「毎度おおきに～！{w=0.4}はい！{w=0.4}次のお客さんどうぞ～！{w=0.4}えぇと、３点合わせて２４０円になります～{w=0.4}……{w=0.55}５００円お預かりします。{w=0.4}ええ～２６０円のお釣りです！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg004', time_ms=100, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('o_02.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('4-0631.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わぁ～とってもおにあいですよ♪{w=0.4}ぜひ買っていってくださいね！{w=0.65}あっ！それはビーズでできたネックレスです♪{w=0.4}青を基調にしてありまして……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg013', time_ms=100, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('d_03.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('1-0842.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えっ？{w=0.4}これはその、あたしが作った『努力！』をイメージしたアクセサリーなんですけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('1-0842.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えっ？{w=0.45}ど、どのあたりがって、このビーズの赤いトコとか、このへんのこんがらがったあたりとか……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=100, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('hn_08.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('6-0288.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えっと……{w=0.55}ここにビーズを入れて、{w=0.4}それから……{w=0.6}ここから糸を入れて……。{w=0.4}ねぇはづき～！{w=0.45}これでいいのぉ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg003', time_ms=100, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('hz_05.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('2-0563.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「追加の商品、追加の商品。{w=0.4}ああぁ！その前にあれを準備して～。{w=0.4}あ～っ！ハナちゃん！それちがうわ！{w=0.4}これを……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=2)
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_08:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0275.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「次は、{w=0.4}スポンジを作って、その次に生クリームを泡立てるんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0275.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、この生地をオーブンで焼いてもらえるかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "キッチンでは、わたしとももちゃんでお客さんに配るケーキを作っている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1000, bgcolor='0x000000')
    $ kag_cm()
    $ kag_wait(1000, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_09:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0276.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「はぁ～{w=0.4}やっと終わったよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0818.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「さ、さすがにつかれたわ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0289.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん、もう動けない～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたしはと言うと、キッチンで、ももちゃんのお手伝いだったし、魔女界での仕事でこういうドタバタはなれっこだったから、みんなほどつかれてはいなかった。"
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('はづき「')
    "はづき「…………」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「お店、はんじょうしましたね！」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0632.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。{w=0.4}かなりつかれたけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0564.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「……{w=0.3}きっとＭＡＨＯ堂始まっていらいのはんじょうじゃないかしら……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0277.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うんうん！{w=0.4}こんなにいそがしいのなんか、久しぶりだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0819.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「これくらいお客さんが入ったら、{w=0.4}マジョリカも文句は言わへんやろ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0843.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ううう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……？」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0565.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ど、どれみちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0844.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ううう、あたしのだけまた売れてない……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0633.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ま、まあ、こういう日もあるわよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0278.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そ、そうだよ！{w=0.4}『一難去ってまた一難』っていうじゃない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0845.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ううう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0820.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ももちゃん。{w=0.4}それ、フォローになってへんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0846.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ね、ねぇ～りずむちゃんはこれ、{w=0.4}いいと思うよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、ええっと、すいません。{w=0.4}わたし、人間界のことよく知らなくって……」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0290.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみヘタ～。{w=0.4}ハナちゃんが作ったの全部売れちゃったよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0847.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ガーン！{w=0.4}どうせあたしは下手くそですよーだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あのその、売れなかったのはたまたまじゃないでしょうか……」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0848.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いいんだいいんだ、どうせあたしなんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0821.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まあ、ええやん！{w=0.4}過ぎたことをくやんでいてもしゃあないってどれみちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0634.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃん、ファイト！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0279.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ねぇねぇ、{w=0.4}それよりも途中だったりずむちゃんの歓迎会の続きをしようよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0291.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんさんせ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0566.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうね。{w=0.4}夕方になっちゃったけど、続きをしましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お店が大いそがしで、それどころじゃなかったですもんね」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0822.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「よっしゃ！{w=0.4}そうと決まったら、ほら！{w=0.4}どれみちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0849.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はう～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あいちゃんがどれみちゃんの背中を押して中庭の方へ連れて行く。"
    extend "\nまだショックから抜け切れていないみたい。"
    $ kag_cm()
    "がっくりとうなだれて、両手をぶらぶらさせながらあいちゃんに押されていった。"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0280.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それじゃあたし、{w=0.4}今からお菓子作ってくるから、りずむちゃんは中庭で待ってて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.55}わたしもお菓子作り……{w=0.55}手伝っていいですか？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0281.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあ、いっしょに作ろう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg020', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_10:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0292.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇおんぷ？{w=0.4}このコップは、ここでいいの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0635.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん、そこに７人分お願いね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0293.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はぁ～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0567.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あっ！{w=0.4}今、テーブルふくから、ハナちゃんちょっと待って！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0823.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃん、イスはそっちに３つお願い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0850.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ううぅ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0824.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃん気にしすぎやって、もうええかげん立ち直りぃや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0568.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしの見たかぎり、{w=0.4}少なくともお客さん１０人にはすすめてたわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0825.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それで全敗やったんか。{w=0.4}そら落ち込むのも無理ないな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "…"
    extend "\n…"
    extend "\n…"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0282.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それじゃ～みんな！あらためてりずむちゃん、{w=0.4}ＭＡＨＯ堂へようこそ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0043.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「かんぱ～い！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、ありがとうございます！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg002', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b1_mo__dash__01_11:
    $ kag_set_bookmark('「１日目」今日も元気にＭＡＨＯ堂？')
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0826.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あかん、安売りのしすぎや……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0569.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「これじゃ、材料を買うお金を考えると……{w=0.55}ま、{w=0.6}マイナスだわ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0827.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「結局今日は赤字やな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「まさか看板に『お店の人にジャンケンで勝ったら半額サービス中！』って書いてあるなんて思わなくって。{w=0.4}すみません」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0283.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「でも、はんじょうはしたから、魔法は失敗してないよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0828.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「問題なんは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg003', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0293.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみジャンケン弱い～！{w=0.4}ハナちゃん一度も負けなかったよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0850.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どーしてあたしは今日にかぎって一度も勝てないのさあ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg002', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0283.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「やっぱり今日のどれみちゃんは『一難去ってまた一難』だね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0828.6.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなオチかいな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.m1_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_m_b2_gamestart
    return
