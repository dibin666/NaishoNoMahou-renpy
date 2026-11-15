#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR/renpy_project"
RENPY_SDK="${RENPY_SDK:-$HOME/.local/opt/renpy-8.6.0-sdk}"
DIST_DIR="$SCRIPT_DIR/dist"
PKG_NAME="NaishoNoMahou"
PKG_DIR_NAME="NaishoNoMahou-1.0.0"

if [[ ! -x "$RENPY_SDK/renpy.sh" ]]; then
    echo "Error: Ren'Py SDK not found at $RENPY_SDK" >&2
    echo "Set RENPY_SDK=/path/to/renpy-sdk and retry." >&2
    exit 1
fi

if [[ -f "$PROJECT_DIR/game/gui/icon.ico" ]]; then
    cp -f "$PROJECT_DIR/game/gui/icon.ico" "$PROJECT_DIR/icon.ico"
fi

mkdir -p "$DIST_DIR"

TMP_BUILD_DIR="$(mktemp -d)"
cleanup() {
    rm -rf "$TMP_BUILD_DIR" "$PROJECT_DIR/tmp"
}
trap cleanup EXIT

compile_linux_launcher() {
    local out_bin="$1"
    local src="$SCRIPT_DIR/tools/linux_launcher.c"
    local zig_bin="${ZIG_BIN:-$HOME/.local/opt/zig-x86_64-linux-0.15.2/zig}"

    if [[ -x "$zig_bin" ]]; then
        "$zig_bin" cc -target x86_64-linux-musl -static -no-pie -Os -s "$src" -o "$out_bin"
    elif command -v gcc >/dev/null 2>&1; then
        if gcc -static -no-pie -Os -s "$src" -o "$out_bin" 2>/dev/null; then
            :
        else
            gcc -no-pie -Os -s "$src" -o "$out_bin"
        fi
    else
        echo "Error: No C compiler (zig or gcc) found to build Linux click-to-run launcher." >&2
        exit 1
    fi
    chmod 0755 "$out_bin"
}

patch_linux_sh() {
    local sh_path="$1"
    python3 - "$sh_path" <<'PY'
import sys
from pathlib import Path

p = Path(sys.argv[1])
txt = p.read_text(encoding="utf-8")
marker = 'if [ -n "${DISPLAY:-}" ] && [ -z "${SDL_VIDEODRIVER:-}" ] && [ -z "${SDL_VIDEO_DRIVER:-}" ]; then'
if marker not in txt:
    snippet = (
        '\nif [ -n "${DISPLAY:-}" ] && [ -z "${SDL_VIDEODRIVER:-}" ] && [ -z "${SDL_VIDEO_DRIVER:-}" ]; then\n'
        '    export SDL_VIDEODRIVER="x11"\n'
        'fi\n'
    )
    anchor = 'LIB="$ROOT/lib/py3-$RENPY_PLATFORM"'
    if anchor in txt:
        txt = txt.replace(anchor, snippet.lstrip("\n") + "\n" + anchor, 1)
    else:
        txt += snippet
    p.write_text(txt, encoding="utf-8", newline="\n")
PY
    chmod 0755 "$sh_path"
}

echo "[1/4] Compiling Ren'Py scripts and bytecode..."
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
    "$RENPY_SDK/renpy.sh" "$PROJECT_DIR" compile

echo "[2/4] Building Linux click-to-play ELF launcher..."
LINUX_LAUNCHER_BIN="$TMP_BUILD_DIR/$PKG_NAME"
compile_linux_launcher "$LINUX_LAUNCHER_BIN"

echo "[3/4] Running Ren'Py distribute..."
if [[ $# -gt 0 ]]; then
    SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
        "$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" distribute \
        --no-update \
        --destination "$DIST_DIR" \
        "$@" \
        "$PROJECT_DIR"
else
    SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
        "$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" distribute \
        --no-update \
        --package linux \
        --package win \
        --destination "$DIST_DIR" \
        "$PROJECT_DIR"
fi

echo "[4/4] Finalizing click-and-play packages and extracted folders..."

LINUX_TAR="$DIST_DIR/${PKG_DIR_NAME}-linux.tar.bz2"
LINUX_DIR="$DIST_DIR/${PKG_DIR_NAME}-linux"
if [[ -f "$LINUX_TAR" ]]; then
    rm -rf "$LINUX_DIR"
    tar -xjf "$LINUX_TAR" -C "$DIST_DIR"
    cp -f "$LINUX_LAUNCHER_BIN" "$LINUX_DIR/$PKG_NAME"
    chmod 0755 "$LINUX_DIR/$PKG_NAME"
    if [[ -f "$LINUX_DIR/${PKG_NAME}.sh" ]]; then
        patch_linux_sh "$LINUX_DIR/${PKG_NAME}.sh"
    fi
    chmod 0755 "$LINUX_DIR/lib/py3-linux-x86_64/"*
    tar -cjf "${LINUX_TAR}.tmp" -C "$DIST_DIR" "${PKG_DIR_NAME}-linux"
    mv -f "${LINUX_TAR}.tmp" "$LINUX_TAR"
fi

WIN_ZIP="$DIST_DIR/${PKG_DIR_NAME}-win.zip"
WIN_DIR="$DIST_DIR/${PKG_DIR_NAME}-win"
if [[ -f "$WIN_ZIP" ]]; then
    rm -rf "$WIN_DIR"
    unzip -q -o "$WIN_ZIP" -d "$DIST_DIR"
fi

PC_ZIP="$DIST_DIR/${PKG_DIR_NAME}-pc.zip"
PC_DIR="$DIST_DIR/${PKG_DIR_NAME}-pc"
if [[ -f "$PC_ZIP" ]]; then
    rm -rf "$PC_DIR"
    unzip -q -o "$PC_ZIP" -d "$DIST_DIR"
    cp -f "$LINUX_LAUNCHER_BIN" "$PC_DIR/$PKG_NAME"
    chmod 0755 "$PC_DIR/$PKG_NAME"
    if [[ -f "$PC_DIR/${PKG_NAME}.sh" ]]; then
        patch_linux_sh "$PC_DIR/${PKG_NAME}.sh"
    fi
    chmod 0755 "$PC_DIR/lib/py3-linux-x86_64/"*
    (cd "$DIST_DIR" && rm -f "${PC_ZIP}.tmp" && zip -q -r "${PC_ZIP}.tmp" "${PKG_DIR_NAME}-pc")
    mv -f "${PC_ZIP}.tmp" "$PC_ZIP"
fi

echo "Packaging complete! Output in $DIST_DIR:"
ls -lh "$DIST_DIR"
