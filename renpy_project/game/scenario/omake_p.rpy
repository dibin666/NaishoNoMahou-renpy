# Auto-generated from 07. omake/omake_p.ks by tools/transpile_ks.py
label kag_omake_p:

label kag_omake_p_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('blind01', 'black', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_poppu.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('note', 'bg014', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_f.c_num=1
    $ kag_history_opt(output=True, enabled=None)
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0263.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「さぁ～て、午前中のデートも終わったし、ＭＡＨＯ堂によってこうかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0264.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「今日はどんなアクセサリー作ろっかな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-005.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('7-0265.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うわっ！な、なに？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0266.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「またおねえちゃんだな～\nまったくしょうがないな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_sound_se('se-009.1', buf=1)
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0267.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「お姉ちゃん！{w=0.55}また何かドジっちゃったでしょ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0268.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あれ、みんな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0373.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「うぅ、ぽ、ぽっぷちゃん……！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0269.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃん！どうしたのその荷物？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0374.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ちょ、ちょっと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0270.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃん、みんなは～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0375.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ん～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0270.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0376.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「す、すみません。{w=0.55}\n荷物、いくつか持ってくれませんか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('7-0271.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ああっ！{w=0.55}ごめん！{w=0.45}よいしょっと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('9-0377.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふう、ありがとうございます」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0272.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃん、重い荷物は１度に運ぶより、何回かに分けて運んだ方がいいと思うよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0378.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。気をつけます」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0273.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ところで、みんなはどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0379.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.55}みなさんは、午後から学校に行ってます」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0274.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「学校？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0380.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、なんでも『音楽クラブ』の合同練習の日とかで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0275.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ハナちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0381.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんも、みなさんといっしょです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0276.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「それでみんないないんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0382.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、わたしがお店番をしてるんです。あ、でも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0383.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「お店番といっても、お客さんがぜんぜん来ないんで、{w=0.5}お店の掃除と片づけをしてたんですけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0277.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「なるほどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0384.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あとは、アクセサリーの仕分けをしたら終わりです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0278.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「それだったら、あたしも手伝うよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0385.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいんですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0279.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「もともと手伝いするつもりだったから、{w=0.6}ぜんぜんオッケーだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0386.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとうございます！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('9-0387.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぽっぷちゃんに手伝ってもらったら、あっという間でしたね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0280.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「へへへ、そんなことないよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0388.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ひとりだとけっこう大変だったんで、助かりました。{w=0.6}どれみちゃんは、まとめて一気にやっちゃえばいいって言ってたけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0281.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねえちゃんのヤツ、テキトーなことを……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0389.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ま、まあ片づけはすんだことですし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0282.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「それにしてもさ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0283.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃん、{w=0.65}あたしが来るまで、ひとりでお店番でやってたんだよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0390.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0284.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「それって、けっこうすごいことじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0391.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0285.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「だって、お店番って『レジ』とか『お店の中の整理』とか色々な仕事があるよね。{w=0.6}それをひとりでやってたんでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0392.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！い、いえ、お客さんは来ませんでしたし、{w=0.45}そんなに大変じゃなかったですよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0286.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ううん。{w=0.55}だってそれはたまたまお客さんが来なかっただけで、{w=0.35}もし来てたらきっといそがしかったと思うんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0393.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは、まあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0287.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おねえちゃんたちも、こんな大変なことまかせっきりにしちゃうなんて、{w=0.55}ちょっとひどくない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0394.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ、わたしがお願いしたんです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0288.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0395.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさんにも、ひとりでお店番するのは大変だよって言われたんですけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0289.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「だったらどうして？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0396.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさんとってもやさしいから、{w=0.6}それに甘えちゃダメかなって思って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0290.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ふ～ん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0397.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「へ、変でしょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0291.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そんなことないけど。{w=0.65}りずむちゃん、マジメすぎじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0398.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0292.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うん！そんなにマジメだと肩こっちゃうよ。{w=0.65}楽しければそれでいいじゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0399.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0293.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「どうせお店はヒマなんだから、何かして遊ぼうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0400.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「う～ん……{w=1.6}\nわかりました！じゃあ何をして遊びましょう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0294.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うんとね～……{w=0.65}なぞなぞとかどう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0401.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、いいですね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0295.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「じゃあ第１問！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0296.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃんが、人間界で最初に会ったのはだれ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】どれみちゃん', current_stem='omake_p', storage=None, target='*true_01', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】ハナちゃん', current_stem='omake_p', storage=None, target=kag_f.case, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p2:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0297.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第２問。ブニュちゃんの手紙で、お姉ちゃんが見ぬかれていたのはなに？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case1='*true_0'+str(renpy.random.randint(1,2))
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】寝坊', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】遅刻', current_stem='omake_p', storage=None, target=kag_f.case1, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p3:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0298.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第３問！{w=0.5}お姉ちゃんのお話で、あたしが何の忘れ物を届けたか覚えてる？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_f.case1='*true_0'+str(renpy.random.randint(1,2))
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_add_link('【Ａ】うわばき', current_stem='omake_p', storage=None, target=kag_f.case1, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】宿題', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p4:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0299.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第４問！{w=0.5}お姉ちゃんのお話で出てきた、あいちゃんのお好み焼きの名前は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case1='*true_0'+str(renpy.random.randint(1,2))
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】イカタコキャベツ大盛りスペシャル', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】豚玉キャベツ大盛りスペシャル', current_stem='omake_p', storage=None, target=kag_f.case1, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p5:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0300.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第５問。{w=0.5}はづきちゃんのお話で、はづきちゃんが気を失ったのは、学校のどこ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】理科室', current_stem='omake_p', storage=None, target='*true_03', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】保健室', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p6:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0301.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「じゃあ第６問。{w=0.5}はづきちゃんのお話で、りずむちゃんがひろった子犬の名前は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case1='*true_0'+str(renpy.random.randint(1,3))
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】スイカ', current_stem='omake_p', storage=None, target=kag_f.case1, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】ラムネ', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p7:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0302.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第７問。{w=0.5}あいちゃんのお話で、りずむちゃんが学校の図書館でさいしょに読んだ本は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case1='*true_0'+str(renpy.random.randint(1,2))
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】白雪姫', current_stem='omake_p', storage=None, target=kag_f.case1, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】人魚姫', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p8:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0303.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第８問！{w=0.5}あいちゃんのお話で、あいちゃんがつまみ食いした、あたしのおやつは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】栗まんじゅう', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】芋かりんとう', current_stem='omake_p', storage=None, target='*true_03', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p9:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0304.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第９問！{w=0.5}おんぷちゃんのお話で、夏祭りの日にあたしがやっていたのは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】くじ引き', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】型抜き', current_stem='omake_p', storage=None, target='*true_03', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p10:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0305.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃん。{w=0.5}そろそろつかれた？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】はい', current_stem='omake_p', storage=None, target='*choices_p10-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】いいえ', current_stem='omake_p', storage=None, target='*choices_p10-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p10__dash__1:
    $ kag_cm()
    $ kag_playse('9-0402.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0306.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「じゃあ、また今度やろうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_omake_p_miss
    call kag_s_wait

label kag_omake_p_choices_p10__dash__2:
    $ kag_cm()
    $ kag_playse('9-0403.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん。平気です」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0307.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「じゃあ続きいくよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.c_num += 1
    jump kag_omake_p_choices_p10_2
    call kag_s_wait

label kag_omake_p_choices_p10_2:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0308.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第１０問。{w=0.5}おんぷちゃんのお話の、８日目のタイトルは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】おんぷと魔法', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】りずむ', current_stem='omake_p', storage=None, target='*true_03', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p11:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0309.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第１１問！{w=0.5}ももちゃんのお話で、ももちゃんが『真髄』と言いまちがえたのはどれ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case1='*true_0'+str(renpy.random.randint(1,3))
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】心臓', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】腎臓', current_stem='omake_p', storage=None, target=kag_f.case1, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p12:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0310.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第１２問！{w=0.5}ももちゃんのお話で、８日目のお天気は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】雨のち晴れ', current_stem='omake_p', storage=None, target='*true_03', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】くもりのち雨', current_stem='omake_p', storage=None, target=kag_f.case, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p13:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0311.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第１３問。{w=0.5}ハナちゃんのお話の、ソナチネ幼稚園で、かけっこをしながら何をして遊んだ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.case1='*true_0'+str(renpy.random.randint(1,3))
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】お馬さんごっこ', current_stem='omake_p', storage=None, target=kag_f.case1, exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】鬼ごっこ', current_stem='omake_p', storage=None, target=kag_f.case2, exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p14:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0312.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第１４問！{w=0.5}ハナちゃんのお話で、夏祭りではぐれちゃったときにハナちゃんは何を使ってさがしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】懐中電灯', current_stem='omake_p', storage=None, target='*choices_p14-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】双眼鏡', current_stem='omake_p', storage=None, target='*choices_p14-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p14__dash__1:
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0313.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「正解！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0314.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃんってすご～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0404.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ。{w=0.6}わたし、こういうのわりと得意なんですよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0315.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そっかあ。\nじゃあね、最後のとっておきの問題行くよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0405.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_omake_p_choices_p15
    call kag_s_wait

label kag_omake_p_choices_p14__dash__2:
    $ kag_cm()
    $ kag_f.case2='*false_0'+str(renpy.random.randint(1,3))
    $ kag_jump('omake_p', storage=None, target=kag_f.case2)
    call kag_s_wait

label kag_omake_p_choices_p15:
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0316.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「第１５問！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0317.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「お話の最初に、りずむちゃんは何人の魔女に怒られてた？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】３人', current_stem='omake_p', storage=None, target='*choices_p15-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】４人', current_stem='omake_p', storage=None, target='*choices_p15-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_omake_p_choices_p15__dash__2:
    $ kag_cm()
    jump kag_omake_p_false_04
    call kag_s_wait

label kag_omake_p_choices_p15__dash__1:
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「……」"
    $ kag_cm()
    $ kag_playse('9-0406.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ど、どうですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_wait(2000, canskip=True)
    $ kag_playbgm('m14', loop=True)
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0318.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おめでとう！全問正解だよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0407.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「やったあ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0319.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「じゃありずむちゃんには、プレゼントを……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0408.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わくわく……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0320.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「って言いたいトコなんだけど、特にないんだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0409.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0321.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そうだ！ちょっと待ってて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0322.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「お待たせ！りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0410.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「今、ぽっぷちゃんが用意した物は、何ですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0323.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「いいからいいから……{w=0.7}いっくよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(800, canskip=True)
    $ kag_sound_se('se-030', buf=1)
    $ kag_wait(800, canskip=True)
    $ kag_playse('9-0411.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「今のは、何の音ですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0324.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「はい、これ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0412.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('r_zoom', '08ぽっぷ-01', time_ms=2000, bgcolor='0x000000')
    $ persistent.cgot2=1
    $ kag_wait(2000, canskip=False)
    $ kag_mesframe()
    $ kag_waitclick()
    $ kag_fadeoutbgm(1000)
    jump kag_extra_return_s
    call kag_s_wait

label kag_omake_p_true_01:
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0325.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「正解！それじゃあ次いくね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.c_num += 1
    $ kag_f.case='*choices_p'+str(kag_f.c_num)
    $ kag_jump('omake_p', storage=None, target=kag_f.case)
    call kag_s_wait

label kag_omake_p_true_02:
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0326.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「また正解！どんどんいくよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.c_num += 1
    $ kag_f.case='*choices_p'+str(kag_f.c_num)
    $ kag_jump('omake_p', storage=None, target=kag_f.case)
    call kag_s_wait

label kag_omake_p_true_03:
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0327.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「すご～い！正解だよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0413.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「やった！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_f.c_num += 1
    $ kag_f.case='*choices_p'+str(kag_f.c_num)
    $ kag_jump('omake_p', storage=None, target=kag_f.case)
    call kag_s_wait

label kag_omake_p_false_01:
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0328.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「残念！ハズレだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0414.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ああ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_omake_p_miss
    call kag_s_wait

label kag_omake_p_false_02:
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0329.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ブブー！ハズレ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0415.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ？おかしいなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_omake_p_miss
    call kag_s_wait

label kag_omake_p_false_03:
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0330.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ハズレ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0416.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「う～ん。むずかしいですねぇ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_omake_p_miss
    call kag_s_wait

label kag_omake_p_false_04:
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0331.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おしい～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('9-0417.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ～！最後でまちがえちゃうなんて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_omake_p_miss
    call kag_s_wait
    "//////////////////////////////////////////////////////////////{nw}"

label kag_omake_p_miss:
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_cm()
    $ layerposition_def()
    jump kag_extra_return_s
    call kag_s_wait
    call kag_s_wait
    return
