# Auto-generated from 02. hazuki/hz_B4.ks by tools/transpile_ks.py
label kag_hz_b4:

label kag_hz_b4_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hazuki.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg005', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hz_b4_hz__dash__04_00:
    $ kag_set_bookmark('「４日目」美空小の怪談')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みんな、どうしてるかなぁ」"
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    "今日は、みんな『音楽クラブ』とかで午前中はわたしがひとりでお店番。"
    extend "お店はほとんどお客さんは来なくて、はっきり言ってヒマでした。"
    $ kag_cm()
    "そういえば、わたしがＭＡＨＯ堂に来てから、ひとりきりになるのって、はじめてだ。"
    $ kag_cm()
    $ kag_sound_se('se-009.1', buf=1)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0572.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、おつかれッス～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0222.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お店、どないやった～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0250.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、ひとりで大丈夫だった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「とってもヒマでした。{w=0.35}あ、どうでした？音楽クラブ」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0164.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ひさびさに合わせた割には、うまくいったんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0135.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん、どれみちゃんが一番ハズしてたね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0573.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え、ええ？{w=0.35}そ、そうかなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0153.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そうだよ。{w=0.35}ハナちゃんズッコケちゃったよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0026.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「アハハハハハ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "さっきの静けさから一転、にぎやかなＭＡＨＯ堂が帰ってきた。"
    extend "やっぱりみんながいるっていいなあ。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0223.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それで、さっきの話やねんけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_hz_b4_hz__dash__04_01:
    $ kag_set_bookmark('「４日目」美空小の怪談')
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0251.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「や、やめてよあいちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0574.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うんうん、早く続きを聞かせてよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんの話ですか？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0136.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「学校の怪談話だよ、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0165.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「たとえば、学校の銅像が夜になると、ちがう方向を向いて立っているとかっていう、ちょっとしたウワサ話ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へぇ、人間界って、そんなに不思議なことがおきるんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0224.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、そら魔女界の方がよっぽど不思議やと思うけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どんな不思議なんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0225.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「色々あんねんて。"
    $ kag_playse('3-0225.2.ogg', buf=0, loop=False)
    extend "先週の話らしいねんけどな、学校の警備員さんが夜中に校内をパトロールしてた時に」"
    $ kag_cm()
    $ kag_playse('3-0225.3', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「音楽室から変な物音が聞こえるんで行って見たんやて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0575.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0252.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「や、やめてよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0226.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「でも教室のドアを開けた瞬間、{w=0.4}その物音は急に消えて『おかしいな』て思った警備員さんが、{w=0.4}教室の中を懐中電灯で照らして調べたんやって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0137.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0166.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そ、それでどうなったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0227.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほら、音楽室の上の方に、作曲家さんらの肖像画がかかってるやんか。{w=0.4}ぐうぜんあれを照らしたんやて。"
    $ kag_playse('3-0227.2', buf=0, loop=False)
    extend "そしたらな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ど、どうしたんですか」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(800, canskip=True)
    $ kag_drawchar('a_05.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('3-0228.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「肖像画がニヤって笑ったんやて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0253.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「マジョリカマジョリカマジョリカマジョリカ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ど、どうしたんですか？はづきちゃん」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0253.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ほらね、こわいものをこわくないって思うためには、\nもっとこわいものの名前を呼ぶと、こわくなくなるじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そういうもの……なんですか？」"
    $ kag_cm()
    $ kag_playse('2-0254.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、こわくないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}別にこわい話じゃないですよ？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0577.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やっぱり本物の魔女だねぇ。{w=0.45}度胸がちがうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "人間って不思議だなあ。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0255.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あれ？……{w=0.6}ない、ないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0256.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どうしよう!」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0578.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どうしたの？{w=0.4}はづきちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0257.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「楽譜がないの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0138.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「楽譜？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0258.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「明日のバイオリンのレッスンに使う楽譜がないの。{w=0.35}多分、学校に忘れて来たんだわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0230.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな取りに行かな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0167.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも、もうすっかり夜になっちゃってるから、今日はやめて明日の朝にしたら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0259.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「明日の朝は別に用事があるから、楽譜を取りに学校に行けないわ……{w=0.55}どうしよう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0231.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どのへんにおいたか、心当たりは本人でないとわからんしなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん、これから学校に行くんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0260.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うん、こわいけど、取りに行かないわけにもいかないし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「学校、連れてってください！」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0261.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？いや、あの……{w=0.55}りずむちゃん、行きたいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「行きたいです。{w=0.35}人間界の学校って見てみたいです」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0168.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね、りずむちゃんがいっしょなら、はづきちゃんも少しはこわくないでしょ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0262.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そ、そりゃあ心強いけど……{w=0.6}こわいことには変わりないし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0232.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「でもまあ、取りに行かへんわけにもいかんわけやし、\nここはりずむちゃんにいっしょに行ってもらうことにしよっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0579.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「しかたないね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0263.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、お願いね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、ちょっと楽しみです」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg058', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()

label kag_hz_b4_hz__dash__04_02:
    $ kag_set_bookmark('「４日目」美空小の怪談')
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0264.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「り、りずむちゃん、ぜったいに手をはなさないでね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "お昼が結構暑かったせいで、何か空気が生暖かい。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ、{w=0.4}しっかりにぎってますよ」"
    $ kag_cm()
    $ kag_playse('2-0265.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「早く音楽室に行きましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。行きましょうか」"
    $ kag_cm()
    "にぎっているはづきちゃんの手は、もうじっとり汗ばんでいる。"
    extend "かなりこわがっていることはわたしにもよくわかった。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg055', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b4_hz__dash__04_03:
    $ kag_set_bookmark('「４日目」美空小の怪談')
    $ kag_cm()
    "夜の校舎は、月明かりがぼんやり届く程度で、ろうかの奥は見えるか見えないかくらいだった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん、音楽室ってどのへんなんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0266.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「この階のいちばん奥にある教室よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あそこですね」"
    $ kag_cm()
    $ kag_playse('2-0267.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「う、うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg250', time_ms=1500, bgcolor='0x000000')
    $ kag_playse('se-007.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('2-0268.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「多分、あのあたりの机の中においちゃったんだと思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃあ、さっそく探しましょう」"
    $ kag_cm()
    "教室の壁をふと見上げると、上の方に絵がかかっている。"
    $ kag_cm()
    "あいちゃんが言ってた肖像画って、あれかあ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なになに？{w=0.35}『ベートーベン』？{w=0.35}ずいぶんこわい顔してるんだなあ」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こんなこわい顔してる絵があると、はづきちゃん、ますますこわがっちゃうんじゃないかな……{w=0.5}そうだ！」"
    $ kag_cm()
    $ kag_sound_se('se-032.1.ogg', buf=1)
    $ kag_sound_se('se-047.ogg', buf=1)
    "わたしは、魔法でベートーベンさんのこわい顔を、笑っている顔に変えてあげた。"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0269.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「な、何？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}ああ、ほら、あのベートーベンさんの顔を……」"
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0270.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「キャアアアアアアッ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はづきちゃん？{w=0.4}どうしたんですか？」"
    $ kag_cm()
    $ kag_playse('2-0271.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わ、わらっ……{w=0.55}イヤアアアアアアッ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-021.ogg', buf=1, loop=False)
    "はづきちゃんが突然かけ出し、音楽室から出て行ってしまった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どこへ行くんですかぁ、はづきちゃ～ん」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('2-0272.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「マジョリカマジョリカマジョリカマジョリカマジョリカマジョリカマジョリカ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "はづきちゃんはいちもくさんに、階下へとかけて行った。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg056', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b4_hz__dash__04_04:
    $ kag_set_bookmark('「４日目」美空小の怪談')
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0273.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あ、あれ、出口は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-021.ogg', buf=1, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん、どうしたんですか？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg062', time_ms=1500, bgcolor='0x000000')
    $ kag_playse('se-007.ogg', buf=1, loop=False)
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('2-0274.ogg', buf=0, loop=False)
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('はづき「')
    "はづき「出口、出口はどこ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-052.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0275.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハア、ハア、やっと追いついた……はづきちゃん？」"
    $ kag_cm()
    "人間を解剖したような人形が、はづきちゃんに寄りかかっている。"
    $ kag_cm()
    $ kag_drawchar('hz_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0276.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「イヤアアアアアアア！！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-021.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「待って、はづきちゃーん！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('2-0277.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「オケケケケ！{w=0.4}学校の、学校の呪いなのよぉ！{w=0.4}オケケケケケケケ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん、どうしちゃったんですか～？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg063', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b4_hz__dash__04_05:
    $ kag_set_bookmark('「４日目」美空小の怪談')
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('se-007.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('hz_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0278.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「オケケケケケ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハァ、ハァ、はづきちゃんって、意外に足が速……」"
    $ kag_cm()
    $ kag_playse('se-051.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「な、何の音……？」"
    $ kag_cm()
    $ kag_cm()
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ、はづきちゃん、{w=0.4}どうして人間の骨格標本なんか抱きしめてるんですか？」"
    $ kag_cm()
    $ kag_playse('2-0279.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「×○△□＄＃％！{w=0.8}うーん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん！？\n{w=0.4}しっかりしてください！はづきちゃん！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg058', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hz_b4_hz__dash__04_06:
    $ kag_set_bookmark('「４日目」美空小の怪談')
    $ kag_cm()
    "まさか、\nはづきちゃんがこんなにこわがるなんて思わなかったなぁ。"
    $ kag_cm()
    $ kag_playse('2-0280.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あ、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はづきちゃん、気がついた？{w=0.4}よかったー！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '02はづき-05', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghz3=1
    $ kag_mesframe()
    $ kag_playbgm('m42', loop=True)
    $ kag_playse('2-0281.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたし、どうしちゃったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「『理科室』って所で気を失っちゃったんです」"
    $ kag_cm()
    $ kag_playse('2-0282.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ああ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ごめんなさい。{w=0.4}わたしが魔法でベートーベンさんの絵を変えちゃったんで、ビックリしちゃったんですよね。{w=0.4}あんなことになるなんて思わなかったんで……」"
    $ kag_cm()
    $ kag_playse('2-0283.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？{w=0.4}あの絵って、りずむちゃんが変えちゃったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ、あの絵のままじゃ、かえってはづきちゃんがこわがると思って」"
    $ kag_cm()
    $ kag_playse('2-0284.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そ、そうだったの……{w=0.55}本当にビックリしたわ。{w=0.4}だってあいちゃんの話のまんまなんですもの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみません」"
    $ kag_cm()
    $ kag_playse('2-0285.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「い、いえ、別に気にしないで。{w=0.4}りずむちゃんがいてくれたから、楽譜も……{w=0.55}そうだ。{w=0.4}楽譜は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg058', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_set_bookmark('「４日目」美空小の怪談')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、これ」"
    $ kag_cm()
    "わたしは音楽室で見つけた楽譜をはづきちゃんにわたした。"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0286.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ああ、よかった。{w=0.4}りずむちゃん、ありがとう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「これを忘れちゃったら、また学校に戻らないといけないですから」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0287.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「やめてよ～{w=0.4}わたし『笑ってるベートーベン』なんてはじめて見ちゃったんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「笑ってるベートーベンさんは、めずらしいものなんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0288.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「めずらしいって言うか、ほとんどの人が、あの絵しか見たことがないと思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか……{w=0.45}でも、ベートーベンさんもたまには笑った方がいいと思いますよ」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0289.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うふふ、そうね。{w=0.4}笑うとけっこうやさしく見えるかも」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですよ。きっとやさしい人ですよ」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hz4_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hz_b5_gamestart
    return
