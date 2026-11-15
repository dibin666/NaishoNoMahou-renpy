# おジャ魔女あどべんちゃ～「ないしょのまほう」跨平台重构调研与架构报告

## 1. 项目背景与原版技术剖析

原作《おジャ魔女あどべんちゃ～「ないしょのまほう」》基于 Windows 时代的 **KiriKiri2 (`2.23 beta`) + KAG (`3.20 release`)** 引擎制作，仅提供 Windows 安装包（InstallShield `Data1.cab` + `No CD Patch/patch.xp3`）。其核心限制在于：

1. **单平台锁定**：依赖 Win32 GUI 菜单栏、`launch.exe`（Alpha-ROM 光盘校验及 Windows 注册表读取，官方补丁 `No CD Patch/patch.xp3` 通过在 `first.ks` 跳转 `*alphaok` 旁路）、原生 Shift-JIS (`cp932`) 编码以及 Windows 系统字体 `ＭＳ ゴシック`。
2. **封闭与专有格式**：所有图像使用 `TLG5.0` 无损压缩并封装在未加密的 `XP3` 归档包内，按钮采用横/纵向多态图集（3 态或 4 态拼接），转场依赖灰度规则遮罩（`rule/*.png`），视频为旧式 MPEG-1 (`640x480`)。
3. **缺少原生 i18n 机制**：脚本文本、变量逻辑与 UI 硬编码在同一套 `.ks`/TJS 代码中，无法直接热切换简中或其他语种。

### 1.1 原版数据包逆向与资产清单

通过对 `おジャ魔女あどべんちゃ～「ないしょのまほう」/Data1.cab`（含内嵌于可执行体偏移 `2876928` 的 `New_File`）与 `No CD Patch/patch.xp3` 的完整逆向分析，确认所有 XP3 归档均为未加密（`flags=0`，Zlib 压缩或原始分块）格式：

| 归档 / 来源 | 内容概览 | 数量 / 关键发现 |
| :--- | :--- | :--- |
| `New_File` (内嵌 XP3) | 核心插件与转场规则图 | `startup.tjs`, `others/about.ks`, `plugin/*.ks` (`plug_zoom`, `plug_gvolume`, `plug_staffroll`, `plug_rclick_tjs`, `ExHistoryLayer`), `rule/*.png` (8 张灰度遮罩) |
| `system.xp3` | 引擎配置与系统光标资源 | `Initialize.tjs`, `Config.tjs`, `AfterInit.tjs`, `Menus.tjs`, `MainWindow.tjs`, `LineBreak_a.png` (`270x24`, 15 帧), `pageBreak_a.png` (`288x24`, 12 帧), `infoI.png` + `infoI_m.png` |
| `scenario.xp3` + `patch.xp3` | 游戏主干及分支剧本 | `first.ks`（采用 `patch.xp3` 免 CD 版本）+ **68 个 `.ks` 剧本**（归档含 78 个条目：1 个 `first.ks`、68 个 `.ks` 剧本及 9 个占位说明 `.txt`，覆盖 `00. part_A` 至 `08. other`，含 6 位角色路线、2 个番外篇、6 个 Endroll、标题/读档/设置/鉴赏菜单） |
| `image.xp3` | 系统 UI 图像 | **27 个 TLG5.0**（右键菜单背景 `800x600`、4 态 `w/4` 右键/返回按钮、3 态 `w/3` 主菜单/Option/Album 按钮、空白存档缩略图 `thm_no` `133x100`） |
| `fgimage.xp3` | 人物立绘与事件 CG | **388 个 TLG5.0**（`char/01..08/`, `event/00..06/`, 46 个 3 态 `cgmode/cg*.tlg` `390x100` 缩略图） |
| `bgimage.xp3` | 背景、框架与过场底图 | **259 个 TLG5.0 + 3 个 PNG + 63 个 JPG**（含 `bg/`, `eyecatch/`, `endroll/`, `mesFrame.tlg`, `c_frm.tlg`, `maintitle.tlg`, `option.tlg`, `album*.tlg`, `memorial_all.png`） |
| `bgm.xp3` | 背景音乐 | **26 个 `.ogg`**（含主题曲与结局演唱曲 `bgm-v01`–`bgm-v03`；`bgm-001..004`, `bgm-002.1`, `bgm-002.2` 在 `sound.xp3>11. bgm/` 中亦有副本） |
| `sound.xp3` | 全程语音与音效 | **6,563 个 `.ogg`**（含角色语音与系统音效；`bgm-v02`/`bgm-v03` 同时在运行时兼容 SE Buffer 回放） |
| `video.xp3` | 片头动画 | **`どれみ1015.mpg`**（MPEG-1 Video `640x480` 30fps + MP2 立体声 44.1kHz，游戏中全屏拉伸至 `800x600`） |

