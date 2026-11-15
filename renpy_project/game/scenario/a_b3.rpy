# Auto-generated from 03. ai/a_B3.ks by tools/transpile_ks.py
label kag_a_b3:

label kag_a_b3_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_ai.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg088', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_a_b3_ai__dash__03_00:
    $ kag_set_bookmark('「３日目」平成足八本物語')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「人間界の商店街はにぎやかですね」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0401.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「魔女界でもこんくらいの所はあるやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうでしょう？\n{w=0.4}わたし、あんまり外に出ないので……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0402.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そしたらあたしの方が、魔女界のいろんな所知ってるかもな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんなにあちこちに行ったりしたんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0403.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほら、見習い試験あるから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そっか」"
    $ kag_cm()
    $ kag_playse('3-0404.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「温泉とか行ったりせえへんの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ベテランの先輩とかは、休みの前になるとよく『温泉に行きたい～』って言ってますけど、わたしは別に……」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0405.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まあ、行きたがんのは年寄りやしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お菓子屋さんとかならたまに行きますけど」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0406.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ところで、あいちゃんの一番好きな食べ物って何なんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0407.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そらやっぱりタコ焼きやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「たこやき……{w=0.6}ですか？」"
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0408.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「り、りずむちゃん、タコ焼き知らんの！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……{w=0.55}こっちの食べ物にはくわしくないので……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0409.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、魔女界にもタコ焼きはあるんやけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか？」"
    $ kag_cm()
    $ kag_playse('3-0410.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、\nひょっとして八太郎さんのことも知らん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りすむ「')
    "りすむ「ええ、どなたですか？{w=0.4}その八太郎さんて」"
    $ kag_cm()
    $ kag_playse('3-0411.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そっかー。{w=0.4}そらタコ焼きのことも知らんかあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは、どんな食べ物なんですか？」"
    $ kag_cm()
    $ kag_playse('3-0412.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「粉でといた生地の中にタコ入れて、タコ焼き用の鉄板で焼くんやけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はあ」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0413.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こう、丸い形に焼けて、外がパリッとしてて、中がとろ～っとやわらかくてな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0414.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ようじをさすと、ぷしゅ～っとゆげが出て、この香りがもうたまらんねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ほお……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0415.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「んで、青のりとソースつけて、１個丸ごとパクッ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぱ、ぱくっ」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0416.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そらもう、おいしいのあついのってもう最高！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんなにすばらしい食べ物が……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0417.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あれは大阪の大発明やな。\n{w=0.4}タコ焼きを考えた人に……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}いい香り……」"
    $ kag_cm()
    $ kag_playse('3-0418.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう！{w=0.4}ちょうどこんな感じの香りがな……{w=0.55}ん？」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_drawchar('a_07.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_waitclick()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('3-0419.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「この香りは……{w=0.6}{nw}"
    $ kag_drawchar('a_02.tlg', time_ms=100, sepia=False, canskip=True)
    extend "タコ焼きや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ！{w=0.4}これがですか！」"
    $ kag_cm()
    $ kag_playse('3-0420.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あそこで焼いてるみたいやな。{w=0.4}ちょっと見てみよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg077', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b3_ai__dash__03_01:
    $ kag_set_bookmark('「３日目」平成足八本物語')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こ、これがタコ焼き……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0421.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あのくしで丸くするんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0422.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわ～。{w=0.4}すごい手さばき～」"
    $ kag_cm()
    $ kag_playse('3-0423.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なかなかの腕前やね」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_a_b3_choices_ai01:
    $ kag_set_bookmark('あいこシナリオ選択肢01')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】……食べてみたいな……', current_stem='a_b3', storage=None, target='*choices_ai01-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】……おいしそうだな……', current_stem='a_b3', storage=None, target='*choices_ai01-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_a_b3_choices_ai01__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag=1
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0424.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、１つ買ってみよか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「やった！」"
    $ kag_cm()
    jump kag_a_b3_after_choices_ai01
    call kag_s_wait

label kag_a_b3_choices_ai01__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0425.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「食べてみる？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいんですか？」"
    $ kag_cm()
    jump kag_a_b3_after_choices_ai01
    call kag_s_wait

label kag_a_b3_after_choices_ai01:
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0426.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ……{w=0.55}しもた……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0427.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おつかい用のお金しか持ってけえへんかった。{w=0.4}これやったら買われへんわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、そうなんですか？」"
    $ kag_cm()
    $ kag_playse('3-0428.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ゴメンな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃあ、また今度……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0429.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('3-0430.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「今からあたしの家にけ～へん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0431.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そしたら、うちで焼いたタコ焼きごちそうするわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ほ、本当ですか！？」"
    $ kag_cm()
    $ kag_playse('3-0432.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマホンマ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「い、行きます！」"
    $ kag_cm()
    $ kag_playse('3-0433.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな行こ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '03あいこ-03', time_ms=1000, bgcolor='0x000000')
    $ persistent.cga2=1
    $ kag_mesframe()

label kag_a_b3_ai__dash__03_02:
    $ kag_set_bookmark('「３日目」平成足八本物語')
    $ kag_cm()
    $ kag_playse('3-0434.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お待ちどうさん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁーー！」"
    $ kag_cm()
    $ kag_playse('3-0435.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どや！{w=0.4}なかなかのモンやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なかなかどころか、さっきひっくり返してるところ見てたけど、もう魔法みたいでした！」"
    $ kag_cm()
    $ kag_playse('3-0436.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、大げさすぎや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それで、これはこのつまようじで？」"
    $ kag_cm()
    $ kag_playse('3-0437.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう。{w=0.4}さっそく食べよか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いただきます！」"
    $ kag_cm()
    "わたしは手前のタコ焼きにようじをさして、口に入れる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もぐもぐもぐ……」"
    $ kag_cm()
    $ kag_playse('3-0438.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、おいしいです～！！」"
    $ kag_cm()
    $ kag_playse('3-0439.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「よかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こんなおいしい食べ物があったなんて……」"
    $ kag_cm()
    $ kag_playse('3-0440.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そう言ってもらえると、作ったかいがあるわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', '03あいこ-03', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b3_ai__dash__03_03:
    $ kag_set_bookmark('「３日目」平成足八本物語')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「しあわせ……」"
    $ kag_cm()
    $ kag_playse('3-0441.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、歯に青のりついてんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃんだって」"
    $ kag_cm()
    $ kag_playse('3-0442.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ここがタコ焼き好きのオトメのなやみどころやね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_playse('3-0443.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まだ食べられるやろ？{w=0.4}もっかい焼こか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの！」"
    $ kag_cm()
    $ kag_set_next_indent('あいこ「')
    "あいこ「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今度は、わたしがやってみたいんですけど……」"
    $ kag_cm()
    $ kag_playse('3-0444.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ちょっと、あのクルッと返すところをやってみたくって……」"
    $ kag_cm()
    $ kag_playse('3-0445.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「わかった！{w=0.4}でも、タコ焼き作りの道はけわしいで？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg033', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b3_ai__dash__03_04:
    $ kag_set_bookmark('「３日目」平成足八本物語')
    $ kag_cm()
    $ kag_playse('3-0446.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「アカンアカン！{w=0.4}そうやのうて、こう！{w=0.55}クルッとひっくり返すねん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_playse('3-0447.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう。{w=0.4}ほら、そこはようしまわな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0448.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「このはみ出たとこ。{w=0.4}はよ入れな焼けてしまうで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こ、こうですか？」"
    $ kag_cm()
    $ kag_playse('3-0449.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もっとグイグイってやらな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、でもせっかく丸くなってたのに」"
    $ kag_cm()
    $ kag_playse('3-0450.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなんもっかい返したったら丸くなるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントだ……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg035', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b3_ai__dash__03_05:
    $ kag_set_bookmark('「３日目」平成足八本物語')
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0451.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほないただきまーす」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}ど、どうでしょうか」"
    $ kag_cm()
    $ kag_playse('3-0452.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もぐもぐもぐ……{w=0.7}うっ！」"
    $ kag_drawchar('a_05.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0453.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おいしいやん！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントですか！？」"
    $ kag_cm()
    $ kag_playse('3-0454.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマホンマ！{w=0.4}りずむちゃんも食べてみ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もぐもぐ……{w=0.55}あ、おいしい！」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0455.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやろ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あとは形ですね。{w=0.4}\nもうちょっときれいに丸くしたいかな」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0456.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「タイミングよくやればきれいになるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そこがむずかしいんですよね……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0457.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あと１００個も焼けばきっとうまくなるから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ひゃ、１００個もですか？」"
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0458.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そらそうや。{w=0.4}毎日のように焼かな、うでもなまるしな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「むむむ……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0459.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「でもまあ、りずむちゃんこんだけできるんやから、{w=0.4}やり方おぼえたらひとりでも作れるやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}レシピもメモしたし、練習してみます」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0460.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うむ、その意気や！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0461.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どないしたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん、そろそろＭＡＨＯ堂に戻らないと」"
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0462.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっ、そうやった！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_mesframe()

label kag_a_b3_ai__dash__03_06:
    $ kag_set_bookmark('「３日目」平成足八本物語')
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_sound_se('se-009.1.ogg', buf=1)
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0463.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「みんなゴメン！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0657.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃ～ん！{w=0.4}遅いよぉ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0163.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どこ行ってたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0464.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、その」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0470.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「たのんだ物、スーパーに売ってなかったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0465.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、そうそう！{w=0.4}めあての物がなかなか売ってなくってな～。な、りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.55}あ！はい！{w=0.4}多分そうでした！」"
    $ kag_cm()
    "『タコ焼きを食べていて遅れた』とはさすがに言えない。\n……わたしもそのふんいきだけはわかった。"
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0471.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「……そう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0164.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「『多分』～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0658.ogg', buf=0, loop=False)
    "どれみ「『そうでした』～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0195.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あいちゃん、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0466.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「な、なに？{w=0.4}おんぷちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0196.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「青のり。{w=0.4}歯についてるわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ！」"
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0467.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まさか！{w=0.4}あたしらちゃんとうがいしたで？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですよ！」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('はづき「')
    "はづき「………………」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0659.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんで、青のりが歯に付いてるのかな～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0165.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「なんで、うがいしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0468.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「う！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0197.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、わたしの見まちがいだったかも。{w=0.4}テヘ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0469.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お、おんぷちゃん！{w=0.4}だましたやろ～！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0198.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「し～らない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0660.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃん。{w=0.4}{nw}"
    $ kag_drawchar('d_09.tlg', time_ms=100, sepia=False, canskip=True)
    extend "食べたんでしょ、{w=0.4}タコ焼き！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0166.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃんも食べたんだよね？{w=0.4}タコ焼き」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0470.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハイ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0472.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「食べちゃったものはしょうがないわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0661.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0167.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「しかたないよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0471.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「スンマセン……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみません……」"
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_playbgm('m408a', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg401.tlg', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('1-0662.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ピリカピリララ　ポポリナペペルト！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0662.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「タコ焼きプレートよ、出てこーい！」"
    $ kag_stopse(buf=0)
    $ kag_fadeoutbgm(1000)
    $ kag_cm()
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0472.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ど、どれみちゃん、なにタコ焼きプレートなんて出してんの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0663.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなの決まってるじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0473.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフフ。{w=0.4}バツとして２人には」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0664.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「タコ焼きを焼いてもらうのさ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0168.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「２人はもう食べたから、焼くだけだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな～」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0199.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしの分もおねがいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0169.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしハナちゃん呼んでくる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.65}あ～……」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0473.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、こうなったらしゃあない。{w=0.4}さ、したくしよか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.7}そうですね。{w=0.4}あ！」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0474.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「これってさっそくだけど練習のチャンスですよね！」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0475.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そっか、そうやな！{w=0.4}いっちょやるか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よ～し。{w=0.4}がんばるぞ～！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.a3_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_a_b4_gamestart
    return
