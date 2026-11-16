# 小魔女DoReMi冒险 ～「秘密的魔法」～

**おジャ魔女あどべんちゃ～「ないしょのまほう」** · Ren'Py 8 跨平台移植版（[游戏展示页](https://dibin666.github.io/NaishoNoMahou-renpy/)）

将原版 KiriKiri2 视觉小说移植至 Ren'Py 8，免环境点击即玩，支持 **日语原版 / 简体中文** 实时切换。

## 游戏截图

| 标题界面 | 序章中文 Logo |
| :---: | :---: |
| ![标题界面](docs/screenshots/01_title_zh.png) | ![序章中文 Logo](docs/screenshots/02_prologue_logo_zh.png) |
| **实机对话** | **特典 CG 相册** |
| ![实机对话](docs/screenshots/03_dialogue_zh.png) | ![特典 CG 相册](docs/screenshots/04_cg_gallery_zh.png) |

## 下载即玩

前往 **[Releases](https://github.com/dibin666/NaishoNoMahou-renpy/releases)** 下载对应安装包，无需安装 Python 或 Ren'Py：

- **Windows (`x86_64` / ARM64 Prism 兼容)**：下载 `NaishoNoMahou-1.0.0-win.zip`，解压后双击 `NaishoNoMahou.exe`
  > 注：Ren'Py 8.6.0 上游暂未提供原生 Windows ARM64 运行时，Windows 11 ARM64 设备可通过系统内置 Prism 转译直接运行 `x86_64` 版。
- **Linux (`x86_64` + `aarch64` ARM64)**：下载 `NaishoNoMahou-1.0.0-linux.tar.bz2`，解压后按架构直接运行（或统一使用 `./NaishoNoMahou.sh`）：
  ```bash
  tar -xjf NaishoNoMahou-1.0.0-linux.tar.bz2
  ./NaishoNoMahou-1.0.0-linux/NaishoNoMahou        # x86_64
  ./NaishoNoMahou-1.0.0-linux/NaishoNoMahou-arm64  # ARM64 (aarch64)
  ```
- **macOS (`Universal`: Apple Silicon `arm64` + Intel `x86_64`)**：下载 `NaishoNoMahou-1.0.0-mac.zip`，解压获得 `NaishoNoMahou.app`（未签名应用首次运行如提示已损坏，可执行 `xattr -cr NaishoNoMahou.app` 或右键「打开」）
- **Android (`arm64-v8a` / `armeabi-v7a` / `x86_64`)**：下载 `NaishoNoMahou-1.0.0-android.apk`，直接安装即可游玩
- **Web (`WebAssembly / HTML5`)**：下载 `NaishoNoMahou-1.0.0-web.zip`，解压至任意静态 HTTP 服务器即可在现代浏览器运行（支持资源按需渐进加载与浏览器存档导入/导出）：
  ```bash
  unzip NaishoNoMahou-1.0.0-web.zip -d naisho-web && python3 -m http.server -d naisho-web 8080
  ```
- **iOS**：Ren'Py iOS 构建依赖 macOS 下的 Xcode 与 Apple 开发者签名（`renios`），需在 macOS 环境中通过 Ren'Py Launcher 生成 Xcode 工程后编译 `.ipa`。

> 存档位置说明：Windows / Linux 默认绿色便携保存在游戏目录旁的 `game/saves/`；macOS 保存在 `~/Library/RenPy/NaishoNoMahou`；Android 与 Web 保存在系统应用沙盒 / 浏览器 IndexedDB 中。

## 主要特性

- **多平台开箱即玩**：提供 Windows、Linux（x86_64 & ARM64）、macOS（Apple Silicon & Intel Universal）、Android APK 与 Web（WASM）完整分发包
- **双语实时切换**：菜单、剧本、UI 按钮与游戏 Logo 支持日语 / 简体中文即时切换
- **字体模式切换**：内置等幅（原作排版比例）与比例字体切换
- **系统与特典完整**：支持 30 格存档/锁定、右键/顶栏菜单、序章点击推进及全特典（CG 相册 / 剧情回忆）

## 从源码构建（可选）

仓库仅含移植脚本与本地化资源；自备原盘安装目录（含 `Data1.cab`）及 `No CD Patch/patch.xp3` 置于根目录后，配合 [Ren'Py 8.6.0 SDK](https://www.renpy.org/)（`RENPY_SDK` 或 `~/.local/opt/renpy-8.6.0-sdk`，按需附带 `sdkarm`、`web`、`rapt` 扩展包及 Android SDK + JDK 21）即可构建：

```bash
python3 tools/extract_and_convert.py   # 提取并转换音画资源与字体
./run_linux.sh                         # 本地启动调试
./build_distributions.sh               # 构建全平台分发包至 dist/
```

技术细节见 [docs/RESEARCH_AND_ARCHITECTURE.md](docs/RESEARCH_AND_ARCHITECTURE.md)。