### 1.2 原版核心行为与脚本特异点

1. **分辨率与消息框布局**：`800x600` 画布；默认消息层 `layer=message0` (`left=20, top=465, width=768, height=105`)，搭配 Layer 3 (`mesFrame.tlg`, `z=25000`, `autohide=true`) 实现淡入淡出对话底框；选择肢与菜单场景重设为 `left=16, top=16, width=768, height=568`。
2. **排版与打字速度**：原版字体 `ＭＳ ゴシック`（等宽 `24px`、行间距 `6px`、白字带 `0x000000` 阴影、`marginRCh=3`），文字速率快/中/慢分别对应 `10 / 30 / 50 ms/字`。
3. **四路独立音频通道**：BGM (`kag.bgm`, 默认音量 `60%`) + 3 个 SE Buffer（`buf=0` 为语音、`buf=1` 为单次音效、`buf=2` 为 `[se_loop]` 循环音效）。音量设置（`plug_gvolume.ks`）提供静音及 `5%`–`100%` 步进。
4. **原版脚本已知瑕疵（重构层需透明兼容）**：
   - `01. doremi/d_B4.ks:316` 调用 `[playbgm storage="se-014"]`，但资源目录仅存在 `se-014.1.ogg` 与 `se-014.2.ogg`（映射为 `se-014.1.ogg`）。
   - `08. other/extra.ks:495` 注释块引用的 `どれみ1012.mpg` 与 `prologue.ks:317` 的 `どれみ1015.mpg` 统一指向转换后的 OP 视频。
   - `07. omake/omake_p.ks:679` 拼写笔误 `f.case1='*ture_0'+intrandom(1,3)` 导致第 11 题答对分支失效，需在运行时纠正为 `*true_0`。
   - `part_A.ks:45` 等多处资源引用省略扩展名（如 `9-0017.2`），且混用正反斜杠与大小写，需建立统一的大小写无关路径解析表 `asset_map.rpy`。

---

## 2. 2025–2026 跨平台视觉小说框架调研与选型

针对 **Linux / Windows 原生跨平台、完善的 i18n 机制、复杂 KAG3 特效/UI 一比一复刻能力** 三个核心指标，对当前主流方案进行了横向评估：

