# Auto-generated from 05. momo/m_B5.ks by tools/transpile_ks.py
label kag_m_b5:

label kag_m_b5_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_momo.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg210', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_m_b5_mo__dash__05_00:
    $ kag_set_bookmark('「５日目」夕日の砂浜')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    "今日は午前中にアクセサリーの大量注文を受けて、みんなでお客さんの所へ届けに行った。"
    $ kag_cm()
    "そして今はその帰り道。"
    $ kag_cm()
    "重い荷物を運んで、みんなは少しおつかれの様子。"
    $ kag_cm()
    "中でもどれみちゃんは見た目にわかりやすく、ぐったりしている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん大丈夫ですか？」"
    $ kag_cm()
    $ kag_set_next_indent('どれみ「')
    "どれみ「…………」"
    $ kag_cm()
    $ kag_playse('3-0884.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ああぁ～りずむちゃん、かまへんて。{w=0.4}どれみちゃん、ただ『麦茶』が飲みたいだけやねんから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そうなんですか？」"
    $ kag_cm()
    $ kag_playse('1-0916.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「む、むぎちゃ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0885.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「な？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あはははは」"
    $ kag_cm()
    $ kag_playse('4-0676.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そういえば、どれみちゃんの『これ』って毎年よね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0605.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0329.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ～そんなに麦茶飲みたいの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0917.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「むぎちゃ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0886.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃ～ん。{w=0.4}今のどれみちゃんは何を言ってもムダやで～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b5_mo__dash__05_01:
    $ kag_set_bookmark('「５日目」夕日の砂浜')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お仕事お仕事……」"
    $ kag_cm()
    "ＭＡＨＯ堂のお手伝いも５日目で、だんだん手なれてきた。"
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0422.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あ、あ～！！！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0887.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ん？{w=0.4}どないしたん、ももちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0676.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「何？」"
    $ kag_cm()
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0606.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0423.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「みんな、どれみちゃんが倒れてる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0888.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ど、どれみちゃん！{w=0.4}大丈夫か～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0330.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0677.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「大丈夫？{w=0.4}どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん、しっかりしてください」"
    $ kag_cm()
    $ kag_playse('1-0918.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「む……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0678.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「『む』？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0919.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「麦茶が切れてるよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0050.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「だぁ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.2.ogg', buf=1)
    $ kag_drawchar('o_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0679.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ど、どれみちゃん～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0889.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなことでいちいち倒れんといて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0331.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ビックリさせないでよ、どれみぃ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0920.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だってぇ～{w=0.6}麦茶がないんだよ～？{w=0.4}これ以上のピンチはどこにあるのさ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0607.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もうどれみちゃんったら、人さわがせなんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0680.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0890.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まったくどれみちゃん、心配かけさせんといて～や」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0921.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなこと言われたって～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、それじゃあ待っててください。{w=0.4}今、麦茶作ってきますから」"
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0922.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「待ってりずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0923.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ダメなんだよぉ。{w=0.4}麦茶のパックが切れてるから～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そうなんだ……」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0424.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「は～い！{w=0.4}じゃああたし、買ってくるよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0924.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おお～っ、ももちゃん、サンキュ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0425.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん！{w=0.4}いっしょにお買い物行こう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ！{w=0.4}あ！は、はい！」"
    $ kag_cm()
    "わたしたちは、元気よくＭＡＨＯ堂を飛び出して行く。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0925.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「たのんだよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg089', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b5_mo__dash__05_02:
    $ kag_set_bookmark('「５日目」夕日の砂浜')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「よかったですね。{w=0.4}安い麦茶パックがあって」"
    $ kag_cm()
    "お買い物をすませて、すぐさま帰り道へと向かう。"
    $ kag_cm()
    "近くのお店ではどれみちゃんの好きなブランドの麦茶がなかったので、少し遠くのお店まで買い物に行っていた。"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0426.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「早く帰って、どれみちゃんに麦茶を飲ませてあげないと」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0427.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだね、早く帰ろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、どれみちゃんはいいなあ」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0428.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どしたの？{w=0.4}急に」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だって、どれみちゃんって、{w=0.4}ドジだけどみんなが大好きで、あんな風にわたしもみんなと仲良くなりたいなあって思っちゃって」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0429.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだね。{w=0.4}確かにどれみちゃんはドジだけど、{w=0.4}とってもやさしいからみんな大好きだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいなあ……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0430.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだ！{w=0.4}麦茶も買ったことだし、ちょっと寄り道して、{w=0.4}りずむちゃんをわたしの一番好きなひみつの場所に案内するよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}いいんですか？{w=0.45}早く帰らなくても」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0431.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃんには悪いけど、りずむちゃんには絶対見せときたいから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_cm()
    $ kag_playse('5-0432.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「いいからいいから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃんが、そこまで言うんだったら……」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0433.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあ、ちょっと遠いからほうきで行くよ。{w=0.4}りずむちゃん、ついてきて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん、待って～」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg081', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b5_mo__dash__05_03:
    $ kag_set_bookmark('「５日目」夕日の砂浜')
    $ kag_cm()
    $ kag_playbgm('se-014.1', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「きれい～」"
    $ kag_cm()
    $ kag_drawchar('m_m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0434.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「でしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この場所だったんですね。{w=0.4}ももちゃんの一番好きなひみつの場所って」"
    $ kag_cm()
    $ kag_drawchar('m_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0435.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！{w=0.4}ここの『夕日の浜辺』を教えたのはりずむちゃんが初めてだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "わたしたちは、しばらく無言で海をながめつづけた。"
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}あのね、ももちゃん」"
    $ kag_cm()

label kag_m_b5_choices_momo02:
    $ kag_set_bookmark('ももこシナリオ選択肢02')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】今なら言えるかも', current_stem='m_b5', storage=None, target='*choices_momo02-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】ももちゃんにはちゃんと聞いてほしい', current_stem='m_b5', storage=None, target='*choices_momo02-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_m_b5_choices_momo02__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_drawchar('m_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0436.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、すごく不安だったんです……」"
    $ kag_cm()
    jump kag_m_b5_after_choices_momo02
    call kag_s_wait

label kag_m_b5_choices_momo02__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag += 1
    $ kag_drawchar('m_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0437.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「な～に？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、女王様のご命令とはいえ、{w=0.4}ＭＡＨＯ堂でみなさんのお世話になるのって、ちょっとイヤだったんです」"
    $ kag_cm()
    jump kag_m_b5_after_choices_momo02
    call kag_s_wait

label kag_m_b5_after_choices_momo02:
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('m_m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今まで人間界に住んだことなんてなかったし、{w=0.4}それに、みんなと仲良くできるか、自信がなかったんです」"
    $ kag_cm()
    $ kag_playse('5-0438.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_drawchar('m_m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0439.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「今でもそう思ってるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！{w=0.55}いえ！{w=0.4}今はちがいます！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だって、人間界はこんなにもきれいで、ももちゃんやみんなも、とてもやさしくしてくれます」"
    $ kag_cm()
    "そしてまた視線を海に戻して、わたしはさらに言葉を続けた。"
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('m_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0440.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしもね、昔、{w=0.4}同じような経験したことあるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('m_m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0441.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたし小さい頃、アメリカっていう……{w=0.6}ここからと～っても遠い場所に住んでいたんだけど、{w=0.4}初めてそのアメリカに行った時、すっごく不安だったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0441.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「『友だちができなかったどうしよう』とか色々考えて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('m_m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0442.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「でもね、まわりの人がすっごくやさしくしてくれて、アメリカのいい所もたくさん見つけていって。"
    $ kag_playse('5-0442.2', buf=0, loop=False)
    extend "それで今は、アメリカのことがすっごく好きになったんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだったんですか」"
    $ kag_cm()
    $ kag_drawchar('m_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0443.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「だから、りずむちゃんの今の気持ち、すっごくよくわかる」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、人間界に来てよかったです！」"
    $ kag_cm()
    $ kag_drawchar('m_m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0444.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「えへへへへ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0446.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それじゃあ、そろそろ帰ろっか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうだ！{w=0.4}ど、どれみちゃんが！」"
    $ kag_cm()
    $ kag_drawchar('m_m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0447.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃん、ひからびちゃってたらどうしよう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あは、あははは……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「まさか……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "本当にきれいな夕日……ちょっともったいないけど、早く帰らないと。"
    $ kag_cm()
    "どれみちゃん、ひからびてないといいけど……"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b5_mo__dash__05_04:
    $ kag_set_bookmark('「５日目」夕日の砂浜')
    $ kag_cm()
    "わたしたちがＭＡＨＯ堂へ戻ってくる頃には、もう日がしずみかけていた。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('se-009.2.ogg', buf=1, loop=False)
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0449.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ただいま！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「遅くなってごめんなさい……」"
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0926.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うぅ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}あっ！！」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0927.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「む、むぎちゃ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0450.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃん～？しっかりして？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ああぁ！{w=0.4}す、すみません！！{w=0.4}今作りますから……」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0928.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もう、待ちくたびれちゃったよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0451.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃん。I'm sorry！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0929.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でも、これでやっと麦茶にありつけるよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、これからお湯をわかして作るんで、すぐには飲めないですよ？」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0929.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ええ！即席タイプのヤツじゃないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみません、即席じゃない方がおいしいかなって思って……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0891.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もうあきらめて、家帰った方がええんとちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0930.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ああぁ～\nあたしって、世界一不幸な美少女だあ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.m5_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_m_b6_gamestart
    return
