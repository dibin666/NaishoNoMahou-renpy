# Auto-generated from 06. hana/hn_B5.ks by tools/transpile_ks.py
label kag_hn_b5:

label kag_hn_b5_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hana.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg014', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hn_b5_hn__dash__05_00:
    $ kag_set_bookmark('「５日目」ひとりぼっちのＭＡＨＯ堂')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「コホン！コホン！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_sound_se('se-024', buf=1)
    $ kag_playse('6-0602.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ！おっはよう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('6-0602.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-024', buf=1)
    $ kag_playse('6-0603.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、寝てるの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「う……」"
    $ kag_cm()
    $ kag_playse('6-0604.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～入るよ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0605.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「り～ず～む～！{w=0.4}そろそろ起きようよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0605.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うぅ」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0606.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハ、ハナちゃん……」"
    $ kag_cm()
    $ kag_drawchar('hn_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0607.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うわぁ～！{w=0.4}りずむ～！顔真っ赤だよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あは、すみません。{w=0.4}コホンコホン！」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0608.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だ、大丈夫です」"
    $ kag_cm()
    $ kag_playse('6-0609.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ホントに？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「コホン、コホン！」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0610.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんどれみ呼んで来る！{w=0.4}ちょっとまってて！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg028', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b5_hn__dash__05_01:
    $ kag_set_bookmark('「５日目」ひとりぼっちのＭＡＨＯ堂')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    $ kag_playse('1-1099.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん～ムニャムニャ。{w=0.4}ステ～キ～……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-1100.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「てへへ、食べられないよ。{w=0.4}こんな大きなステ～キ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-025', buf=1)
    $ kag_playse('1-1101.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん～もう、限界さぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-025', buf=1)
    $ kag_playse('1-1102.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ムニャムニャ、そんなにムリだよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-026', buf=1, loop=False)
    $ kag_stopbgm()
    $ kag_playbgm('m52', loop=True)
    $ kag_playse('1-1103.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う、うわぁ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_drawchar('d_p_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1104.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「な、何？何？{w=0.4}宇宙人の逆襲！？{w=0.4}せっかくステーキ食べてるときに、宇宙人なんて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0611.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1105.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あれ？{w=0.4}ハナちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0612.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ～！{w=0.4}開けて～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1106.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う、うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(800, canskip=True)
    $ kag_drawchar('d_p_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1107.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃんダメじゃん。{w=0.4}他の人に見つかったらどうすんのさ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_m_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0613.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あのね、大変なの！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1108.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どうかした？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_m_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0614.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむが、りずむが……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_p_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1109.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん落ち着いて！{w=0.4}りずむちゃんがどうしたの！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_m_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0615.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「とにかく早くきて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1110.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ちょ、ちょっと待ってよ！{w=0.4}まず着替えさせ……{w=0.55}{nw}"
    $ kag_drawchar('d_p_05.tlg', time_ms=600, sepia=False, canskip=True)
    extend "あああ～！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '06ハナ-05', time_ms=1500, bgcolor='0x000000')
    $ persistent.cghn4=1
    $ kag_mesframe()

label kag_hn_b5_hn__dash__05_02:
    $ kag_set_bookmark('「５日目」ひとりぼっちのＭＡＨＯ堂')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「コホン！{w=0.4}どれみちゃん。{w=0.4}すみません」"
    $ kag_cm()
    $ kag_playse('1-1111.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それよりも大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}なんとか……{w=0.65}コホンコホン！」"
    $ kag_cm()
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-1112.ogg', buf=0, loop=False)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん。{w=0.4}いろいろとありがとうございます……」"
    $ kag_cm()
    $ kag_playse('1-1113.ogg', buf=0, loop=False)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「……」"
    $ kag_cm()
    $ kag_drawchar('d_m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1114.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん？{w=0.4}どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0617.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんのせいだ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1115.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0618.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんが昨日の夜、いっぱいりずむに迷惑かけちゃったから！{w=0.4}だからりずむが病気に……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ちがうよハナちゃん！」"
    $ kag_cm()
    $ kag_playse('6-0619.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えっ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「コホン！コホン！」"
    $ kag_cm()
    $ kag_drawchar('d_m_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1116.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん。{w=0.4}寝てなきゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、どれみちゃんもハナちゃんも、{w=0.4}この部屋にいない方がいいと思います」"
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0620.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この部屋にいたら、{w=0.4}わたしのカゼをうつしてしまうかもしれないから」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0621.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そんなことないよぉ～！{w=0.4}ハナちゃんならへっちゃらだよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、わたしのせいでハナちゃんやどれみちゃんがカゼを引いてしまったら」"
    $ kag_cm()
    $ kag_playse('6-0622.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1117.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、わかった。{w=0.4}ハナちゃん、行こう。{w=0.4}りずむちゃんをゆっくり休ませてあげようよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0623.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「う、うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1118.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあ、何かあったらすぐ呼んでね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「…………」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-031.1', buf=1)
    $ kag_freeimage(layer='0', page='fore')
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「コホン！{w=0.4}コホン！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でもうれしいな。{w=0.4}病気の時、誰かがそばにいてくれるのって」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今まで、わたしずっとひとりだったから……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「………………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……………………」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg065', time_ms=2000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m413a', loop=True)

label kag_hn_b5_hn__dash__05_03:
    $ kag_set_bookmark('「５日目」ひとりぼっちのＭＡＨＯ堂')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの、みなさん。{w=0.4}今からわたしの家に遊びに来ませんか？」"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「えっ！{w=0.4}あ、ごめんなさい。{w=0.4}わたしちょっと用事があって」"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「わたしも～{w=0.4}ごめんね、またさそってね」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「マジョリズム、あなたってなんか魔女っぽくないわね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ちがう方向から、声が聞こえる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ。{w=0.4}どうして？」"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「だって、あなた魔女なのに、魔法が失敗ばかりで。{w=0.4}あっ、使わなくても失敗ばかりしてるわね、アハハハ」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな、わたしだって……」"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「ムリムリ。{w=0.4}あなたなんて何をやってもムダよ」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしは、わたしは……」"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「ねぇ、マジョリズム？」"
    $ kag_cm()
    "また別の方からだ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！」"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「マジョリズム、{w=0.4}いつもひとりだけどお友だちと遊ばないの？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ」"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「はは～ん、なるほど。{w=0.4}\nあなた、友だちいないんでしょう？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんなことないです！{w=0.4}わたしにだってお友だちくらいいます！」"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「それは誰なの？」"
    $ kag_cm()

label kag_hn_b5_choices_hn02:
    $ kag_set_bookmark('はなシナリオ選択肢02')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】どれみちゃん', current_stem='hn_b5', storage=None, target='*choices_hn02-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】ハナちゃん', current_stem='hn_b5', storage=None, target='*choices_hn02-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_hn_b5_choices_hn02__dash__1:
    $ kag_f.judgeflag=0
    jump kag_hn_b5_after_choices_hn02
    call kag_s_wait

label kag_hn_b5_choices_hn02__dash__2:
    $ kag_f.judgeflag += 1
    jump kag_hn_b5_after_choices_hn02
    call kag_s_wait

label kag_hn_b5_after_choices_hn02:
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    "あれ？誰だっけ？"
    extend "思い出せない。"
    $ kag_cm()
    $ kag_set_next_indent('？？？「')
    "？？？「やっぱりいないじゃない」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('up', 'bg012', time_ms=2000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハア、ハア、コホンッコホンッ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしにだって、お友だちくらい……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……………………」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('down', 'black', time_ms=500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b5_hn__dash__05_04:
    $ kag_set_bookmark('「５日目」ひとりぼっちのＭＡＨＯ堂')
    $ kag_cm()
    $ kag_playse('6-0624.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……？」"
    $ kag_cm()
    $ kag_playse('6-0625.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「大丈夫。{w=0.4}りずむはひとりじゃないよ。{w=0.4}ハナちゃんがいっしょだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0626.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「タオルもかえて、これでよし、っと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b5_hn__dash__05_05:
    $ kag_set_bookmark('「５日目」ひとりぼっちのＭＡＨＯ堂')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    "ここは魔女界にあるわたしの部屋……。じゃなくて、ＭＡＨＯ堂だ。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ、夢だったんだ」"
    $ kag_cm()
    $ kag_sound_se('se-006.1', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0627.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あぁーーーー！{w=0.4}りずむが起きた！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m14', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0628.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0629.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、りずむ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハ、ハナちゃん？」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0630.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇー！{w=0.4}りずむ、元気になった？{w=0.4}元気になった！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}だいぶよくなりました」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0631.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん、い～っぱい心配したんだよ～！{w=0.4}りずむ、ずっと眠ったまんまで……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ？」"
    $ kag_cm()
    "わたしのまくら元を見ると、そこにはぬれタオルが落ちている。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「これって……{w=0.6}ハナちゃんが……？」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0632.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、ありがとう」"
    $ kag_cm()
    $ kag_sound_se('se-006.1', buf=1)
    $ kag_drawchar('d_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1119.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あっ！{w=0.4}やっぱり、りずむちゃん起きてる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃん、どうして見習い服着てるのかな？"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0635.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、もう平気なの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}おかげさまで」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0992.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そらよかったな～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0772.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ほんと、よかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1120.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だいぶ、顔色もよくなったみたいだしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさんありがとうございます。{w=0.4}ご心配おかけしました」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0993.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何言うてんの。{w=0.4}困った時はおたがい様やって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ところでどれみちゃん。{w=0.4}\nどうして見習い服なんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1121.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ドキッ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0634.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ、まだパジャマ姿なんだよ～。{w=0.4}ねっ、どれみ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1122.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0685.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん、朝にパジャマでＭＡＨＯ堂に来てから、{w=0.4}家に戻ってないのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええっ！」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0994.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんでな、なんぼなんでもそのカッコはマズいから、{w=0.4}せめて見習い服にでも～って話になってな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0636.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それで、今日はず～っとどれみちゃん、{w=0.4}見習い服なんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみません、わたしのせいで」"
    $ kag_cm()
    $ kag_drawchar('d_m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1123.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いいって、いいって！{w=0.4}そんなこと気にしなくて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん、ありがとう」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg015', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b5_hn__dash__05_06:
    $ kag_set_bookmark('「５日目」ひとりぼっちのＭＡＨＯ堂')
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0635.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「よかったね、{w=0.4}りずむ元気になって！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんたちのおかげです」"
    $ kag_cm()
    $ kag_playse('6-0636.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへ～、そんなこと気にしなくていいよ！{w=0.4}だって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だって？」"
    $ kag_cm()
    $ kag_playse('6-0637.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむは友だちだもん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん……{w=0.55}はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hn5_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hn_b6_gamestart
    return