| 框架 / 引擎 | 跨平台与分发 | i18n 多语言能力 | KAG3 转场与定制 UI 契合度 | 综合评估 |
| :--- | :--- | :--- | :--- | :--- |
| **Ren'Py 8.x (`8.6.0`, Python 3)** | 原生生成 Linux (`x86_64`) 与 Windows 免安装发行包，内置 SDL2/OpenGL2 硬件加速与字体打包 | **行业标杆**：内置 `tl/<lang>/` 抽取、`TranslateString` 与界面语言热切换，支持多语种字体回退与独立排版 | **极高**：原生 `ImageDissolve` 直接对应 KAG `rule/*.png`；ATL/MatrixColor/Transform 支持震动、Sepia、缩放、马赛克与任意坐标按钮 | **首选推荐**。既满足 100% 功能复刻，又提供最标准的可持续多语言翻译生态 |
| **WebGAL / WebGAL Craft** | 基于 Web + Electron/Tauri，支持 Win/Linux | 支持多语言文件夹与字体替换 | 剧本语法偏向轻量化现代 ADV，缺少对 KAG3 复杂动态 TJS 表达式、`rule` 灰度转场序列、局部 4 态按钮与 2000 行定制历史层的开箱适配 | 中等（UI/脚本重改成本高于 Ren'Py） |
| **Godot 4 + Dialogic 2** | 原生支持 Win/Linux | 内置 CSV/PO 本地化，强大 | 通用游戏引擎优势在玩法融合；但重现 KAG3 特定消息框悬挂缩进、通用规则转场与右键 30 槽存档系统需编写大量 GDScript 基础架构 | 中等（工程冗余较大） |
| **Pixi'VN / Monogatari** | Web 优先，桌面依赖打包外壳 | 配合 i18next 等 JS 库实现 | 更适合网页发行；桌面端系统菜单栏、鼠标滚轮历史回顾、复杂存档元数据与视频流控制成熟度弱于 Ren'Py | 较低 |
| **Unity + Naninovel** | 商业引擎全平台支持 | 官方本地化插件支持 | Naninovel 为付费闭源商业插件，运行时体积大，不利于轻量纯正移植与开放多语言协作 | 不适用 |
| **KiriKiri SDL2 / Kirikiroid2** | 可运行原 XP3 | **弱**：直接沿用 Shift-JIS 单语言原代码，缺乏结构化翻译提取与动态语言热切换机制 | 原生兼容但难以优雅扩展多语言 UI、字体切换与现代维护 | 不符合 i18n 重写目标 |

**最终选型**：采用 **Ren'Py 8 (`8.6.0` SDK)**。

---

## 3. 系统重构架构设计

### 3.1 工程目录规划

```text
.
├── RESEARCH_AND_ARCHITECTURE.md          # 本调研与架构文档
├── run_linux.sh / build_distributions.sh # 启动脚本与 Linux/Windows 打包脚本
├── tools/
│   ├── tlg5_fast.c -> libtlg5.so         # C 高性能 TLG5.0 无损解码共享库 (LZSS 4096B)
│   ├── extract_and_convert.py            # Data1.cab/XP3 自动化解包、切图与转码管线
│   ├── transpile_ks.py                   # KAG3 (.ks) -> Ren'Py (.rpy) 全量编译器
│   └── verify_project.py                 # 资产完整性、剧本标签可达性与 i18n 自动化校验
└── renpy_project/
    └── game/
        ├── options.rpy / gui.rpy         # 800x600 配置、音频通道、打包规则与窗口图标
        ├── asset_map.rpy                 # 大小写无关资产路径及无扩展名自动解析表
        ├── kag_runtime.rpy               # KAG3 宏/转场/特效/TJS 变量桥接/存档锁/语音同步引擎
        ├── screens_kag.rpy               # 顶栏菜单、Title、右键菜单、30槽存读档、2000行历史、Extra鉴赏
        ├── i18n.rpy                      # 日文(ja) / 简中(zh_cn) 运行期热切换与独立 OpenType (.otf) 字体映射
        ├── tl/zh_cn/                     # 简体中文 UI、菜单、书签、选项、Omoide 标题与系统提示翻译
        ├── scenario/*.rpy                # 自动生成的 68 个剧本模块 + _label_index.rpy 索引
        ├── images/ / audio/ / video/     # 全 ASCII 安全路径：PNG 资产、6589 个 OGG、WebM VP8+Vorbis OP 视频
        └── fonts/                        # 从 NotoSansCJK-{Regular,Bold}.ttc 拆分的 8 个独立 OpenType (.otf) 字体
```

### 3.2 关键技术映射

