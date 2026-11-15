# 小魔女DoReMi冒险 ～「秘密的魔法」～

**おジャ魔女あどべんちゃ～「ないしょのまほう」** · Ren'Py 8 跨平台移植版（Windows / Linux）

将原版 KiriKiri2 视觉小说移植至 Ren'Py 8，免环境点击即玩，支持 **日语原版 / 简体中文** 实时切换。

## 游戏截图

| 标题界面 | 序章中文 Logo |
| :---: | :---: |
| ![标题界面](docs/screenshots/01_title_zh.png) | ![序章中文 Logo](docs/screenshots/02_prologue_logo_zh.png) |
| **实机对话** | **特典 CG 相册** |
| ![实机对话](docs/screenshots/03_dialogue_zh.png) | ![特典 CG 相册](docs/screenshots/04_cg_gallery_zh.png) |

## 下载即玩

前往 **[Releases](https://github.com/dibin666/NaishoNoMahou-renpy/releases)** 下载对应压缩包，无需安装 Python 或 Ren'Py：

- **Windows (`x86_64`)**：下载 `NaishoNoMahou-1.0.0-win.zip`，解压后双击 `NaishoNoMahou.exe`
- **Linux (`x86_64`)**：下载 `NaishoNoMahou-1.0.0-linux.tar.bz2`，解压后执行：
  ```bash
  tar -xjf NaishoNoMahou-1.0.0-linux.tar.bz2 && ./NaishoNoMahou-1.0.0-linux/NaishoNoMahou
  ```

> 绿色便携存档：所有存档与全局解锁进度默认保存在游戏目录旁的 `game/saves/` 中。

## 主要特性

- **双平台开箱即玩**：独立封装运行环境，支持 Windows / Linux 桌面直启
- **双语实时切换**：菜单、剧本、UI 按钮与游戏 Logo 支持日语 / 简体中文即时切换
- **字体模式切换**：内置等幅（原作排版比例）与比例字体切换
- **系统与特典完整**：支持 30 格存档/锁定、右键/顶栏菜单、序章点击推进及全特典（CG 相册 / 剧情回忆）

## 从源码构建（可选）

仓库仅含移植脚本与本地化资源；自备原盘安装目录（含 `Data1.cab`）及 `No CD Patch/patch.xp3` 置于根目录后，配合 [Ren'Py 8 SDK](https://www.renpy.org/)（`RENPY_SDK` 或 `~/.local/opt/renpy-8.6.0-sdk`）即可构建：

```bash
python3 tools/extract_and_convert.py   # 提取并转换音画资源与字体
./run_linux.sh                         # 本地启动调试
./build_distributions.sh               # 构建 Windows / Linux 分发包至 dist/
```

技术细节见 [docs/RESEARCH_AND_ARCHITECTURE.md](docs/RESEARCH_AND_ARCHITECTURE.md)。
