# Auto-generated from 01. doremi/d_B1.ks by tools/transpile_ks.py
label kag_d_b1:

label kag_d_b1_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_doremi.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg001', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_d_b1_d__dash__01_00:
    $ kag_set_bookmark('「１日目」最初のお仕事！失敗してもがんばろう！')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0084.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあ、さっそくりずむちゃんにお仕事の説明しなくっちゃね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい！\n……あの、どんなお仕事なんでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0025.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「一言で言うと、いろいろなアクセサリーを作って、それを売る、っていう流れなの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「アクセサリー作り……ですか……？」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0032.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そや。まあ、めったに売れへんのが困りモンやねんけどな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0024.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そーだねー。何で売れないんだろうねぇ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0034.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「まあまあ、売れゆきの話はそのくらいにして」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0033.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「けど、いきなりアクセサリーをって言うても、りずむちゃん、ようわからへんと思うから、ここは誰か教えてあげるのが一番はやいんとちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0085.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「は～い！じゃあ、あたしが教えるよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0035.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「えっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0026.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「えっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0034.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「えっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0025.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「えっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0407.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0086.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まかせてまかせて！じゃあ、２階にいこう！{w=0.2}りずむちゃん！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ、は、はい」"
    $ kag_cm()
    "どれみちゃんは、わたしの手を引いて２階へとあがった。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "あまりのすばやさに、残ったみんながポカンとしてる。"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0036.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「な、なんとかなるんじゃない。ちょっと心配だけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0026.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃん、きっとりずむちゃんのこと気に入ったんだよ……{w=0.5}でも大丈夫かなあ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0024.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんも、どれみといっしょに手伝う～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0027.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ハナちゃん、だめよ！{w=0.33}今日はレジをわたしとやる番だから、一階にいましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0025.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「むう～ハナちゃんわかった。{w=0.35}はづきとお仕事がんばる……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0035.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「な～んか心配やな～……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()

