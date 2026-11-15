# Auto-generated from 05. momo/m_B7.ks by tools/transpile_ks.py
label kag_m_b7:

label kag_m_b7_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_momo.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg012', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_m_b7_mo__dash__07_00:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_playse('se-036.ogg', buf=1, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}ん、ん～」"
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ん、朝……{w=0.6}ふあ～！」"
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    "朝日がわたしの部屋をまぶしく照らしている。"
    $ kag_cm()
    "ふとんから体を起こし『伸び』をする。"
    $ kag_cm()
    "まだ眠いけど、ゆうべわたしは『あること』を実行しようと心に決めていた。"
    $ kag_cm()
    "そのために目覚まし時計をセットしていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ようし！{w=0.4}今日はチャレンジしてみるぞ！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "誰もいないキッチン。"
    $ kag_cm()
    "普段ならももちゃんが、お菓子作りをしていて甘い香りが絶えない場所だけど、今はかすかに夏の陽の匂いがする。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「人間界にいられる日もあと少し……{w=0.6}何とかひとりでお菓子が作れるようになりたいと意気込んだのはいいけれど……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん！きっとできる！{w=0.4}よ～し！がんばるぞ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「まずは……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お菓子のレシピよ出てきて！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    "魔法で出てきたお菓子のレシピの表紙に目を通す。"
    $ kag_cm()
    "そこには『超！初心者のお菓子作り』『猿でもわかるお菓子の作り方』……{w=0.45}など、"
    extend "お菓子作りの入門本ばかり……。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それじゃあ始めよう！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_01:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    "わたしが最初に選んだのは『ショートケーキ』。"
    extend "その材料と道具を用意する。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よ～し！{w=0.4}まずはボウルに玉子を入れて……」"
    $ kag_cm()
    $ kag_sound_se('se-053.ogg', buf=1)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ……」"
    $ kag_cm()
    "玉子が上手く割れずにつぶれちゃった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あはは……{w=0.6}失敗は誰にでもつきものよね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg241', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "さらに数分後……。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううぅ～」"
    $ kag_cm()
    "わたしは冷や汗をかきながらボウルの中の『玉子のカラ入り』スポンジの生地を見つめる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.45}や、やっぱりいきなりケーキは難しすぎだよね。{w=0.4}でも、ひとりでももちゃんみたいなお菓子を作れるようになりたいな」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_02:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0497.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Good morning！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0906.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、おはようさ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0958.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おはよう、ももちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0498.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あれ？{w=0.4}りずむちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0693.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「今日はまだ見てないけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0353.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむね～朝からずっとキッチンに入ったままなんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0499.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「え？{w=0.4}そうなの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0354.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0959.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いったい何やってるんだろうね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0907.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何か作ってるんかな～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "ガシャーーン！"
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0500.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0694.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なっ、なに？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-022.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg216', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_03:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_playse('5-0501.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わ！わわっ！{w=0.4}ケホッ、ケホッ……{w=0.5}何コレ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0908.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほ、ほんまや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0355.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ま、前が見えないよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「コホッコホッ、みなさん？」"
    $ kag_cm()
    $ kag_playse('1-0960.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「り、りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！{w=0.4}そうです！」"
    $ kag_cm()
    $ kag_playse('2-0620.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「これ、小麦粉よね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0695.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……{w=0.55}そうみたいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0961.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんで小麦粉が？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「す、すみません」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_04:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、わたしお菓子を作ろうとして、{w=0.4}それで小麦粉をふるいにかけようとしたら……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0696.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なるほどね。{w=0.4}それでふるいを落としちゃったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみません……」"
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0621.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「失敗は誰にでもあるものよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0356.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみの方が、も～っとすっごい失敗、い～っぱいしてるから大丈夫」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0962.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え～っ！！{w=0.4}いっぱいはしてないよぉ～ってハナちゃん？{w=0.4}ハナちゃんは、去年赤ちゃんだったでしょ？{w=0.4}覚えてるの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0357.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「よく覚えてないけど、{w=0.4}きっとそうだよ、たぶん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0963.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん、ひどい……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0622.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、{w=0.4}どうしてこんなに朝早くからお菓子作りをしてるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、{w=0.6}ももちゃんとお菓子を作ってみなさんに食べてもらったとき、{w=0.4}おいしそうに食べてくれた笑顔が、なんとなく忘れられなくて……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それで、お菓子作りにチャレンジしようかなって思ったんですけど……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0909.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうやったんか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0502.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「だったら、あたしも手伝うよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('5-0503.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「いっしょにお菓子作りしよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}すみません」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0504.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみません。{w=0.4}わたし、どうしても、ひとりでやってみたくて」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0964.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「……{w=0.2}うん！{w=0.45}わかった！{w=0.4}じゃあそのかわり、応援するね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0623.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「がんばってね！{w=0.4}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0697.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも、何か手伝えることがあったら言ってね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0358.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「でき上がったら、『ししょく』させてね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0505.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「みんな。{w=0.4}でも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0910.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ささ、ももちゃんも行こ行こ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0506.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「う、うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、ありがとうございます」"
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_05:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0359.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、どんなお菓子作ってるのかな～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0624.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「いまから、楽しみよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0965.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でも、何で急にお菓子作りなんだろ？{w=0.4}それにどうして『ひとりで～』なんだろうね～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0698.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それはあれよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0911.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん、あれやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0360.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「『あれ』って？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0699.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんはきっと、{w=0.4}ももちゃんにあこがれてるんじゃないかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0912.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、ももちゃんと特に仲よかったからなぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0966.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え～でもさぁ、{w=0.4}仲がいいんだったら、それだけでいいじゃん～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0700.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしは仲がいいからこそ……{w=0.55}だと思うな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0701.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしだったら、{w=0.4}好きな友だちができることで、自分ができないことがあったら、{w=0.4}いっぱい努力して追いつきたいって思うもん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0967.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなもんかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0702.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんだって、{w=0.4}もしわたしたち全員が魔女になって、{w=0.4}どれみちゃんだけが魔女見習いのままだったらどうする？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0968.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そりゃあ～早く魔女になるためにあたしもがんばるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0913.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、{w=0.4}お菓子が作れるまでひとりで特訓してるんちゃうかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0969.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そっか、なるほどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0361.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「じゃあ！{w=0.4}おいしいお菓子ができるように、い～っぱい応援しないと！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0970.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_06:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0507.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0508.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ううん、やっぱりほっとけない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg241', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_07:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    "部屋中に失敗したお菓子や材料が散乱している。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}はぁ、これも失敗」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしてうまくいかないんだろう」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん、落ち込んでもダメ！\n{w=0.4}もっともっと練習しないと！」"
    $ kag_cm()
    $ kag_sound_se('se-006.1.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん？」"
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0509.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.5}はい？」"
    $ kag_cm()
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0510.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、ひとりで大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何とかなりますよ。{w=0.4}たぶん……」"
    $ kag_cm()
    $ kag_playse('5-0511.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ちょっとだけ手伝おうか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん、ありがとう。{w=0.4}気持ちはうれしいけど、わたし、ひとりで作ってみたいんです」"
    $ kag_cm()
    $ kag_playse('5-0512.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん、初めていっしょにケーキを作ったとき、{w=0.4}実はわたし、けっこう衝撃的だったんです」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0513.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「へ？{w=0.4}しょうげきてき？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}初めてケーキを作っているところを見たのも衝撃だったんだけど、{w=0.4}気持ちをこめて作ったお菓子って、こんなにおいしくなるっていうのがすごく感動したんです」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だから、わたしもひとりでみなさんによろこんでもらえるお菓子を作りたい」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0514.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……{w=0.25}ＯＫ！わかった。{w=0.4}あたし、りずむちゃんを信じる。{w=0.4}がんばってね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はいっ。{w=0.4}ももちゃん、ありがとう」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_08:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0971.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もう２人きりになってけっこう時間すぎたよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0914.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なんか、どないなってるかめっちゃ気になんなぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0972.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「さっきからたまにお鍋が落ちたような大きな物音が聞こえるけど、{w=0.4}まさかけんかなんかしてないよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0915.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなことないと思うけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0362.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんおなかすいてきちゃったよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-006.1.ogg', buf=1)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0973.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あっ、ももちゃん。{w=0.4}どうだった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0515.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、どうしてもひとりでやりたいんだって。{w=0.4}だからわたし、りずむちゃんを信じることにした」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0703.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「『信じる』？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0516.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Yes。{w=0.4}りずむちゃんは、みんなによろこんでもらえるようなお菓子を作りたいって、本気で思ってるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0916.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやなあ。{w=0.4}ももちゃんがそこまで言うんやったら、ほっとこか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0625.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でも、やっぱり心配だわ。{w=0.4}けがとかしなきゃいいけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0704.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「まあ、お菓子作りぐらいで大きなけがなんてしないとは思うけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_09:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0975.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうは言ってもさあ、やっぱ気になるよねぇ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0626.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「確かに気になるけど、ももちゃんもあそこまで言ってたし、{w=0.4}ここでわたしたちが入っていってもジャマなだけだと思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0918.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「せやなあ。{w=0.4}りずむちゃんがせっかくやる気出してがんばってんのに、{w=0.4}水差すみたいやからなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0705.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なら、バレないように、そ～っとのぞいてみるのはどうかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0976.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そっかぁ～！{w=0.4}その手があったね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0977.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあ、いくよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m408a', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg401.tlg', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('1-0978.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ピリカピリララ　ポポリナペペルト！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0979.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんなかわいいハムスターになれぇ～！」"
    $ kag_stopse(buf=0)
    $ kag_fadeoutbgm(1000)
    $ kag_cm()
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '05ももこ-07-1', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgm4=1
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_10:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっと、こうしてこうやって……{w=0.55}きゃっ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ～あ、また最初からやり直し。{w=0.4}さすがにちょっとヘコむなあ」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん、がんばんなきゃ！」"
    $ kag_cm()
    $ kag_changetype('cross', '05ももこ-07-2', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('1-0980.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんか大変そうだねぇ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0919.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まあ、ひとりでやるのは初めてやろうしなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0706.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でもめげないでがんばってるのよ。{w=0.4}大丈夫じゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0981.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだね！{w=0.4}じゃあ、いこっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0627.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ちょっと待ってどれみちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0982.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん？{w=0.4}どうしたのはづきちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0628.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あれ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0983.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん？{w=0.4}あっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'white', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', '05ももこ-07-3', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('3-0920.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ももちゃん……{w=0.55}先に来てたんか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0984.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ももちゃん、やっぱり心配だったんだね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0707.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ううん、ちがうと思うよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0985.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0708.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「多分、きっとももちゃんは見届けたいんじゃないかしら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0986.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「……{w=0.2}そっか。{w=0.4}ももちゃん、『信じる』って言ってたもんね。{w=0.4}心配なんかしてないよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(5000)
    $ kag_playse('3-0921.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうとなったら長居は無用。{w=0.4}いこか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0709.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ちょっと待って！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0987.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今度はどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0710.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ハナちゃんがいないわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0987.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ええ～っ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0922.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どこいったんや～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0629.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「さっきまでいたのに……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0711.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いたわ！{w=0.45}あそこよ！{w=0.4}テーブルの上」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'white', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', '05ももこ-07-4', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('1-0988.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんでハナちゃん、あんなところに」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0923.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あれは、どう見てもお菓子をねらってる感じやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0630.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「まさかハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0712.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「たしか、ハナちゃんさっきからおなかすいたって言ってたわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0989.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ああ、もう～！\n{w=0.4}ハナちゃんつまみ食いしちゃだめじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'white', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', '05ももこ-07-4', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('6-0363.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「さっさっさっさっさ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0364.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「しゅたっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0365.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん、もう限界だもんね！{w=0.4}ちょっとだけ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0520.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「だめ～っ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0366.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わわ、もも！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0521.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ハナちゃん、お願いだからおとなしくして。{w=0.4}りずむちゃん、一生懸命なんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0367.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「だってハナちゃん、もうおなかすいちゃったよぉ。{w=0.4}おなかと背中がくっついちゃうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0990.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃんジャマしちゃメ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0368.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「だあってハナちゃん、{w=0.4}とってもとってもおなか、すいちゃったんだもん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0991.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ガマンしなさい！{w=0.4}りずむちゃん、がんばってるんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0369.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ぶっぶのぶー！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0992.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ももちゃんごめんね。{w=0.4}よく言い聞かせておくから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0522.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ううん、ありがとう。どれみちゃん。心配して来てくれたんだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0993.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあたしたちはもう行くから。{w=0.4}おいしいお菓子、楽しみにしてるね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_m_b7_mo__dash__07_11:
    $ kag_set_bookmark('「７日目」楽しさはおいしさの隠し味')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、できました！けど……」"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0370.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「すごーい！{w=0.4}お菓子がい～っぱいある！{w=0.4}ハナちゃんこれにする～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}ハナちゃん、それは、はじっこがこげちゃってるから」"
    $ kag_cm()
    $ kag_playse('6-0371.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「いいのいいの、へ～きへ～き！{w=0.4}ぱくっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0372.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おいしい～！{w=0.4}ほらどれみも食べてみて～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0994.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どれどれ。はむっ……{w=0.4}ホントだ！おいしい！！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0713.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしも食べてみようかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0924.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほなあたしも！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0631.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うん、おいしいわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「で、でも、形とかが……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0995.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「形なんて、ぜんぜん気にならないよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0925.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まずは中身や。{w=0.4}うわ、どれみちゃん、{w=0.4}こっちのヒトデ型のやつめっちゃおいしいで！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それ、星なんですけど」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0926.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なははは、まーまー細かいことは言いっこなしってことで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0373.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんがいただき～。{w=0.4}もぐもぐう～んおいしい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0996.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハ、ハナちゃんひど～い……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0524.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あはははは。{w=0.4}ハナちゃんの口のまわりお菓子だらけだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "みんなが笑っている。"
    $ kag_cm()
    "わたしが作ったお菓子を食べて、笑顔のみんなが……{w=0.55}この笑顔が見たくて、わたしはお菓子を作っていたんだ……"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0997.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「というわけでももちゃん、いつまでもうかうかしてられないね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0525.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「へ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0927.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「新たなお菓子作りのライバル出現！{w=0.4}その名もマジョリズムちゃんや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0632.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「がんばらないと追い越されちゃうわね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん……」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0526.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！{w=0.4}追いつかれないようにがんばらなきゃ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうございます。{w=0.4}でもライバルにはまだまだです」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0998.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃ、お茶を入れて来るね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0374.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おー！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0527.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃんおつかれ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん、ありがとう！」"
    $ kag_cm()
    "ももちゃんが、そしてみんながいてくれたからおいしいお菓子ができたんだよ。"
    $ kag_cm()
    "だから、わたしは帰るまでにこの気持ちを伝えたい。"
    $ kag_cm()
    "きっと、必ず……"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.m7_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_m_b8_gamestart
    return
