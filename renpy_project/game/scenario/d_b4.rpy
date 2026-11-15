# Auto-generated from 01. doremi/d_B4.ks by tools/transpile_ks.py
label kag_d_b4:

label kag_d_b4_gamestart:
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

label kag_d_b4_d__dash__04_00:
    $ kag_set_bookmark('「４日目」みんなのまほう？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0234.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日はお客さんこないねぇ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_playse('1-0235.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「今日もあついねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0081.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「こうあついと、お客さんどころか、外に歩いている人がおらんな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0236.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ねえ、こっちのうちわ、もう乾いたんじゃないかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0056.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ダメよ、まだ生乾きだと思うわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0237.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いいっていいって、こうやってあおげばその分早く乾いちゃって、一石二鳥さあ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0082.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「今日あついのを見こして、手作りうちわをこしらえたのはええアイデアやってんけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0057.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「暑すぎて、誰も来なかったのは盲点よね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おまけに、みんなの分だけ作って力つきましたね……」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0045.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇねぇ～どれみ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0238.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どしたの？ハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0046.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あのね、ハナちゃんね、海に行きたい～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0239.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0058.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でも、まだお仕事が終わってないし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0083.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「う～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0059.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「まだお昼過ぎたばっかりで、閉店までには早いよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0084.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「う～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0066.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お客さんが来なくても、お店は開けておかないと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0085.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「う～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0047.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃん海に遊びにいきた～い！{w=0.3}ね、りずむは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.3}わ、わたしですか？」"
    $ kag_cm()
    $ kag_playse('6-0048.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「いっしょにお砂でお城つくろ～よ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0086.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「う～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0240.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う～んってあいちゃん、\nさっきからうなってどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0087.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「よっしゃ決めた！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0241.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「わあ、びっくりした」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0088.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「海いくで～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0049.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わ～い！さすがあいこ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0242.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あいちゃん……{w=0.6}海って……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0089.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「しゃあ～らっぷ！どれみちゃん！！{w=0.3}ええか、よう考えてみ。{w=0.45}あたしらまだ小学生やで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0243.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0090.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「来年は中学！{w=0.33}中学生になったら今にもまして勉強せなあかん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0244.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0091.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それやったら今のうち思いっきし遊ばんと！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0245.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0092.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それにな、今は夏休みや！夏休み！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0246.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0093.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「休みやのに、なんではたらかなあかんねん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0247.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うんうん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0094.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「マジョリカと来たら、あたしらほうっとって温泉やで！温泉！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0248.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん！うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0095.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「せやから……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0249.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「せやから？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0096.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「海にいって思いっきりあそぼ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0250.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg080', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('se-014', loop=True)

label kag_d_b4_d__dash__04_01:
    $ kag_set_bookmark('「４日目」みんなのまほう？')
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0050.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「わ～い！うっみ！{w=0.35}うっみ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ～風が気持ちいい～」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0251.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ほんとだね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0067.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、海は初めて？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.3}本で見たことはあったんですけど、波の音とかすごいですね」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0060.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「冬とかはもっとすごいんだよ！{w=0.45}こう、ドドーンって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ～！{w=0.3}そうなんですか？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0061.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！{w=0.45}それで、あそこのガケっぷちで着物を着て、演歌を歌うんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは……{w=0.6}何かの行事なんですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0059.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん、そんな行事ないわ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0068.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「演歌は海って決まってるわけでもないし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0051.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「よ～し！{w=0.4}ハナちゃんさっそく、お城作る！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0060.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「じゃあわたしも手伝ってあげるわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0052.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0252.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もう、ハナちゃんはしゃぎすぎだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0069.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「まぁまぁ、ハナちゃん、きっとうれしいのよ。{w=0.35}久々にみんなで遊べて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0053.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ぎゃあああ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0062.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ほんと、ぎゃあああ～とか言ってるし～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0253.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだね！{w=0.4}ぎゃあああ～って叫ぶぐらいうれしいんだね……{w=0.45}って、"
    $ kag_drawchar('d_05.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('1-0253.2', buf=0, loop=False)
    extend "『ぎゃあああ』っていったい！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg082', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0097.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃん、はづきちゃん、どないしたん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0254.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん！{w=0.4}大丈夫！？{w=0.4}どこもけがしてない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0054.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん、だいじょうぶだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いったいどうしたの？はづきちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0061.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それがね。…みんな見て、まわりを」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0063.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「まわりって……{w=0.6}{nw}"
    $ kag_drawchar('m_06.tlg', time_ms=100, sepia=False, canskip=True)
    extend "あっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "砂浜には、ゴミがあちこちに散らかっていた。"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0255.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うっわ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0098.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「海に捨てられたゴミがうちあげられてんねんな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0062.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「これじゃ、とても遊ぶどころじゃないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0064.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「アレとか、タンスだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いくらなんでもひどいわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、だったらわたし、魔法で砂浜をきれいにします」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0256.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうだね。{w=0.4}\nパパーッとやっちゃってよ、りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「あら、みなさんおそろいでどうしたんですの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0065.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あ、玉木さん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0257.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「げ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0062.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「っ！」"
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0098.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「っ！」"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0071.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「っ！」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0054.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「砂浜よ、きれいに……」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0258.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ダメええ～っ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}わわっ！どれみちゃん？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('？？？「')
    "？？？「……」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0259.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あははは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0260.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「玉木がいるんだから、魔法はダメだよ。{w=0.4}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「玉木……{w=0.55}さん？」"
    $ kag_cm()
    $ kag_drawchar('t_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「何ですの？今の呪文みたいな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0066.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ななな、何でもない、何でもない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0099.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやそや。{w=0.4}な？おんぷちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「え？{w=0.65}ええ、そうよ。{w=0.4}ね？はづきちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0063.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「え？{w=0.65}わたし？{w=0.4}あああの、その……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0003.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「な～んか怪しいですわね～？{w=0.5}砂浜がなんとかっておっしゃってませんでした？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0067.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「すすす、砂浜がきれいにならないかなって、言ってたの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0261.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうそう！そうなんだよ！{w=0.65}ね？{w=0.5}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？……{w=0.65}はい」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('t_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「そうでしたの？……{w=0.55}まあ、いいですけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0262.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ところでぇ～、{w=0.3}\nところで玉木はどうしてこんな所にいるのさぁ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「新学期の校内新聞に使う景色を探してたんですのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0068.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あれ？{w=0.4}玉木さん、新聞委員じゃないよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「島倉さんが、どうしてもワタクシを表紙にかざりたいっておっしゃるから、{w=0.5}こうしてワタクシにふさわしい景色はないかとさがしてるんですのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0100.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なんや、そういうことか……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「シンガッキ？"
    extend "コウナイシンブン？」"
    $ kag_cm()
    $ kag_drawchar('t_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「こちらの方は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0263.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「この子はりずむちゃん。{w=0.4}ハナちゃんの親戚で、遊びに来てるんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はじめまして」"
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0008.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「はじめまして。{w=0.4}ワタクシは玉木麗香。{w=0.55}春風さんたちのクラスメートですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よろしくおねがいします」"
    $ kag_cm()
    $ kag_playse('8-0009.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「それで、みなさん海水浴にでもいらしたのかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0264.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「っていうか、あついから涼みに来ようかな～って思ってさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0055.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんお砂でお城を作りに来たの！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「な、なるほど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0101.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「でもこんな砂浜が汚れてたら、涼むどころじゃないな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0011.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「そうですわね。{w=0.5}海辺だったらワタクシの美貌も引き立つかと思ったんですけど……{w=0.5}ハァ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だから、片づけようかなって思ったんですけど……」"
    $ kag_cm()
    $ kag_drawchar('t_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「こんなに散らかってるんですのよ？{w=0.4}無理に決まってるじゃありませんの！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0265.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんなで手分けすれば、あそこの岩場あたりまでならできるんじゃないかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0069.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん、そうだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ムリムリ。{w=0.4}ムダですわよ、そんなこと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0064.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「でも、ほんのちょっとでもきれいになれば、ムダってことはないんじゃないかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0102.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そや。{w=0.5}まあ、ムリに手伝って～とは言わへんけどな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「新学期の校内新聞に使うんじゃなかったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0014.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「そんなの、ここじゃなくってもワタクシにお似合いな景色なんて山ほどありますわ。"
    $ kag_playse('8-0014.2', buf=0, loop=False)
    extend "みなさんだけでお好きにやればいいじゃありませんの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.7}あの」"
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0015.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「？何ですの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「玉木さんって……{w=0.65}人間ですよね？」"
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('t_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0016.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「んな！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0266.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そ、そんなのあたりまえじゃ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0017.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ぬぬぬ……{w=0.55}巻機山さんの親戚だけあって、失礼なところはそっくりですわね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0056.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「む！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0018.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あなたたちと話していると、失礼がうつりますわ。{w=0.3}\nそれじゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0267.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「行っちゃった……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0065.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「仕方ないわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0268.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんダメじゃ～ん！{w=0.45}もし魔女だってバレたら、魔女ガエルになっちゃうよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみません。{w=0.5}ちょっと魔女に似てるかなって、思って……」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0269.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へ？{w=0.4}玉木に似た魔女がいるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ、その……」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0103.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それにしても、『人間ですか？』って聞かれたときの玉木の顔、おもろかったな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「普通、聞かれないからね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「悪いことしちゃいましたね」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0270.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どうせ玉木だし、気にしなくていいよ。{w=0.3}\nそれじゃ、ゴミ拾いしよっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg083', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b4_d__dash__04_02:
    $ kag_set_bookmark('「４日目」みんなのまほう？')
    $ kag_cm()
    "みんなちりぢりに、ゴミ拾いをはじめて１時間くらいがたった。"
    $ kag_cm()
    "流れ着いた木の枝とか、空き缶とかを拾い集める。"
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいたた……{w=0.5}ずっとかがんでいたら、腰が痛いですね」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0271.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホントだよね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それにしても、いろんな物が落ちてますね」"
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0272.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんかこう、金銀財宝とかおっこちてたらいいのにね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふ、わたしさっききれいなビン拾っちゃいました」"
    $ kag_cm()
    $ kag_playse('1-0273.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホント～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.45}けっこうこった作りだったんで、気に入っちゃいました」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0274.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「雑貨ショップ店員らしくなってきたねえ。{w=0.4}ね、見せてよそのビン」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「これです」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('どれみ「')
    "どれみ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「中にガラス玉が入っていて、ちょっと珍しいですよね」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0275.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「これ、ラムネの空きビンじゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？こっちでは普通なんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0276.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん～まぁ、わりとね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0277.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だったら、帰るときのおみやげにしたらいいんじゃないかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そうか。{w=0.3}そうですよね」"
    $ kag_cm()
    $ kag_playse('1-0278.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしもアクセサリーに使えそうな物さがそうかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}これは？」"
    $ kag_cm()
    "足もとに落ちている、ビニール袋のような物体をつつく。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}ぷにぷにしてる。{w=0.3}なんだろうこれ？」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0279.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それはクラゲだよ。{w=0.3}一応生き物なんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へええ、そうなんですか……」"
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0019.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「まったく、クラゲも知らないなんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！玉木さん……」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0280.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「玉木？{w=0.35}帰ったんじゃなかったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0020.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ゴミを拾わないからって、人間扱いされないんじゃたまらないですもの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ご、ごめんなさい！ちょっと、その、言い方が……」"
    $ kag_cm()
    $ kag_drawchar('t_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「冗談ですわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_playse('8-0022.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「わざわざイナカから出てきた方に、この町の砂浜のゴミ拾いをさせるのは、児童会長として見るに忍びないですから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうございます」"
    $ kag_cm()
    $ kag_drawchar('t_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0023.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「べ、別に、りずむさんにお礼を言われる覚えはありませんわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0281.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃ、あとちょっとがんばろうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg217', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b4_d__dash__04_03:
    $ kag_set_bookmark('「４日目」みんなのまほう？')
    $ kag_cm()
    "玉木さんが手伝ってくれたおかげもあって、砂浜のゴミ拾いは思ったよりも早く終わった。"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ありがとう、玉木さん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0024.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「これくらい当然ですわ。{w=0.5}それじゃワタクシはこのへんで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お疲れさまでした」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「玉木さん、やさしいよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですね」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0282.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんだかんだ言ってもね……{w=0.75}あれ、ハナちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0066.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あっちでお城作ってるわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0283.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ホントだ。{w=0.45}あれ？ぽっぷもいる」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0104.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ゴミ拾いが自由研究の課題に使えそうや～言うて、途中から手伝ってくれてん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0284.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「しまった！その手があったか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0105.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「２年生と同じ研究してどないすんねんな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ねえ、これ見て。{w=0.3}アクセサリーに使えそうじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0106.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うわぁ～。{w=0.35}きれいな石やな～。{w=0.55}あたしはさっき岩場の方でガラス玉拾てん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0067.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしも小ビンを見つけたわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0285.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんな仕事熱心だね。{w=0.4}さっきりずむちゃんも、ラムネのビンひろってたし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0107.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ホンマ？{w=0.3}みしてみして」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、これですけど」"
    $ kag_cm()
    $ kag_playse('3-0108.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うわ～。なつかしい～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0068.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「最近見かけないわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「この取れそうで取れないビー玉がポイントよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「人間界ではあまり珍しくないみたいなんで、わたしのおみやげにしようかなって思ってるんですけど」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0109.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな。{w=0.4}売り物にはなれへんけど、宝物にはなるやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0069.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ゴミばっかりかって思ってたけど、けっこう役に立ちそうな物ってあるわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0286.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「こうしちゃいられないよ。\nあたしもなんか見つけなきゃ！{w=0.3}ええと～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0286.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「アクセサリーに使えて、自由研究の課題にも使えそうな奴落ちてないかな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんったら……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0110.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんな都合のええモン見つかるはずないやろ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん……{w=0.6}行っちゃったわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしも、探してみます」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg083', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m60', loop=True)

label kag_d_b4_d__dash__04_04:
    $ kag_set_bookmark('「４日目」みんなのまほう？')
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0287.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ねえ、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0288.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「さっき言ってた、玉木が魔女に似てるって……{w=0.5}あれ、なんだったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？ああ……仕事場の先輩魔女でよく似た人がいるんで……{w=0.65}ちょっととっつきにくい感じで、正直言って苦手なんです」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0289.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まあ、魔女って気むずかしい人が多いからね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そう思ったらなんか、玉木さんが魔女みたく見えちゃって」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0290.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「玉木の場合、気むずかしいって言うより、自分勝手なだけなんだけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}それは、魔女だっていっしょかも知れないです」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0291.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔女界でのお仕事で、わたしは自分が失敗しないようにってことだけしか考えてなかったし……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「先輩魔女たちも自分の仕事さえうまくいけばいいって思ってたみたいだし……」"
    $ kag_cm()
    $ kag_set_next_indent('どれみ「')
    "どれみ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お互いが自分のことだけ考えてたら、うまくいかないんだなって」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0292.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「マジョリカも最初、そんな感じだったな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0293.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしが魔女だ～って言っちゃって、魔女ガエルになっちゃって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0293.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それからは早く元の姿にもどせ～もどせ～\n一人前の魔女になれ～ってうるさくってさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そりゃまあ、魔女ガエルになっちゃったんなら……」"
    $ kag_cm()
    $ kag_drawchar('d_12.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0294.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それで自分だけ温泉に行っちゃったりするんだよ？{w=0.4}\nそれも１度や２度じゃないんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0294.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おまけに修学旅行についてきちゃったりさ。{w=0.45}そりゃもうひどいったらありゃしない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あはは……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0295.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「でもね、あたしたちが困ったとき助けてくれたり、相談に乗ってくれたりするから、けっこう頼りにもしてるんだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0296.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんの先輩魔女だって、実はいいところあるかもしれないじゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}そうでしょうか」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0297.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あるよ、きっと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……」"
    $ kag_cm()
    $ kag_playse('1-0298.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃ、そろそろ戻ろっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん」"
    $ kag_cm()
    $ kag_playse('1-0298.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}ありがとう」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    "どれみちゃんは、返事の代わりに笑顔でこたえてくれた。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.d4_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_d_b5_gamestart
    return