label kag_d_b1_d__dash__01_01:
    $ kag_set_bookmark('「１日目」最初のお仕事！失敗してもがんばろう！')
    $ kag_cm()
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0087.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えっと、こうして、こうやって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、こうですね……」"
    $ kag_cm()
    "見よう見まねでアクセサリー作りにいどむ。"
    $ kag_cm()
    $ kag_playse('1-0088.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ヨイショ……{w=0.45}{nw}"
    $ kag_drawchar('d_05.tlg', time_ms=100, sepia=False, canskip=True)
    extend "って、ああっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-005.ogg', buf=1)
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんの手がすべって、ビーズがバラける。"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0089.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あははは、ドンマイドンマイ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "テーブルに広がったビーズをかき集める。"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0090.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どう、りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい、何とか……」"
    $ kag_cm()
    $ kag_playse('1-0091.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ねぇ、りずむちゃんは魔女界でどんなお仕事してたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？、そ、それは……」"
    $ kag_cm()
    "ど、どう言ったらいいのかなあ。"
    $ kag_cm()
    $ kag_set_next_indent('どれみ「')
    "どれみ「……？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっと、かんたんなお手伝いとか、お使いとか、お茶くみとか。"
    extend "先輩魔女について、いろいろとやってました」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、失敗ばっかりで、いつも怒られてました」"
    $ kag_cm()
    $ kag_playse('1-0092.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いつも怒られてたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい……{w=0.7}何をやってもうまくいかなくって。"
    extend "しまいには自分の名前もまちがえちゃうくらいで……{w=0.6}あっ」"
    $ kag_cm()
    "にぎりしめていたビーズがすべって、床に落ちてしまった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ごめんなさい！"
    extend "はずかしいことに、いつもこんな感じなんです……。"
    extend "あっ、今拾いますね」"
    $ kag_cm()
    "床に落ちたビーズに手をのばしたとき、その上からどれみちゃんが手を重ねてきた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみ……ちゃん？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0093.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はずかしいなんてことないよ。{w=0.45}こんなの失敗のうちにはいんないじゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……はい」"
    $ kag_cm()
    $ kag_playse('1-0094.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「失敗しても、{w=0.65}次はがんばるっ！っていう気持ちがあれば、きっとうまく行くよ！{w=0.6}ね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん……」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0095.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしなんかさぁ、{w=0.5}いつも失敗の連続だよぉ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「れ、連続ですか？」"
    $ kag_cm()
    $ kag_playse('1-0096.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん、なんかね、{w=0.5}いつも空回りっていうか、タイミングが悪いっていうか。{w=0.3}その時は、うまくいってると思ってても、後でみんなに怒られたりなんてしょっちゅうだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0097.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「最近はハナちゃんまで、あたしのことをドジだ～ドジだ～って言い出しちゃって、{w=0.45}そりゃあもう、涙なしには語れないよ、{w=0.45}あたしの苦労は～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふっ」"
    $ kag_cm()
    $ kag_playse('1-0098.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お客さんも、あたしの個性ってものを、ち～っともわかってくれないし、もうあたしったら世界一不幸な……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、どれみちゃん。\nそのビーズ、長すぎませんか……？」"
    $ kag_cm()
    "どれみちゃんは話に夢中で、その間ずっとビーズメーカーのハンドルを回しっぱなしだった。"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0099.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？{w=0.55}うわわわわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こんなに長くして、何かに使えるんでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0100.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そ、そりゃあほら、ベッベルトとか、のれんとか、なべしきとか～{w=0.65}あ、なべしきはさすがに無理かもだけど……{w=0.5}あぁ、とにかく、これはこれでどうにかなるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふっ、そうですね」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0101.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あはははは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんは、わたしと同じか、それ以上の失敗の神様に愛されているかも。"
    extend "そう思うとちょっとだけ肩の力が抜けてきた。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg002', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_d_b1_d__dash__01_02:
    $ kag_set_bookmark('「１日目」最初のお仕事！失敗してもがんばろう！')
    $ kag_cm()
    "店内はざわめいている。"
    extend "\nたくさんのお客さんがつめかけて、ちょっとしたラッシュ状態だ。"
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「これをくださいな」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0027.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ハ～イ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('お客さん「')
    "お客さん「これ、なかなかすてきね。"
    extend "いただこうかしら」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0036.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「毎度おおきに～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0028.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ありがとうございました～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0026.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ございました～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0029.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「……今日はすごいわ、こんなに売れて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0037.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ほんと、たまにあるよね、よく売れる日が」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0037.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「今日は、お店のモンいっぱい売れたし、久々に繁盛やなぁ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0027.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんも、がんばっちゃったもんね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0028.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ハナちゃん、えらい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0030.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あとは、どれみちゃんたちが追加を持ってきてくれるから、それまで一休みね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0038.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()

label kag_d_b1_d__dash__01_03:
    $ kag_set_bookmark('「１日目」最初のお仕事！失敗してもがんばろう！')
    $ kag_cm()
    "わたしとどれみちゃんは、せっせとアクセサリー作りをしていた。"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0102.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あれ、なんかお店の方、ずいぶん静かになったね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そういえば、そうですねぇ？」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0103.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まさか、品物が全部売り切れちゃって、お客さん帰っちゃったかも！{w=0.35}早いところ作らないと！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、が、がんばります」"
    $ kag_cm()
    $ kag_playse('1-0104.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「わっせ、わっせ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0105.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「よいしょ、よいしょ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0106.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えっほ、えっほ……{w=0.4}{nw}"
    $ kag_drawchar('d_01.tlg', time_ms=100, sepia=False, canskip=True)
    extend "りずむちゃん、こっちは半分くらい終わったけど、そっちはどう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい、もうちょっとで終わります」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0107.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え！りずむちゃん早いなあ。{w=0.4}{nw}"
    $ kag_drawchar('d_02.tlg', time_ms=100, sepia=False, canskip=True)
    extend "よーし！あたしだって負けないんだからね！{w=0.35}そうだ！たしかここに……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "そう言いながら、どれみちゃんは足の下に置いてある箱をごそごそといじり始めた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん……{w=0.35}何やってるんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0108.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ふっふっふ……{w=0.4}じゃ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんの頭と同じくらいの大きさのビーズのかたまりをさしだす。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こ、これは……？」"
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0109.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「こんなこともあろうかと取っておいた、\nあたしの超大作！」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0109.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「これをほどくと、ネックレスの１０個や２０個なんてあっという間さ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はあ……超大作なのに、ほどいちゃうんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0110.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ん、ま、まあその、みんなにはお店に出せない～って反対されちゃって。ホントは、後でほどこうって思ってたんだけどね」"
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0110.2', buf=0, loop=False)
    extend "どれみ「あたしは結構いけてると思ってんだけどな～{w=0.55}どうこれ？りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ビーズのかたまりは、色や形は抜きにして、どこからほどいていいのかわからないって所だけはよくできていた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、えと、その……それでネックレスを１０個作った方が、お店にとってはうれしいんじゃないかと……」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0111.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「う、スルドイ……{w=0.3}そっか、やっぱりその方がいいよね。"
    $ kag_playse('1-0111.2', buf=0, loop=False)
    extend "さよなら、あたしの青春……{w=0.25}トホホ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、これ、どうやったらほどけるんですか？」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0112.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「え？ここらへんをたしか……{w=0.55}あれ、こっちだったかな……？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こことかはどうですか？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0113.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ！そこだ！{w=0.45}りずむちゃん、ちょっと持ってて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、はい」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0114.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「それじゃ行くよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-015.ogg', buf=0, loop=False)
    $ kag_cm()
    if kag_get_skip_mode()<=1:
        $ kag_playbgm('m52', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ！」"
    $ kag_cm()
    $ kag_stopse(buf=0)
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0115.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ああ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "糸がほどけて、ビーズのかたまりがくずれて、わたしの手の中からこぼれ落ちる。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ご、ごめんなさい！」"
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('1-0116.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、足もとあぶないよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「きゃあっ！」"
    $ kag_cm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_cm()
    $ kag_playse('1-0117.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「よく見ないと……{w=0.4}{nw}"
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    extend "ってどわあっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('1-0118.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おーっとっとっと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんは、反対側の戸棚までケンケンパの状態で進んでいく。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あ、あぶない！」"
    $ kag_cm()
    "わたしは思わず両手で目をふさいでしまう。"
    $ kag_cm()
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('down', 'black', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_playse('se-051.ogg', buf=1, loop=False)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('up', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0119.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「せ、せ～ふ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0039.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どしたん？{w=0.35}なんか大きい音がしたけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あいちゃん」"
    $ kag_cm()
    $ kag_sound_se('se-052.ogg', buf=1)
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0039.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「っ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！」"
    $ kag_cm()
    $ kag_playse('3-0040.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「どれみちゃん！{w=0.45}上！{w=0.45}上！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0120.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "どれみちゃんが、あいちゃんの指さした方を向いた瞬間。"
    $ kag_cm()
    if kag_get_skip_mode()==0:
        $ kag_playse('se-015.ogg', buf=1, loop=False)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0121.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぎゃああああっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「きゃあっ！」"
    $ kag_cm()
    $ kag_drawchar('a_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0041.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うわわわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_wait(100, canskip=False)
    if kag_get_skip_mode()==0:
        $ kag_playse('se-015.ogg', buf=1, loop=False)
    "戸棚の上にあったビーズの箱が落ち、部屋中がビーズの海になってしまう。"
    $ kag_cm()
    "それだけではおさまらず、階段から、ビーズがお店の中にまで広がっていく。"
    $ kag_stopse(buf=1)
    $ kag_cm()

label kag_d_b1_d__dash__01_04:
    $ kag_set_bookmark('「１日目」最初のお仕事！失敗してもがんばろう！')
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg013', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('se-015.ogg', buf=1, loop=False)
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「キャー！何？何？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0029.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ノォーーー」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0028.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「アハハハ、ビーズの滝だ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0038.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ちょ、ちょっとどういうこと～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0032.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どれみちゃん！一体何をしてたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0039.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「はづきちゃん！あぶない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0033.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「キャー」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.1.ogg', buf=1)
    $ kag_drawchar('m_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0030.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「まずお客さんを避難させないと！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('o_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0040.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「みなさん！早くこっちへ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)

label kag_d_b1_d__dash__01_05:
    $ kag_set_bookmark('「１日目」最初のお仕事！失敗してもがんばろう！')
    $ kag_changetype('cross', '01どれみ-01.tlg', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgd1=1
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('4-0041.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……それで？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ビーズだらけの店内。"
    extend "さいわいお客さんのピークは過ぎていたので、お客さんがビーズを踏んで転ぶことはなかった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃんとわたしで、ビーズのかたまりをほどこうとして……」"
    $ kag_cm()
    $ kag_playse('3-0042.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ～こないだの失敗作か」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0122.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「し、失敗作ぅ？{w=0.65}あれは、あたしが」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「シャラーップ！{w=0.6}りずむちゃん、続けて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0123.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うぅ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ほどけたら、バラバラになっちゃって、わたしが落ちたビーズを踏んじゃって……」"
    $ kag_cm()
    $ kag_playse('2-0034.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「……{w=0.3}だいたいわかったわ。りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0124.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんな、ここはあたしの顔にめんじて、許して？{w=0.4}ね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_d_b1_d__dash__01_05b:
    $ kag_set_bookmark('「１日目」最初のお仕事！失敗してもがんばろう！')
    $ kag_changetype('cross', 'bg013', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('o_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0042.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうはいかないわ。{w=0.4}戸棚の上にビーズの箱を置いたのはどれみちゃんでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0125.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ギクッ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0043.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「おとついデラが持ってきた材料を運ぶときに、おんぷちゃんに、あれほど上に置きな～って言われてたやんか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0029.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そ～だ、そ～だ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0126.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ううう……スイマセン」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0043.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ビーズの片づけ、どれみちゃんがやってよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0127.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「えええ～！{w=0.3}そんなぁ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0044.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「罰やから、当然やろ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、わたしも……{w=0.3}手伝います」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0045.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ～りずむちゃんは悪くないからええねん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ、でも、その……」"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0035.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あいちゃんもおんぷちゃんも、そのくらいでいいじゃない。{w=0.4}２人とも反省してるんだし、みんなで片づけましょうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0032.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだよ！みんなでパパーっと片づけようよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0046.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ん～、そやな、あたしらもちょっと言い過ぎたか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0044.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうね。"
    extend "じゃあわたしたちは１階を片づけるから、どれみちゃんとりずむちゃんは２階をお願い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0128.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「みんな～。{w=0.5}やっぱ持つべき物は親友だよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0129.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へへ、失敗しちゃったね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……{w=0.7}みなさん、やさしいんですね。"
    extend "わたしが魔女界にいた時は……」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0130.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0131.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「過ぎたことをくよくよ悩んでも解決しないよ。"
    $ kag_playse('1-0131.2', buf=0, loop=False)
    extend "散らかしたビーズは片づければいいんだし、失敗したらあやまればいいだけじゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……は、はい」"
    $ kag_cm()
    "たしかにどれみちゃんの言うとおりだ。"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0132.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ってまあ、あたしが言うのも変だけどね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふっ」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0133.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「さ、片づけよっか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、どれみちゃん」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0134.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「何？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「アクセサリー作り、面白かったです！」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0135.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うん！{w=0.45}またいっしょにやろうね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.d1_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_d_b2_gamestart
    call kag_s_wait
    return
