# Auto-generated from 00. part_A/part_A.ks by tools/transpile_ks.py
label kag_part_a:

label kag_part_a_gamestart:
    if kag_f.re_scenario==0:
        $ kag_set_rclick(True)
        $ kag_history_opt(output=None, enabled=False)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_changetype('blind01', 'eyecatch', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg069', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=True)

label kag_part_a_apart:
    $ kag_set_bookmark('りずむのお仕事')
    $ kag_cm()
    $ kag_playbgm('m63', loop=True)
    "光り輝く太陽。"
    $ kag_cm()
    "青い空には、白い雲が色あざやかに広がっている。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg086', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    "人間の世界では美空市と呼ばれている街の中心から、\nいくぶん離れた場所にわたしは立っていた。"
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0017.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「わたし、方向オンチだから、お使いは苦手中の苦手なんだけど、がんばらなくっちゃね」"
    $ kag_stopse(buf=0)
    if persistent.firstclear!=0:
        $ kag_playse('9-0017.2', buf=0, loop=False)
    $ kag_cm()
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「なんたって、女王様じきじきのお仕事だもの！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg090', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    "そう。"
    $ kag_cm()
    "わたしはＭＡＨＯ堂のマジョリカさんへ、女王様からのお手紙をお届けするという仕事をしに、人間界までやってきたのだった。"
    $ kag_cm()
    "道を行く人影はまばら。"
    $ kag_cm()
    "人間界の街並みは、本でしか見たことがなかったので、ちょっと興味深い。"
    $ kag_cm()
    "…………。"
    $ kag_cm()
    "…………。"
    $ kag_wait(1500, canskip=True)
    $ kag_cm()
    "いけない。街並みに見とれている場合じゃなかった。マジョリカさんのＭＡＨＯ堂へ急がなくっちゃね。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg207', time_ms=1500, bgcolor='0x000000')
    $ kag_playse('bgm-001.ogg', buf=1, loop=False)
    $ kag_mesframe()
    "さわやかな風が吹き、ところどころで聞こえるセミの鳴き声。"
    $ kag_cm()
    "木々の日ざしの下を、ひたすら歩く。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg096', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    if persistent.firstclear!=0:
        $ kag_playse('9-0018.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あれれ？たしかＭＡＨＯ堂ってここら辺だと思ったのに……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あたりを見回してみる。"
    $ kag_cm()
    "…………"
    $ kag_cm()
    "…………"
    $ kag_cm()
    "…………"
    $ kag_cm()
    "地図の読み方をまちがえちゃったのかな？"
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg089', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(1000, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg093', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(1000, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg079', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('bgm-001.ogg', loop=True)
    "もう３０分は歩いたと思う。"
    $ kag_cm()
    "いや、１時間くらいかも知れない。"
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0019.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「お、おかしいなぁ……{w=0.6}たしか地図ではここらあたりだと思うんだけど……」"
    $ kag_cm()
    $ kag_stopse(buf=0)
    if persistent.firstclear!=0:
        $ kag_playse('9-0019.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「３本目の曲がり角に大きな木なんてなかったし、{w=0.7}その前の佐藤さんの家なんていう、珍しい名前の人の家を見逃すはずがないし」"
    $ kag_cm()
    $ kag_stopse(buf=0)
    if persistent.firstclear!=0:
        $ kag_playse('9-0019.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「元に戻ろうにも、どこをどう歩いてきたのかさっぱりだし……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg085', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "誰もいない、小さな公園にたどり着いたわたしは、あたりを見渡す。"
    $ kag_cm()
    "ふと目に入るブランコ。"
    $ kag_cm()
    "トボトボ歩き、ブランコに腰をおろす。"
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0020.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「はあ……{w=0.65}また迷っちゃった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0020.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「ＭＡＨＯ堂に行って、マジョリカさんにお手紙を届けなくっちゃいけないのに」"
    $ kag_stopse(buf=0)
    if persistent.firstclear!=0:
        $ kag_playse('9-0020.3.ogg', buf=0, loop=False)
    $ kag_cm()
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「どうしてわたしってダメなのかな？{w=0.55}こんな簡単なこともできないなんて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_wait(1500, canskip=True)
    if persistent.firstclear!=0:
        $ kag_playse('9-0020.4.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「……いっそ魔法でほうきに乗って、空から探しちゃおうかな？」"
    $ kag_stopse(buf=0)
    if persistent.firstclear!=0:
        $ kag_playse('9-0020.5.ogg', buf=0, loop=False)
    $ kag_cm()
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「……ううん、そんなところを人間に見つかって、{w=0.55}魔女ガエルにでもなってしまったら、ほんとうにお仕事クビになっちゃう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「わたし……{w=0.7}わたし……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_pausebgm()
    $ kag_playse('1-0002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    if persistent.firstclear!=0:
        $ kag_playse('9-0022.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「わ、わあっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'A-1', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgot3=1
    $ kag_mesframe()
    $ kag_cm()
    $ kag_resumebgm()
    $ kag_playse('1-0003.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「どこか具合でもわるいの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "急に話しかけられて、あやうくブランコから落ちるところだった。"
    $ kag_cm()
    "あれ？"
    $ kag_cm()
    "この人、かすかに見覚えがあるような、ないような……"
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0023.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あっ！その……{w=0.5}わたし……えと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0024.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「この人はたしか、この前魔女界でみた……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg085', time_ms=100, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m52.ogg', loop=True)
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「わっわっわぁ～！どうしたの！どうしたの！？どこか痛いの！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0025.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あっ、いや、そのっ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「泣いてるなんてただごとじゃないよ！{w=0.55}なにがあったの？話してみてっ！？{w=0.55}それともどこか痛いの？{w=0.55}そうだ！え～っとお医者さんに救急車にパトカーに～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "あわてふためく女の子を見て、あっけにとられる。"
    $ kag_cm()
    "女の子はそんなわたしの様子に気づかずに、さらにパニくっている。"
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0026.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「クスっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「へっ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0028.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あははは……{w=0.75}ふふふ……{w=0.75}あはは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「えっ？へへへ、ふふ、あははははは～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0029.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あっ、ごめんなさい！急に笑ったりして……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0008.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「あっ、ううん、こっちこそ、いきなりあわてちゃって、てへへ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'A-1', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('1-0009.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「それより、どうしたの？{w=0.55}なにか困っていたようだけど……{w=0.65}あたしでよかったら話してみてよ、相談にのってあげるよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0030.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そうだった。"
    $ kag_cm()
    "今、わたしは道に迷っている最中だったんだ。"
    $ kag_cm()
    "せっかくだから、目の前の女の子に道案内をお願いしようかな。"
    $ kag_cm()
    "あ、でもその前に、この子に確かめてみたいことがある。"
    $ kag_cm()

label kag_part_a_choices01:
    $ kag_set_bookmark('選択肢01')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('以前、魔女界で女の子を見ていたことを話す。', current_stem='part_a', storage=None, target='*choices01-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('自分が魔女であることを話す。', current_stem='part_a', storage=None, target='*choices01-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_part_a_choices01__dash__1:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_doremi += 1
        $ kag_f.sn_hana -= 1
        $ kag_f.route='A'
    $ kag_f.event_01=0
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg085', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    if persistent.firstclear!=0:
        $ kag_playse('9-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「じゃあ、そのぉ、いきなりでなんですけど……{w=0.7}あなたはたしか……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「たしか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0032.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「この前ほうきに乗って……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0011.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「ギクっ！{w=0.6}ほ、ほうきにのってぇ……{w=0.6}\nって、い、いきなりなにを！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0033.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「ポロンをかざしたりして……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「ギクギクっ！{w=0.6}ポっ！ポロンをかざしたりしてぇ～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0034.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「とても楽しそうに飛んでた……{w=0.5}ま」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「まっ……！」"
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0035.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「ま……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0014.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「まぁっ……！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0036.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「魔女見習いさん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_freeimage(layer='0', page='front')
    $ kag_playse('1-0015.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「だあぁぁぁぁ～っ！{w=0.75}もうおしまいだぁぁぁ！！{w=0.7}\nあたしの未来がぁぁぁ～っ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_wait(2500, canskip=True)
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0016.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「ん？{w=0.75}ん？？{w=0.75}って、あれ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0037.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「ぷっ、フフフ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0017.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「あ、あのぉ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0039.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あははははは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0018.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「もしもぉ～し……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0040.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あはは、ごめっ、ごめんなさい……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0041.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「まさか、こんな所であなたに会えるなんて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0019.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「へ？あのぉ、言っている意味がよくわからないんですけどぉ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0042.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あっ、ごめんなさい、びっくりさせちゃって……{w=0.75}\nわたし、魔女なの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0042.2', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「女王様からお言付けをもらって、今、魔女界からきたばかりなの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    if persistent.firstclear!=0:
        $ kag_playse('9-0042.3', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「このお手紙を、ＭＡＨＯ堂のマジョリカさんに渡すために来たんだけど」"
    $ kag_stopse(buf=0)
    if persistent.firstclear!=0:
        $ kag_playse('9-0042.4', buf=0, loop=False)
    $ kag_cm()
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「その……{w=0.6}わたしドジだから、迷子になっちゃって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_part_a_after_choices01
    call kag_s_wait

label kag_part_a_choices01__dash__2:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_doremi -= 1
        $ kag_f.sn_hana += 1
        $ kag_f.route='B'
    $ kag_f.event_01=1
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg085', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    if persistent.firstclear!=0:
        $ kag_playse('9-0043.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「実は、ですね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0020.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「実は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    "（わたし、魔女なんです！）"
    $ kag_cm()
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「…………」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "ふと思ったんだけど。"
    $ kag_cm()
    "もしも人ちがいだったら、\nとりかえしのつかないことになるんじゃ……。"
    $ kag_cm()
    "ここは人間界。"
    $ kag_cm()
    "わたしは魔女なんだから、こんな大事なことをかるがるしく口にだすわけにはいかない。"
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    if persistent.firstclear!=0:
        $ kag_playse('9-0044.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「えーと……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「…………」"
    $ kag_cm()
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「…………」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「？？」"
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0045.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「（どうしよう。{w=0.55}自分が名乗ってもやっぱり魔女ガエルになっちゃうのかな……）」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0045.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「（でも自分から名乗ったなんて話、{w=0.7}聞いたこともないし……{w=0.6}もっと魔女ガエルの呪いのこと、勉強しておけばよかった……）」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0022.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「もしかして、あなた、魔女？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    if persistent.firstclear!=0:
        $ kag_playse('9-0046.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「え……えええええ！！☆☆△◇○！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_image('bg085', layer='0', page='fore', left=0, top=0, visible=True, sepia=True)
    $ kag_mesframe()
    "もうダメだ。"
    $ kag_cm()
    "わたしは魔女ガエルにされてしまうんだ。"
    $ kag_cm()
    "ああ……まだやりのこしたことがたくさんあったのに……"
    $ kag_cm()
    "わたしの頭の中では、魔女ガエル村で過ごす自分の新生活が現実であるかのように広がっていた。"
    $ kag_cm()
    "どうしよう。ママになんて言おう。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_image('d_07', layer='0', page='fore', left=0, top=0, visible=True, sepia=False)
    if persistent.firstclear!=0:
        $ kag_playse('9-0047.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「どうして？どうしてばれちゃったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0023.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「この間、女王様のお城のそばにいたでしょ？{w=0.55}ほら、あたしがふざけてほうきに乗ってて落ちそうになっちゃった時にさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0048.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「えっ！わたしのこと、覚えていたんですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "やっぱりあの時の魔女見習いさんだったんだ。"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0024.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「い、いやまぁ、そういうわけでもないんだけど、{w=0.2}\nまぁ、その……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0048.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0025.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「とにかく、あたしは魔女見習いだしさ。{w=0.55}{nw}"
    $ kag_drawchar('d_01.tlg', time_ms=100, sepia=False, canskip=True)
    extend "魔女ガエルになる心配はないよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0049.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「はぁぁぁ～。よかったぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg069', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m63', loop=True)
    "光り輝く太陽……。"
    $ kag_cm()
    "青い空には白い雲が色あざやかに広がっている。"
    $ kag_cm()
    "人間の世界では美空市と呼ばれている街の中心からいくぶん離れた公園のブランコに魔女の子はいた。"
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg085', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    if persistent.firstclear!=0:
        $ kag_playse('9-0050.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「生きてるって、{w=0.65}ステキ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0026.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「それで、どうしてこんな所にいたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0051.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「あっ、そうだった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0051.2', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「わたし、女王様からお言付けをもらって、{w=0.7}今、魔女界から来たばかりなの」"
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0051.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「このお手紙をＭＡＨＯ堂のマジョリカさんに、渡すために来たんだけど、"
    $ kag_stopse(buf=0)
    if persistent.firstclear!=0:
        $ kag_playse('9-0051.4.ogg', buf=0, loop=False)
    extend "その……{w=0.6}わたしドジだから、迷子になっちゃって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(2000)
    jump kag_part_a_after_choices01
    call kag_s_wait

label kag_part_a_after_choices01:
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0027.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「そうなんだ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0052.ogg', buf=0, loop=False)
    $ kag_set_next_indent('魔女の子「')
    "魔女の子「はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0028.ogg', buf=0, loop=False)
    $ kag_set_next_indent('女の子「')
    "女の子「ＭＡＨＯ堂だったら案内したげるよ！{w=0.6}\nいっしょに行こっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そっと手を差し出される。"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0029.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あっ、まだ名前言ってなかったよね。{w=0.6}あたしはどれみ。春風どれみ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0053.ogg', buf=0, loop=False)
    $ kag_set_next_indent('マジョリズム「')
    "マジョリズム「わたしは、マジョリズム」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0030.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「マジョリズム……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0030.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあ、りずむちゃんって呼ぶね！よろしく！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0054.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「りずむ……{w=0.6}はい、よろしく！どれみちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "ブランコから立ち上がり、どれみちゃんの手をとる。"
    $ kag_cm()
    "わたしたちは、ＭＡＨＯ堂に向かって歩き出した。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg014', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_bookmark('ＭＡＨＯ堂')
    $ kag_cm()
    "わたしたちがＭＡＨＯ堂に着くと、入り口の前に女の子が３人いる。"
    $ kag_cm()
    "表情からすると、ちょっと困っている様子みたい。"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おぉ～い、みんなぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「あっ、どれみちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0003.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「どれみちゃん、どこいってたん！{w=0.5}遅刻やで！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0032.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ごめんごめん！{w=0.5}{nw}"
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    extend "ってみんな、なんで入り口の前に立ってるの？{w=0.55}中に入ればいいのに」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「忘れたの？どれみちゃん、カギ当番だったでしょ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0033.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なぁ！そうだった！！{w=0.5}{nw}"
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    extend "ごめんなちゃい……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0034.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あれ、でも、ハナちゃんたちは中にいないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0003.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「それがなんか出かけてるみたい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0035.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「買い物かなぁ～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0003.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「それより……{w=0.5}どれみちゃん、後ろにいる子は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0055.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「その……{w=0.6}あの……」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_part_a_choices02:
    $ kag_set_bookmark('選択肢02')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('自己紹介する', current_stem='part_a', storage=None, target='*choices02-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('とまどう', current_stem='part_a', storage=None, target='*choices02-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_part_a_choices02__dash__1:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_ai += 1
        $ kag_f.sn_momo += 1
        $ kag_f.sn_hazuki -= 1
        $ kag_f.route=kag_f.route+'A'
    if persistent.firstclear!=0:
        $ kag_playse('9-0056.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、はじめまして、マジョリズムといいます……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「もしかして……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「魔女？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0057.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0036.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ついさっき人間界に来たばっかりなんだって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そっか。{w=0.55}はじめまして！妹尾あいこです！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「藤原はづきです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「My name is Momoko Asuka！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_part_a_after_choices02
    call kag_s_wait
    ":{nw}"

label kag_part_a_choices02__dash__2:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_ai -= 1
        $ kag_f.sn_momo -= 1
        $ kag_f.sn_hazuki += 1
        $ kag_f.route=kag_f.route+'B'
    $ kag_set_next_indent('りずむ「')
    "りずむ「…………」"
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0037.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あっ、紹介するね！！{w=0.35}この子は魔女界から来たマジョリズムことりずむちゃんでーす！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はじめまして。妹尾あいこです！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「藤原はづきです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「My name is Momoko Asuka！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0058.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ、はじめまして、マ、マジョリズムです……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "自己紹介は、わたしにとって数ある苦手な科目のうち、ベスト３に入るものだ。"
    $ kag_cm()
    jump kag_part_a_after_choices02
    call kag_s_wait

label kag_part_a_after_choices02:
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0038.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃんは女王様から、手紙をマジョリカに届けるように頼まれたんだってさ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0059.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「これなんですけど……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "わたしは、そっと手紙を差し出した。"
    $ kag_cm()
    "あいこちゃんがそれを手にとる。"
    $ kag_cm()
    $ kag_playse('se-056.ogg', buf=1, loop=False)
    $ kag_wait(1500, canskip=True)
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あかん！魔法文字や！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あいちゃんだめよ、人のお手紙、勝手に見ちゃ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0008.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「大丈夫やてはづきちゃん、どっちみち読まれへんねんから！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「みんな、どうしたの？入り口の前で話しこんじゃって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あっ、おんぷちゃん！お仕事じゃなかったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0003.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ドラマのロケ地が雨で、今日は撮影が中止になったの」"
    $ kag_cm()
    $ kag_playse('4-0003.2', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「英語の勉強でもしようかと思ったんだけど、天気がいいから、散歩ついでに寄ってみたの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0008.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうなんだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「……ところでどれみちゃん、この子は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0060.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_part_a_choices03:
    $ kag_set_bookmark('選択肢03')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('りずむ「あっ、あのぉ……わ、わたし……」', current_stem='part_a', storage=None, target='*choices03-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('りずむ「は、はじめ……まして……マジョリズムといいます」', current_stem='part_a', storage=None, target='*choices03-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_part_a_choices03__dash__1:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_doremi += 1
        $ kag_f.sn_onpu -= 1
        $ kag_f.route=kag_f.route+'A'
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0039.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おんぷちゃん、この子はりずむちゃん。魔女界から来たんだって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「瀬川おんぷです。よろしく」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0061.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「よ、よろしくお願いします……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_part_a_after_choices03
    call kag_s_wait

label kag_part_a_choices03__dash__2:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_doremi -= 1
        $ kag_f.sn_onpu += 1
        $ kag_f.route=kag_f.route+'B'
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「瀬川おんぷです。よろしく」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0062.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「こっ、こちらこそよろしくお願いします！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_part_a_after_choices03
    call kag_s_wait

label kag_part_a_after_choices03:
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ところでみんな、なんで入り口の前にいるの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0009.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そや、立ち話もなんやし、さっさとはいろか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0009.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃん、カギカギ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0040.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あっ、ごめんごめん！今開けるね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    "どれみちゃんは、ごそごそと自分のポケットに手を入れる。"
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0008.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「直射日光は、お肌によくないのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0009.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「紫外線も強いし、日射病にもなりかねないしね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_wait(1000, canskip=True)
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もうどれみちゃん、なにしてんの、はよ開けて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0041.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ……{w=0.6}う……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「どうしたのどれみちゃん、具合でもわるいの？{w=0.55}\n顔色、よくないわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どれみちゃん、ダイジョーブ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0042.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや、その……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……？」"
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0011.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「はは～ん、読めたでどれみちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0043.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ギク！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0011.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「まさか、どれみちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0044.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あの……{w=0.6}その……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「カギ！忘れたんやろ～っ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0045.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「スイマセン……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_fadeoutbgm(1000)
    $ kag_wait(2000, canskip=True)
    $ kag_playse('se-022.ogg', buf=1, loop=False)
    $ kag_playse('7-0001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「お姉ちゃ～ん～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0001.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「どれみ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopse(buf=1)
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0046.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぽっぷ？それにハナちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('7-0002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「お姉ちゃん、こ、これ、忘れ物……{w=0.65}ハァ、ハァ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0002.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ハナちゃんつかれた、ハァ、ハァ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_11.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0047.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おおお～！カギだぁ～！！{w=0.5}\nアリガトー！！さすがぽっぷ！わが妹よ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0003.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「わ、わかったよ、お姉ちゃん～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0009.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「さすがねぽっぷちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「ぽっぷちゃん、えらいわ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0003.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「えへ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ハナちゃんもありがとうな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0011.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「おつかれハナちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ハナちゃんえらいっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0004.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「ん？{w=0.65}あれ、この人は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('？？？「')
    "？？？「じぃぃぃーーーーー」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0063.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ……あっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0048.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「この子はりずむちゃん。{w=0.66}魔女界から来たんだって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0064.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「よ、よろしくです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたしはペコっと頭を下げる。"
    $ kag_cm()
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ちぃーす！ハナちゃんだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0005.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「春風ぽっぷです。ご覧の通りカギを忘れてしまうそそっかしいお姉ちゃんですが、仲良くしてやってください」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0049.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぽっぷ！{w=0.6}そそっかしいはよけいだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0065.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「こ、こちらこそ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0050.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ところでハナちゃん、なんでぽっぷといっしょに？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ぽっぷといっしょに、宿題やってたの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0051.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃんはがんばりやさんだね。{w=0.7}じゃあ、カギも来たし、{w=0.2}ささ、いざＭＡＨＯ堂へ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0014.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「もう、しゃあないなぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    if persistent.firstclear!=0:
        $ kag_playse('9-0066.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふふふ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    "みんなに続いてＭＡＨＯ堂に入る。"
    $ kag_cm()
    "お使いは、どうにか無事にうまくいきそう。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_sound_se('se-031.1.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m52', loop=True)
    $ kag_playse('3-0015.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あっちゃー！やられたっ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0052.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どうしたの？あいちゃん！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0016.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「みんな、コレ見て！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「なになに～？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「これって、マジョリカの置き手紙？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0053.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なになに……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0054.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「リリカママから、温泉の招待状をもらった。{w=0.55}\nお前たちの分も、あるにはあるんじゃが、店を休むわけにはイカン！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0054.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「夏休みとはいえども、今はかせぎ時じゃからな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0054.3', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「よって、代わりといってはなんじゃが、妖精たちを連れて行くことにした」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0054.4', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まぁ、１０日ぐらいしたら帰るので、みやげを楽しみに待っとれ。マジョリカより」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0054.5', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「追伸、"
    $ kag_playse('1-0054.6', buf=0, loop=False)
    extend "みんなくれぐれも遅刻なぞせんようにな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0054.7', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「特にどれみ！おまえときたら最近たるんどるぞ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0055.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「な、な、な、なによこれー！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「さっそく遅刻がバレてるね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「さすがはマジョリカ。{w=0.5}どれみちゃんの行動はお見通しね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0008.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみ、遅刻遅刻～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0014.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「だめよどれみちゃん、遅刻はいけないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0056.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「スンマセン。気をつけます」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_05.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('1-0056.2', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「……って、それどころじゃないっしょ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0017.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ふっ、どれみちゃん、ナイスツッコミ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0057.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「へへ、どもども！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0015.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「２人とも、冗談やっている場合じゃないわよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0058.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そっか。りずむちゃん、どうしようか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0011.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「どうかしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_part_a_choices04:
    $ kag_set_bookmark('選択肢04')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('りずむ「どうしよう、お手紙……」', current_stem='part_a', storage=None, target='*choices04-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('りずむ「やっとＭＡＨＯ堂に着いたのに、肝心のお手紙が渡せないなんて……」', current_stem='part_a', storage=None, target='*choices04-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_part_a_choices04__dash__1:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_hazuki += 1
        $ kag_f.sn_momo += 1
        $ kag_f.sn_hana += 1
        $ kag_f.sn_ai -= 1
        $ kag_f.route=kag_f.route+'A'
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「手紙？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0014.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃん、女王様から預かったお手紙を、マジョリカに届けるために来たんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_part_a_after_choices04
    call kag_s_wait

label kag_part_a_choices04__dash__2:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_hazuki -= 1
        $ kag_f.sn_momo -= 1
        $ kag_f.sn_hana -= 1
        $ kag_f.sn_ai += 1
        $ kag_f.route=kag_f.route+'B'
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「マジョリカに手紙を届けにきたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0067.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい。あの、女王様からのお手紙なんです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_part_a_after_choices04
    call kag_s_wait

label kag_part_a_after_choices04:
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0014.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「その手紙、ちょっと見せて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "おんぷちゃんに、持ってきた手紙を渡す。"
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    $ kag_playse('4-0015.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、後ろに小さくＭＡＨＯ堂のみなさんへって書いてあるわよ。{w=0.6}だったら、わたしたちが開けて見ても平気なんじゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0068.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0016.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ほら、うしろのココに書いてある」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0069.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あっ、ホントだ……{w=0.65}すみません、わたし、気がつかなくて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0015.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それなら、おんぷちゃん、読んでみてくれる？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0059.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「おんぷちゃん、魔法文字読めるもんね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0009.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「おんぷー！読んで読んで！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0017.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「じゃあ、開けて読むわね。{w=0.5}いい？りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-056.ogg', buf=1, loop=False)
    $ kag_playse('4-0018.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ＭＡＨＯ堂のみなさん、お元気ですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0018.2', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「今回は、おりいってみなさんにお願いがあります」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0018.3', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「この手紙をもってきたマジョリズムを、{w=0.5}８日間ＭＡＨＯ堂で修行させていただけないでしょうか？」{nw}"
    $ kag_drawchar('o_05.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_waitclick()
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_wait(500, canskip=True)
    $ kag_playse('A-0001.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「ええ～～～っ？」　"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「しゅ、修行？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "まさか、女王様の手紙にわたしのことが書いてあるなんて。"
    extend "\nさらに、わたしに修行をせよとは、いったい全体どうなってしまっているんだろう。"
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0019.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「続けて読むわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_playse('4-0020.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「マジョリズムはごらんの通り、ＭＡＨＯ堂のみなさんと同い年です」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0020.2', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「そこでまだ、魔女界で働き出して間もないマジョリズムに、３年間以上ＭＡＨＯ堂で働いてきた先輩として」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0020.3', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「お仕事のやり方を教えてあげてほしいのです。短い間ですが、よろしくお願いします」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「……{w=0.55}{nw}"
    $ kag_playse('4-0021.ogg', buf=0, loop=False)
    extend "だって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「………………」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0060.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ねぇねぇ、おんぷちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0022.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なに？どれみちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0061.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まさか、そのあとに遅刻はしてはいけません！{w=0.55}な～んて書いてないよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0023.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「フフ！大丈夫よ、書いてないわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0062.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「はぁ、よかった～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0018.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そんなん書いてるはずないやろ……{w=0.65}\nあれ、りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0016.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「………………」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「………………………………」"
    $ kag_cm()
    $ kag_drawchar('hn_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0010.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、かたまってるよ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0019.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうとうショックうけたみたいやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0063.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「もしもーし、りずむちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「………………」"
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はっ！はい！なんでしょう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0016.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「とりあえず、\nわたしたちとお仕事をすればいいんだよね？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はあ、まあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0024.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それだけなのかしら？{w=0.3}ちょっとひっかかるのよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0017.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「What?」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0017.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わざわざ人間界に行かせて、それもどうしてここのＭＡＨＯ堂なのかしら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0020.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「うん。{w=0.4}そこはわからへんな～{w=0.6}でも女王様がわざわざ手紙を送ってくるっていうことは、なんかあんのとちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0064.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんかって、何？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「いや、それもわからへんけど。{w=0.3}りずむちゃんは心当たりない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「まさか……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    "たしかにわたしは、お仕事をはじめたばっかりだ。"
    $ kag_cm()
    "でも、魔女が魔女見習いにお仕事を教えてもらうのは、ちょっと変だ。"
    $ kag_cm()
    $ kag_stopse(buf=0)
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0022.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あたしらでよかったら力になるから、{w=0.3}話、聞かしてくれへん？」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    "心当たりが全くないわけでもない。"
    $ kag_cm()
    "話してしまった方がいいのだろうか。"
    $ kag_cm()
    $ kag_drawchar('hn_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0011.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、お仕事うまくできないの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0065.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハ、ハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')

label kag_part_a_choices05:
    $ kag_set_bookmark('選択肢05')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('相談する', current_stem='part_a', storage=None, target='*choices05-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('相談しない', current_stem='part_a', storage=None, target='*choices05-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_part_a_choices05__dash__1:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_doremi -= 1
        $ kag_f.sn_hazuki -= 1
        $ kag_f.sn_onpu -= 1
        $ kag_f.sn_ai += 1
        $ kag_f.sn_momo += 1
        $ kag_f.sn_hana += 1
        $ kag_f.route=kag_f.route+'A'
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'A-2', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgot4=1
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m413a', loop=True)
    if persistent.firstclear!=0:
        $ kag_playse('9-0076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、その、お仕事、失敗ばっかりで……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、物をかたづけるのもうまくできないし……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0078.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「コピーの１枚もうまくできないし……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0023.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0079.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いつもそんな調子で、みんなに迷惑ばかりかけてるんです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0079.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「先輩の魔女たちは、当たり前にできることばっかりなのに。{w=0.65}わたしだけひとり……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0079.3', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしがいけないんです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0018.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そんなふうに思いこんじゃダメだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0080.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    jump kag_part_a_after_choices05
    call kag_s_wait

label kag_part_a_choices05__dash__2:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_doremi += 1
        $ kag_f.sn_hazuki += 1
        $ kag_f.sn_onpu += 1
        $ kag_f.sn_ai -= 1
        $ kag_f.sn_momo -= 1
        $ kag_f.sn_hana -= 1
        $ kag_f.route=kag_f.route+'B'
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'A-3', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgot5=1
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m413a', loop=True)
    if persistent.firstclear!=0:
        $ kag_playse('9-0081.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし……{w=0.6}たぶんお仕事をクビになったんだと思います」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('A-0002.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「ええっ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0082.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「たぶん、お仕事を失敗ばかりしてるのが女王様にも伝わっちゃったんです」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0082.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「もう、魔女界に帰ってこなくていいって言われてるんだと思います」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0066.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「い、いや、まだそうとは決まったわけじゃ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('2-0018.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうよ。ちゃんと８日間って書いてあるんだし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0083.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いいえ、きっとそうです！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0083.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「この間はマジョリンさんの前でヘマしちゃったし、みんな、わたしのことが、キライなんだと思います……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('1-0067.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「そんなはずはない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0083.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「っ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0068.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あの女王様がそんなこと言うはずない！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0069.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、大声出しちゃって、ゴメン」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「………………」"
    $ kag_cm()
    "びっくりした。"
    $ kag_cm()
    "ななめ上から、大声で怒られたことはいっぱいあったけど、正面から見すえられて大きな声を出されたことはなかった。"
    $ kag_cm()
    "たしかにどれみちゃんの言うように、女王様が言うはずがないと、わたしも思いたい。"
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0070.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「とにかく、やってみようよ。{w=0.45}うまくいかなくたって、そんなのへっちゃらだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0084.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも、それではみなさんに迷惑が……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0019.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「迷惑なんかじゃないよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    if persistent.firstclear!=0:
        $ kag_playse('9-0085.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_part_a_after_choices05
    call kag_s_wait

label kag_part_a_after_choices05:
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0020.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしもね、日本に転校してきて、初めは困ったこととか、失敗したこととかいっぱいあったよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0020.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「でもそんな時に、ここにいるみんなに教えてもらったり、助けてもらったりした」"
    $ kag_cm()
    $ kag_playse('5-0020.3.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「だから、ひとりでうまくいかないことがあったら、みんなでやってみたらいいんじゃないかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0086.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0025.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ももちゃんの言う通りよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0025.2', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ドラマとかでも、監督さんがいて、カメラさんがいて、照明さんがいて、メイクさんがいて、脚本家さんがいて」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('4-0025.3', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「音楽をつくる人がいて……いろんな人が一生懸命がんばって作るのよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0087.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「おんぷちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0019.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「わたしたちでできることなら手伝うわ。{w=0.6}いっしょにがんばりましょう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0088.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はづきちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0024.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「元気だしって。{w=0.5}\nこうなったら立派に仕事ができるようになって、先輩の魔女をびっくりさせたったらええねん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0089.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あいちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0012.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ、元気出して！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0090.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ハナちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0071.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あたしもドジばっかりだけど、なんとかなるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0091.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「どれみちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0072.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「困ったことがあったらいつでも言ってよ！{w=0.6}あたしたち、みんなりずむちゃんの力になるよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('A-0003.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「うん！」　"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0092.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、ありがとうございます！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0026.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「ちょっとは元気出たみたいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0093.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「は、はい。さっきよりは」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(5000)
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0020.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「とりあえず、りずむちゃんのお泊まりする場所を決めないといけないわね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0013.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんのお部屋のとなりが空いてるよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0006.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ハナちゃん、それってブニュちゃんの部屋じゃない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0014.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんをおいて温泉になんか行っちゃう人知らないも～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0073.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どうせいないんだし、８日間の間だけ借りちゃおうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「だったら、魔法で模様替えしちゃおうよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0025.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ほな、マジカルステージやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0094.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、わたしがやります。そこまでみなさんに頼りっぱなしなのは、申しわけないですから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg011', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playbgm('m67', loop=True)
    $ kag_drawchar('hn_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0015.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ねーねーりずむ。なんかためしに魔法使ってみて～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0095.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え……{w=0.65}では、この部屋のものをちょっとかたづけますね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-032.1.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'bg216', time_ms=500, bgcolor='0x000000')
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_wait(1000, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg011', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    "床に散らかっている物が１カ所にまとまった。"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0007.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「すご～い！さっすが魔女～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0096.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「いえ、そんな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0016.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ダメだよ、りずむー！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0097.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('6-0017.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「魔法を使うときは、呪文を言わなくっちゃ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0098.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゅ、呪文！？そんな、呪文って？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0074.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ハナちゃん、魔女は呪文を言わなくたって、魔法が使えるでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0018.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それじゃつま～んな～い！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0099.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「つ、つまらない……{w=0.6}ですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_part_a_choices06:
    $ kag_set_bookmark('選択肢06')
    $ kag_cm()
    $ kag_choices_begin()
    $ kag_add_link('呪文を唱える', current_stem='part_a', storage=None, target='*choices06-1', exp=None, x=None, y=None, color=None, size=None)
    $ kag_add_link('呪文を唱えない', current_stem='part_a', storage=None, target='*choices06-2', exp=None, x=None, y=None, color=None, size=None)
    $ kag_choices_end()
    call kag_s_wait

label kag_part_a_choices06__dash__1:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_doremi -= 1
        $ kag_f.sn_onpu -= 1
        $ kag_f.sn_hana += 1
        $ kag_f.route=kag_f.route+'A'
    if persistent.firstclear!=0:
        $ kag_playse('9-0100.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わかりました。{w=0.55}わたしも呪文を唱えてみます」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0019.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ホント！やった～！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0101.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしの呪文は……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_part_a_after_choices06
    call kag_s_wait

label kag_part_a_choices06__dash__2:
    $ kag_cm()
    if kag_f.re_scenario==0:
        $ kag_f.sn_doremi += 1
        $ kag_f.sn_onpu += 1
        $ kag_f.sn_hana -= 1
        $ kag_f.route=kag_f.route+'B'
    if persistent.firstclear!=0:
        $ kag_playse('9-0102.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0020.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「呪文があった方がぜったいかっこいいって！{w=0.65}ね、どれみもそう思うでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0075.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ……{w=0.6}その、まぁ……{w=0.65}はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0103.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃ、{w=0.55}じゃあ……{w=0.75}やってみます」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「やった！わくわく」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    if persistent.firstclear!=0:
        $ kag_playse('9-0104.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたしの呪文は……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    jump kag_part_a_after_choices06
    call kag_s_wait
    ":【選択肢０６の２おわり】{nw}"

label kag_part_a_after_choices06:

label kag_part_a_inputspell:
    $ kag_set_bookmark('呪文入力')
    $ kag_cm()
    $ kag_input('spell', prompt='※呪文を20文字以内で入力してください。', title='呪文の入力')
    if kag_f.spell==' ':
        jump kag_part_a_inputspell
    if kag_f.spell=='':
        jump kag_part_a_inputspell
    if kag_f.testmode==1:
        pass
    if kag_f.testmode==0:
        if len(kag_f.spell) > 20:
            jump kag_part_a_inputspell
        pass
    $ kag_wait(500, canskip=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「[kag_f.spell]」"
    $ kag_fadeoutbgm(1500)
    $ kag_sound_se('se-032.2.ogg', buf=1)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'white', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('cross', 'bg012', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('A-0004.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「おおぉ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "魔女界にある、わたしのお部屋と同じ作りに変えてみた。"
    extend "\nいつもより片づいているんだけど、みんなにはだまっておこう。"
    $ kag_cm()
    $ kag_playbgm('m14', loop=True)
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0076.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「これで泊まるところは決まったね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0105.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0026.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「あとは、そのカッコやねんけど、どうにかなれへんかな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0106.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？ま、まずいですか？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('3-0027.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「まずいっちゅーか、{w=0.5}ほら、いかにも魔女ですー！って感じやん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if kag_f.event_01==0:
        jump kag_part_a_event__dash__01
    if persistent.firstclear!=0:
        $ kag_playse('9-0107.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「そっか……{w=0.65}それでどれみちゃんが一目でわかったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0077.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「魔女の服装は、こっちでは珍しいからね」"
    $ kag_stopse(buf=0)
    $ kag_cm()

label kag_part_a_event__dash__01:
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0108.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「じゃあ、魔法で人間界の服装に着替えますね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0021.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「待ってりずむちゃん。{w=0.5}それならわたしが着ていないお洋服を、お家から持ってくるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0078.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ギクッ。{w=0.6}い、いやほら、はづきちゃんの着ていないお洋服はよそ行きばっかりだしさ。{w=0.5}お仕事で動きづらそうだし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0028.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「それやったらどれみちゃん貸してあげたら？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0079.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「うーん。{w=0.5}着れなくなったお下がりならあまってるけど、りずむちゃんのサイズにあわないと思うし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0008.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「おかあさん、あたしに着せるつもりで残しておいてるんだろうな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0022.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「ハナちゃんが、\n魔法でバトルレンジャーＶにしてあげる！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0080.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「いや、りずむちゃんは、正義の味方をやりに来たんじゃないんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0109.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、わたしが魔法で……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0022.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「大丈夫。りずむちゃんは人間界初めてなんだし、わたしたちがコーディネイトしてあげるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0022.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「せっかく人間界に来たんだし、やっぱり着物だよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0029.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「着物やったら、今のカッコぐらい目立つで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0081.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ねぇねぇ、角の喫茶店の制服はどう？あれ、かわいいんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0023.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「りずむ～！いっしょにバトルレンジャーＶやろうよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0023.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「やっぱり、わたしのお洋服を……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0030.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ちょっと～。みんなちゃんと考えな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    if persistent.firstclear!=0:
        $ kag_playse('9-0110.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あのう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "わたし、どんなカッコになっちゃうんだろう？"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0028.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「わたしの服をりずむちゃんに貸してあげる。{w=0.6}これなら問題ないでしょ？りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0111.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.35}あ、はい。{w=0.75}それではお言葉に甘えて……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0023.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Oh！It's a good idea！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0082.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「まぁ、りずむちゃんがそう言うなら、いいか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0024.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そうね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0029.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「決まりね。わたし、いったん家に帰って服をとってくるわ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0112.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「お、お願いします！」"
    $ kag_stopse(buf=0)
    $ kag_drawchar('o_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_wait(800, canskip=True)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0083.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「じゃあお店に戻ろうか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    if persistent.firstclear!=0:
        $ kag_playse('9-0113.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', 'Black', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    "ほんの１日のお使いのつもりだったのに、８日間もいることになっちゃった。"
    $ kag_cm()
    "でも、がんばってみるしかないよね。"
    $ kag_cm()
    "そのとき、わたしにしてはめずらしく前向きだったと思うけど、どうしてそうだったのかは、後でわかることになる。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'bg096', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0030.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「いけない。女王様の手紙を持ってきちゃった」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0031.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「でも、やっぱりひっかかるのよね。{w=0.6}どうしてなんだろう……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0032.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あれ？もう１枚手紙があったんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('se-056.ogg', buf=1, loop=False)
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0033.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「これって……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_wait(1500, canskip=True)
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0033.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「なるほど、そういうことだったのね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle01', 'bg014', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    if persistent.firstclear!=0:
        $ kag_playse('9-0114.ogg', buf=0, loop=False)
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、よろしくお願いします！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1500)
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    if kag_f.route=='AAAAAA':
        jump kag_m_b1_gamestart
    if kag_f.route=='AAAAAB':
        jump kag_m_b1_gamestart
    if kag_f.route=='AAAABA':
        jump kag_d_b1_gamestart
    if kag_f.route=='AAAABB':
        jump kag_d_b1_gamestart
    if kag_f.route=='AAABAA':
        jump kag_a_b1_gamestart
    if kag_f.route=='AAABAB':
        jump kag_a_b1_gamestart
    if kag_f.route=='AAABBA':
        jump kag_d_b1_gamestart
    if kag_f.route=='AAABBB':
        jump kag_d_b1_gamestart
    if kag_f.route=='AABAAA':
        jump kag_m_b1_gamestart
    if kag_f.route=='AABAAB':
        jump kag_m_b1_gamestart
    if kag_f.route=='AABABA':
        jump kag_hz_b1_gamestart
    if kag_f.route=='AABABB':
        jump kag_o_b1_gamestart
    if kag_f.route=='AABBAA':
        jump kag_a_b1_gamestart
    if kag_f.route=='AABBAB':
        jump kag_a_b1_gamestart
    if kag_f.route=='AABBBA':
        jump kag_o_b1_gamestart
    if kag_f.route=='AABBBB':
        jump kag_o_b1_gamestart
    if kag_f.route=='BABAAA':
        jump kag_hn_b1_gamestart
    if kag_f.route=='BABAAB':
        jump kag_m_b1_gamestart
    if kag_f.route=='BABABA':
        jump kag_hz_b1_gamestart
    if kag_f.route=='BABABB':
        jump kag_o_b1_gamestart
    if kag_f.route=='BABBAA':
        jump kag_a_b1_gamestart
    if kag_f.route=='BABBAB':
        jump kag_a_b1_gamestart
    if kag_f.route=='BABBBA':
        jump kag_o_b1_gamestart
    if kag_f.route=='BABBBB':
        jump kag_o_b1_gamestart
    if kag_f.route=='ABBBAA':
        jump kag_a_b1_gamestart
    if kag_f.route=='ABBBAB':
        jump kag_a_b1_gamestart
    if kag_f.route=='ABBBBA':
        jump kag_o_b1_gamestart
    if kag_f.route=='ABBBBB':
        jump kag_o_b1_gamestart
    if kag_f.route=='ABBAAA':
        jump kag_hn_b1_gamestart
    if kag_f.route=='ABBAAB':
        jump kag_m_b1_gamestart
    if kag_f.route=='ABBABA':
        jump kag_hz_b1_gamestart
    if kag_f.route=='ABBABB':
        jump kag_o_b1_gamestart
    if kag_f.route=='BBBAAA':
        jump kag_hn_b1_gamestart
    if kag_f.route=='BBBAAB':
        jump kag_hn_b1_gamestart
    if kag_f.route=='BBBABA':
        jump kag_hz_b1_gamestart
    if kag_f.route=='BBBABB':
        jump kag_o_b1_gamestart
    if kag_f.route=='BBBBAA':
        jump kag_hn_b1_gamestart
    if kag_f.route=='BBBBAB':
        jump kag_a_b1_gamestart
    if kag_f.route=='BBBBBA':
        jump kag_o_b1_gamestart
    if kag_f.route=='BBBBBB':
        jump kag_o_b1_gamestart
    if kag_f.route=='ABAAAA':
        jump kag_hn_b1_gamestart
    if kag_f.route=='ABAAAB':
        jump kag_m_b1_gamestart
    if kag_f.route=='ABAABA':
        jump kag_hz_b1_gamestart
    if kag_f.route=='ABAABB':
        jump kag_d_b1_gamestart
    if kag_f.route=='ABABAA':
        jump kag_a_b1_gamestart
    if kag_f.route=='ABABAB':
        jump kag_a_b1_gamestart
    if kag_f.route=='ABABBA':
        jump kag_d_b1_gamestart
    if kag_f.route=='ABABBB':
        jump kag_d_b1_gamestart
    if kag_f.route=='BBAAAA':
        jump kag_hn_b1_gamestart
    if kag_f.route=='BBAAAB':
        jump kag_hn_b1_gamestart
    if kag_f.route=='BBAABA':
        jump kag_hz_b1_gamestart
    if kag_f.route=='BBAABB':
        jump kag_hz_b1_gamestart
    if kag_f.route=='BBABAA':
        jump kag_hn_b1_gamestart
    if kag_f.route=='BBABAB':
        jump kag_a_b1_gamestart
    if kag_f.route=='BBABBA':
        jump kag_hz_b1_gamestart
    if kag_f.route=='BBABBB':
        jump kag_d_b1_gamestart
    if kag_f.route=='BAAAAA':
        jump kag_hn_b1_gamestart
    if kag_f.route=='BAAAAB':
        jump kag_m_b1_gamestart
    if kag_f.route=='BAAABA':
        jump kag_hz_b1_gamestart
    if kag_f.route=='BAAABB':
        jump kag_d_b1_gamestart
    if kag_f.route=='BAABAA':
        jump kag_a_b1_gamestart
    if kag_f.route=='BAABAB':
        jump kag_a_b1_gamestart
    if kag_f.route=='BAABBA':
        jump kag_d_b1_gamestart
    if kag_f.route=='BAABBB':
        jump kag_d_b1_gamestart
    call kag_s_wait
    return
