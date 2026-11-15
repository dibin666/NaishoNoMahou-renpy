# Auto-generated from 06. hana/hn_B3.ks by tools/transpile_ks.py
label kag_hn_b3:

label kag_hn_b3_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hana.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg096', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hn_b3_hn__dash__03_00:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0511.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おっかいも～の、おっかいも～の」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ハナちゃんが、両手に冷えたジュースがたくさん入っている袋を持ちながら、ごきげんで歩いている。"
    $ kag_cm()
    "３時のおやつ用に、わたしたちは冷たいジュースを買い出しに出かけた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、わたしも手伝いましょうか？」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0512.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ううん！{w=0.4}これくらい平気平気～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0513.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「帰ったらみんなで、{w=0.4}プリンとシュークリーム食べながらジュース飲もうね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg047', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b3_hn__dash__03_01:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_playse('7-0216.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「それじゃ～みんなならんで～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "しばらくすると、幼稚園の前を通りがかった。"
    extend "\n園内からは、夏の暑さに負けないくらい元気な声が聞こえてくる。"
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0513.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしたんですか？ハナちゃん」"
    $ kag_cm()
    $ kag_playse('6-0514.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「今、ぽっぷの声がしなかった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0217.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「それじゃあ、次は鬼ごっこして遊ぼう～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0515.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やっぱり、ぽっぷだ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0516.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇ！{w=0.4}りずむ、行ってみよう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？{w=0.4}は、はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg051', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b3_hn__dash__03_02:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0218.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「じゃんけんで鬼を決めよう～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('園児\u3000「')
    "園児　「は～い！」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0219.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「じゃあいっくよ～！{w=0.4}じゃ～んけ～ん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0517.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ぽっぷ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0220.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ハナちゃん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg047', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b3_hn__dash__03_03:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0221.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あっ！{w=0.4}りずむちゃんも！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0518.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ちぃ～っす！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぽっぷちゃん、こんにちは」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0222.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「２人ともどうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0519.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんたち、お使い行ってたんだよね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('6-0520.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そしたら、ぽっぷの声が聞こえたの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0223.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そっか～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0521.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇねぇ、ぽっぷは何やってるの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0224.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「今日はあたし、この幼稚園の『１日お姉さん』をしてるんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0522.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ぽっぷカッコイ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0225.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そ、そっかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0523.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.45}カッコイイ！{w=0.4}それにぽっぷ、すご～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0226.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えっ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0524.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「だって、あそこのみんなの……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0525.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「お姉さんなんだもん！{w=0.4}すごいよ～！{w=0.4}ね！{w=0.4}りずむもそう思うよね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ハナちゃんは、グラウンドでぽっぷちゃんの言いつけどおり、"
    extend "ならんで座っている園児たちの方を見る。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！{w=0.4}あんなにたくさんいるちっちゃい子たちのめんどうが見られるなんて、すごいと思います」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0227.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えへへ、ありがと！{w=0.4}それじゃあ、あたし、そろそろ行かないと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0526.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、そうだぽっぷ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0227.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「なに？」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0527.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんたちも『１日お姉さん』したい～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0228.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ！？」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0528.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇ～ダメ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん。{w=0.4}わたしたち、お使いの途中だし」"
    $ kag_cm()
    $ kag_playse('6-0529.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ちょっとくらい寄り道しても大丈夫だよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_hn_b3_choices_hn01_1:
    $ kag_set_bookmark('はなシナリオ選択肢01')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】そんな……', current_stem='hn_b3', storage=None, target='*choices_hn01_1-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】ちょっとくらいなら', current_stem='hn_b3', storage=None, target='*choices_hn01_1-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_hn_b3_choices_hn01_1__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「そんな……」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0530.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇ～ぽっぷ～いいでしょ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0229.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うん、幼稚園の先生に聞いてみるね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_hn_b3_after_choices_hn01_1
    call kag_s_wait

label kag_hn_b3_choices_hn01_1__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag=1
    $ kag_set_next_indent('りずむ「')
    "りずむ「ちょっとくらいなら……」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0230.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「それじゃあ、幼稚園の先生に聞いてみるね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_hn_b3_after_choices_hn01_1
    call kag_s_wait
    "【分岐終わり】{nw}"

label kag_hn_b3_after_choices_hn01_1:
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0531.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やったあ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg050', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()

label kag_hn_b3_hn__dash__03_04:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0532.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、えっと……」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0231.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えっと、新しいお姉さんを紹介するね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0232.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ハナお姉さんと、りずむお姉さんです！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0533.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんだよ～！{w=0.4}よろしく～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの、りずむと言います。{w=0.4}よろしくお願いします」"
    $ kag_cm()
    $ kag_set_next_indent('園児\u3000「')
    "園児　「よろしくおねがいしまぁ～す！」"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0534.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「は～い！{w=0.4}ハナちゃんとお砂場で遊びたい人、お砂場に集合～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-022.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あっ！{w=0.4}ハナちゃん待ってくださ～い」"
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0233.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あ、あの……{w=0.55}みんな！？{w=0.4}ま、待ってよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg049', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b3_hn__dash__03_05:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "あまり広くはないスペースに、ハナちゃんと園児たち十数人が遊んでいる。"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0535.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「アハハハ～、アハハハ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0234.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ハ、ハナちゃん、{w=0.4}何作ってるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0536.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへ～ないしょ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0235.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そ、そうなんだ。{w=0.4}あれ？{w=0.55}りずむちゃんどうしたの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぽ、ぽっぷちゃん。{w=0.4}わたし、何をしたらいいのでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0236.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ハナちゃんみたいに、いっしょに遊んでいればいいと思うよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか……？」"
    $ kag_cm()
    "そう言われても……"
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0237.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃん、もっと気楽でいいよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0537.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「できた！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "園児のお友だちも、ハナちゃんのまわりに集まってきた。"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0238.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ハナちゃん、どうしたの……{w=0.6}{nw}"
    $ kag_drawchar('p_06.tlg', time_ms=100, sepia=False, canskip=True)
    extend "うわっ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0538.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「じゃ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0539.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「へへ～マジョリカ！{w=0.4}似てるでしょ～。{w=1}{nw}"
    $ kag_drawchar('hn_07.tlg', time_ms=100, sepia=False, canskip=True)
    extend "わっ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0239.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ちょ、ちょっと、ハナちゃ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0540.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どうしたの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0240.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「どうしもこうしたもないよ！\n{w=0.4}これって思いっきりブニュちゃんじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0541.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん。{w=0.4}マジョリカだよ。{w=0.4}ダメ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0241.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「当たり前じゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg049', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b3_hn__dash__03_06:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0242.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「はぁはぁはぁ……{w=0.65}あ、あははは！{w=0.4}みんな！タコさんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('園児\u3000「')
    "園児　「わぁ～！」"
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0542.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えぇ～ハナちゃん、{w=0.4}マジョリカがよかったな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0243.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ダ～メ！{w=0.4}ブニュちゃん作っても、みんなわかんないじゃ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0543.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そっか～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg051', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0244.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「次はね、{w=0.4}かけっこしよう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('園児\u3000「')
    "園児　「は～い！」"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0544.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「お馬さんごっこしながら！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0245.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「なっ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0545.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「きっと楽しいよ～『お馬さんごっこのかけっこ』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0246.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「じゃ、じゃあ、{w=0.4}ぽっぷおねーさんは、{w=0.4}朝礼台でみんなをみてるからねぇ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-021.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}ぽっぷちゃん？{w=0.4}あ、いやちょっと待っ……{w=0.6}うわぁ！？」"
    $ kag_cm()
    "わたしの背中に園児のお友だちがいきなり乗っかってくる。"
    $ kag_cm()
    "ふりむくとハナちゃんはもう園児のお友だちを乗せていた。"
    $ kag_cm()
    "ぽっぷちゃん、ずるーい！"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0546.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「しゅっぱ～つ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハ、ハナちゃ～ん……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg049', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b3_hn__dash__03_07:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0547.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ～楽しかった～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハァ、{w=0.45}ハァ、{w=0.45}ハァ。{w=0.4}も、もうダメ」"
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0247.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃん、大丈夫？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もうダメ。{w=0.4}限界です……」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0548.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どうしたのりずむ～？{w=0.4}元気ないよ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハ、ハナちゃん。{w=0.4}も、もう少しつかれない遊びにしませんか？」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0549.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}わかった！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「よ、よかった～」"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0550.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「じゃ～次は鬼ごっこしよう～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_playbgm('m52', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ！？」"
    $ kag_cm()
    $ kag_set_next_indent('園児\u3000「')
    "園児　「はぁ～い！」"
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0248.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ちょ、ちょっとハナちゃん！？{w=0.4}今、つかれない遊びって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0551.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「だからつかれない遊び。鬼ごっこ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そ、そんなぁ～」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg047', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b3_hn__dash__03_08:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0552.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「みんな～また遊びに来るからね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg096', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0553.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「今日は楽しかったね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「つ、つかれました」"
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0249.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「わたしもヘトヘトだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0554.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、ぽっぷ～。{w=0.4}今日、楽しくなかった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううん！{w=0.4}とってもつかれたけど、楽しかったです」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0250.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そうだね！{w=0.4}あたしも、久しぶりに幼稚園にいた頃みたいに遊んじゃったよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0555.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「本当に？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}本当です！{w=0.4}わたし、こんなにヘトヘトになるまで遊ぶのって久しぶりだったから」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だから……{w=0.6}楽しかったです！」"
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0556.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「よかった！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0252.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ところで今日二人とも、お使いの途中じゃなかったっけ？{w=0.4}こんなに遅くなっちゃっていいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0557.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あ、忘れてた」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「い、急がないと！」"
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0558.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0559.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ほら～！{w=0.4}ぽっぷも早く早く！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0253.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えっ！{w=0.4}な、何であたしまで！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0560.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ほらほら～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぽっぷちゃん、急いで～！」"
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0254.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「待ってよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'bg014', time_ms=1000, bgcolor='0x000000')
    $ kag_cm()
    $ kag_wait(1500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'bg017_b', time_ms=1000, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_hn_b3_hn__dash__03_09:
    $ kag_set_bookmark('「３日目」みんなで遊ぼう！１日おねぇさん')
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('どれみ「')
    "どれみ「…………」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "テーブルの上には、暑さのあまり、とけてしまったプリン。"
    $ kag_cm()
    "すっかりふやけて、しぼんでしまったシュークリーム。"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「プリン、ドロドロになっちゃったね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0674.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「シュークリーム、しぼんじゃったね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0758.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんたち、遅いね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0618.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「二人とも、どこまで買い物に行っちゃったんだろうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0978.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「帰ってきたら、じっくり聞かせてもらわんとな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', 'bg014', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0064.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「フッフッフッフ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', 'white', time_ms=1000, bgcolor='0x000000')
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hn3_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hn_b4_gamestart
    return
