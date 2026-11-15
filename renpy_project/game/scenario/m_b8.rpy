# Auto-generated from 05. momo/m_B8.ks by tools/transpile_ks.py
label kag_m_b8:

label kag_m_b8_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_momo.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg229', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_m_b8_mo__dash__08_00:
    $ kag_set_bookmark('「８日目」友だちとわたし')
    $ kag_cm()
    "今日の天気は雨。"
    $ kag_cm()
    "強い勢いで、朝からふり続いている。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0528.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「雨だね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0714.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ひさびさね、雨の日なんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0928.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ここんとこずっとええ天気やったからな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0999.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ところでりずむちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0715.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いないみたいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0929.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃん知らん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0375.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ううん。{w=0.4}ハナちゃん、今日はまだ一度もりずむ見てないよ～？」{nw}"
    $ kag_history_opt(output=False, enabled=None)
    $ kag_waitclick()
    $ kag_history_opt(output=True, enabled=None)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1000.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、明日帰っちゃうんだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_sound_se('se-009.1.ogg', buf=1)
    $ kag_set_next_indent('りずむ「')
    "りずむ「おはようございます！」"
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0930.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「お、おはようさん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「……{w=0.3}りずむちゃん、元気そうだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0633.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0529.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……な、{w=0.4}何でしょう？」"
    $ kag_cm()
    $ kag_playse('5-0529.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、明日魔女界に帰っちゃうんでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0529.6.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それで今日なんだけど、みんなでりずむちゃんの……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、わたし！」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0529.7.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「えっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、今日はいっぱいみなさんのお手伝いします！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg005', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b8_mo__dash__08_01:
    $ kag_set_bookmark('「８日目」友だちとわたし')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    "お店の開店時間になった。"
    $ kag_cm()
    "けれど雨はふりやむけはいすらない。"
    $ kag_cm()
    "お客さんどころか、人っ子ひとり歩いていないので、今日はみんなでアクセサリーの作りおきをしている。"
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0635.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あ、ハナちゃん。{w=0.4}ここはそうじゃなくてこうするの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0377.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇ、はづき～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0636.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「なに？{w=0.4}ハナちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0378.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「なんか静かだね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0637.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん、ハナちゃん」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0379.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0638.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何か手伝うことないですか？」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0639.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「えっ！{w=0.4}そうね……{w=0.65}じゃあ、このでき上がった糸を、{w=0.4}箱につめてもらってもいいかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_drawchar('hn_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0380.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねぇ～りずむ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「？」"
    $ kag_cm()
    $ kag_playse('6-0381.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、明日本当に帰っちゃうの？{w=0.4}ハナちゃんさびしいなあ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……{w=0.6}女王様のいいつけだから……{w=0.7}しかたないんです」"
    $ kag_cm()
    $ kag_playse('6-0382.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「でも」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え、えっと！この糸をここに入れてあっちに持っていけばいいですね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg003', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b8_mo__dash__08_02:
    $ kag_set_bookmark('「８日目」友だちとわたし')
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「お客さん、{w=0.65}来ないね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0931.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「雨の日はしゃあないで～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1003.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そうなんだけどさ～。{w=0.4}やっぱ雨の日はやだね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0932.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。{w=0.4}なんか気持ちまで落ち込んでしまうな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0933.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん、あいちゃん！」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0934.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃんどしたん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、何か、手伝うことないかな～って」"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「こっちは足りてるから大丈夫だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか。{w=0.4}なら、おんぷちゃんの所を見てきます」"
    $ kag_cm()
    $ kag_drawchar('d_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-1006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、無理してないといいけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0935.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg017_b', time_ms=1500, bgcolor='0x000000')
    $ kag_bgdraw()
    $ kag_mesframe()

label kag_m_b8_mo__dash__08_03:
    $ kag_set_bookmark('「８日目」友だちとわたし')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0718.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あら？{w=0.4}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「何か手伝うことないですか？」"
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ど、どうかしました？」"
    $ kag_cm()
    $ kag_playse('4-0719.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ん～{w=0.6}そうね、それじゃあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい」"
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0720.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「この商品が入った箱を、{w=0.4}レジのももちゃんの所に持っていってほしいの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0721.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしちょっと手がはなせないからお願い、{w=0.5}ねっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0722.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それがすんだら、{w=0.4}ももちゃんの所を手伝ってきて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ、{w=0.45}は、はい」"
    $ kag_cm()
    $ kag_playse('4-0723.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ももちゃんに、元気出すように言っといてね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}あっ、はい！」"
    $ kag_cm()
    "わたしは明日になったら魔女界に帰る。"
    $ kag_cm()
    "そうしたら、お別れをしなくちゃならない。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg002', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b8_mo__dash__08_04:
    $ kag_set_bookmark('「８日目」友だちとわたし')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん？」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0530.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「んあ？あ、りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、これ、おんぷちゃんが」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0531.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あ、新しいアクセサリーだね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん」"
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0532.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあ、後でわたしがお店に並べておくね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0533.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの。{w=0.4}わたし、今日ずっとももちゃんのお手伝いしたいんですけど……。{w=0.4}ダメでしょうか？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0534.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ううん、ぜんぜんＯＫ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg252', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "朝から強くふっていた雨も、だいぶ弱まって来たみたいだ。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg002', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b8_mo__dash__08_05:
    $ kag_set_bookmark('「８日目」友だちとわたし')
    $ kag_cm()
    $ kag_playbgm('m60', loop=True)
    "ＭＡＨＯ堂の入り口にあるレジ。"
    $ kag_cm()
    "いつもはひとりいればじゅうぶんなスペースに、わたしとももちゃんの二人が座っている。"
    $ kag_cm()
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0535.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('5-0536.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、明日魔女界に帰っちゃうんだよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、女王様のご命令ですから。{w=0.4}残念ですけど」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0537.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ねぇ、りずむちゃん！{w=0.4}今日、家に泊まりにおいでよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}え、えっと……」"
    $ kag_cm()
    $ kag_drawchar('m_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0538.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ダメェ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ！{w=0.45}ダメじゃないけど。{w=0.4}いいんですか？おジャマしても」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0539.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！{w=0.4}パパとママにあたしが言っとくから！{w=0.4}ノープロブレム！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「それじゃあ、おジャマさせていただきます」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0540.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「お店が終わったらいっしょに帰ろう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg041', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "日中、ずっとふっていた雨も晴れ渡り、星空が広がる。"
    $ kag_cm()
    "ＭＡＨＯ堂での仕事も終わり、わたしは飛鳥邸にお泊まりに来た。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '05ももこ-08', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgm5=1
    $ kag_mesframe()

label kag_m_b8_mo__dash__08_06:
    $ kag_set_bookmark('「８日目」友だちとわたし')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_playse('5-0542.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ええ～！{w=0.4}りずむちゃんって寄宿舎に住んでるの～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_playse('5-0543.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そっか～。{w=0.4}じゃあ、門限とかもあるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。{w=0.4}舎監の先生がきびしいので、少しでも遅れるとそれはもう長いお説教が待ってます」"
    $ kag_cm()
    $ kag_playse('5-0544.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ちょっと大変だね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、でもお仕事で遅くなったりした時はお夜食を用意してくれたり、やさしいところもありますよ」"
    $ kag_cm()
    $ kag_playse('5-0545.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあ、いい先生なんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしもそう思います。{w=0.4}みんなはこわがってるみたいだけど」"
    $ kag_cm()
    $ kag_playse('5-0546.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うちのクラスの関先生も、{w=0.4}怒るとこわいけどとってもやさしいよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「なんだか舎監の先生ににてますね」"
    $ kag_cm()
    $ kag_playse('5-0547.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0548.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「なんか寄宿舎って、とっても楽しそうじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうですか？」"
    $ kag_cm()
    $ kag_playse('5-0549.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「修学旅行で友だちといっしょの部屋で寝泊まりしたけど、楽しかったよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「寄宿舎は、ひとり部屋なので……{w=0.55}それにわたし、お友だちの家にお泊まりなんて、{w=0.4}初めてです」"
    $ kag_cm()
    $ kag_fadeoutbgm(5000)
    $ kag_playse('5-0550.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あ、そういえば、{w=0.4}あたしも自分の部屋で、誰かとお泊まりするのは初めてだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「そうなんだ……」"
    $ kag_cm()
    $ kag_playse('5-0551.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('ももこ「')
    "ももこ「…………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_playse('5-0552.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「８日間、あっという間だったね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん」"
    $ kag_cm()
    $ kag_playse('5-0553.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「学校に行ったり、海を見に行ったりしたよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん」"
    $ kag_cm()
    $ kag_playse('5-0554.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あっ！{w=0.4}それから金色のちょうちょ！{w=0.4}あれはとっても楽しかったよね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん」"
    $ kag_cm()
    $ kag_playse('5-0555.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「楽しかったです。{w=0.4}ももちゃんと、みんなと過ごした８日間はホントに楽しかった。{w=0.4}でも……」"
    $ kag_cm()
    $ kag_playse('5-0556.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、今はすごくさびしいです。{w=0.4}せっかく、ももちゃんとお友だちになれたのに、{w=0.4}もうお別れなんて」"
    $ kag_cm()
    $ kag_playse('5-0557.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg042', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()

label kag_m_b8_choices_momo03:
    $ kag_set_bookmark('ももこシナリオ選択肢03')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('【Ａ】ももちゃんと、お別れしたくない', current_stem='m_b8', storage=None, target='*choices_momo03-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('【Ｂ】出会わなければよかった。', current_stem='m_b8', storage=None, target='*choices_momo03-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_m_b8_choices_momo03__dash__1:
    $ kag_cm()
    $ kag_f.judgeflag=0
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、ももちゃんとお別れしたくない。{w=0.4}このまま……」"
    $ kag_cm()
    $ kag_drawchar('m_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0558.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしね、今までいろんなお別れしてきたんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    jump kag_m_b8_after_choices_momo03
    call kag_s_wait

label kag_m_b8_choices_momo03__dash__2:
    $ kag_cm()
    $ kag_f.judgeflag += 1
    $ kag_set_next_indent('りずむ「')
    "りずむ「こんな思いをするくらいなら、ももちゃんに出会わなきゃよかった」"
    $ kag_cm()
    $ kag_drawchar('m_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0559.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あたしは、そうは思わないな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？」"
    $ kag_cm()
    $ kag_playse('5-0560.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……{w=0.55}あたしね、今までいろんなお別れしてきたんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    jump kag_m_b8_after_choices_momo03
    call kag_s_wait

label kag_m_b8_after_choices_momo03:
    $ kag_cm()
    $ kag_drawchar('m_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0561.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「アメリカへ行く時の日本のお友だち。{w=0.4}日本へ帰る時のアメリカのお友だち。"
    $ kag_playse('5-0561.2', buf=0, loop=False)
    extend "それから……{w=0.65}マジョモンローとの、お別れ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    "わたしも、ももちゃんも、次の言葉が出ない。"
    $ kag_cm()
    $ kag_drawchar('m_p_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0562.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「お別れする時はいつもさみしかった。{w=0.4}すっごくつらくて、悲しくて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "これ以上言葉を重ねたら、それだけ早く明日がやってきてしまいそう。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん……」"
    $ kag_cm()
    $ kag_drawchar('m_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0563.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「でもね。{w=0.4}マジョモンローやお友だちといっしょにいた思い出を思いかえすだけで、{w=0.4}お別れのつらさなんて忘れちゃうんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('bgm-v04', loop=True)
    $ kag_playse('5-0564.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃんはわたしのこと、{w=0.4}ずっと覚えててくれるよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「もちろん！」"
    $ kag_cm()
    $ kag_drawchar('m_p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0565.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「だったら大丈夫。{w=0.4}わたしだってりずむちゃんのこと……{w=0.6}ずっと忘れない。"
    $ kag_playse('5-0565.2', buf=0, loop=False)
    extend "だから、今はさびしいけど、{w=0.4}きっと楽しかった思い出だけは残るよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん」"
    $ kag_cm()
    $ kag_drawchar('m_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0566.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたし思うんだ。{w=0.4}お別れは悲しむためにあるんじゃなくて、{w=0.4}次の楽しい出会いをむかえるためにあるんだって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    "グスッ"
    $ kag_cm()
    $ kag_drawchar('m_p_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0567.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あはっ、泣いちゃった。{w=0.4}悲しくないのに……{w=0.45}なんか変だね」"
    $ kag_cm()
    $ kag_drawchar('m_p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0568.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そろそろ寝ようか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うん」"
    $ kag_cm()
    $ kag_drawchar('m_p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0569.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それじゃ、おやすみ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おやすみなさい」"
    $ kag_cm()
    $ kag_sound_se('se-058.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'black', time_ms=100, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.m8_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_m_c_gamestart
    return
