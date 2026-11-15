# Auto-generated from 02. hazuki/hz_B5.ks by tools/transpile_ks.py
label kag_hz_b5:

label kag_hz_b5_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hazuki.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hz_b5_hz__dash__05_00:
    $ kag_set_bookmark('「５日目」思い出の砂浜')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_playse('2-0290.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「んっ……{w=0.55}うぅ～ん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0291.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ふぅ……{w=0.55}今日のお仕事もあと少しで終わりね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "今日もＭＡＨＯ堂でお仕事をしていたみんなは、３時のおやつ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん、おつかれさま」"
    $ kag_cm()
    $ kag_playse('2-0292.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あっ、ありがとうりずむちゃん。{w=0.4}でもそんなにつかれたわけじゃないのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0233.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お客さんほとんどけえへんかったしなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0139.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それにしても、今日も暑かったよね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ももちゃんの言うとおりだ。でも、３時過ぎの今でもまだまだ暑い。"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0169.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そろそろ夕方になるから、少しは涼しくなるかもしれないけど、{w=0.4}これだけあついとそれだけでつかれちゃうわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0293.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「何か涼しくなるようなモノを考えたら、売れるんじゃないかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0140.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「はづきちゃん、Nice idea！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0234.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なるほど～{w=0.4}そら名案やな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0155.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「はづきすごーい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0170.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね……{w=0.55}じゃあ、どんなのがいいかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0294.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「う～ん、涼しくなるものっていうと……{w=0.5}たとえば冬に使うカイロの逆みたいなのとか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0235.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「でもはづきちゃん、それやったら普通に売ってんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0295.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あっ、確かにそうよね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0141.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それならさ、ＭＡＨＯ堂っぽく、かわいいやつを作ってみるとか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0156.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「う～ん、かわいいやつ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、なら実際に涼しくなるんじゃなくて、涼しい気分になる雑貨とかはどうでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0171.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「たとえば風鈴みたく、涼しく感じるような工夫をしてってことかしら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0296.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あ、でも単純に、ＭＡＨＯ堂特製うちわとかでもいいかも？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0580.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0297.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0581.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う～……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん、\n何かいいアイディアでもうかんだんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0582.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「海に行きた～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0027.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「だあああっ！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.2.ogg', buf=1)
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0583.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うみうみう～み～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0298.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ど、どれみちゃん落ち着いて……{w=0.5}突然どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0584.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だってはづきちゃん！{w=0.4}もう毎日毎日暑すぎだよ～！{w=0.4}それにここんところずっとＭＡＨＯ堂のお仕事だしさぁ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0585.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんなで海に行ってパーっと遊ぼうよ！{w=0.4}あたしたち小学生なのに毎日働きすぎさ～！！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0585.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだ！これから行こうよ！{w=0.4}お店はちょっと早く閉めてさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0586.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「海はイイよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0586.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「泳がなくてもさ、砂遊びしたり、波打ち際で遊んだり、きっと楽しいよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0586.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「潮の香りをかぎながらボ～っとしたり……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0587.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それにほら、今から行けば海に沈む夕日なんかも見れちゃうんだよ！{w=0.4}きっとすっご～くキレイだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('2-0299.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0172.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0236.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どないしたん、はづきちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0300.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「こんな暑いお部屋の中じゃ、いいアイディアなんてきっと浮かばないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0300.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「やっぱりここは場所も変えて、涼しいところで気分転換した方がいいと思うの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0588.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やったあ！さすがはづきちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0157.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんも海行きたい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、わたしも行ってみたいです！」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0173.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあ、行っちゃおっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0237.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もぉ～どれみちゃんにはかなわへんなぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0142.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「でもちょっと楽しそうだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0301.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お店も少し早く閉めちゃいましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0589.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあさっそくしゅっぱ～つ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg080', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b5_hz__dash__05_01:
    $ kag_set_bookmark('「５日目」思い出の砂浜')
    $ kag_cm()
    $ kag_playbgm('m14', loop=True)
    $ kag_playse('se-014.2.ogg', buf=1, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわぁ、広～い！」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0302.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフ。{w=0.4}りずむちゃん楽しそうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！思ってたよりもずっと広くてきれいで、なんだかうきうきしてきます」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0591.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「夕方までめいっぱい遊んじゃおう～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0029.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「お～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg082', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b5_hz__dash__05_02___________:
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0158.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「キャハハハハハ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ハナちゃんは靴を脱ぎ、波打ち際で水遊びをしている。"
    extend "\nそのそばには、同じくはだしになった、どれみちゃんとももちゃんがいる。"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0592.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん、それっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-029.1.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0159.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あっ、アハハハ。ハナちゃんもおかえし～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-029.1.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0593.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うわわっ！{w=0.4}くっそ～、負けないんだから～」"
    $ kag_stopse(buf=1)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-029.2.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0143.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「もう、２人ともぬれちゃうよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0144.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「へ？わ、わわっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-033.ogg', buf=1)
    $ kag_ws(buf=0, canskip=True)
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0025.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「あはははは」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0145.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「も～！こうなったら２人も道連れなんだから～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-029.2.ogg', buf=1)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0594.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うわっ！{w=0.4}あはははは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0160.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あはははははは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0146.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それそれ！{w=0.4}あはははは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg083', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわぁ……{w=0.65}砂がすごく熱いですね」"
    $ kag_cm()
    "わたしは乾いた砂を一つかみして、にぎった手のすき間からサラサラと落とした。"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0303.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうね。{w=0.4}はだしで歩いたら、足の裏をヤケドしちゃいそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えぇっ！ヤケドですか！？」"
    $ kag_cm()
    $ kag_playse('2-0304.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でも、砂を掘ってみると中はけっこう冷たいのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へぇ……」"
    $ kag_cm()
    "わたしは、ためしに砂を少し掘ってみた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.5}あれ、ほんとだ。{w=0.4}中はひんやりしてますね」"
    $ kag_cm()
    $ kag_playse('2-0305.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうでしょう。{w=0.4}それにね、ほら、あっちの砂がぬれてるあたりだと、{w=0.4}ちっちゃな子が砂でお山を作ったり、トンネルを掘ったりするの」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_hz_b5_choices_hz02:
    $ kag_set_bookmark('はづきシナリオ選択肢02')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】ちょっと子供っぽいですね', current_stem='hz_b5', storage=None, target='*choices_hz02-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】それやってみたいです', current_stem='hz_b5', storage=None, target='*choices_hz02-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait
    "【分岐Ａ】{nw}"

label kag_hz_b5_choices_hz02__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag += 1
    $ kag_set_next_indent('りずむ「')
    "りずむ「ちょ、ちょっと子供っぽいですよね……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0306.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「何言ってるの。{w=0.4}せっかく来たんだから楽しみましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ、そうですよね！」"
    $ kag_cm()
    jump kag_hz_b5_after_choices_hz02
    call kag_s_wait

label kag_hz_b5_choices_hz02__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、わたしそれやってみたいです！」"
    $ kag_cm()
    jump kag_hz_b5_after_choices_hz02
    call kag_s_wait

label kag_hz_b5_after_choices_hz02:
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0307.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃあ、いっしょに遊びましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0308.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「行きましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたしたちはその場で靴をぬぎ、ぬれた砂の方へと走っていく。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わっ！なんだか不思議な感じですね」"
    $ kag_cm()
    $ kag_playse('2-0310.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「山を作りましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい」"
    $ kag_cm()
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg083', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b5_hz__dash__05_03___________:
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「できた！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ？はづきちゃん？」"
    $ kag_cm()
    "山の向こうで、トンネルを掘っていたはずのはづきちゃんがいない。"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0312.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、こっちこっち」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん？」"
    $ kag_cm()
    $ kag_playse('se-014.2.ogg', buf=1, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「キャッ！くすぐったい！」"
    $ kag_cm()
    "わたしの足もとを、波が通り過ぎていった。"
    $ kag_stopse(buf=1)
    $ kag_cm()
    $ kag_playse('2-0313.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフ。{w=0.4}りずむちゃん、手を洗いましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "はづきちゃんは、打ち寄せる波で手を洗っている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ\t「')
    "りずむ	「あ、そっか」"
    $ kag_cm()
    "わたしは、自分の手のひらが砂で汚れていたことに気がつき、はづきちゃんにならって波で手をゆすいだ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「このためにこっちに来たんですね」"
    $ kag_cm()
    $ kag_playse('2-0314.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うふふ。{w=0.4}それもあるけど、さっきりずむちゃん、足もとの砂が動いてくすぐったがったでしょ」"
    $ kag_cm()
    $ kag_playse('2-0314.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ちょっと驚かせちゃおうかな～と思って……{w=0.55}ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ～、はづきちゃんヒドイです」"
    $ kag_cm()
    $ kag_playse('2-0315.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフ。{w=0.4}ごめんなさい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もぅ～……ふふ、あははは……」"
    $ kag_cm()
    $ kag_playse('2-0316.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うふふふふ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0595.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お～い！{w=0.4}いっしょに遊ぼうよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ふと岩場の方を見ると、あいちゃんとおんぷちゃんも、どれみちゃんたちの方へと向かっている。"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0317.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしたちも行きましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg081', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b5_hz__dash__05_04___________:
    $ kag_cm()
    $ kag_playse('se-014.2.ogg', buf=1, loop=False)
    "ひとしきり遊んだみんなは、夕日をながめている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「きれい……」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0318', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、はい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '02はづき-06', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghz4=1
    $ kag_mesframe()

label kag_hz_b5_hz__dash__05_05___________:
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわぁ、かわいい！」"
    $ kag_cm()
    $ kag_playse('2-0319.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でしょ？桜貝っていうの。これを使って何かかわいい小物ができないかしら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「砂といっしょに小ビンにつめたらどうでしょうか？」"
    $ kag_cm()
    $ kag_playse('2-0319.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「いいわね！きっとかわいい小物ができるわ」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「帰ったら、さっそく作ってみましょう」"
    $ kag_cm()
    $ kag_playse('2-0319.6.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃあ、暗くなる前に帰りましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('2-0319.7.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「みんなのところに行きましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg015', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b5_hz__dash__05_06___________:
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0597.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日は楽しかったね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0238.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマや～どれみちゃんがいきなり『海に行きたい～！』ってさけんだときは、{w=0.4}どないしよかと思ったけど、行ってよかったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0175.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん。{w=0.4}いいリフレッシュになったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0147.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「いっぱい遊べたしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0161.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんとっても楽しかった！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0598.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「家に帰ってぽっぷに今日のこと話したら、うらやましがるかなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0320.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんどうかした？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ。えっとその、みんな本当に仲がいいなぁって思って……」"
    $ kag_cm()
    $ kag_playse('2-0321.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、魔女界で友だちがいなかったから、こんな風に遊んだ思い出ってないんです」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0322.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お砂で山を作るなんて、幼稚園を出てからやってなかったですし、そもそも海に行ったのだって初めてでしたし」"
    $ kag_cm()
    $ kag_playse('2-0323.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0324.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「また、みんなで遊びにいきましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_playse('2-0325.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「思い出は、きっとこれからも、たくさんできるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですよね！」"
    $ kag_cm()
    "わたしは、はづきちゃんからもらった桜貝をにぎりしめた。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hz5_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hz_b6_gamestart
    return
