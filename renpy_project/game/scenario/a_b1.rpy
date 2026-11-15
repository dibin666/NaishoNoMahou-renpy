# Auto-generated from 03. ai/a_B1.ks by tools/transpile_ks.py
label kag_a_b1:

label kag_a_b1_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_ai.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg001', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_a_b1_ai__dash__01_00:
    $ kag_set_bookmark('「１日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0646.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあ、どうしようか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0467.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「う～ん。まずはりずむちゃんに、ＭＡＨＯ堂のことを知ってもらった方がいいかもしれないわね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0261.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うーん……{w=0.5}ほんなら、あたしがＭＡＨＯ堂を案内したるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうございます！」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0191.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしたちは、いつも通りにお店を開けましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0158.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0647.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあ、あたしとはづきちゃんとハナちゃんは、あっちでアクセサリー作ってようか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0181.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん、わかった！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0262.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほなおいで。{w=0.4}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
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
    $ kag_changetype('note', 'bg018', time_ms=1500, bgcolor='0x000000')
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_a_b1_ai__dash__01_01:
    $ kag_set_bookmark('「１日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_playbgm('m60.ogg', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0263.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ま、こんなもんかな。{w=0.4}広いようでけっこう大したことないやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}いちおうおぼえました、けど……」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0263.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「？」"
    $ kag_cm()
    "お店においてある道具の説明を受けながら、１階と２階を案内される。"
    $ kag_cm()
    "あいちゃんの言うとおり広くはないんだけど、ＭＡＨＯ堂はちょっと複雑な間取りだ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、方向オンチなものですから……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0264.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あははは！{w=0.4}まさかＭＡＨＯ堂の中では迷わへんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そうだといいんですけど」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0265.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、そろそろお店開けるみたいやな。{w=0.4}あたし今日はレジの担当するけど、りずむちゃんはどうする？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でしたら、わたしもお手伝いさせてくださ……」"
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_sound_se('se-003', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「へ？」"
    $ kag_cm()
    $ kag_resumebgm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0266.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんかたいかたい。もっとリラックスせな！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい」"
    $ kag_cm()
    $ kag_playse('3-0267.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなん『あたしもやるー！』でええねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はあ……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg002', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b1_ai__dash__01_02:
    $ kag_set_bookmark('「１日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ちょ、ちょっとドキドキします……」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0268.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何が？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、人間のお客さん相手って、初めてで」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0269.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そりゃそやな。{w=0.4}そやけど、魔女のお客さん相手と大して変わらへんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ま、魔女のお客さんも相手したことないです」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0270.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「え、ホンマ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}わたし、コピーとかお茶くみとか、お片づけとかの仕事ばっかりだったんで」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0271.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ふーん。{w=0.4}なんかＯＬみたいやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ＯＬ？」"
    $ kag_cm()
    $ kag_playse('3-0272.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こっちやったら、りずむちゃんみたいな仕事をする女の人を、ＯＬって言うねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか」"
    $ kag_cm()
    $ kag_playse('3-0273.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お客さん相手って言ってもむずかしいことないって。{w=0.4}あいそよく話ししたらええだけや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「問屋魔女の、デラさんみたいな感じでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0274.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう。{w=0.4}デラはかなりの商売人やからな。{w=0.4}マジョリカなんかいっつもあの笑顔に負けてるしな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふっ」"
    $ kag_cm()
    $ kag_playse('3-0275.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっ！{w=0.4}いらっしゃいませ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あ……」"
    $ kag_cm()
    $ kag_playse('3-0276.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何かおさがしですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "……"
    $ kag_cm()
    $ kag_playse('3-0277.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、それようにあいますよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "……"
    $ kag_cm()
    $ kag_playse('3-0278.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう。{w=0.4}うちのお父ちゃんとかも、すぐ穴あいた～とかなんとか言うて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "……"
    $ kag_cm()
    "……？\nく、くつしたのことかな？{w=0.4}アクセサリーと、どう関係が……"
    $ kag_cm()
    $ kag_playse('3-0279.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まいどおおきに！{w=0.4}りずむちゃん、お会計」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、え？{w=0.4}あの……{w=0.55}わたし……」"
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0280.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっ！{w=0.4}はい！全部で３８０円になります～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0281.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はい！{w=0.4}３８０円ちょうど、いただきます。{w=0.4}こちらが商品になります！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あいちゃんがレジに入って、会計をする。{w=0.4}さらに、お客さんがお金を出している間に、商品を包むのまで終えてしまった。"
    $ kag_cm()
    $ kag_playse('3-0282.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ありがとうございます～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうございました！」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0283.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そういえば、まだりずむちゃんに会計のやり方教えてなかったな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}すごい」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0283.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんか、うまく言えないですけど、さすがベテラン店員っていうか」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0284.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「大したことあれへんて。{w=0.4}こんなんすぐなれるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0285.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「とりあえず、こっち来て。{w=0.4}会計のやり方教えるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg002', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b1_ai__dash__01_03:
    $ kag_set_bookmark('「１日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、お買い上げあ……{w=0.55}ありがとうございます\n……{w=0.5}です」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、えっと……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0286.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、お客さんに合計金額言わな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい……{w=0.6}えっと……{w=0.55}その……{w=0.5}あの……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0287.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほら、お客さん待たせたらアカン」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっと……{w=0.6}全部で４６０円になります……」"
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの！{w=0.4}す、すみませんすみません！」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0288.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん。{w=0.4}すみませんやのうて、『ありがとうございます』や」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうございま……{w=0.6}す？」"
    $ kag_cm()
    $ kag_playse('3-0289.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もう行ってもうたで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あうう……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0290.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほらりずむちゃん、次のお会計」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あああ、どうしよう。"
    extend "そ、そうだ、こういう時こそ……"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0291.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この商品を包装して！」"
    $ kag_cm()
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('note', 'white', time_ms=1500, bgcolor='0x000000')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('note', 'bg002', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    "包装紙がふわっと浮かび、商品を包み始めようとする。"
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0292.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「わわわ！{w=0.4}アカーン！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「？」"
    $ kag_cm()
    $ kag_playse('3-0293.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっ！{w=0.4}空飛ぶタコヤキー！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「え？{w=0.4}どこどこ？」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0294.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はい！４０円のお釣りになります」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「？？」"
    $ kag_cm()
    "お客さんが視線をそらしている間に、あいちゃんは浮かんでいる包装紙を無理やり押さえこみ、ものすごい早さでラッピングを終わらせた。"
    $ kag_cm()
    $ kag_playse('3-0295.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、ありがとうございました～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あのう……？」"
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0296.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、ちょっと向こうで待ってて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg004', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b1_ai__dash__01_04:
    $ kag_set_bookmark('「１日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0297.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、あんなとこで魔法つこたらアカン！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「す、すみません。{w=0.4}つい……」"
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0298.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「目の前で包装紙が勝手に商品包み始めたら、誰かておかしいって思うよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_playse('3-0299.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「とにかく気ぃつけて、人前で魔法は使わんように」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、すみませんでした」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0300.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、こっち来て」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0301.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もっかい教えるから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい！」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0302.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「コツさえつかめたら簡単やから。{w=0.4}ちょっとやってみ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}えっと、紙をななめにしいて、箱をおいて……」"
    $ kag_cm()
    $ kag_playse('3-0303.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}あれ？{w=0.4}これじゃ包みきれないかな？」"
    $ kag_cm()
    $ kag_playse('3-0304.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ううん、箱をおく位置がおかしいねん。{w=0.4}貸してみ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('3-0305.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「入りきるかどうかわからへんのやったら、こうやって先に奥の方を巻いてみて、確かめたらいいねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そっか」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0306.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほら。{w=0.4}うまいこと包めたやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントだ！{w=0.4}すごいですね」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0307.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そらぁあたしも、ちょっとは練習したからな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしもやってみます」"
    $ kag_cm()
    $ kag_playse('3-0308.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。{w=0.4}練習あるのみやで。{w=0.4}あ！{w=0.5}それとな、もう１つコツがあったわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_playse('3-0309.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あんな、ゆっくりでええから、ていねいに包んでな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0309.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そしたらお客さんは、りずむちゃんが遅いからって怒ったりせえへんから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg016', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b1_ai__dash__01_05:
    $ kag_set_bookmark('「１日目」がんばることの大切さ')
    $ kag_cm()
    "レジの仕事をこなすうちに、気がつけば日は西にかたむいていた。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b1_ai__dash__01_06:
    $ kag_set_bookmark('「１日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0310.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はい。{w=0.4}１０００円お預かりします。{w=0.4}２００円のお返しです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}お待たせしました！{w=0.4}こちらが商品になります」"
    $ kag_cm()
    $ kag_playse('3-0311.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ありがとうございます～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとうございます！」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0312.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「だいぶ上手になってきたやん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃんのおかげです」"
    $ kag_cm()
    $ kag_playse('3-0313.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ううん、あたしはただ教えただけや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん……」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0314.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「魔法を使わんでもこれくらいできるようにならな、８日間大変やで？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔女界だったら何でも魔法ですませられるんで、うっかりたよっちゃうんですよね」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0315.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そら魔女やからしゃあないところはあるけど。{w=0.4}こっちではそうもいかんしな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔法を使わないでも、きれいなアクセサリーを作ったりできるんだから、もっとみなさんを見習わないといけないですね」"
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_sound_se('se-003.ogg', buf=1)
    $ kag_resumebgm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へ？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0316.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「かたいかたい！{w=0.4}『見習う』なんていわんと、気軽にどんどん覚えてったらええねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はあ」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0317.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、もうお店おしまいやから、片づけよか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg013', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b1_ai__dash__01_07:
    $ kag_set_bookmark('「１日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「気軽に、か……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0318.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、片づけ終わった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！{w=0.4}は、はい！」"
    $ kag_cm()
    $ kag_playse('3-0319.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなら、ちょっとこっち来てくれへん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わかりました」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0320.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「フフフ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、１階のそうじのお手伝いじゃないんですか？」"
    $ kag_cm()
    $ kag_playse('3-0321.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ええからええから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_a_b1_ai__dash__01_08:
    $ kag_set_bookmark('「１日目」がんばることの大切さ')
    $ kag_cm()
    $ kag_sound_se('se-034.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わあっ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「み、みなさん、これは？」"
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0322.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんの歓迎会に決まってるやん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0192.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあ、主役も来たから、始めましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0323.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほらりずむちゃん。{w=0.4}もっと真ん中に来て」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0648.ogg', buf=0, loop=False)
    "どれみ「せ～の！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0034.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「りずむちゃん、ＭＡＨＯ堂へようこそ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「み、みなさん……{w=0.55}ありがとうございます！」"
    $ kag_cm()
    $ kag_drawchar('m_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0159.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ほらほら。{w=0.4}飲んだ飲んだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0324.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ももちゃん、お酒やないねんから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0193.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、今日はずっと包装するのをがんばっていたみたいだったわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}あいちゃんのおかげで、どうにかうまく包めるようになりました」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0325.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん飲み込み早かったで。{w=0.4}ちょっとコツ教えたらあっという間や」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0649.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホント？{w=0.4}あたしにもコツ教えてよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？は、はい」"
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0326.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃんには何回も教えたやろ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0650.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや～ちょっと油断すると忘れちゃうんだよね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0327.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もう～どれみちゃんは～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0182.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ！{w=0.4}今日は楽しかった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0468.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「フフ、よかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0328.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('3-0329.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「今日はけっこうつかれたんちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんなことないです」"
    $ kag_cm()
    $ kag_playse('3-0330.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホンマです！{w=0.4}あ……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0651.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃんといっしょにいたから、大阪弁がうつっちゃったね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ですね」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0331.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そしたら大阪弁も教えたる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！{w=0.4}お、おおきに！」"
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0332.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「アカンアカン。{w=0.4}ぜんぜんなってへん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0035.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「アハハハ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ……」"
    $ kag_cm()
    "お仕事って、がんばって苦労しておぼえるだけじゃないんだ。"
    extend "\nみんなの笑顔を見ていて、そんなことをふと感じた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0333.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なに？{w=0.4}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「明日もよろしくね！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.a1_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_a_b2_gamestart
    return
