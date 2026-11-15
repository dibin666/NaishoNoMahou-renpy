# Auto-generated from 03. ai/a_B5.ks by tools/transpile_ks.py
label kag_a_b5:

label kag_a_b5_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_ai.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg005', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_a_b5_ai__dash__05_00:
    $ kag_set_bookmark('「５日目」お父さんってなに？')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0676.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ふぁ～。{w=0.55}みんなおはよう～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おはようございます」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0200.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「おはよう。{w=0.4}どれみちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0677.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おはよう……{w=0.4}あれ、あいちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0170.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「まだ来てないよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今日はちょっと遅いですね」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0474.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そのうち来ると思うから、先に準備してましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_sound_se('se-009.2.ogg', buf=1)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0678.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃん、おは……」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_drawchar('a_11.tlg', time_ms=50, sepia=False, canskip=True)
    $ kag_playse('3-0508.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ああぁ～！！{w=0.5}ハラ立つわ～～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_resumebgm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0679.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、あいちゃん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0475.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「お、落ちついて、あいちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0201.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「何があったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0509.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何もかんもないわ……{w=0.55}まったくお父ちゃんは！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お父ちゃん？」"
    $ kag_cm()
    $ kag_playse('3-0510.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうや、最近のお父ちゃんと来たら、毎晩毎晩、夜遅くまでお酒飲んで、{w=0.4}しかも家に帰って来たと思たら、服も着替えずに玄関でひっくり返って寝てしまうねんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0680.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そ、そうなんだ……{w=0.65}\nでもウチのお父さんも時々あるよ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0511.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それが毎日やで！{w=0.5}毎日！{w=0.4}{nw}"
    $ kag_drawchar('a_11.tlg', time_ms=600, sepia=False, canskip=True)
    extend "まったく自分の健康のこと考えんと、もう酒ばっか飲んでからに～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0202.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「つまり、\nあいちゃんはお父さんのことが心配なわけね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0512.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まあ、そういうことや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0171.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「だったら、お父さんにそう言えばいいんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0513.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「でも、お父ちゃんの楽しみ減らすのもなあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0681.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いくら楽しみでも毎晩は多いよねぇ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0203.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「体によくないんだから、やっぱり言ってあげた方がいいんじゃないかしら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0514.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……？」"
    $ kag_cm()

label kag_a_b5_ai__dash__05_01:
    $ kag_set_bookmark('「５日目」お父さんってなに？')
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0682.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え！あ、あの……{w=0.6}すみません！{w=0.4}やっぱりいいです！」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0683.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんか、よくわからないって顔してるよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}あの」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0204.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お父ちゃんって、どんな方なんでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0684.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0205.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そっか。{w=0.4}魔女界にはママしかいないもんね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0206.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「人間界には、ママの他にパパがいるのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさんにもパパがいるんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0685.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、いるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0476.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしのパパは、映画監督をしてるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0172.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしのお父さんは建築家だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0686.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしのお父さんは釣りの雑誌で記事を書いてて、ふだんはパソコンの前でうなってるし、{w=0.4}週末になるとだいたい釣りに行っちゃうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0207.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしのお父さんは電車の運転手だから、{w=0.4}年に何度かしか会えないのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0477.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わかったかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっと……{w=0.6}つまり……{w=0.55}『お父さん』とは、映画監督や建築家などをしながら、週末には釣りに行き、年に何回かしか会えない方のことだと……？」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0687.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや、そうじゃなくて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0208.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんなにそれぞれのお父さんがいるから、お仕事もちがうのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なるほど……」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0478.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ど、どうにかわかってもらえたかしら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg203', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()

label kag_a_b5_ai__dash__05_02:
    $ kag_set_bookmark('「５日目」お父さんってなに？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "その日の午後、あいちゃんとわたしはお使いに出かけた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そういえば……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0515.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、まだ『お父さん』のこと、よくわかってなくって」"
    $ kag_cm()
    $ kag_playse('3-0516.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「『お父さん』は人それぞれやから、説明するのは大変やろな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃんの『お父さん』は、どんな人なんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0517.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしのお父ちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0518.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('3-0519.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「明るくて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0520.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「冗談が好きで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うんうん」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0521.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「短足で」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え」"
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0522.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……{w=0.3}おならがくさい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、おなら？」"
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0523.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もーあれはアカン。{w=0.4}音もでかいから、ご近所様に迷惑やっていっつも言うてんねんけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「け、煙とかも出るんでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0524.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あはは！{w=0.4}それはないない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どんなお仕事をされてるんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0525.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「タクシーの運転手。{w=0.4}ほら、あんな感じの車で、お客さんを運ぶねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、上にかざりがついている車ですか？」"
    $ kag_cm()
    $ kag_playse('3-0526.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それで、あの……{w=0.55}最近はお酒が多いと」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0527.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「他はともかく、お酒だけは健康に悪いから、ひかえてほしいねんけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何かいいところとかって、ないんですか」"
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0528.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんなハッキリと……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0529.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ないもんはないから、しゃーないやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お父さんを替えることってできないんですか？」"
    $ kag_cm()
    $ kag_playse('3-0530.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それはでけへんよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか……」"
    $ kag_cm()
    $ kag_playse('3-0531.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お父ちゃんとお母ちゃんがおれへんかったら、あたしが生まれてくることもなかったんやから、{w=0.4}ホンマは感謝せなアカンねんけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃんのママは、どんな人なんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0532.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「やさしくてな、あったかくてな。{w=0.4}いつもそばにいてくれたらって、よう思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg208', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()

label kag_a_b5_ai__dash__05_03:
    $ kag_set_bookmark('「５日目」お父さんってなに？')
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いっしょに暮らしていないんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0533.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。{w=0.4}あたしの小さいころにちょっとワケがあってな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いっしょに暮らしたいとは思わないんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0534.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そう思って、魔女見習いになってんけどな。{w=0.4}こればっかりはなかなかうまくいかへんわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「う～ん……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0535.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんがなやまんでもええって。{w=0.4}もうなれたし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、それってすごくつらいことじゃないですか」"
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしは、ママとはなれて暮らすのが当たり前だって思っているから気にならないだけで」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もしそれが当たり前じゃないとしたら、悲しいことだと思います」"
    $ kag_cm()
    $ kag_playse('3-0536.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん、そうやな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「できることなら、わたしだってママといっしょに暮らしたいですし……」"
    $ kag_cm()
    $ kag_playse('3-0537.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ごめんなさい。{w=0.4}わたしのことなんかどうでもいいですよね」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0538.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなことない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0539.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんの気持ちわかる。{w=0.4}あたしなんて、お母ちゃんに会いたいって毎日思ってる」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('3-0540.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「せやけどな、お父ちゃんはあたしがおらなアカンねん。"
    $ kag_playse('3-0540.2', buf=0, loop=False)
    extend "あたしだけ勝手言うわけにもいかへん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0540.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「だらしなくても、あたしのお父ちゃんは世界でただひとりやもん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん……」"
    $ kag_cm()
    $ kag_playse('3-0541.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「だからいつかは、きっといつかはみんなで暮らせればって、そう思てんねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん……{w=0.5}あいちゃんは、やさしいんですね」"
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('あいこ「')
    "あいこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みんなのことを考えて、がまんもして……{w=0.55}わたしなんか自分のことばっかりでせいいっぱいなのに」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0542.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしかて、がまんでけへんこともあるで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……」"
    $ kag_cm()
    $ kag_playse('3-0543.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなときは、これや」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハーモニカ？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0544.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。{w=0.4}このハーモニカはな、お父ちゃんとお母ちゃんをつなぐ、あたしの宝もんやねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0545.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「これ吹くと、さみしい気分がどっか飛んでいくみたいでな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}あいちゃんのお父さんとお母さん、また、いっしょに暮らせるといいですね」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0546.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん、ありがとう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "古いハーモニカには、あいちゃんの思いがいっぱいつまっている、そんな輝きが見えるような気がした。"
    $ kag_cm()
    "目の前の女の子を幸せにできる魔法は、魔女のわたしでも思いつかない。"
    extend "\nそれならせめて、言葉だけでも……"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.a5_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_a_b6_gamestart
    "B	あいこ	5	4866	:"
    return
