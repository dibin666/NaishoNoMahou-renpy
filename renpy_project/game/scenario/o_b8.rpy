# Auto-generated from 04. onpu/o_B8.ks by tools/transpile_ks.py
label kag_o_b8:

label kag_o_b8_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_onpu.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg016', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_o_b8_op__dash__08_00:
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "今日のお仕事もようやく終わり。"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0822.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃ、おつかれさま～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0548.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「おつかれさま、また明日ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0805.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おつかれさ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0247.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おつかれ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0277.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「みんな、バイバ～イ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ？おんぷちゃん、みんなといっしょに帰らないんですか？」"
    $ kag_cm()
    $ kag_playse('4-0507.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ねぇりずむちゃん、{w=0.4}よかったら今夜、うちに泊まりに来ない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_playse('4-0508.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ママに話したら、ぜひいらっしゃいって。{w=0.4}どう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。{w=0.4}わかりました」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0509.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「決まりね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、でも……{w=0.55}準備ってどうすればいいのかな？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0510.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「別に何もいらないわよ。{w=0.4}あ、パジャマとか持ってく？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃあ、ちょっと待っててください！{w=0.4}すぐに準備するから」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0511.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あわてなくてもいいわよ～{w=0.5}って、聞こえてないかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg097', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b8_op__dash__08_01:
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、誰かの家にお泊まりするのって初めてなんです」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0512.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうなんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ＭＡＨＯ堂みたいな所に、いそうろうなんてするのも初めてでしたけどね」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0513.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ、{w=0.4}この８日間初めてばっかりだったんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}人間界の学校に行ったり、おんぷちゃんのライブを見に駅前に行ったり、{w=0.4}海を見に行ったり、ラジオの収録スタジオに行ったり……{w=0.5}あれ、全部初めてかも」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0514.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。{w=0.4}わたしといっしょにいたから、毎日めまぐるしかったでしょ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「確かに、{w=0.4}いろんな所に行って、いろんな人に会って、{w=0.4}とてもめまぐるしかったです。{w=0.4}でも」"
    $ kag_cm()
    $ kag_playse('4-0515.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「毎晩寝る前に、明日は何が起こるんだろうって、{w=0.4}ずっとわくわくしてました」"
    $ kag_cm()
    $ kag_playse('4-0516.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "わたしがこんな風に考えられる様になったのは、おんぷちゃんのおかげ。"
    $ kag_cm()
    "でも、明日になったら、わたしは魔女界に帰る。"
    $ kag_cm()
    "そうしたら、いつものわたしに戻っちゃうのかな……？"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0517.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、そろそろつくわよ……{w=0.55}ほら、ここがわたしのお家」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg038', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b8_op__dash__08_02:
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おしゃれなお家ですね」"
    $ kag_cm()
    $ kag_playse('4-0518.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうかな？{w=0.4}わたしは見なれてるからわかんないけど。{w=0.4}さ、入って入って」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg039', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b8_op__dash__08_03:
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0519.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ただいま～{w=0.4}りずむちゃんも来たわよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    "どこからも返事はなかった。"
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0520.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あれ？{w=0.4}おかしいな……{w=0.55}ママったらまだ帰ってきてないのかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どこかにおでかけでしょうか？」"
    $ kag_cm()
    $ kag_playse('4-0521.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うーん、そんなはずはないんだけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg039', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0522.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「おかしいなあ……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あれ、メモが置いてある」"
    $ kag_cm()
    $ kag_playse('4-0523.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ホントだ。{w=0.4}なんだろう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0524.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「『おんぷちゃん、りずむちゃん、ごめんなさい。{w=0.4}急な打ち合わせで遅くなります。{w=0.4}夕飯はお寿司を頼んだので、２人で食べてちょうだいね』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0525.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「だって。{w=0.4}りずむちゃん、ママ遅くなるんだって。{w=0.4}とりあえずごはんにしましょうか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃんのママもいそがしそうですね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('4-0526.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いつものことだから、仕方ないけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "おんぷちゃんが、桶をテーブルに運んできた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、これは？」"
    $ kag_cm()
    $ kag_playse('4-0527.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お寿司よ。{w=0.4}あ、そうか、りずむちゃんお寿司を食べるのって初めてなんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}この桶の中に、食べ物が入ってるんですか？」"
    $ kag_cm()
    $ kag_playse('4-0528.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうよ。{w=0.4}ほら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ホントだ……{w=0.55}ちょっとすっぱいにおいがしますね」"
    $ kag_cm()
    $ kag_playse('4-0529.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「酢飯っていって、ご飯とお酢を合わせてあるから、{w=0.4}そのせいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんかお寿司を見てたらわたし、{w=0.4}おなかがすいてきました」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0530.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ、それじゃすぐにしたくするから、{w=0.4}ちょっと待ってて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg037', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b8_op__dash__08_04:
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おいしいです！」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0531.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフフ、よかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「この、イクラっていうのが乗っかってる……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0532.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「軍艦巻きね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そう、あ、この玉子焼きもおいしいです！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こっちのはなんですか？」"
    $ kag_cm()
    $ kag_playse('4-0533.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ウニが乗ってるのよ。{w=0.4}ちょっとわたしは苦手だけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれどれ。{w=0.4}あ！おいしいです～」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0534.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、まるで外国の人みたいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0535.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お寿司は日本の食べ物だから、{w=0.4}外国の人にも人気があるのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔女界にもあるのかも知れないけど、{w=0.4}わたしは初めてです」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0536.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「こっちのトロもおいしいわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントですか？{w=0.4}どれどれ……」"
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_freeimage(layer='0', page='fore')
    "ぱくっ"
    $ kag_cm()
    "つーん"
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}か、から―！」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0537.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ああ、ワサビね。{w=0.4}フフフ。{w=0.4}そんなにからかった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "からいのからくないのってそれはもう。"
    extend "わたしは涙と鼻水の洪水で、おんぷちゃんに答えるどころじゃなかった。"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0538.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、はい、お茶」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとう……」"
    $ kag_cm()
    $ kag_playse('4-0539.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「熱いから気をつけてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}ふう～」"
    $ kag_cm()
    $ kag_playse('4-0540.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「先に言っておけばよかったわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしてこんなにからいのが入ってるんですか？」"
    $ kag_cm()
    $ kag_playse('4-0541.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うーん。{w=0.4}大人の味っていうか、入っていた方がおいしいからじゃないかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃんは平気なんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0542.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なれちゃえばどうってことないわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うーん……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0543.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ダメならワサビはずす？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいえ！{w=0.4}チャレンジします！」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0544.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そんなにがんばるものじゃないと思うんだけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "ぱくっ"
    $ kag_cm()
    "つーん"
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}△□○☆◎！！」"
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0545.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「だ、大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.65}さっきよりは」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0546.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう。{w=0.4}それじゃわたしも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ぱくっ"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('4-0547.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……{w=0.6}△□○☆◎！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、おんぷちゃん？」"
    $ kag_cm()
    "わたしはあわてておんぷちゃんにお茶をついだ。"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0548.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「これはさすがに、ちょっとききすぎかもね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おいしいんですけどね」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg037', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b8_op__dash__08_05:
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0549.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……{w=0.4}ふぅ、おなかいっぱいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしもちょっと食べ過ぎちゃいました」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0550.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ、それじゃあ、{w=0.4}少しおちついたらお風呂にしましょうか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですね」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg037', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b8_op__dash__08_06:
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしのお部屋も、おんぷちゃんのお部屋みたく明るい感じにしようかな」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0552.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんはどんな感じのお部屋が好き？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしは、今のＭＡＨＯ堂みたいなのが好きですね。{w=0.4}あれはマジョリカさんの趣味ですよね」"
    $ kag_cm()
    $ kag_playse('4-0553.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ちがうわ。{w=0.4}ハナちゃんが自分の魔法で作り変えたのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんが？{w=0.4}すごい」"
    $ kag_cm()
    $ kag_playse('4-0554.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「１番最初のＭＡＨＯ堂は、{w=0.4}いかにも魔女がいそうな、ものすごく暗い感じでね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0554.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それをどれみちゃんとはづきちゃんとあいちゃんが、明るい感じに改装したのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんだ。{w=0.4}わたしがふだん働いている所もちょっと暗い感じで、本とか書類とか山積みで、{w=0.4}もうすこし明るくてきれいな所だったらって思ってるんですけどね」"
    $ kag_cm()
    $ kag_playse('4-0555.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんは、お城で働いてるのよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0556.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「だったら、お城を明るく改装しちゃえばいいじゃない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ！{w=0.4}そんなことしたら……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0557.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「怒られる？{w=0.4}でも、自分がやってみたいって思ったことだったら、{w=0.4}始めからやらないよりはやってみたら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_cm()
    $ kag_playse('4-0558.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしはね、いろんなことができるんじゃなくて、いろんなことがしたい。{w=0.4}それだけなの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}ほかのみんなも、そうなんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0559.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「きっとそうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('4-0560.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ねぇ、ちょっと付きあってほしいところがあるんだけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、どこですか？」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0561.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お散歩」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "おんぷちゃんは、だまって窓の向こうを指さした。"
    $ kag_cm()
    "窓の外には、夜の町並みが広がる。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg058', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b8_op__dash__08_07:
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うわぁ……」"
    $ kag_cm()
    $ kag_playse('4-0562.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「風が気持ちいいわね」"
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    "見おろす町明かりは、夜空の星が鏡に写ったかのようだ。"
    $ kag_cm()
    $ kag_playse('4-0563.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「この景色、りずむちゃんにも見せたかったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、よくこうやってお散歩してるの？」"
    $ kag_cm()
    $ kag_playse('4-0564.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。{w=0.4}たまに、お仕事でつらいことや、悲しいことがあったりした時によく来るかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0565.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「これがわたしのストレス発散なのかもね、{w=0.4}フフッ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こんなきれいな景色を見たら、悲しいことなんて忘れちゃいそうですね」"
    $ kag_cm()
    $ kag_playse('4-0566.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ホントはね、{w=0.4}いろんなことをして、失敗したり怒られたりして、{w=0.4}もうお仕事なんてやめたいって思ったこともあるの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ……」"
    $ kag_cm()
    $ kag_playse('4-0567.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ＭＡＨＯ堂のお手伝いも、めんどくさいって思ってた。"
    $ kag_playse('4-0567.2', buf=0, loop=False)
    extend "なんでみんなこんなことするんだろうって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('4-0568.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしね、{w=0.4}魔女見習いになったばかりの頃は、魔法って便利で、なんでもできるって思ってた」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0568.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「だから、人の気持ちを変える魔法なんかも使ってたわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それって禁断の……」"
    $ kag_cm()
    $ kag_playse('4-0569.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん。{w=0.4}その頃は、今みたく親しい友だちもいなくて、{w=0.4}どんなことでも魔法を使って解決してて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0570.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「きっとよくないことがおこるって、どれみちゃんたちに言われていても、{w=0.4}かまわず使ってたわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃんたちは、友だちじゃなかったんですか？」"
    $ kag_cm()
    $ kag_playse('4-0571.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしにとっては、だけどね。{w=0.4}友だちなんていらないって思ってたし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな……」"
    $ kag_cm()
    $ kag_playse('4-0572.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ファンのみんなだって、ホントのわたしなんて誰にもわからないんだから、{w=0.4}テキトーにやっておけばいいんだし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0573.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「魔法でわたしの人気が上がるように、{w=0.4}みんなの記憶を変えたっていいんだし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、それはちがうと思います」"
    $ kag_cm()
    $ kag_playse('4-0574.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん、わたしもそう思う」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_playse('4-0575.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんは、どうしてそう思うの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)

label kag_o_b8_choices_op03:
    $ kag_set_bookmark('おんぷシナリオ選択肢03')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】禁断の魔法だから', current_stem='o_b8', storage=None, target='*choices_op03-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】意味がないから', current_stem='o_b8', storage=None, target='*choices_op03-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_o_b8_choices_op03__dash__1:
    $ kag_cm()
    $ kag_f.event_04=0
    $ kag_f.judgeflag=0
    $ kag_playse('4-0576.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……{w=0.25}そうね。{w=0.4}その通りよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('4-0577.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんたちにも、同じことを言われてたしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_o_b8_after_choices_op03
    call kag_s_wait

label kag_o_b8_choices_op03__dash__2:
    $ kag_cm()
    $ kag_f.event_04=1
    $ kag_f.judgeflag += 1
    $ kag_set_next_indent('りずむ「')
    "りずむ「その時は、それでいいのかもしれないですけど、{w=0.4}おんぷちゃんが何も変わらなかったら、結局は……」"
    $ kag_cm()
    $ kag_playse('4-0578.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう。{w=0.4}同じことのくり返しよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.55}どれみちゃんたちに、{w=0.4}それを教わったって言いましたよね」"
    $ kag_cm()
    $ kag_playse('4-0579.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_o_b8_after_choices_op03
    call kag_s_wait

label kag_o_b8_after_choices_op03:

label kag_o_b8_op__dash__08_08:
    $ kag_set_bookmark('「８日目」りずむ')
    $ kag_cm()
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('cross', '04おんぷ-08', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgo5=1
    $ kag_mesframe()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それって、なんですか？」"
    $ kag_cm()
    $ kag_playbgm('bgm-v04', loop=True)
    $ kag_playse('4-0580.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「大したことじゃないのよ。{w=0.4}ただ『友だちだから』って。{w=0.4}そう言われたわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.6}それだけ……{w=0.5}ですか？」"
    $ kag_cm()
    $ kag_playse('4-0581.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう。{w=0.4}それってすごいことじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('4-0582.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「たったそれだけで、{w=0.4}協力しあったり、時には誰かを助けたり、{w=0.4}本気で言いあったり」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0583.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃんたちに会うまで、{w=0.4}わたしはそんなこと考えもしなかった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それは、わたしも……{w=0.55}です」"
    $ kag_cm()
    $ kag_playse('4-0584.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「今でも？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「今はちがいます。{w=0.4}ただ、魔女界に帰ったら同じなのかなって……」"
    $ kag_cm()
    $ kag_playse('4-0585.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃんが同じだって思うなら、同じよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_playse('4-0586.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「だったら、逆のことだってあるんじゃないかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしが、ちがうと思ったらちがう……？」"
    $ kag_cm()
    $ kag_playse('4-0587.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そう。{w=0.4}何だか魔法みたいだけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そのために、わたしを散歩にさそってくれたんですか？」"
    $ kag_cm()
    $ kag_playse('4-0588.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「少しは気分変わった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg058', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "わたしはあらためて夜景を見わたす。"
    $ kag_cm()
    "ひとつひとつの明かりは、誰かの明かり。"
    $ kag_cm()
    "そのひとつひとつが、わたしと同じようになやんだり、かなしんだり……"
    $ kag_cm()
    "今はそうかもしれないけど、きっと明日はよろこんだり、笑ったりできるかもしれない。"
    $ kag_cm()
    "だってこの夜の景色も、かならず朝に変わっていくんだから。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '04おんぷ-08', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_playse('4-0589.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「やっぱり、おんぷちゃんってすごいです」"
    $ kag_cm()
    $ kag_playse('4-0590.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どうして？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だって、明日魔女界に帰ったら、{w=0.4}本当にちがうんじゃないかって思えたから」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、ありがとう」"
    $ kag_cm()
    $ kag_playse('4-0591.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そろそろ戻りましょうか。{w=0.4}寒くなって来ちゃったし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.2}はい」"
    $ kag_cm()
    "おんぷちゃんの表情は、とてもやさしかった。"
    extend "だから、もう少し夜景をみていたかったけど、戻ることにした。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.o8_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_o_c_gamestart
    return
