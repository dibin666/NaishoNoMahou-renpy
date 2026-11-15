# Auto-generated from 04. onpu/o_B7.ks by tools/transpile_ks.py
label kag_o_b7:

label kag_o_b7_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_onpu.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg001', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_o_b7_op__dash__07_00:
    $ kag_set_bookmark('「７日目」おんぷと魔法')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_playse('se-020.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=1)
    $ kag_drawchar('p_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0175.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「お姉ちゃ～ん、みんな～、来たよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0798.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おっ、ぽっぷちゃん、ゆかたよう似合てんで～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0176.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えへへ……{w=0.55}あいちゃんありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0177.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あれ？{w=0.4}もう、まだ片づけ終わってないの～。{w=0.4}早く行こうよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "今日は夏祭りの日。"
    extend "お店が終わったら、みんなで遊びに行くことになっていたんだけど、閉店まぎわまでお客さんがけっこういたので、お掃除が遅れてしまっていた。"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0816.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ごめんごめん。{w=0.4}ぽっぷ、ちょっと掃除手伝ってよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0178.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「え～っ！{w=0.4}せっかくきれいにゆかた着たのに、汚れちゃうじゃ～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0817.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まぁまぁ、ちょっとそのへんをほうきではくだけだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0179.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「もう～しょうがないなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg020', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b7_op__dash__07_01:
    $ kag_set_bookmark('「７日目」おんぷと魔法')
    $ kag_cm()
    $ kag_drawchar('o_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0473.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それじゃあ、いくね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m408d', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg404.tlg', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('4-0474.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「プルルンプルン　ファミファミファー」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0475.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんな、かわいいゆかた姿に、なれ～っ！」"
    $ kag_stopse(buf=0)
    $ kag_fadeoutbgm(1000)
    $ kag_cm()
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg020', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ……{w=0.65}これがゆかたですか～」"
    $ kag_cm()
    "ぽっぷちゃんが着ているのは、さっきから見ていたんだけど、\nじっさいに着てみると、なかなか不思議な着ごこちだ。"
    $ kag_cm()
    $ kag_drawchar('o_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0476.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、とってもよく似合ってるわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとうおんぷちゃん。{w=0.4}ちょっと照れくさいです」"
    $ kag_cm()
    $ kag_drawchar('o_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0477.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフフ。{w=0.4}それじゃあみんな、行きましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0040.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「お～っ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg075', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b7_op__dash__07_02:
    $ kag_set_bookmark('「７日目」おんぷと魔法')
    $ kag_cm()
    $ kag_playbgm('bgm-003', loop=True)
    "すっかり日も落ちて、暗くなった道をやって来たわたしたちは、夏祭りが行われている会場の入り口にたどり着く。"
    $ kag_cm()
    "会場内は、親子連れやカップル、友だち同士と、いろんな人でにぎわっている。"
    $ kag_cm()
    $ kag_stopse(buf=0)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ～、すごくにぎやかですねぇ～」"
    $ kag_cm()
    $ kag_drawchar('p_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0180.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「お姉ちゃん、{w=0.4}はぐれないように気をつけてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "人ごみはおんぷちゃんのミニライブの時にも体験したけど、夏祭りはそれとはまたちがったにぎやかさだ。"
    $ kag_cm()
    $ kag_drawchar('d_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0818.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どっちかっつーと、{w=0.4}はぐれるのはあんたの方でしょうが」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0181.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そんなことないもん！{w=0.4}お姉ちゃんがちゃんとついてこないからじゃない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_y_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0819.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃあ、どっちがお姉ちゃんかわからないじゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0182.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あはははは！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0543.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「２人とも、相変わらず仲いいわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0246.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「お祭りになるといっしょにはしゃぐところは、{w=0.4}さすが姉妹って感じだよね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0276.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇねぇ、早く行こうよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0799.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、めいっぱい遊ぶで～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0478.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、行きましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg076', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b7_op__dash__07_03:
    $ kag_set_bookmark('「７日目」おんぷと魔法')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん、{w=0.4}あの『金魚すくい』っていうのはなんですか？」"
    $ kag_cm()
    $ kag_drawchar('o_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0479.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あれは、すくい網で金魚をすくって、{w=0.4}網が破れるまでに取れた金魚がもらえるのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へええ～。{w=0.4}あの型抜きっていうのは？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg075', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('4-0480.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「つまようじで絵柄の形に型を抜くの。{w=0.4}途中で割れないようにきれいに抜けたら、景品がもらえるのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ん～。{w=0.4}何だか難しそうですね……」"
    $ kag_cm()
    $ kag_playse('4-0481.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん、手先は器用な方？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えーっと……{w=0.55}自分ではそこそこだとは思うんですけど……」"
    $ kag_cm()
    $ kag_drawchar('d_y_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0820.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どわぁっ！{w=0.4}また割れちゃったよ～トホホ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0183.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「お姉ちゃんヘタだなぁ。{w=0.4}あたしなんてカンペキだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0821.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぽっぷ、そのひょうたん、２つになってない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0184.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「え？{w=0.45}あああ～。{w=0.4}もう割れちゃってたんだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_drawchar('o_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0482.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん見て。{w=0.4}あっちであいちゃんたちがくじ引きやってるわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}あ、ホントだ」"
    $ kag_cm()
    "向かいの屋台ではあいちゃんがくじ引きのひもを選んでいる最中だった。"
    extend "どうやら、ひもを引くとかごの中にある景品のどれかがひっぱり上げられるようだ。"
    $ kag_cm()
    $ kag_drawchar('a_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0800.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「むむむむ……{w=0.6}神様仏様えびす様……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0544.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あいちゃん、気合いよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0801.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「これや！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_y_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0545.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ああ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0802.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あかん、またバトルレンジャーのカードセットや……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_y_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0546.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「さっきから３個目よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_y_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0803.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もう～おっちゃん！{w=0.4}これバトルレンジャー以外ホンマに当たるんかいな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おっちゃん「')
    "おっちゃん「てやんでい！{w=0.4}ハズレなしだつってんだろーが！{w=0.4}べらぼうめい！」"
    $ kag_cm()
    $ kag_drawchar('hz_y_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0547.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「……{w=0.25}確かに、ハズレじゃあないわよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0804.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それはそやねんけど……{w=0.55}まあ、こんだけあったらどれみちゃん喜ぶやろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0483.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あいちゃんも以外と、こういうの熱くなるのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふっ、そうですね」"
    $ kag_cm()
    $ kag_drawchar('o_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0484.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「もうちょっと真ん中の方に行ってみましょうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg072', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg072', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b7_op__dash__07_04:
    $ kag_set_bookmark('「７日目」おんぷと魔法')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何だか、こっちの方は特に人が多いですね……」"
    $ kag_cm()
    $ kag_drawchar('o_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0485.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「本当ね。{w=0.4}りずむちゃん、はぐれないように気をつけてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}あの、みんなは……？」"
    $ kag_cm()
    $ kag_playse('4-0486.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「花火を見る場所は決めてあったから、始まる時間になったら移動すればいいわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですね」"
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0084.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あら？{w=0.4}あなたは確か……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ」"
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0085.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「りずむさん……{w=0.5}でしたわよね？{w=0.4}学校で一度お会いした……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっと……{w=0.6}玉木さん。{w=0.4}こ、こんばんは」"
    $ kag_cm()
    $ kag_drawchar('o_y_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0487.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「玉木さんも来てたんだ。{w=0.4}何ていうか、と、とってもステキなゆかたね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0086.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「さすがは瀬川さん、わかってらっしゃる。{w=0.4}今日のために特別にあつらえた一流ブランドのゆかたですのよ。{w=0.4}やはりワタクシにはこれくらい豪華なゆかたでないと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、ハデですね……」"
    $ kag_cm()
    $ kag_playse('8-0087.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ワタクシの美しさが、このゆかたでさらに引き立つというものですわ。{w=0.4}オーッホッホッホッ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('通行人Ａ「')
    "通行人Ａ「なぁ、あれ見ろよ、すっげーゆかた……」"
    $ kag_cm()
    $ kag_set_next_indent('通行人Ｂ「')
    "通行人Ｂ「うわ、ハデ！{w=0.4}何だ、何かのイベントか？」"
    $ kag_cm()
    $ kag_playse('8-0088.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ああ、みなさんの視線が痛いですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('通行人Ｃ「')
    "通行人Ｃ「……{w=0.5}おい、あのハデなゆかたのとなりにいる子、あれって……」"
    $ kag_cm()
    $ kag_set_next_indent('通行人Ｄ「')
    "通行人Ｄ「……{w=0.45}おう、まちがいないよ、ぜってーそうだって……」"
    $ kag_cm()
    $ kag_playbgm('se-023.ogg', loop=True)
    "まわりがザワつき始めた。"
    extend "どうやら、玉木さんの話題ではないらしい。"
    $ kag_cm()
    $ kag_set_next_indent('通行人Ｅ「')
    "通行人Ｅ「あ、あの～、瀬川おんぷさん……{w=0.45}ですよね？」"
    $ kag_cm()
    $ kag_drawchar('o_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0488.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えっ……{w=0.6}あ、あの……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('通行人Ｅ「')
    "通行人Ｅ「やっぱりそうだ！{w=0.4}おいみんな！{w=0.4}おんぷちゃんがいるぞ！！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ……？{w=0.4}キャッ！？」"
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0089.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「な、なんですの！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('通行人Ｂ「')
    "通行人Ｂ「おんぷちゃ～ん」"
    $ kag_cm()
    $ kag_drawchar('o_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0489.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、えっと、ちょっと待ってくださ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('通行人Ｃ「')
    "通行人Ｃ「おんぷちゃん、サインください！」"
    $ kag_cm()
    $ kag_set_next_indent('通行人Ｄ「')
    "通行人Ｄ「おんぷちゃん、握手を……！」"
    $ kag_cm()
    "あたりは、あっという間に大混乱になってしまった。"
    $ kag_cm()
    $ kag_playse('4-0490.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、あの、みなさんちょっと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_drawchar('t_y_04.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('8-0090.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あなたたち、いいかげんになさい！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '04おんぷ-07', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgo4=1
    $ kag_mesframe()

label kag_o_b7_op__dash__07_05:
    $ kag_set_bookmark('「７日目」おんぷと魔法')
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_set_next_indent('通行人Ｅ「')
    "通行人Ｅ「な、なんだよ、おまえ……」"
    $ kag_cm()
    $ kag_playse('8-0091.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ワタクシは、児童会長玉木麗香！{w=0.4}\n瀬川さんの学友ですわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('8-0092.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あなたたち、瀬川さんが迷惑しているのがわかりませんの！？{w=0.4}そんなことでよく瀬川さんのファンだと言えますわね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('通行人たち「')
    "通行人たち「………………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「玉木さん……」"
    $ kag_cm()
    $ kag_playse('8-0093.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「それだけでなく、{w=0.4}あなたたちはお祭りを楽しんでいる他の方々にも大迷惑ですわ！{w=0.4}まったく……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0491.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんな、ごめんなさい！{w=0.4}今日はプライベートだから、握手とか、サインはできないの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん……」"
    $ kag_cm()
    $ kag_set_next_indent('ファンたち「')
    "ファンたち「お、おんぷちゃんがそう言うなら……」"
    $ kag_cm()
    "玉木さんとにらみ合っていたおんぷちゃんのファンたちも、"
    extend "おんぷちゃんが仕事で来ていないのだとわかると、ぞろぞろとちり始めた。"
    $ kag_cm()
    $ kag_playse('8-0094.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「まったく、ここにこれほどに美しいわたくしがいるというのに……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それはあんまり関係ないような……」"
    $ kag_cm()
    $ kag_playse('8-0095.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「何ですって？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、いえ……何でもないです。すみません」"
    $ kag_cm()
    $ kag_playse('4-0492.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「玉木さん。{w=0.4}ありがとう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('8-0096.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「べ、別に当然のことをしたまでですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「玉木さん、かっこよかったです」"
    $ kag_cm()
    $ kag_playse('8-0097.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ほ、ほら、{w=0.4}ボヤボヤしてるとまた誰かに見つかっちゃいますわよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0493.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。{w=0.4}行きましょう、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}玉木さん、それじゃ」"
    $ kag_cm()
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg249', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_o_b7_op__dash__07_06:
    $ kag_set_bookmark('「７日目」おんぷと魔法')
    $ kag_cm()
    $ kag_bgmopt(volume=None, gvolume=40)
    $ kag_playbgm('bgm-003', loop=True)
    $ kag_drawchar('o_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0494.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ここまで来れば大丈夫みたいね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「玉木さんのおかげで助かっちゃいましたね」"
    $ kag_cm()
    $ kag_playse('4-0495.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも、玉木さんがあんな目立つゆかたを着てなかったら、{w=0.4}わたしも気づかれなかったと思わない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……{w=0.6}そういえば」"
    $ kag_cm()
    $ kag_drawchar('o_y_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0496.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「玉木さんのせいでピンチになって、玉木さんに助けられちゃったわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「玉木さん、{w=0.4}あんなたくさんのファンの前で一歩も引かなくって、{w=0.4}かっこよかったです」"
    $ kag_cm()
    $ kag_drawchar('o_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0497.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうよね。{w=0.4}さすがは我らが児童会長さんよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふ。{w=0.4}ですね」"
    $ kag_cm()
    $ kag_playse('4-0498.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あんな騒ぎになっちゃ、{w=0.4}魔法を使うわけにもいかなかったしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('りずむ「')
    "りずむ「他の人にばれたら、魔女ガエルになっちゃいますからね。{w=0.4}……{w=0.55}人間界では、魔法って結構不便なのかな？」"
    $ kag_cm()
    $ kag_bgmopt(volume=None, gvolume=65)
    $ kag_playbgm('m42', loop=True)
    $ kag_playse('4-0499.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そんなことないわよ。{w=0.4}楽しいことを、魔法を使ってもっと楽しくできるじゃない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そう言えば……{w=0.6}このゆかたって、おんぷちゃんが魔法で出してくれたんですよね」"
    $ kag_cm()
    $ kag_drawchar('o_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0500.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ええ、だって夏祭りなんだから、ゆかたを着た方が気分がもりあがるじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そっか……{w=0.6}確かに、今日はとても楽しかったです」"
    $ kag_cm()
    $ kag_playse('se-038.1', buf=1, loop=False)
    if kag_get_skip_mode()!=0:
        $ kag_stopse(buf=1)
    $ kag_playse('4-0501.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わぁ～りずむちゃん、{nw}"
    $ kag_playse('se-038.1', buf=2, loop=False)
    if kag_get_skip_mode()!=0:
        $ kag_stopse(buf=2)
    extend "見て見て！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-038.2', buf=1, loop=False)
    if kag_get_skip_mode()!=0:
        $ kag_stopse(buf=1)
    $ kag_playse('se-038.1', buf=1, loop=False)
    if kag_get_skip_mode()!=0:
        $ kag_stopse(buf=1)
    $ kag_playse('se-038.3', buf=2, loop=False)
    if kag_get_skip_mode()!=0:
        $ kag_stopse(buf=2)
    $ kag_playse('4-0502.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「きれい～」"
    $ kag_stopse(buf=0)
    $ kag_playse('se-038.2', buf=1, loop=False)
    if kag_get_skip_mode()!=0:
        $ kag_stopse(buf=1)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ホントですね～」"
    $ kag_cm()
    $ kag_drawchar('o_y_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0503.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、いけない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？{w=0.4}どうかしましたか？」"
    $ kag_cm()
    $ kag_playse('4-0504.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「花火の時間までに、みんなとの待ち合わせの場所に行かなくっちゃ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わ、忘れてた……」"
    $ kag_cm()
    $ kag_playse('4-0505.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みんな心配してるかも。{w=0.4}確か花火はあっちで見ようって話してたような{w=0.4}……{w=0.55}あの人ごみを通るのはけっこう大変ね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん。{w=0.4}こんなときはやっぱり」"
    $ kag_cm()
    $ kag_drawchar('o_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0506.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そっか、魔法よね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.o7_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_o_b8_gamestart
    return
