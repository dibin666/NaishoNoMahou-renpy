# Auto-generated from 01. doremi/d_B7.ks by tools/transpile_ks.py
label kag_d_b7:

label kag_d_b7_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_doremi.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_d_b7_d__dash__07_00:
    $ kag_set_bookmark('「７日目」おたがいの気持ち')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0084.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃんとりずむちゃん、ずいぶん熱心に作業してるわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0085.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「今朝からずっとだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0129.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いつもやったらこの時間、『お茶にしよ～よ～』ってさわぎ始めんのにな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0059.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇ～！{w=0.45}お茶にしよ～よ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0130.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お、今日はハナちゃんからのリクエストや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0086.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ＯＫ！ハナちゃん、今用意するね！{w=0.4}どれみちゃんたちも呼んできて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0060.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「は～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b7_d__dash__07_01:
    $ kag_set_bookmark('「７日目」おたがいの気持ち')
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0371.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうそう、そこはこういう風に……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    "朝からわたしは、どれみちゃんにはた織り機の使い方を習っていた。"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0372.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うんうん、なかなかいい感じじゃ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんかうれしいです！"
    extend "わたし、はじめての仕事って、決まって失敗するから、今日もどんな失敗するのか心配だったのに」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0373.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんは、はた織り向いてるのかもね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えへへ……」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0374.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あれ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしたんですか？」"
    $ kag_cm()
    $ kag_playse('1-0375.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、ここ、色はみだしてるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、ああ！」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0376.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はみでてるところまでほどいて、やりなおしだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ～あ。"
    extend "せっかくうまくいってると思ったんだけどな～」"
    $ kag_cm()
    $ kag_playse('1-0377.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ドンマイドンマイ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0061.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ～！{w=0.25}りずむ～！{w=0.3}お茶の用意できたよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0378.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「オッケェ～！わかったよハナちゃん！{w=0.35}今行く～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、わたし、もうちょっとやってからにしたいんですけど」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0379.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やりなおしてもまだ時間はあるから、一休みしよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0380.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ね、行こ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_cm()
    $ kag_playse('1-0381.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなところ目立たないから大したことないって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！"
    extend "そんなところ、って……」"
    $ kag_cm()
    "目立たなくっても、ちゃんと仕上げた方がいいんじゃないかなぁ……。"
    $ kag_cm()
    "どれみちゃんって、ちょっとテキトーすぎなんじゃ……。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0062.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれ～み～！{w=0.3}りずむ～！{w=0.3}何してるの～？」"
    $ kag_freeimage(layer='0', page='fore')
    $ kag_cm()
    $ kag_playse('5-0087.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃ～ん、りずむちゃ～ん！{w=0.45}早くしないと食べちゃうよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0382.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ほら、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、わかりました……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_d_b7_d__dash__07_02:
    $ kag_set_bookmark('「７日目」おたがいの気持ち')
    $ kag_playbgm('m60', loop=True)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0131.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「んでなぁ～、そこでお父ちゃんがなぁ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0383.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうそう、うちのお父さんもだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0085.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うふふふ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0132.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんどうしたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}え？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0093.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お父さんの話だと、りずむちゃんは入ってこれないかもね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ、まあ、そういうわけでも……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0088.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあさ、りずむちゃんのママはどんな魔女なの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしのママ、ですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0086.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お仕事とか、何をしているの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お城から遠くはなれた所で、ケーキ屋さんをやってるって聞いてます」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0089.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうなんだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0384.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうそう！ケーキと言えば、近所のお菓子屋さんのケーキにすっごいのがあってさ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0063.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「え！{w=0.55}それどんなの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0385.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それがさ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "一休みっていってたけど、けっこう時間が経っちゃってる。"
    $ kag_cm()
    "そろそろ始めないと、今日中に終わらなくなりそう。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}ごちそうさまでした」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0090.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「もういいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}仕事が残ってますから」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0386.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあ、あたしも行くよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b7_d__dash__07_03:
    $ kag_set_bookmark('「７日目」おたがいの気持ち')
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0387.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「糸をほどくのはあたしがやるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、いいですよ。"
    extend "わたしが……」"
    $ kag_cm()
    $ kag_playse('1-0388.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「こういうのは、りずむちゃんよりなれてるあたしにまかせてよ。{w=0.55}ここをこうやって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0389.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ちがった。{w=0.45}こっちかな？あれ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0390.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ～もうわかんなくなってきちゃった。{w=0.6}こうなったら一か八か！えい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_playse('se-008.2.ogg', buf=1, loop=False)
    $ kag_playbgm('m52', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あぁ……」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0391.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ありゃ……」"
    $ kag_stopse(buf=0)
    $ kag_stopse(buf=1)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こんがらがっちゃいましたね」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0392.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ド、ドンマイドンマイ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ドンマイって、どうするんですか？{w=0.5}これ」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0393.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どどど、どうしよう～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0133.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なになに～どうしたん？{w=0.4}{nw}"
    $ kag_drawchar('a_05.tlg', time_ms=100, sepia=False, canskip=True)
    extend "う～わ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0091.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ありゃぁ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0087.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「これはもう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0394.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やっぱり、はさみで切るしかないよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ？{w=0.45}ちょ、ちょっとどれみちゃん？」"
    $ kag_cm()
    $ kag_stopbgm()
    "チョキン"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ああ……」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0395.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ごめんね、りずむちゃん。これはこれで、何か別のアクセサリーにでもしようよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.75}じゃないです」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0396.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ごめんじゃないです！{w=0.45}せっかく、せっかくうまくできていたのに。{w=0.4}あと少しで完成だったのに！」"
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0397.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それに、からまったからってハサミで切っちゃうなんて、いいかげんすぎです！」"
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0398.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「な！{w=0.55}なによそれ！{w=0.45}たしかに悪いのはあたしだけどさ、そんな言い方ってないじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0134.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まあまあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0088.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「２人とも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0399.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それに元はといえば、まちがったのりずむちゃんの方じゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！{w=0.55}わたしが、わたしが悪いって言うんですか？」"
    $ kag_cm()
    $ kag_playse('1-0400.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなこと言ってないよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それじゃ、悪いのは誰だって言うんですか！」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0094.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ちょっと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0092.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「よしなよ、ケンカは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}どれみちゃんは、いつもいいかげんだと思う」"
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0401.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ムカ！{w=0.3}\nりずむちゃんは細かいことばかり気にしすぎだよ！{w=0.4}そんなことだから、魔女界でもうまくいかないんじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！」"
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0402.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0135.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あちゃ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0089.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m407', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg413', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('6-0064.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ポロリンピュアリン　ハナハナピ！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg004', time_ms=100, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0403.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('circle02', 'bg414', time_ms=600, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('6-0065.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おっきな水の入ったバケツよ、出ろ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg004', time_ms=100, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_ws(buf=0, canskip=True)
    $ kag_playse('se-029.3.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('どれみ「')
    "どれみ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0093.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「びしょぬれだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0136.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なんであたしらまで……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0090.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ハナちゃん、ヒドイわ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_drawchar('hn_m_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0066.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ！りずむ！{w=0.5}ケンカはダメだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0404.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "……"
    $ kag_cm()
    "どうして、\nどうしてわたしがこんな目にあわなきゃいけないの！？"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「元に戻れ！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('note', 'white', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(800, canskip=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('note', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    "まばゆい光につつまれ、\nびしょぬれだったみんなの服が元どおりになる。"
    extend "\n水びたしになった店内もいつもの通りに戻った。"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0094.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ふあ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0137.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「さっすが魔女やな。一瞬で元どおりや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.8}グスッ」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0095.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ\t「')
    "おんぷ	「りずむちゃん……{w=0.45}泣いてるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「グス……{w=0.65}もう……{w=0.6}イヤです」"
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0405.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もうイヤ！」"
    $ kag_playse('se-021.ogg', buf=0, loop=False)
    $ kag_cm()
    "わたしは２階の自分の部屋へかけだした。"
    $ kag_cm()
    $ kag_drawchar('hn_m_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0067.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「来ないで！」"
    $ kag_cm()
    $ kag_playse('6-0067.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「っ！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b7_d__dash__07_04:
    $ kag_set_bookmark('「７日目」おたがいの気持ち')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんで……{w=0.45}なんでわたし、こんな所にいるんだろ？」"
    $ kag_cm()
    $ kag_sound_se('se-024.ogg', buf=1)
    $ kag_playse('2-0091.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}何ですか」"
    $ kag_cm()
    $ kag_playse('2-0092.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「その、ちょっと話があるの。{w=0.4}出てきてくれない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ひとりにさせてください」"
    $ kag_cm()
    $ kag_playse('2-0093.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「……そう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "はづきちゃんの足音が遠ざかる。"
    $ kag_cm()
    "わたしは、まくら元においてあるラムネのビンを手にする。"
    $ kag_cm()
    "ビンの中のガラス玉がカラカラと乾いた音をたてる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハア……」"
    $ kag_cm()
    $ kag_sound_se('se-024.ogg', buf=1)
    $ kag_playse('3-0138.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なぁりずむちゃん。{w=0.4}出てきてくれへんかな？とにかく話あわな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0095.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだよ。まずはお茶でものみながらさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}ラムネ」"
    $ kag_cm()
    $ kag_playse('5-0096.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「へ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0139.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ラ、ラムネって言われても、縁日とかやないと売ってへんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ラムネを持ってきてくれたら、部屋から出てもいいです」"
    $ kag_cm()
    $ kag_playse('5-0097.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「なんかババみたいなこと言ってるよ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0140.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマやな……{w=0.65}でも何とかさがすしかないか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}ないならいいです。"
    extend "別に」"
    $ kag_cm()
    "わたしはホウキを取り出した。"
    $ kag_cm()
    $ kag_playse('5-0098.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0141.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、りずむちゃん！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg015', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b7_d__dash__07_05:
    $ kag_set_bookmark('「７日目」おたがいの気持ち')
    $ kag_cm()
    "あたりはすっかりまっ暗になってしまった。"
    $ kag_cm()
    "行くあてもなく、ホウキに乗ってさまよっていたら、ＭＡＨＯ堂に戻ってきてしまった。"
    $ kag_cm()
    "ＭＡＨＯ堂の明かりはついている。"
    $ kag_cm()
    "もうみんな帰って、ハナちゃんだけかな？\nわたしは玄関ではなく、出てきたときと同じく、２階にある自分の部屋の窓から、中に入った。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b7_d__dash__07_06:
    $ kag_set_bookmark('「７日目」おたがいの気持ち')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}明かり、つけなきゃ」"
    $ kag_cm()
    "ぴとっ"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「つめたぁ！"
    extend "な、何？」"
    $ kag_cm()
    $ kag_playse('4-0096.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフフ、わたしよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、おんぷちゃん……？」"
    $ kag_cm()
    $ kag_playse('se-058.ogg', buf=1, loop=False)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b7_d__dash__07_07:
    $ kag_set_bookmark('「７日目」おたがいの気持ち')
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0097.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('4-0098.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ラムネ。飲みたかったんでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい」"
    $ kag_cm()
    $ kag_playse('4-0099.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あいちゃんとももちゃんが探してきてくれたのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('4-0100.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}ごめんなさい。"
    extend "その、みんなに、迷惑をかけちゃって」"
    $ kag_cm()
    $ kag_playse('4-0101.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いいんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0102.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「友だちだったら、ケンカぐらいするわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、みんなまで巻き込んじゃって」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0103.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう思ってくれるんだったら、仲直り。{w=0.6}してほしいんだけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('4-0104.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんがＭＡＨＯ堂にきて、一番心配してたのって誰だと思う？」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_d_b7_choices_d03:
    $ kag_set_bookmark('どれみシナリオ選択肢03')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】どれみちゃん', current_stem='d_b7', storage=None, target='*choices_d03-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】ハナちゃん', current_stem='d_b7', storage=None, target='*choices_d03-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_d_b7_choices_d03__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag += 1
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0105.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんは、りずむちゃんが元気になってほしいって思ってるんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}そうかもしれません」"
    $ kag_cm()
    jump kag_d_b7_after_choices_d03
    call kag_s_wait

label kag_d_b7_choices_d03__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0106.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ハナちゃんは、どれみちゃんもりずむちゃんも大好きだから、{w=0.45}２人がケンカするのを見てられなかったんじゃないかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_playse('4-0107.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ハナちゃん。{w=0.3}入ってきて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん」"
    $ kag_cm()
    $ kag_playse('6-0068.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、ごめんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしの方こそ……{w=0.6}ごめんなさい」"
    $ kag_cm()
    jump kag_d_b7_after_choices_d03
    call kag_s_wait

label kag_d_b7_after_choices_d03:
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0108.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんは、\nどれみちゃんのこと、どう思ってるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……」"
    $ kag_cm()
    $ kag_playse('4-0109.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「キライになった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よく……{w=0.55}わからないです」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0110.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんのこと、全部キライ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぜ、全部というわけじゃ……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0111.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「誰だって、いいところもあれば悪いところもあるでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0112.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それはどれみちゃんだってりずむちゃんだって、いっしょじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('4-0113.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんは、どれみちゃんのいいところだって知ってるでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}はい」"
    $ kag_cm()
    $ kag_playse('4-0114.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「だったら、仲直りできるんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、どうしたらいいんでしょう……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0115.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「かんたんよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0116.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「伝えればいいのよ。{w=0.45}今のりずむちゃんの、すなおな気持ち」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「気持ち……」"
    $ kag_cm()
    $ kag_playse('4-0117.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんに会えばわかるわ。{w=0.35}行きましょ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg003', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b7_d__dash__07_08:
    $ kag_set_bookmark('「７日目」おたがいの気持ち')
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0142.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お、やっと出てきたな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、こんな遅くまで……{w=0.55}ホントにごめんなさい」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0094.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「いいのよ。気にしないで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0099.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0406.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみ……{w=0.45}ちゃん」"
    $ kag_cm()
    $ kag_playse('1-0407.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「これ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ！タペストリー……{w=0.6}これ、どれみちゃんが、作りなおしたの？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0408.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん。{w=0.45}りずむちゃんが朝から作ってたのを、あたしがダメにしちゃったから、おわびにと思ってさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0409.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あんまり、うまくないんだけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん。"
    extend "こんなに上手にできるのに、わたし、どれみちゃんにヒドイこと言っちゃって……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0410.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それは言いっこなしだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん、ごめんなさい」"
    $ kag_cm()
    $ kag_playse('1-0411.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしこそ、ごめんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0069.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それじゃあ２人とも、仲直りのあくしゅ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0412.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m14', loop=True)
    "わたしとどれみちゃんは、おたがいの両手をにぎりあった。"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへ、りずむとどれみ、やっと笑った」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0413.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へへへ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0118.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃ、仲直りできたことだし！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0100.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ご飯にしよう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0143.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まかしとき！あとあっためるだけやから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やった！ハナちゃんおなかペッコペコ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、家には帰らないんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0095.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「実は今日、みんなでＭＡＨＯ堂に泊まろうって決めたのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだったんですか」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0144.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほなしたくしてくるから、みんな座って待っといて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0414.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあ、あたしも手伝う！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0415.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わ、わたしも手伝います！」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0416.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、行こ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.d7_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_d_b8_gamestart
    return
