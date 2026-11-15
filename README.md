# おジャ魔女あどべんちゃ～「ないしょのまほう」 (Ren'Py 8 Cross-Platform Port)

原作（KiriKiri2 / KAG3）向 **Ren'Py 8** 移植的跨平台版本（v1.0.0），支持 **Linux x86_64** 与 **Windows x86_64** 开箱即玩，并内置 **日语（原版）/ 简体中文** 双语实时切换。

> 本仓库仅包含移植源码、剧本转译结果、简中本地化脚本与图像、解包转码工具及打包脚本；不包含原版游戏的解包音画媒体与字体包（完整即玩包请从 **Releases** 下载）。

---

## 玩家快速游玩（推荐）

前往本仓库的 **[Releases](https://github.com/dibin666/NaishoNoMahou-renpy/releases)** 页面下载对应平台的免安装压缩包，无需预先安装 Python 或 Ren'Py：

- **Linux (`x86_64`)**: `NaishoNoMahou-1.0.0-linux.tar.bz2`
  ```bash
  tar -xjf NaishoNoMahou-1.0.0-linux.tar.bz2
  cd NaishoNoMahou-1.0.0-linux
  ./NaishoNoMahou
  ```
- **Windows (`x86_64`)**: `NaishoNoMahou-1.0.0-win.zip`
  解压后直接双击运行 `NaishoNoMahou.exe`。

### 存档位置

`options.rpy` 将 `config.save_directory` 设为 `None`，采用**绿色便携模式**：所有存档与全局解锁进度（`persistent`）默认保存在游戏根目录旁的 `game/saves/` 中，方便整体备份与迁移。

### 主要特性

- **双平台点击即玩**：Linux 自带轻量静态 ELF 启动器（自动配置 X11 / 原生 GTK3 菜单栏）及独立封装运行库，Windows 直接运行 `NaishoNoMahou.exe`。
- **日语原文 / 简体中文切换**：涵盖全部 60 份可本地化剧本文件、UI 字符串、标题菜单、简体中文游戏 Logo 及按钮图片（`renpy_project/game/tl/zh_cn/`）。
- **字体模式切换**：支持「等幅ゴシック（1:2 原作排版准据）」与「プロポーショナルゴシック」切换。
- **KAG 特性兼容**：还原 30 格存档/锁定/书签备注、缩略图、右键系统菜单、顶栏菜单及完整 **特典（CG 相册 / 剧情回忆 / 隐藏特典）**；序章支持自动播放与点击推进。

---

## 仓库目录结构

```text
.
├── build_distributions.sh        # 编译脚本与构建 Linux / Windows 分发包
├── run_linux.sh                  # 本地通过 Ren'Py SDK 直接运行工程
├── docs/
│   └── RESEARCH_AND_ARCHITECTURE.md  # 原版引擎逆向分析与移植架构文档
├── renpy_project/
│   └── game/
│       ├── asset_map.rpy         # 资源与多态按钮映射表
│       ├── gui.rpy / options.rpy # 界面样式、声道、便携存档及打包规则
│       ├── i18n.rpy              # 多语言与字体运行时切换支持
│       ├── kag_runtime.rpy       # KAG3 语义兼容运行时（图层/转场/音效/快捷键）
│       ├── screens_kag.rpy       # 菜单、对话框、存档界面、历史与设置面板
│       ├── gui/                  # 应用与窗口图标
│       ├── scenario/             # 转译自原版的 68 个场景剧本及索引
│       └── tl/zh_cn/             # 简体中文文本翻译与本地化 UI/标题图片
└── tools/
    ├── extract_and_convert.py    # 从原版 Data1.cab + patch.xp3 提取/转换媒体资源
    ├── tlg5_fast.c               # KiriKiri TLG5.0 C 解码器源码
    ├── transpile_ks.py           # KAG (.ks) 到 Ren'Py (.rpy) 的剧本转译器
    ├── linux_launcher.c          # Linux 静态点击启动器源码
    ├── verify_project.py         # 全工程静态与无头集成校验入口
    └── runtime_smoke_test.py     # 无头实机运行时与核心路径冒烟测试
```

---

## 开发者从源码构建（可选）

### 环境依赖

- [Ren'Py 8 SDK](https://www.renpy.org/)（默认读取 `RENPY_SDK` 环境变量，或 `~/.local/opt/renpy-8.6.0-sdk`）
- Python 3 + `Pillow`（校验工具使用）、`gcc`（编译 `tlg5_fast.c` 与 `linux_launcher.c`）、`cabextract` / `ffmpeg`（仅首次从原盘解包转换资源时需要）
- （可选）`zig` 静态链接 Linux 启动器；若未安装将回退使用 `gcc`

### 1. 准备原版资源（仓库不含音画与字体包）

将原版安装盘目录 `おジャ魔女あどべんちゃ～「ないしょのまほう」/`（含 `Data1.cab` 与 `appl.ico`）以及官方免 CD 补丁 `No CD Patch/patch.xp3` 置于仓库根目录，然后提取并转换资源：

```bash
python3 tools/extract_and_convert.py
```

如需重新转译 `.ks` 剧本（仓库已自带转译及修复后的 `.rpy` 剧本，一般无需重跑）：

```bash
python3 tools/transpile_ks.py
```

### 2. 校验工程与运行测试

```bash
# 运行静态校验与无头运行冒烟测试（无声音输出可通过 SDL_AUDIODRIVER=dummy）
SDL_AUDIODRIVER=dummy python3 tools/verify_project.py

# 使用本地 Ren'Py SDK 启动游戏
./run_linux.sh
```

### 3. 打包分发包

```bash
./build_distributions.sh
```

构建产物将输出到 `dist/` 目录（包括 `NaishoNoMahou-1.0.0-linux.tar.bz2` 与 `NaishoNoMahou-1.0.0-win.zip` 及其解压目录）。
