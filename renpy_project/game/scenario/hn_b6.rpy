# Auto-generated from 06. hana/hn_B6.ks by tools/transpile_ks.py
label kag_hn_b6:

label kag_hn_b6_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_hana.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg016', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_hn_b6_hn__dash__06_00:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    "夕方。"
    $ kag_cm()
    "ふだんなら家に帰る子供たちや、買い物袋を持ったお母さんたちとかが行き来する時間なんだけど、今日にかぎっては浴衣を着た人たちがまざっている。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg004', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0995.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あ、どれみちゃん。{w=0.4}ビーズの腕輪足らへんようになりそうだから、いっぱい作ってな！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1124.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はぁ～い。{w=0.4}りょう～か～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0686.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ど、どれみちゃん。{w=0.4}元気出して」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1125.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だってさ～。{w=0.4}今日は美空市の夏祭りじゃ～ん。{w=0.4}それなのにさ、何でお仕事しなくちゃいけないのさ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0637.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃん忘れたの～？{w=0.4}マジョリカ、ずぅ～っと前に、『祭りの日は夜がかせぎどきじゃ！』って言ってたじゃない」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0996.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「マジョリカちゃっかりしてんな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1126.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうなんだけどさ～外はお祭りでにぎわってるのにお仕事なんて。"
    $ kag_playse('1-1126.2', buf=0, loop=False)
    extend "あたしって、世界一不幸な美少女だあ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん」"
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0997.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん！用意できた～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}でも、いいんですか？」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0998.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「何が？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさんがお仕事をしているのに、{w=0.4}わたしとハナちゃんだけお祭りに行ってしまって」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0999.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ええって。{w=0.4}せっかく人間界に来たんやから、いっぱい楽しんでってもらわな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0773.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そうそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「で、でも、お金までいただいてしまって……」"
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0687.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「いいのよ。{w=0.4}お客様なのに、今までいっぱいＭＡＨＯ堂を手伝ってもらったから、{w=0.4}そのお礼よ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-009.1', buf=1)
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0638.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇりずむ。{w=0.4}準備できた～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}できました」"
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0639.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それじゃ～行こう、行こう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-1000.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃん、ごきげんやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0640.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}だって、りずむといっしょにお祭りに行けるんだもん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1127.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いいなぁ。{w=0.4}あたしもいっしょにお祭り行ってもいい？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0774.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どれみちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1128.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うそうそ、りずむちゃん、ハナちゃん、{w=0.4}いっぱい楽しんできてね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0641.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それでは、行って来ます」"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1129.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あっ！{w=0.4}待って！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('hn_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0642.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1130.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おみやげ、よろしくね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あはは……{w=0.6}わかりました！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg075', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b6_hn__dash__06_01:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    $ kag_playbgm('bgm-003', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「こ、これが人間界のお祭りなんですね……」"
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0643.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「にぎやか～」"
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0643.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それじゃあ、色々回ってみようよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg072', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b6_hn__dash__06_02:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0644.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～{w=0.3}ハナちゃんからはなれちゃダメだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "ドンッ"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！{w=0.4}すみません、すみません！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハ、ハナちゃん待って～！」"
    $ kag_cm()
    "ものすごい人ごみの中、歩くたびに人とぶつかっちゃう。"
    extend "そうこうするうちに、前を歩いているハナちゃんとの距離が開いていく。"
    $ kag_cm()
    "追いつくために、小走りで人の波をかきわけてみようとしたんだけど……。"
    $ kag_cm()
    "ドンッ"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ああっ、すみませんすみません」"
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('？？？「')
    "？？？「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すみませんすみません」"
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0149.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「べ、別にそんなにあやまらなくてもけっこうですわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0645.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～何やってるの～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん。{w=0.4}ちょっとこの方にぶつかってしまいまして……」"
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0646.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「あっ！{w=0.4}玉木ちゃ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0150.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「あら！巻機山さん？{w=0.4}\nこの子……{w=0.6}巻機山さんのお知り合い？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0647.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}お友だちのりずむだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0648.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ！{w=0.4}お友だちの玉木ちゃんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「り、りずむと言います！{w=0.4}よ、よろしくお願いします！」"
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0151.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「りずむさんね。{w=0.4}ワタクシは美空第一小学校、児童会長の玉木麗香ともうしますわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あれ？{w=0.4}この話し方。鉄琴さんみたい」"
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0152.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「どうかしまして？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あ！{w=0.4}何でもないです！鉄琴さん」"
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0153.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「て、鉄琴さん？{w=0.4}ところで、巻機山さんがいると言うことは、飛鳥さんたちもいっしょなのかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0649.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ううん！{w=0.4}今日はハナちゃんとりずむだけだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0154.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あ、そう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0650.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねえ！{w=0.4}玉木ちゃんもお祭りいっしょに行こうよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0155.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「えっ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0651.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「いいからいいから～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0156.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あっ、ちょっと巻機山さん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの！{w=0.4}わたしも玉木さんとお祭り、見て回りたいです。{w=0.4}いっしょに行きましょう」"
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('玉木「')
    "玉木「……」"
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0652.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「じゃあきまりだよね！{w=0.35}ね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0157.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ま、まあ、二人がそこまでおっしゃるんでしたら」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0653.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やった～！{w=0.4}よかったね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0654.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ん～それじゃあ……{w=0.6}まずはあっちの方に行こう～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg074', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b6_hn__dash__06_03:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0158.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「『ダーツのお店』？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「だ～つ？"
    extend "\n何だろう『だ～つ』って」"
    $ kag_cm()
    $ kag_drawchar('t_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0159.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「オーッホッホッホ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0654.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_cm()
    $ kag_drawchar('t_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0160.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ワタクシの得意なダーツのお店に行くなんて、{w=0.4}巻機山さん、さすがですわね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの『だ～つ』って、何ですか？」"
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0161.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「まあ！{w=0.4}りずむさんは、ダーツをご存知ないんですの！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。すみません」"
    $ kag_cm()
    $ kag_drawchar('hn_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0655.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんも知らないよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0162.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ま、巻機山さんもですの！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0656.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0163.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あのボードに向かってダーツを投げて、{w=0.4}点数の高い所にさされば勝ちですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0657.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ほえ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0164.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「おじさん、{w=0.4}１回、お願いしますわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('8-0165.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「お二人とも、{w=0.4}先にワタクシが手本を見せますわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "玉木さんが『それらしい』フォームでダーツをかまえる。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('8-0166.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「むむむむ……{w=0.6}えいっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "スタンッ！"
    $ kag_cm()
    $ kag_drawchar('t_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0167.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「『９０点』ふぅ。{w=0.4}まあまあですわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0168.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「まあ、ちょっとやそっとではワタクシほどのうでまえには」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "スタンッ！"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「や、やりました～！！！{w=0.4}１００点です」"
    $ kag_cm()
    $ kag_drawchar('t_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0169.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「追いつけませんわ。{w=0.4}{nw}"
    $ kag_drawchar('t_y_08.tlg', time_ms=100, sepia=False, canskip=True)
    extend "ええっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0658.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おおぉ～！{w=0.4}りずむ、すご～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あはっ。{w=0.4}玉木さん！これでいいんですよね！」"
    $ kag_cm()
    $ kag_drawchar('t_y_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0171.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ま、まあ……{w=0.65}そうですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0659.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やったね、りずむ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    "わたしは、１００点の景品『カエルの人形』を店の人からもらった。"
    $ kag_cm()
    $ kag_drawchar('t_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0172.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ま、負けませんわよ！{w=0.4}おじさん。{w=0.4}もう１回、お願いしますわっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "玉木さんは、ふたたび店番の人に１００円をわたした。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg074', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b6_hn__dash__06_04:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    $ kag_playse('8-0173.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「はぁ、はぁ、はぁ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0660.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「玉木ちゃん、おしかったね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0174.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ど、どういうことなんですの！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0661.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「１０回ぜ～んぶ、９０点！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0175.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ううう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「『だ～つ』ってとてもおもしろいですね」"
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0176.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「コホンッ！{w=0.4}ま、まあ、今日は少し肩の調子がちょっと……{w=0.55}ふだんなら全部、{w=0.4}１００点の所に当たるんですのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0662.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「すっご～い！{w=0.4}さすが玉木ちゃんだね～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}すごいです」"
    $ kag_cm()
    $ kag_drawchar('t_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0177.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ううう……{w=0.55}そ、それより！お二人とも！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0662.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0178.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「次はあのお店に行きませんこと？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg076', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b6_hn__dash__06_05:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    "たくさんの魚が泳ぐプールがある。"
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0179.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「さ、次はこの金魚すくいをしましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あの……{w=0.55}『きんぎょすくい』って、何なのでしょうか……？」"
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0180.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「金魚すくいも知らないんですの！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}すみません」"
    $ kag_cm()
    $ kag_drawchar('hn_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0663.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんもよくわかんな～い」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0181.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ま、巻機山さんも！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0664.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}どうやるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0182.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「それじゃあ、ワタクシがお手本をお見せしますわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('8-0183.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「おじさん、１回お願いしますわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg076', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "数分後……。"
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0665.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「玉木ちゃん、惜しかったね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「……」"
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0666.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「い～ち、に～い、さ～ん。{w=0.4}３匹！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('8-0184.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ううっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「『きんぎょすくい』ってとてもおもしろいですね」"
    $ kag_cm()
    "１回で１０匹も取れちゃった。"
    $ kag_cm()
    $ kag_drawchar('t_y_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0185.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「コホンッ！コホン！{w=0.4}ま、まあ、今日は少し手首の調子がちょっと……{w=0.55}普段なら１回で５０匹は軽いんですのよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0667.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えぇ～！{w=0.4}玉木ちゃんすご～いっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「すごいです！」"
    $ kag_cm()
    $ kag_drawchar('t_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0186.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「キィー！！{w=0.4}次はあのお店で勝負ですわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "玉木さんは『くじ引き』を指さした。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、勝負って？」"
    $ kag_cm()
    $ kag_drawchar('hn_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0668.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「勝負？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0187.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「え、えっ！{w=0.4}あ、ちがいますのよ。{w=0.4}あのお店で遊びませんこと？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0669.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg075', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('left', 'black', time_ms=800, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わ、わっぷ！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('left', 'bg075', time_ms=800, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "ちょうど、前を歩いていた２人とわたしの間を数人の人が横切った。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あれ？{w=0.4}ハナちゃん？玉木さん？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「み、見失っちゃった……」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハ、ハナちゃん～！{w=0.4}玉木さん～！」"
    $ kag_cm()
    "その場に立ち止まり、二人の名前を呼んでみたけど返事はない。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ううぅ、どうしよう」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！{w=0.4}そうだ、くじびきのお店！{w=0.4}\nきっとあそこに行けば！」"
    $ kag_cm()
    "わたしは、人ごみをかき分けくじ引きのお店へといそいだ。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg072', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "何度も人とぶつかりながら、なんとかたどりついた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「いない……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ど、どうしよう。{w=0.4}わたし、はぐれちゃった」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg075', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b6_hn__dash__06_06:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    $ kag_playbgm('bgm-003', loop=True)
    $ kag_drawchar('hn_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0670.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「玉木ちゃん！りずむ、いた～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0188.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「こっちにはいないみたいですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0671.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0189.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「こんなに人がいっぱいじゃ、さがしようがないですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0672.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんこっちをさがすから、{w=0.4}玉木ちゃんあっちをさがしてきて！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0190.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ちょ、ちょっと！？{w=0.4}巻機山さん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0191.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「わ、わかりましたわよ！{w=0.4}ワタクシも探しますわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg073', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b6_hn__dash__06_07:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    $ kag_drawchar('hn_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0673.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～、どこ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0674.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「むうぅ、こうなったら！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_playbgm('m407', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg413', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('6-0675.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ポロリンピュアリン　ハナハナピ！」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_changetype('circle02', 'bg414', time_ms=600, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('6-0676.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむを見つけられる道具よ～出ろ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_sound_se('se-047', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg073', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('hn_m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0677.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「なにこれ？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('6-0677.2', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おおおぉーー！{w=0.45}遠くの人が近くに見えるぅ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0677.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「これでりずむをさがすんだね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg075', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('bgm-003', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、玉木さん、どこに行っちゃったのかな？」"
    $ kag_cm()
    "ハナちゃんたちとはぐれてから色々歩き回り、元の入り口に戻ってきてしまった。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こうしていても仕方がない。よぉ～し！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg073', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃんたちに会わせて！」"
    $ kag_cm()
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？ふ、風船が！？」"
    $ kag_cm()
    "手元にあったカエルの人形が、風船のようにふくらみだした。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg249', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b6_hn__dash__06_08:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    $ kag_drawchar('hn_m_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0678.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～どこ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0679.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ん？{w=0.4}なんだあれ？"
    $ kag_playse('6-0679.2', buf=0, loop=False)
    extend "カエルさんの風船？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0680.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「さっきりずむがもらったカエルさんの人形そっくり……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0680.2', buf=0, loop=False)
    $ kag_set_next_indent('ハナ「')
    "ハナ「あ、そっか！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0681.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、見つけた！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg073', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_hn_b6_hn__dash__06_09:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    "わたしは、魔法でふくらんだカエルを見つめていた。"
    $ kag_cm()
    "しかし、ふくらんだこと以外に、特に変わったことはない。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんで人形がふくらんだのかな？」"
    $ kag_cm()
    "わたしは、大きくなったカエルをプニプニ指で押しながらつぶやいた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「魔法、失敗だったのかな」"
    $ kag_cm()
    $ kag_playse('6-0682.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ！」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん！ハナちゃん～！！{w=0.4}どこですか～！」"
    $ kag_cm()
    $ kag_sound_se('se-004', buf=1)
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('hn_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0683.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん！」"
    $ kag_cm()
    $ kag_drawchar('hn_m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0684.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「よかった。やっと会えた」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ええ！{w=0.4}もうどうしようかと思っちゃいました」"
    $ kag_cm()
    $ kag_drawchar('hn_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0685.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「このカエルさんの人形が教えてくれたんだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "大きくなったカエルの人形を、つんつん指で押すハナちゃん。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしが魔法を使ったら、{w=0.4}急に大きくなって」"
    $ kag_cm()
    $ kag_playse('6-0686.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「そうなんだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、{w=0.4}ハナちゃんに会えたのに、元に戻らないですね。{w=0.4}なんでだろ？」"
    $ kag_cm()
    $ kag_drawchar('hn_m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0687.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「さぁ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-004', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「誰か来る！」"
    $ kag_cm()
    $ kag_drawchar('hn_m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0688.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ええ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん、早くかくれてください！」"
    $ kag_cm()
    $ kag_drawchar('hn_m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0689.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「う、うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')

label kag_hn_b6_hn__dash__06_10:
    $ kag_set_bookmark('「６日目」～お祭り勝負！りずむと玉木？～')
    $ kag_cm()
    $ kag_sound_se('se-004', buf=1)
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0192.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「りずむさん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「玉木さん！」"
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0193.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ようやく見つかりましたわ。{w=0.4}りずむさん、さがしていたんですのよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「す、すみませんでした。{w=0.4}でも、どうしてここが？」"
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0194.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「どうしてって、りずむさんを探してたら、{w=0.4}りずむさんの持っていた人形を大きくなったものが見えて、{w=0.4}気になって来てみたらりずむさんがいたってわけですわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「（そっか、わたしが魔法で『ハナちゃんたちに会わせて！』って言ったから……）」"
    $ kag_cm()
    $ kag_drawchar('t_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0195.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あれ？{w=0.4}あのでっかい人形は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "『大きな人形』はどこにも見当たらない。"
    $ kag_cm()
    "そのかわり、『普通の大きさ』の人形が落ちている。"
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0196.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ワタクシの見まちがいだったのかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0197.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「それにしても……{w=0.6}せっかくりずむさんが見つかったのに、{w=0.4}今度は巻機山さんをさがさないと」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0690.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんはここにいるよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0198.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「なんだ。{w=0.4}巻機山さんもいらしたの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0691.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「玉木ちゃん。{w=0.4}ありがとう！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0199.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0692.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「だって玉木ちゃん、りずむのこと探してくれたんだよね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0200.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ワタクシは、{w=0.4}ただりずむさんとの『くじ引き勝負』がまだだったから……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0693.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「勝負？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「勝負なんてしてましたっけ？」"
    $ kag_cm()
    $ kag_drawchar('t_y_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0201.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「と、とにかく！{w=0.4}せっかくそろったんですから、{w=0.4}お祭りの会場に戻りますわよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0694.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「玉木ちゃん待って！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0695.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「えへへへ～……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ハナちゃんが、玉木さんと手をつなぐ。"
    $ kag_cm()
    $ kag_drawchar('t_y_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0202.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「あ、暑苦しいじゃありませんの！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0696.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「だって～{w=0.4}こうしていれば、もうはぐれないでしょ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('t_y_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('8-0203.ogg', buf=0, loop=False)
    $ kag_set_next_indent('玉木\u3000「')
    "玉木　「ううぅ、{w=0.4}た、確かにそうかもしれませんけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_y_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0697.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむも！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ハナちゃんは、もう片方の手をさし出した。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hn_y_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0698.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それじゃあ、行こう～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "お祭りの本番は、まだまだこれからだよね。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.hn6_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_hn_b7_gamestart
    return
