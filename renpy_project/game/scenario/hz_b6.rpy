# Auto-generated from 02. hazuki/hz_B6.ks by tools/transpile_ks.py
label kag_hz_b6:

label kag_hz_b6_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hazuki.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg012', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hz_b6_hz__dash__06_00:
    $ kag_set_bookmark('「６日目」りずむと子犬')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    "東の窓から、まぶしい朝日がさしこんでいる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「さあ、今日もがんばらなくっちゃ！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg014', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「まずは玄関のはき掃除っと……{w=0.55}あれ？」"
    $ kag_cm()
    "玄関の前に子犬が１匹、倒れている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……{w=0.55}どうしたの？"
    extend "まさか、死んじゃってるの？」"
    $ kag_cm()
    $ kag_set_next_indent('子犬\u3000「')
    "子犬　「きゅ～ん」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よかった、生きてる……{w=0.5}でも苦しそう」"
    $ kag_cm()
    $ kag_set_next_indent('子犬\u3000「')
    "子犬　「きゅ～んきゅ～ん」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よしよし……{w=0.45}あれ？首輪がついてる。"
    extend "\nってことは、誰かの犬なのかな？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あなたはどこから来たの？"
    extend "……{w=0.55}え？」"
    $ kag_cm()
    $ kag_wait(1200, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、おなかがすいたぁ？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b6_hz__dash__06_01:
    $ kag_set_bookmark('「６日目」りずむと子犬')
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0162.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「なに？りずむ……{w=0.55}どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この子犬、玄関前でたおれてたんですよ」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0163.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うわぁ、かわいい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「話を聞いたら『おなかがすいた』っていうんでミルク飲ませてあげてるんです」"
    $ kag_cm()
    $ kag_playse('6-0164.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇねぇ、ハナちゃんもだっこする～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ミルクを飲み終わるまで、もうちょっと待ってくださいね」"
    $ kag_cm()
    $ kag_playse('6-0165.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん、わかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ、この子、よっぽどおなかがすいてたんですね」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0166.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「でも、どこからきたのかなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「とりあえず今のところはお店であずかりませんか。{w=0.4}このままほっとくわけにもいかないし」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0167.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg013', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b6_hz__dash__06_02:
    $ kag_set_bookmark('「６日目」りずむと子犬')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0326.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あら、この子犬どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この子、おなかがすいててお店の前で倒れてたんです」"
    $ kag_cm()
    $ kag_playse('2-0326.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうなの。りずむちゃん、わたしにもだっこさせて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、どうぞ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0326.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ウフフ、かわいい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントですね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0326.4.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でも、首輪をつけてるってことは飼い犬よね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0326.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どうしてお店の前で倒れてたのかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この子に聞いたんですが、覚えてないって言うんです」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0177.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、そうか。{w=0.4}魔女は動物の言葉がわかるんだもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0240.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「しかし、覚えてないっちゅーのも変やなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0601.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まさか、す、捨てられて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0178.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それなら首輪をつけてないでしょう。{w=0.4}理由はわからないけど、迷子だと思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「子犬なんで、あんまり言葉もはっきりしてないんですよ」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0241.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうかあ。{w=0.4}それはしゃあないなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0327.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「飼い主さん、仕事の合間にでも探しましょうよ。{w=0.4}子犬の足だから、きっとそんなに遠くないところにいると思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0602.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだね。{w=0.4}このまま飼っとくってわけにもいかないもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0168.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「え～、ハナちゃん飼いたい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0149.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ダメだよハナちゃん。{w=0.4}飼い主さん、心配してるかもしれないし、大体マジョリカがいいって言わないよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0603.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだよ、マジョリカにエサ代がもったいないって捨てられちゃうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0169.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うう～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「とりあえず、お店の目の届くところにいてもらいませんか？{w=0.4}外に出しちゃうとまた迷子になっちゃうかもしれないし」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0179.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。{w=0.4}つないでおくってのもかわいそうな気がするし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0604.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「めんどうはみんなで見ようよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0328.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「飼い主さん、早く見つかるといいわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg002', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b6_hz__dash__06_03:
    $ kag_set_bookmark('「６日目」りずむと子犬')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、１５０円のお返しです」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0329.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「なんで今日に限って\nこんなにお客さんきちゃうのかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0170.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そうだよ、ハナちゃんプリンとぜんぜん遊べない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0242.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃん、その『プリン』て……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0171.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ワンちゃんの名前。プリンに決定！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0243.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、まあええけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0150.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Cookie！Cookieったら、ご飯だよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0330.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ももちゃん、その『クッキー』って……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0151.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「茶色でかわいいから『Cookie』！{w=0.4}いい名前でしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0331.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あのう……{w=0.55}飼うわけじゃないんだけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0605.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ステーキ！ステーキ、どこ行ったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0244.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0332.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0180.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「つけた名前が、全部食べ物ってのも問題あるけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b6_hz__dash__06_04:
    $ kag_set_bookmark('「６日目」りずむと子犬')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('子犬\u3000「')
    "子犬　「わんわん」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0333.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「すっかり元気になったわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ。よかったです」"
    $ kag_cm()
    $ kag_playse('2-0334.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「元気にお店の中を走り回って……{w=0.45}{nw}"
    $ kag_drawchar('hz_05.tlg', time_ms=100, sepia=False, canskip=True)
    extend "って、え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっダメ！」"
    $ kag_cm()
    $ kag_set_next_indent('子犬\u3000「')
    "子犬　「わんわん！」"
    $ kag_cm()
    $ kag_set_next_indent('お客さんＡ「')
    "お客さんＡ「わっ」"
    $ kag_cm()
    $ kag_set_next_indent('お客さんＢ「')
    "お客さんＢ「な、なんなの？{w=0.4}この子犬」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ごっ、ごめんなさい。{w=0.4}まだ子犬でしつけができてなくて」"
    $ kag_cm()
    $ kag_set_next_indent('お客さんＡ「')
    "お客さんＡ「びっくりしたなあ。{w=0.4}子犬とはいえちゃんとつないでおいてくれないと」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみません」"
    $ kag_cm()
    $ kag_set_next_indent('お客さんＢ「')
    "お客さんＢ「ホント、しっかりしてよね」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0335.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「はい。{w=0.4}申し訳ありませんでした」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そんなわたしたちを知ってか知らずか、子犬はまだ店の中を走り回っている。"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0336.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ほら、おいで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "はづきちゃんがだき上げると、子犬はきょとんとした表情ではづきちゃんを見た。"
    $ kag_cm()
    $ kag_playse('2-0337.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「元気になったのはいいけど、お店ではおとなしくしてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('子犬\u3000「')
    "子犬　「…………」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0337.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしたの？{w=0.4}はづきちゃん」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0338.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「なんかこう……{w=0.65}生あたたかいような……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ぽとっ"
    $ kag_cm()
    "何かしずくのようなものが、はづきちゃんのスカートからたれた。"
    $ kag_cm()
    "ぽとっ"
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_playse('2-0338.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「っ！こ、これって！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お……{w=0.55}おしっこ！」"
    $ kag_cm()
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0339.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「キャアアアアアアアアアッ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "はづきちゃんは抱いていた子犬をはなした。"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0340.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ど、どうしようりずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ちょっと待って。はづきちゃんこっちに来て」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg018', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b6_hz__dash__06_05:
    $ kag_set_bookmark('「６日目」りずむと子犬')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃんのスカートよ、キレイになれっ！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0341.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「助かったわ～ありがとう、{w=0.4}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それにしても、子犬とはいえ、何とかしないといけないですね」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0342.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうね。{w=0.4}お客さんにも迷惑かかっちゃうし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0606.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぎゃあああ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0343.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あれはどれみちゃんの声！{w=0.35}りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ。どれみちゃん、どうしたのっ！？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_hz_b6_hz__dash__06_06:
    $ kag_set_bookmark('「６日目」りずむと子犬')
    $ kag_cm()
    $ kag_playse('1-0607.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「むぎゅう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そこには、リボンでぐるぐる巻きにされたどれみちゃんが横たわっていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こ……これはどういうこと……」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0344.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん、大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0608.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「大丈夫じゃないっす。{w=0.4}ステーキがあたしをリボンでぐるぐる巻きにしてくれて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0152.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「アハハハハハ！バウムクーヘンみた～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0609.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんであたしがこんな目に……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0245.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こらあコージ！{w=0.4}なにやってんねん！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0345.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あいちゃんまで名前付けちゃったのね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0246.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「飼い主がみつかるまでの名前やったら、別にええかなぁって思て」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0181.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お父さんの名前をそのままつけるっていったい……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0247.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「この名前やと気分が乗んねん。{w=0.4}子犬のうちのしつけがいちばん大事なんや。{w=0.4}ここはしっかりしかっとかんと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0346.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「しかたないわね。{w=0.4}がんばって！あいちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('子犬\u3000「')
    "子犬　「わんわん」"
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0247.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「っ！」"
    $ kag_cm()
    $ kag_set_next_indent('子犬\u3000「')
    "子犬　「きゅ～ん、きゅ～ん」"
    $ kag_cm()
    $ kag_set_next_indent('あいこ「')
    "あいこ「…………………………」"
    $ kag_cm()
    $ kag_wait(1000, canskip=True)
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0248.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……{w=0.55}しゃあないなあ。{w=0.5}ホンマにかわいいやっちゃなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0172.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、あいこがやさしくなった！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('3-0249.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃん、あたしはいつもやさしいで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0347.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うふふ、不思議な子犬ね。{w=0.4}まるでどれみちゃんみたい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0031.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「あはははは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0610.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あのー。{w=0.65}もしもーし。{w=0.5}すいませーん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0610.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「助けてくださーい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_hz_b6_hz__dash__06_07:
    $ kag_set_bookmark('「６日目」りずむと子犬')
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    "もうすっかり夕暮れ時。"
    extend "みんな子犬の世話でくたくたの様子。"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0182.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それにしても……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0250.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「子犬の世話ってつかれんな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0153.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「結局、１日中引っかき回されっぱなしだったよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0611.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしなんかぐるぐる巻きにまでされてさぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0348.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしなんて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0183.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「しつけるったって、今日１日じゃ、どうしようもないし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「早く、飼い主さんをさがさなきゃいけませんね」"
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0251.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「少なくともマジョリカが帰ってくるまでには、なんとかせんとなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-009.1.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、いらっしゃいませ」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('男の人「')
    "男の人「すみません。{w=0.5}ちょっとうかがいたいんですが」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0612.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はい、何か？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('男の人「')
    "男の人「この辺でこんな子犬を見ませんでしたか？」"
    $ kag_cm()
    $ kag_playse('1-0613.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？子犬って……{w=0.55}{nw}"
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    extend "あっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0614.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ステーキじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('男の人「')
    "男の人「へ？」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0615.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、いや……{w=0.45}見たも何も、ここにいますよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('男の人「')
    "男の人「えっ、ホントですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0349.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どうしたの？{w=0.35}どれみちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0616.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、この人、ステーキの飼い主さんみたいだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「本当ですか？」"
    $ kag_cm()
    $ kag_set_next_indent('子犬\u3000「')
    "子犬　「わんわん！」"
    $ kag_cm()
    $ kag_set_next_indent('男の人「')
    "男の人「あっ、スイカ！よかった～心配したぞ」"
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0252.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なんや、結局食べ物の名前か」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0184.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「よかったわね、飼い主さんが見つかって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    "子犬をだきかかえた。そっか、行っちゃうのか……"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0349.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_playse('2-0349.6.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ちょっとさびしいけど、ちゃんとお返ししましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0349.7.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「この子のことを心配して探してくれる人のもとが、いちばん幸せなはずだもの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですね……この子にとって、それがいちばんいいことなら、しかたないですもんね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「迷子になってお店の前に倒れてたんです。でも、もう大丈夫です」"
    $ kag_cm()
    $ kag_set_next_indent('男の人「')
    "男の人「ありがとうございます。こら！スイカ！もうひとりでうろうろするんじゃないぞ！」"
    $ kag_cm()
    $ kag_set_next_indent('スイカ「')
    "スイカ「わん！」"
    $ kag_cm()
    $ kag_set_next_indent('男の人「')
    "男の人「みなさん、本当にありがとうございました」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0253.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いえいえ、どういたしまして。{w=0.4}元気な子犬ちゃんでしたよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0350.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でも、ちょっぴりさみしいわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「仕方ないです」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('スイカ「')
    "スイカ「わんわん！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？……{w=0.5}そんな」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0351.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今、あの子犬が『ありがとう』って」"
    $ kag_cm()
    $ kag_playse('2-0352.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ホント？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ、はっきり聞こえました」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0353.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そう、よかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん……{w=0.55}また会おうね、スイカちゃん」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hz6_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hz_b7_gamestart
    return