1. **视觉与字体一致性（`Noto Sans Mono CJK` 精确对齐）**：
   - 从系统 `NotoSansCJK-Regular.ttc` 与 `NotoSansCJK-Bold.ttc` 拆分生成 8 个独立 OpenType 字体文件（`NotoSansMonoCJKjp/sc` 与 `NotoSansCJKjp/sc` 各含 Regular/Bold，避免 `N@file.ttc` 语法触发 Ren'Py `lint` 加载告警，并提升 FreeType/HarfBuzz 跨平台一致性），将原版 `ＭＳ ゴシック`（`24px` 等宽、行距 `6px`、白字黑影）准确映射为 `NotoSansMonoCJKjp-Regular.otf`。
   - 日文模式使用日文字形（`NotoSansMonoCJKjp` 等宽 1:2 / `NotoSansCJKjp` 比例），简体中文模式使用简中字形（`NotoSansMonoCJKsc` / `NotoSansCJKsc`），并通过 `config.font_replacement_map` 自动关联对应 Bold 字重。
2. **TLG5.0 解码与图集自动化切分**：
   - 使用 C 语言实现标准 4096 字节环形缓冲 LZSS 解码器 `libtlg5.so`，配合 Python/Pillow 将 674 张 TLG5.0 转为标准 RGBA PNG。
   - 按原版 KAG 坐标规范自动切片：右键/返回 `w/4` 按钮切为 idle/clicked/hover/disabled；Title/Option/Album/CG 缩略图 `w/3` 切为 idle/hover/down；`LineBreak_a.png`（15 帧 `18x24`）与 `pageBreak_a.png`（12 帧 `24x24`）拆帧并重构为往复动画；`infoI.png` 与 `infoI_m.png` 合并为带 Alpha 通道的 PNG。
3. **KAG3 剧本转译器 (`transpile_ks.py`) 与运行时 (`kag_runtime.rpy`)**：
   - **完整状态机还原**：实现 `first.ks` 中全部宏观指令（`[mesFrame]`, `[changeType_*]`, `[selType_*]`, `[choices]`, `[cg_on_*]`, `[se_loop]`, `[cwt]`, `[wait1]`, `[wait2]` 等）、`f.*` 路线变量、`sf.*` -> `persistent.*` 全局收集标记。
   - **对话与语音精确同步**：将 `[playse storage=... buf=0]` + 文本 + `[ws]` / `[l]` / `[cm]` 编译为带文本积累（支持同页 `[l]` 追加续写）、`{nw}` 自动衔接及强制/可跳过语音等待的 Ren'Py 语句，保留原版行内暂停点与点击等候动画。
   - **TJS 表达式与动态分支**：将 `part_A.ks`（含 6 选分支、64 路 `f.route` 判定、`[input]` 咒文输入模态框）及所有 `cond="..."` / `[if]` / `[emb]` 安全转换为等效 Python/Ren'Py 运行时求值；保留 6500+ 条文本与语音对应的可翻译条目结构。
4. **全功能 UI 与扩展系统复刻**：
   - **顶部系统菜单栏**（System / Text / Movie / Volume / Display / Language / Help）：支持快速存读档、返回标题、文字速度（Fast/Normal/Slow/Instant）、字体切换、OP 动画开关（`persistent.movie_skip`）、BGM/Voice/SE 五档独立混音及日/简中一键热切换。
   - **右键菜单 & 30 槽位存读档**（`plug_rclick_tjs.ks`）：6 页 x 5 槽（`データ 1～5` 至 `26～30`），完整支持截图缩略图、时间、路线书签、自定义注释输入框与 `[x]` 存档锁（防误删/误覆盖），以及 `load.ks` 从标题直达读档页的行为。
   - **2000 行可滚动历史记录**（`ExHistoryLayer.ks`）：还原右置滚动条、关闭按钮、行高 `26px` 与 `2000` 行上限记录。
   - **Extra 鉴赏模式**（`extra.ks`）：7 页角色 CG 相册（含 3 态缩略图解锁与全图浏览）与 7 类角色章节回想（Omoide）。
