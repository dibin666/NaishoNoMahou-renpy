# Auto-generated from 05. momo/m_B2.ks by tools/transpile_ks.py
label kag_m_b2:

label kag_m_b2_gamestart:
    $ kag_history_opt(output=False, enabled=None)
    if kag_f.re_scenario==1:
        $ kag_set_rclick(False)
    $ kag_wait(200, canskip=True)
    $ kag_cancelskip()
    $ kag_cm()
    $ kag_changetype('cross', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_changetype('blind01', 'eye_momo.tlg', time_ms=1000, bgcolor='0x000000')
    $ kag_changetype('blind01', 'bg096', time_ms=1000, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_history_opt(output=True, enabled=None)

label kag_m_b2_mo__dash__02_00:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_playbgm('bgm-001', loop=True)
    "照りつける太陽。"
    extend "道路がかげろうのようにゆれている。"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0284.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあ、今日は町の中を案内するね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg091', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_01:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0285.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「この公園は緑がいっぱいでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わあ……{w=0.65}すごいですね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg068', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0286.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「毎年夏にここでたくさんの人がきもだめしをするんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「きもだめし……？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0287.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「きもだめしって、火の玉とか幽霊とか出てきてこわいけど、とってもおもしろいんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0287.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうだ、たぶん今年もやるからりずむちゃんも参加しようよ、きもだめし」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あの、わたし、こわいのとかって苦手で……」"
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0288.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そう？{w=0.4}じゃあしょうがないね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_playbgm('m60', loop=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg079', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "毎年花火大会がある河原。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg085', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "ブランコと砂場とすべり台だけの小さな公園。"
    extend "そういえば、昨日はじめてどれみちゃんと会ったのは、この公園だっけ。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg027', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "どれみちゃんの家。"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg093', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    "学校へ通じる長い坂道。"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg060', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_02:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_playbgm('bgm-001', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「わぁ～！{w=0.4}大きいですね～」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0289.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ここがあたしたちの通う、美空第一小学校だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「へええ……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0290.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「入りたい？{w=0.4}じゃあ、中に入ってみる？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？{w=0.4}わたし、入っていいんですか？」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0291.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！{w=0.4}どうせ夏休みだし、大丈夫だよ！{w=0.4}あたしたち、アヤシーものじゃないし！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし魔女だし、ホントはじゅうぶんあやしいと思うんですど……」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg053', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_03:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「静かですね……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0292.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ふだんは、すっごくにぎやかなんだけどね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0293.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ねえ！{w=0.4}りずむちゃんは学校のどこ見てみたい？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ん～、音楽室とか図書室とか、見てみたいです」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0294.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「お～！{w=0.4}ミュージックルームにライブラリーね！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「えっ？{w=0.4}う、うん！」"
    $ kag_cm()
    $ kag_playse('5-0295.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「じゃあ、さっそく Let's go！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg248', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_04:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_playse('se-007.ogg', buf=0, loop=False)
    $ kag_ws(buf=0, canskip=True)
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「気持ちいい風……」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0296.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あたしたち、音楽クラブなんだよ。{w=0.4}どれみちゃんがピアノ、はづきちゃんがバイオリン。"
    $ kag_playse('5-0296.2', buf=0, loop=False)
    extend "あいちゃんがハーモニカでおんぷちゃんがフルート。{w=0.4}そしてわたしが……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0297.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ギターを担当して合唱の練習してるの」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「みなさん、\nいろいろな楽器が演奏できてすごいですね！」"
    $ kag_cm()
    $ kag_playse('5-0298.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「へへ、じゃあ、次、図書室へ行ってみよう～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg224', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_05:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「本がたくさんですね～」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0299.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「すごいでしょ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でも魔女界とちがって、ほうきを使わないから高さはないんですね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_sound_se('se-007', buf=1)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0300.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Oh！{w=0.4}ぽっぷちゃ～ん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0185.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あ、あれ？{w=0.4}ももちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぽっぷちゃん！」"
    $ kag_cm()
    $ kag_playse('7-0186.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg224', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_06:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0187.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ももちゃんとりずむちゃん、ここで何してたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0301.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃんに学校案内してたんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0188.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そうなんだ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0302.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ぽっぷちゃんは？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0189.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あたし？{w=0.4}あたしは読書感想文用に読む本を探しにきたんだ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0303.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「まだまだ夏休みは始まったばっかりなのに、ぽっぷちゃんすごいねぇ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0303.2', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「わたしなんか宿題まだぜ～んぜんだよ～アハハハハ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0190.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「知らないよ～？{w=0.4}お姉ちゃんみたいに後であわてても～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0190.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あっ、そうだ！{w=0.3}りずむちゃん。学校見学はどう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「校舎がとっても広くて、色々な物がおいてあってびっくりです」"
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0191.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そうでしょ～！{w=0.4}あたしも去年入学したときはびっくりしたなぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「わたし、人間界のこと、ほとんど知らないからとても新鮮でした」"
    $ kag_cm()
    $ kag_drawchar('m_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0304.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「う～ん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0192.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ももちゃん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「どうしたの？」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0305.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ねぇ！{w=0.4}りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい？」"
    $ kag_cm()
    $ kag_playse('5-0306.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「せっかく学校へ来たんだから、授業していかない？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？」"
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0193.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「へっ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0307.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「りずむちゃんに人間界のことを教える授業をするの！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0307.2.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「あたしとぽっぷちゃんが先生になってさ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0194.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えぇ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg253', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_07:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    "わたしは教室の一番前の席に座っている。そしてももちゃんは、なぜか見習い服。"
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0195.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「も、ももちゃん、何で見習い服なの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "何よりもまずそれが気になったらしいぽっぷちゃんがももちゃんに質問する。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「うんうん」"
    $ kag_cm()
    $ kag_drawchar('m_m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0308.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ノォ～、{w=0.4}ぽっぷちゃん、これからわたしたちは先生だよ？{w=0.4}だから……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m408d', loop=True)
    $ kag_freeimage(layer='3', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='0', page='back')
    $ kag_changetype('circle02', 'bg405.tlg', time_ms=300, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_playse('5-0309.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ペルタンペットン　パラリラポン」{nw}"
    $ kag_ws(buf=0, canskip=True)
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0310.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「先生になれ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('circle02', 'white', time_ms=300, bgcolor='0x000000')
    $ kag_sound_se('se-047.ogg', buf=1)
    $ kag_cm()
    $ kag_wait(800, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '05ももこ-02', time_ms=1500, bgcolor='0x000000')
    $ persistent.cgm1=1
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_08:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_playse('7-0196.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「も、ももちゃん……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0311.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ノォ～！{w=0.4}今からは『ティーチャーももこ』だよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0197.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あ……{w=0.55}あう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「かっ、かっこいい！{w=0.4}ティーチャーももこ！」"
    $ kag_cm()
    $ kag_playse('7-0198.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「えええっ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0312.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「OK！それじゃあ、さっそく授業を始めますよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_playse('5-0313.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それじゃあ、まずは人間界の規則についての授業をしま～す」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0314.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「はい！{w=0.4}これはなんと読みますか？{w=0.4}\nん～と……{w=0.6}りずむちゃん！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ま……{w=0.65}まほうです」"
    $ kag_cm()
    $ kag_playse('5-0315.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「Good！{w=0.4}正解！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0199.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「も、ももちゃん、この授業っていったい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0316.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「人間界で、魔法は人前で使っちゃいけませ～ん。{w=0.4}それは、魔女だとバレてしまうからで～ス！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_playse('7-0200.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あは、あははは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('cross', '05ももこ-02', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playse('5-0317.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それでは、\nこれで人間界についての授業を終わります！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('ももこ「')
    "ももこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……？」"
    $ kag_cm()
    "静まる教室。"
    extend "\nティーチャーももこはわたしに何かを期待する目線を送っている。"
    extend "\nな、なんだろう？"
    $ kag_cm()
    $ kag_playse('7-0201.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「き、きり～つ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "そうか、号令だ！\nハッとなってわたしはあわてて立ち上がる。"
    $ kag_cm()
    $ kag_playse('7-0202.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「れい～。{w=0.4}ちゃくせき～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('5-0318.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「はい！{w=0.4}終わり～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ありがとうございました～」"
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg253', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_09:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    "まさか、人間界の学校でももちゃんに授業を受けたなんて、\n女王様もびっくりするだろうな。"
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0203.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「はぁ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ももこ「')
    "ももこ「……」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_drawchar('p_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「……」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('5-0319.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「二時間目、国語！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playbgm('m52', loop=True)
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0204.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「に、二時間目ぇぇ！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0320.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ここからは、ぽっぷ先生の授業だよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0205.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あ……{w=0.6}え……{w=0.55}あ、あたし？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0321.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「うん！{w=0.4}だって、日本語はぽっぷちゃんの方が先輩だから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ぽっぷ先生！{w=0.4}お願いします！」"
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0206.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「なんであたしが……{w=0.6}ああ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0207.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「で、では、今から国語の授業を始めます！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'black', time_ms=1500, bgcolor='0x000000')
    $ kag_wait(500, canskip=True)
    $ kag_changetype('note', 'bg001', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_10:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「すっ、ちゃっ、さささささっ」"
    $ kag_cm()
    $ kag_drawchar('a_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0829.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん、何やってんの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、あいちゃん。{w=0.4}みんな……」"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0637.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「学校から帰ってきたのね。{w=0.4}どうだった？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「し、しまった。{w=0.4}まだまだ修行が足りないわ！」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0570.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「しゅ、修行！？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「でもみなさん、さすがですね。{w=0.4}１発で見つけられるなんて」"
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0851.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「は？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃんから教わったんです。"
    extend "\n日本の人は、大なり小なり必ず忍術の心得があるって」"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「帰ってきていきなり見つかるなんて、わたしもまだまだですね」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0045.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「ええ～っ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、そうだそうだ。{w=1}ええ～い、ひかえおろっ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0852.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「りずむちゃん、ひょっとして……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「おっかしいなあ。{w=0.4}もう１回、ひかえおろっ！！」"
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0571.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それも、ももちゃんに教わったの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「な、なんでわかるんですか！？」"
    $ kag_cm()
    $ kag_drawchar('a_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0830.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「なんでって、そらわかるって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「こうしたら日本人なら誰でも『ははっ～』っていっていっせいにひれ伏すって、{w=0.4}ももちゃんに教わったんです」"
    $ kag_cm()
    $ kag_drawchar('m_n_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0322.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ダメだよ、りずむちゃん。{w=0.4}むやみに使っちゃいけないって」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ももちゃん。{w=0.4}すみません、使ってみたくてつい……」"
    $ kag_cm()
    $ kag_drawchar('m_n_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0323.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「その技がきくのは、アクダイカンってヤツとその一味だけなんだから」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「え？{w=0.4}そうなんですか？{w=0.4}……{w=0.55}わたし、カンちがいしてました」"
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0831.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ももちゃん、そういう問題やないと思うよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_n_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0324.1.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「早く日本の習慣になれるためには、見えていることだけを真似ていてはダメデース。"
    $ kag_playse('5-0324.2', buf=0, loop=False)
    extend "その『腎臓』に飛び込んでいかないとイケマセーン」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0638.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「『真髄』って言いたいみたいね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0832.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「アカン、聞いてへん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_n_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0325.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「一にも二にも、修行あるのみデース」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！{w=0.4}わたし、がんばります！」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「……」"
    $ kag_cm()
    $ kag_drawchar('m_n_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0326.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「さ、りずむちゃん、困ったときはこの一言だよ……。{w=0.4}\nRepeat　after　me！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい！」"
    $ kag_cm()
    $ kag_stopbgm()
    $ kag_drawchar('m_n_10.tlg', time_ms=100, sepia=False, canskip=True)
    $ kag_playse('5-0327.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「『ヒデエヤ、ゴインキョ！』」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「『ヒデエヤ、ゴインキョ！』」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_quake(time_ms=500, hmax=5, vmax=15)
    $ kag_sound_se('se-018.2.ogg', buf=1)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……みなさん、なんでこけてるんですか？」"
    $ kag_cm()
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_11:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0853.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なんか、ビミョーにっつーかはげしく間違ってるよね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0833.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0572.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「きっと昔の日本のことを今の人間界の文化みたいに、{w=0.4}ももちゃんが教えちゃってるのかもしれないわ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0834.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「日本文化っちゅーより、テレビとちゃう？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0639.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「りずむちゃん。{w=0.4}人間界ぜんたいがそういう感じだと思ってるかもね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0855.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ぽ～っ～ぷ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0208.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うっ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0856.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あんたも、その場にいたんでしょ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0209.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_10.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0857.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「だったら何で……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0210.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「だ、だってしょうがないじゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0856.5.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「？」"
    $ kag_cm()
    $ kag_drawchar('p_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0211.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「ももちゃんが魔法で先生になって、{w=0.4}りずむちゃんが目をキラキラさせながら授業してたんだよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_playse('7-0212.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「とても止められるような状況じゃないよ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_06.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0858.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ももちゃん、なりきっちゃうからね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0835.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「ああなると、{w=0.4}ちょっとやそっとのツッコミでは止まれへんしなあ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0573.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「そ、それは仕方ないわよね……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_04.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0640.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「それならなおさら、わたしたちがりずむちゃんにきちんと人間界のことを説明しなおさなきゃ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0836.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そやな。{w=0.4}誤解されたまま、ちゅうのも困るしな」"
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

label kag_m_b2_mo__dash__02_12:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_playbgm('m67', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ここに糸を通して……」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0328.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「そうそう」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0294.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「それで、ここにビーズを入れるんだよ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    "ももちゃんとハナちゃんにビーズメーカーの使い方を教わっていると、キッチンに行った５人が戻ってきた。"
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい」"
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0329.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それで、このレバーを回して」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「……」"
    $ kag_cm()
    $ kag_playse('5-0330.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「それで、最後にこことここを結んで」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0295.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「でき上がりだよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「ふう～。{w=0.4}で、できました！」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0331.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「やったね！{w=0.4}りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_05.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0574.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「あ、あの、{w=0.4}お取り込みの最中、ごめんなさい」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0332.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ん？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0837.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「りずむちゃん……{w=0.65}ちょっとええかな？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「はい、何でしょう？」"
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0641.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あ、あのね。{w=0.4}今日りずむちゃんが習ったことなんだけど」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0333.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ねぇ～、みんな～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0296.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どうしたの？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0859.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あ、いや、何でもないよ～ももちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0838.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「そうそう！{w=0.4}何でもない。何でもない～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_03.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0642.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「あは、あははは……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0334.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「ん？それよりさ、{w=0.4}今りずむちゃん、ビーズのアクセサリー作ったんだよ～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0297.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「うん！{w=0.4}初めてなのにとぉっても上手なの～。{w=0.4}みんなも見て見て～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0860.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「どれどれ？{w=0.4}わあ～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0575.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「きれいね～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「あ、ありがとうございます」"
    $ kag_cm()
    "なんかちょっと照れくさい。"
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0643.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「この、青いビーズの使い方がきれいよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0839.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「始めてとは思えへんできばえやな～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0576.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「それにこの大きさ……{w=0.55}ネックレスにはちょうどいい大きさよね」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hn_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('6-0298.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ハナ\u3000「')
    "ハナ　「どれみより上手～」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0213.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「そうそう、お姉ちゃんのよりず～っとかわいいよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_09.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0861.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「なにさぁ～その言い方～！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='1', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg008', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()
    $ kag_cm()
    $ kag_playbgm('m42', loop=True)
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0862.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「ね、ねぇ……{w=0.55}みんな」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('hz_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('2-0577.ogg', buf=0, loop=False)
    $ kag_set_next_indent('はづき「')
    "はづき「……{w=0.55}うん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('a_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('3-0840.ogg', buf=0, loop=False)
    $ kag_set_next_indent('あいこ「')
    "あいこ「今日のところはやめとこか」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('o_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('4-0644.ogg', buf=0, loop=False)
    $ kag_set_next_indent('おんぷ「')
    "おんぷ「また明日にしましょうよ」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0214.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「うんうん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('d_01.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('1-0863.ogg', buf=0, loop=False)
    $ kag_set_next_indent('どれみ「')
    "どれみ「あんなにうれしそうだもんね、りずむちゃん」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ kag_changetype('note', 'bg016', time_ms=1500, bgcolor='0x000000')
    $ kag_mesframe()

label kag_m_b2_mo__dash__02_13:
    $ kag_set_bookmark('「２日目」ももこ先生の体験入学！？')
    $ kag_cm()
    $ kag_playbgm('m39', loop=True)
    $ kag_set_next_indent('りずむ「')
    "りずむ「ももちゃん、今日はありがとう！」"
    $ kag_cm()
    $ kag_drawchar('m_02.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0335.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「どういたしまして！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_set_next_indent('りずむ「')
    "りずむ「また、人間界について色々教えてください！」"
    $ kag_cm()
    $ kag_playse('5-0336.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「No problem！{w=0.4}えっへん、まかせて～！{w=0.4}今度は『サクラ吹雪』について教えてあげるよ！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_freeimage(layer='0', page='fore')
    $ kag_playse('A-0047.ogg', buf=0, loop=False)
    $ kag_history_opt(output=False, enabled=None)
    $ kag_history_opt(output=True, enabled=None)
    $ kag_set_next_indent('「')
    "「ダメええ～～っ！！」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('m_08.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('5-0337.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ももこ「')
    "ももこ「んあ？」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_drawchar('p_07.tlg', time_ms=600, sepia=False, canskip=True)
    $ kag_playse('7-0215.ogg', buf=0, loop=False)
    $ kag_set_next_indent('ぽっぷ「')
    "ぽっぷ「あたし、知～らないっ……」"
    $ kag_stopse(buf=0)
    $ kag_cm()
    $ kag_fadeoutbgm(1000)
    $ kag_freeimage(layer='0', page='back')
    $ kag_freeimage(layer='3', page='back')
    $ persistent.m2_s=1
    if kag_f.re_scenario==1:
        jump kag_extra_return_s
    jump kag_m_b3_gamestart
    return
