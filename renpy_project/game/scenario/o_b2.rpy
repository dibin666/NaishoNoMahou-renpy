# Auto-generated from 04. onpu/o_B2.ks by tools/transpile_ks.py
label kag_o_b2:

label kag_o_b2_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_onpu.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg004', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_o_b2_op__dash__02_00:
    $ kag_set_bookmark('「２日目」わからない？チャイドルのお仕事')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0516.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「大体わかったかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたしは、昨日の続きをあいちゃんとはづきちゃんに教わっていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0752.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほんなら、りずむちゃんもやってみよか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    "うまくできるかな？"
    extend "わたしは、緊張しつつもはづきちゃんが座っていた場所へ移動した。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('se-008.1.ogg', buf=1, loop=False)
    "わたしは、教えられた通りに糸をセットし、足踏みペダルを踏んだ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}こ、こんな感じですか？」"
    $ kag_cm()
    "ちょっと心配なので、２人に聞いてみた。"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0517.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うん！{w=0.4}りずむちゃん上手よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0753.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほんまや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ほ、本当ですか！？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0518.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「初めてとは思えないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0754.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うんうん。{w=0.4}りっぱなもんや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0519.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それじゃあ、次につむいだ糸を……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('4-0249.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「できた！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "上からおんぷちゃんの声が聞こえる。"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0520.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「おんぷちゃん、課題終わったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0250.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0755.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おんぷちゃん、おつかれさん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0251.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ありがと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    "なんだろ？"
    extend "状況がよく飲み込めないわたしは首をかしげる。"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0252.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあわたし、この課題を学校に出してくるね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、おでかけですか？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0253.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうよ。{w=0.4}今から学校に行ってくるの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「学校？」"
    $ kag_cm()
    $ kag_playse('4-0254.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_o_b2_choices_op01:
    $ kag_set_bookmark('おんぷシナリオ選択肢01')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】おもしろそうですね', current_stem='o_b2', storage=None, target='*choices_op01-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】わたしも行きたいです', current_stem='o_b2', storage=None, target='*choices_op01-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_o_b2_choices_op01__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「人間界の学校は、どんな感じなんですか」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0255.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どんな感じって言われても……{w=0.55}口で説明するより、じっさいに見てもらった方が早いかも。{w=0.4}りずむちゃんも来る？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_o_b2_after_choices_op01
    call kag_s_wait

label kag_o_b2_choices_op01__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag=1
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしも……{w=0.6}い、行きたいですっ！」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0256.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えっ？{w=0.4}だったら、いっしょに行く？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_o_b2_after_choices_op01
    call kag_s_wait
    "【分岐終わり】{nw}"

label kag_o_b2_after_choices_op01:
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！{w=0.4}あ、まだ教えてもらってる途中でした……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0521.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「教えるのは、学校行ってからでも別にかまわないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0756.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「行ってきーや、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それでは、お言葉に甘えまして」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg093', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b2_op__dash__02_01:
    $ kag_set_bookmark('「２日目」わからない？チャイドルのお仕事')
    $ kag_cm()
    $ kag_playbgm('bgm-001', loop=True)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0257.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、学校へ行きたいなんて急にどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あのわたし、おんぷちゃんにお願いがあるって言うか……」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0257.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの……{w=0.55}その……」"
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0258.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なに？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの！{w=0.4}わたしをおんぷちゃんの弟子に……{w=0.65}して……{w=0.55}ください」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0259.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「弟子って言われても、わたし弟子なんてとったことないからわからないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0259.2.ogg', buf=0, loop=False)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どうしてりずむちゃんはわたしの弟子になりたいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、それは……{w=0.55}その……」"
    $ kag_cm()
    $ kag_playse('4-0260.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ハッキリ言ってよ。{w=0.4}どうしてなの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「その……{w=0.6}き、昨日……{w=0.65}おんぷちゃんを見てて、すごいなって……{w=0.55}わたしも、おんぷちゃんみたいに、いろんなことができたらって……{w=0.6}思って」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0261.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いろんなこと？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わ、わたしだったら、あんなにきれいなアクセサリー、たったの１時間でなんてとてもできないし、ＭＡＨＯ堂のお仕事以外にいっぱいお仕事あるみたいだし……」"
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}おんぷちゃん？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0262.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんは、わたしがいろいろなことができるように見える？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}は、はい……」"
    $ kag_cm()
    $ kag_playse('4-0263.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わかった。{w=0.4}それじゃわたしといっしょにいましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それって……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0264.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「その後弟子になるかどうかは、りずむちゃんが決めてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！{w=0.4}ありがとうございます」"
    $ kag_cm()
    "やった！"
    extend "とりあえずは見習い期間ってことね。"
    extend "\n魔女が魔女見習いの見習いになるって言うのはちょっとフクザツだけど……"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0265.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ところで、りずむちゃんは学校って初めて？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔女界の学校には行ってるんですけど、{w=0.4}人間界の学校ってどんなところだろうって、ずっと思ってまして」"
    $ kag_cm()
    $ kag_playse('4-0266.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうなんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「人間界の学校については、{w=0.4}本でしか見たことがなくて……」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0267.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「本？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔女界の学校に、人間界の学校について書いてある本があるんです」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0268.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「その本にはどんなことが書いてあったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええと確か……{w=0.55}人間界の学校という所は、広くて大きくて」"
    $ kag_cm()
    $ kag_playse('4-0269.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「授業中におしゃべりをしたり、よそ見をしたりすると、{w=0.4}廊下で水の入ったバケツを持たされたり」"
    $ kag_cm()
    $ kag_playse('4-0270.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うんうん……{w=0.55}{nw}"
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    extend "え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それから……{w=0.5}浜辺で夕日に向かって走る先生がどの学校にも必ずひとりいて、{w=0.4}とても楽しいと書いてありました」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0271.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、そ、そう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0272.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「何か少しちがうような……{w=0.55}というよりその本って一体……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何かまちがっているでしょうか……？」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0273.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「う、ううん！{w=0.4}そんなことないわ。{w=0.4}細かいところはともかく、大体オッケーよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そういえば、おんぷちゃんって勉強家なんですね」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0274.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だって……{w=0.6}本には『人間界の学校には夏休みという、長い休みがある』って書いてありました。{w=0.4}今って、その夏休みですよね？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0275.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「せっかくのお休みなのに、課題をしているなんてすごいです」"
    $ kag_cm()
    $ kag_playse('4-0276.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ……{w=0.5}これのことね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "おんぷちゃんは、さっきＭＡＨＯ堂でやっていた課題のノートが入った、自分のバッグを見た。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}わたしだったら、お休みの日は休んじゃいます」"
    $ kag_cm()
    $ kag_playse('4-0277.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「この課題はね、夏休みに入る前にわたしがお仕事で学校を休んじゃったから、{w=0.4}その分課題として出されたものなのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ……{w=0.65}お仕事？」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ＭＡＨＯ堂って、そんなにいそがしいんですか？」"
    $ kag_cm()
    $ kag_playse('4-0278.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ああ、ちがうの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0279.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたし、ＭＡＨＯ堂以外にもお仕事があるのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それって、チャイドルの？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0280.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「チャイドルって言うのかどうかはわからないけど、そうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それって、どんなお仕事なんでしょう？」"
    $ kag_cm()
    $ kag_playse('4-0281.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね……{w=0.5}歌を歌ったり、ドラマに出演したり……{w=0.55}簡単に言うと、魔女界のマジョプリマさんみたいなお仕事かな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えええ～～！！！！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「『マジョプリマさん』って、あの有名な女優のマジョプリマ様のことですか！？」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0282.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「う、うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('4-0283.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、すごいです！！」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0284.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、ありがとう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、でも……」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0284.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃんって、『学校』と『ＭＡＨＯ堂』と『歌とかのお仕事』の３つを毎日してるんですよね？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0285.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、大変じゃないんですか？{w=0.4}わたしだったら、１つのことをするのだけでもいっぱいいっぱいになっちゃうのに……」"
    $ kag_cm()
    $ kag_playse('4-0286.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「普通に考えたら大変かもね。{w=0.4}でも、わたしは好きでやってることだから。{w=0.4}学校もＭＡＨＯ堂も仕事もとても好きだから、平気よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.7}そうですか？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0287.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん！{w=0.4}きっとそのうち、りずむちゃんもわかると思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「大変だけど……{w=0.65}平気……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0288.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、そろそろ学校に着くわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg220', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "美空第一小学校の校舎が見えてきた。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg053', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b2_op__dash__02_02:
    $ kag_set_bookmark('「２日目」わからない？チャイドルのお仕事')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_wait(800, canskip=True)
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0289.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「おまたせ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい」"
    $ kag_cm()
    $ kag_playse('4-0291.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあ、\nせっかく学校に来たんだから、中を見てみる？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0067.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「あら？瀬川さん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0292.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「玉木さん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0068.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「こんな所で何を……{w=0.5}あら？その方は？{w=0.4}この学校じゃ見ない顔のようですけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "女の子は、おんぷちゃんの後ろにいるわたしをジロリと見る。"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0293.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、この子は、ハナちゃんのいとこで、巻機山りずむちゃんっていうの。{w=0.4}夏休みだからＭＡＨＯ堂に遊びにきてるのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「り、りずむと言います……{w=0.65}よろしくお願いします……」"
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0069.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「そうでしたの。{w=0.4}りずむさんとおっしゃるのですね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい」"
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ところで！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('8-0071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「りずむさんは、この学校の児童かしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ、ちがいます」"
    $ kag_cm()
    $ kag_drawchar('t_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「困りますわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ」"
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「他校の児童がこの学校に来られるのは、あまり感心できることではないですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('t_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「この学校で、何か問題でも起こされたら大変じゃありませんこと？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0294.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「玉木さん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「瀬川さん？{w=0.4}ワタクシは児童会長ですわ。{w=0.4}学校の秩序を守るのは当然のことじゃなくて？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_drawchar('t_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わ、わたし……あの……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0295.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「平気よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、おんぷちゃん？」"
    $ kag_cm()
    $ kag_playse('4-0296.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ここはわたしにまかせて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そう言うとおんぷちゃんは目を閉じ、深呼吸をする。"
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「瀬川さん、何してらっしゃるのかしら？{w=0.4}ワタクシの話はまだ終わってませんわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0297.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「玉木さん、ひどいわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ワタクシはこの学校のことを……{w=0.6}{nw}"
    $ kag_drawchar('t_08.tlg', time_ms=600, sepia=False, canskip=True)
    extend "えっ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '04おんぷ-02', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgo1=1
    $ kag_mesframe()

label kag_o_b2_op__dash__02_03:
    $ kag_set_bookmark('「２日目」わからない？チャイドルのお仕事')
    $ kag_cm()
    $ kag_playse('4-0298.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うぅっ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('8-0078.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「せ、瀬川さん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0299.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「玉木さん……{w=0.65}りずむちゃんはただ、この学校を見たかっただけなのに」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('8-0079.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「うっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0300.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「美空小のよい所を見せるのはそんなに悪いことなの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "涙を流しながら『キッ』と玉木さんをにらむ。"
    extend "うまく言えないけど、絶妙のタイミングだ。"
    $ kag_cm()
    $ kag_playse('8-0080.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「で、ですからワタクシは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0301.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「確かに、この学校の生徒以外の人が入ることで悪いことも起きるかもしれない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0301.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "おんぷちゃんがうったえるような瞳で玉木さんを見つめる。"
    extend "でも、どうしていちいち玉木さんに背中を向けるのかな？"
    $ kag_cm()
    $ kag_playse('4-0302.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いろんな人に、この学校のすばらしい所を知ってもらって、{w=0.4}交流を深めることはとても大切なことだと思うわ！」{nw}"
    $ kag_history_opt(output=False, enabled=None)
    $ kag_waitclick()
    $ kag_history_opt(output=True, enabled=None)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('8-0081.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「それはまあ、その通りですわ。{w=0.4}でも……！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0303.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "パアっと笑顔になるおんぷちゃん。"
    $ kag_cm()
    $ kag_playse('8-0082.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「そ、そーですわ！{w=0.4}この学校のすばらしい所を見て回るのでしたら、{w=0.4}児童会長のこの玉木麗香、{w=0.4}りずむさんを大歓迎いたしますわ！{w=0.4}オーッホッホッホッホ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg053', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b2_op__dash__02_04:
    $ kag_set_bookmark('「２日目」わからない？チャイドルのお仕事')
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0304.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「さすがは玉木さん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0305.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「さ、りずむちゃん、行きましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、えっ？」"
    $ kag_cm()
    "なっ、なに？何がおこったの？"
    $ kag_cm()
    $ kag_playse('4-0306.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いいからいいから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そう言い、おんぷちゃんはわたしの手を引き校舎の中へと消えていく。"
    $ kag_cm()
    $ kag_drawchar('t_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0083.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「でも、次からは児童会長である、このワタクシの許可を……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0083.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あら？瀬川さん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-037.ogg', buf=1, loop=False)
    $ kag_playse('8-0083.3', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「瀬川さん、どこ？{w=0.4}瀬川さん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg248', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b2_op__dash__02_05:
    $ kag_set_bookmark('「２日目」わからない？チャイドルのお仕事')
    $ kag_cm()
    $ kag_playse('se-007.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0307.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はぁ、はぁ、はぁ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はぁ、はぁ……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0308.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うまくいったね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "呼吸が整ったおんぷちゃんが、わたしに笑顔で話しかける。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}どういうことでしょうか？{w=0.4}わたしには、さっぱり……」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0309.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「まだわかんない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……{w=0.7}さっぱり……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0310.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ、さっきのは、全部わたしのお芝居よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、え！{w=0.4}ええぇ～～～！？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「さ、さっきの全部、お芝居だったんですか！？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0311.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}し、信じられません……{w=0.6}だって……{w=0.55}おんぷちゃん、泣いてました……」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0312.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「涙と笑いの演技はお芝居の基本よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あはは、すごい……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0313.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあ……{w=0.55}児童会長のおすみつきをもらったし、{w=0.4}学校案内に行きましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg087', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b2_op__dash__02_06:
    $ kag_set_bookmark('「２日目」わからない？チャイドルのお仕事')
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    "帰り道の途中にちょっと寄り道をして、公園のベンチで休憩することになった。"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0314.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えーと、りずむちゃん、今日はどうだった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "おんぷちゃんはベンチでとなりに座っているわたしに話しかける。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「とても楽しかったです。人間界の学校を見学できるなんて、めったにないことですから」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0315.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう、ならよかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたしたちは、しばらくだまって夕日をながめていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃんって、やっぱりすごいですね」"
    $ kag_cm()
    "夕日をながめたまま、わたしはでつぶやいた。"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0316.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だって、あんなにすごい演技ができるんですから」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0317.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そんなことないわ。{w=0.4}このくらいの演技ができる人はたくさんいるし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、やっぱりあんなに感情がこもった演技ができるなんてすごいです」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0318.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ、ありがと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それに、今日。{w=0.4}わたし、とってもうれしかったです」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしが困ってる時も助けてくれて。"
    extend "それにおんぷちゃん、{w=0.4}本当はいそがしいはずなのに学校の案内までしてくれて」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「本当に本当にうれしかったです」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('4-0319.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「スゥ～スゥ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    "おんぷちゃんは、うつむきながら眠ってしまっていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今日は、つかれてたんですね」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん……{w=0}今日はありがとう」"
    $ kag_cm()
    "わたしは、眠っているおんぷちゃんにささやいた。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.o2_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_o_b3_gamestart
    return
