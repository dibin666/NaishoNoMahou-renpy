# Auto-generated from 01. doremi/d_B8.ks by tools/transpile_ks.py
label kag_d_b8:

label kag_d_b8_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_doremi.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg012', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_d_b8_d__dash__08_00:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「すぅ……すぅ……」"
    $ kag_cm()
    $ kag_playse('1-0417.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「くか～くか～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('1-0418.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「んが～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ん……{w=0.6}ふあぁ～」"
    $ kag_cm()
    $ kag_playse('1-0419.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん。"
    extend "朝ですよ」"
    $ kag_cm()
    $ kag_playse('1-0420.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん～{w=0.55}あ、おはよ、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おはようございます」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b8_d__dash__08_01:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    "太陽がまだ真上までは来ていないくらいのころ、残ったみんなでなにげないおしゃべりをしていた。"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0421.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや～きのうのパーティは楽しかったね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0096.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、あんなに歌が上手だったなんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃんのギターも、ステキでした」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0101.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん、ありがとう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0119.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、ラムネはそうとう気に入ってたみたいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！"
    extend "あんなしゅわしゅわした飲み物、初めてです！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それに、中のガラス玉が、ふたの役目だったなんて、人間界の飲み物は奥が深いです！」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0145.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「さがしたかいあったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、あの玉ってどうやって入れたんでしょう？」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0422.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「さあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0097.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ビンの口をあっためてから入れるとか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0146.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなんなんかな～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「う～ん。"
    extend "なんだか魔法みたいですね」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ね～ね～。{w=0.45}今日はどうするの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0147.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0098.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃんに決めてもらったら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0423.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだね。{w=0.45}\nりずむちゃん、何かやりたいことってある？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええと……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()

label kag_d_b8_d__dash__08_02:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0099.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「いいの？りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何がです？」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0148.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何がって、今日で最後やねんから、何も仕事せんでもええんとちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん。"
    extend "どちらかっていうと、遊ぶよりかはお仕事をしたかったし、それに」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0423.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「アクセサリー作るのは、楽しいから……」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、何作ってるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、これはコースターです。"
    extend "白と青を交互にまぜると、ラムネみたいできれいかなって思って」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ホントだ～！{w=0.45}すごくきれい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0149.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんやるなぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0100.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もうりっぱなアクセサリー職人って感じね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えへへ、職人ってそんな……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0424.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんが、魔女界で雑貨ショップ開いたらいいじゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0150.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おもしろそうやなぁ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0101.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「いきなり今から、っていうのはムリだけど、将来の夢ってことでいいんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「将来の夢……{w=0.55}考えたこともなかったです」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0425.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そう？{w=0.45}あたしはあるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃんの将来の夢ってなんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0426.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そりゃあもう。ステーキ屋さんを開いて、１日中ステーキを食べることさあ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0151.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お店の人が食べてどないすんねん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0102.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん、昔から変わらないのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんね、プリン屋さんがいい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0427.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「プリン屋さん、ってハナちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えっとね～やきそばプリンに～カレープリンに～ハンバーグプリンに～ステーキプリン！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0428.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ステーキプリン！？それのった！{w=0.45}いっしょにお店やろうよハナちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0152.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、それはアカン……{w=0.6}と思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「え～！{w=0.45}そんなことないよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0103.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう、ハナちゃんったら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ……」"
    $ kag_cm()
    "わたしの将来、か……"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg096', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b8_d__dash__08_03:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0429.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや～今日のお昼は楽しみだね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いろいろ買い込みましたけど、お昼はなんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0430.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃん特製お好み焼き！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お好み……{w=0.55}焼き？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0431.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「小麦粉とかをといて、具を入れて鉄板で焼くんだけど、あいちゃんが作ったお好み焼きがまたたまらないくらいおいしいんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「人間界にはいろんな料理があるんですね」"
    $ kag_cm()
    $ kag_playse('1-0432.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「魔女界にもあるんじゃないかな？たこ焼きだってあるくらいだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔法でどうにかしちゃうから、料理ってしたことなくって……」"
    $ kag_cm()
    $ kag_playse('1-0433.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そりゃそうだよね。{w=0.45}マジョリカだって何百年も生きてるくせに、あたしより知らないことがあったりするくらいだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「女王様の命令じゃなくて、ただの観光だったらもっといろんな所に行けたと思うんですけど、そうもいかないですよね」"
    $ kag_cm()
    $ kag_playse('1-0434.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「こうしてりずむちゃんとお買い物に行ったりするのって、今日で最後なんだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。"
    extend "明日には帰らないといけませんから」"
    $ kag_cm()
    $ kag_drawchar('d_12.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0435.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホントは今日の買い物を、ハナちゃんに行ってもらおうと思ったんだけどね。{w=0.45}いざたのもうって時にいないんだよね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今日はももちゃんの家に行くって言ってましたよ。"
    extend "なんでも見たいテレビがあるとかで」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0436.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え！そうなの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしがマジョリカさんの部屋を借りちゃってるせいで、見たい番組を見のがしたとかで、今日は帰ってこないみたいですよ」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0437.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そっかあ。{w=0.55}それじゃ今日はりずむちゃんひとりなんだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0438.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だったら、うちに来なよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_playse('1-0439.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ひとりより２人の方が楽しいって。{w=0.45}それにぽっぷもいるしさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0440.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「夕べはあたしがりずむちゃんの部屋に泊まったし、おあいこでってことでさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふ、そうですね。"
    extend "わかりました」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0441.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあたし、家によってお母さんにひとこと言ってくるから、先にＭＡＨＯ堂に帰ってて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_d_b8_d__dash__08_04:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0104.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「じゃありずむちゃん、今日はどれみちゃん家でお泊まりなのね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「最後の日なんで、ちょっとくらいなら……{w=0.55}と思いまして」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0153.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「かまへんやろ。{w=0.55}にしても昨日とはうってかわって２人の仲、良うなってるやん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「昨日のことは……{w=0.5}反省してます」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0154.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はづきちゃんな、りずむちゃんがいてへん時に、すごい剣幕でどれみちゃんに怒ってんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0105.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「もう、あいちゃんやめてよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0155.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あれは幼なじみやないと言われへんな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃんとどれみちゃんって、\n幼なじみなんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0106.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「幼稚園の頃からのつきあいなのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいなぁ。"
    extend "\nわたし、幼なじみって近くにいないんですよ」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0156.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしも生まれたんは大阪やから、こっちに幼なじみっておれへんよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、じゃあ、あいちゃんっていつ引っ越してきたんですか？」"
    $ kag_cm()
    $ kag_playse('3-0157.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「３年生の頃にな、お父ちゃんの都合でこっちに引越して来てん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんだ……{w=0.5}わたし、みんなのこと全然知らなくて……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0442.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お待たせ！それじゃお昼にしよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0107.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0158.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほんじゃ始めよか！{w=0.45}あいこ特製豚玉、キャベツ大盛りスペシャル！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0443.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いよっ！待ってました！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0159.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はづきちゃん。{w=0.45}ご飯よそって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0108.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？{w=0.45}お好み焼きなのに、ご飯も食べるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0444.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「普通お好み焼きだけじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0160.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何いうてんの、お好み焼きはおかずや。ご飯も食べなバランス悪いやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0445.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0109.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そういうものなの……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0161.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「食べたらわかる！{w=0.45}さ、始めんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b8_d__dash__08_05:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0110.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃ、また明日ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0162.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「またな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0446.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ほんじゃね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「また明日」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0447.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、行こうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg097', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b8_d__dash__08_06:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、誰かの家にお泊まりって初めてです」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0448.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうなんだ。{w=0.45}まあたいした家じゃないけどね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんか、明日帰るのってホントかなって思っちゃいます」"
    $ kag_cm()
    $ kag_playse('1-0449.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「毎日いろんなことがあって、ホントに目まぐるしいくらいで、あっという間で……」"
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0450.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、あのさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0451.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「……{w=0.45}ううん。{w=0.45}何でもない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg029', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b8_d__dash__08_07:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    "どれみちゃん家にお招きされて、おどろいたことが２つ。"
    extend "１つは、初めてテレビを見たこと。"
    extend "もう１つは……"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '01どれみ-08', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgd5=1
    $ kag_mesframe()

label kag_d_b8_d__dash__08_08:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_playse('1-0452.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ええ！りずむちゃんって寄宿舎暮らしなの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔女界では、みんな寄宿舎に入って、学校に行くんですよ」"
    $ kag_cm()
    $ kag_playse('7-0095.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「へええ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0453.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いいねぇ、あこがれちゃうねぇ。{w=0.45}寄宿舎」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そうですか？」"
    $ kag_cm()
    $ kag_playse('1-0454.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だってさー。{w=0.45}家の手伝いとかしなくてもいいし、うるさい妹はいないし～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0096.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねえちゃん！それどういう意味？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしは、こうして誰かが家にいる方が楽しくていいと思うんですけど」"
    $ kag_cm()
    $ kag_playse('7-0097.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「寄宿舎の方がいいって。{w=0.45}誰かさんにおまんじゅう取られたりしないからさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0455.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぽっぷ、その誰かさんって、誰？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0098.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「誰でしょうね～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_playse('1-0456.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ねえ、学校に行ってるんだったら、\nいつお仕事してるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「学校は午前中までで、お昼を食べたらお仕事なんです」"
    $ kag_cm()
    $ kag_playse('1-0457.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え！{w=0.3}午前中だけなの？{w=0.6}\nいいなあ～あたしもそっちに行きたいよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0099.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねえちゃんったら……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg028', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0458.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあさ、今度魔女界に行った時、りずむちゃんの寄宿舎に遊びに行ってもいい？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「先生の許可を取れば、ＯＫだと思いますけど」"
    $ kag_cm()
    $ kag_drawchar('d_p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0459.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やった！ああ～あこがれの寄宿舎ぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え！"
    extend "て、転校するんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0460.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それはムリだけど、１日くらい体験入学させてよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はあ、まあ、先生がなんて言うかですけど」"
    $ kag_cm()
    $ kag_drawchar('d_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0461.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「やっぱ寄宿舎って言うくらいだから、制服とかってあるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしがこっちに来たときの、あの服ですけど」"
    $ kag_cm()
    $ kag_drawchar('d_p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0462.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なぁ～んだ。{w=0.45}そっか～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('7-0100.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「く～……く～……」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_d_b8_d__dash__08_09:
    $ kag_set_bookmark('「８日目」最後の夜')
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ？」"
    $ kag_cm()
    $ kag_drawchar('d_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0463.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぽっぷ。{w=0.45}風邪ひくよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('7-0101.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ん、むにゃ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0464.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ほら、起きて。{w=0.45}自分の部屋で寝なよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('7-0102.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0465.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん待ってて。ぽっぷ連れて行くから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "人間界に来て、気づいたことが２つ。"
    extend "\nそれは家族と友だち。"
    extend "\nみんなにとっては当たり前だけど、大切なんだって。"
    $ kag_cm()
    "帰ったら、さっそくママに会いに行こう。"
    extend "\nそれから……"
    $ kag_cm()
    $ kag_playse('se-031.1.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('d_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0466.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お待たせ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぽっぷちゃん、眠いのをがまんしてたんですね」"
    $ kag_cm()
    $ kag_playse('1-0467.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でもお子様だから、今頃は夢の中だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふ、悪いですよ」"
    $ kag_cm()
    $ kag_drawchar('d_p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0468.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_playbgm('bgm-v04', loop=True)
    $ kag_playse('1-0469.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「昨日のこと、ごめんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな」"
    $ kag_cm()
    $ kag_playse('1-0470.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ううん。{w=0.45}ちゃんとあやまらなきゃって思ってて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0471.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はづきちゃんに言われちゃったんだ。"
    $ kag_playse('1-0471.2', buf=0, loop=False)
    extend "『りずむちゃんのことわかってるのに、どうしてあんなこと言ったの』って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('1-0472.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「わかってたのに、わかってたつもりなのに、どうして言っちゃったんだろうって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいんですよ、どれみちゃんの言う通りだから」"
    $ kag_cm()
    $ kag_playse('1-0473.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？{w=0.45}そんな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ずっとどうしてなんだろうって、わたしも考えてたんですけど、昨日おんぷちゃんに言われてわかりました」"
    $ kag_cm()
    $ kag_set_next_indent('どれみ「')
    "どれみ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしのことを心配してくれている人がいるのに、わたしが気づかなかったから」"
    $ kag_cm()
    $ kag_drawchar('d_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0474.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だから、ありがとう。"
    extend "どれみちゃん」"
    $ kag_cm()
    $ kag_playse('1-0475.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃんに会えて、うれしかったです。"
    extend "\nこれからも友だちでいてください」"
    $ kag_cm()
    $ kag_drawchar('d_p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0476.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん！{w=0.45}ずっと友だちだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg029', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "どれみちゃんと出会って、見つけたものが２つ。"
    extend "１つは、自分の気持ち。"
    extend "もう１つは……"
    $ kag_cm()
    "言ったら、みんなどんな顔をするかな？"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.d8_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_d_c_gamestart
    return
