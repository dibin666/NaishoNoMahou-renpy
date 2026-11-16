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

if [[ -f "$SCRIPT_DIR/tools/prepare_platform_assets.py" ]]; then
    python3 "$SCRIPT_DIR/tools/prepare_platform_assets.py"
fi

mkdir -p "$DIST_DIR"

TMP_BUILD_DIR="$(mktemp -d)"
cleanup() {
    rm -rf "$TMP_BUILD_DIR" "$PROJECT_DIR/tmp"
}
trap cleanup EXIT

compile_linux_launcher() {
    local target_triple="$1"
    local out_bin="$2"
    local src="$SCRIPT_DIR/tools/linux_launcher.c"
    local zig_bin="${ZIG_BIN:-$HOME/.local/opt/zig-x86_64-linux-0.15.2/zig}"

    if [[ -x "$zig_bin" ]]; then
        "$zig_bin" cc -target "$target_triple" -static -no-pie -Os -s "$src" -o "$out_bin"
    elif command -v zig >/dev/null 2>&1; then
        zig cc -target "$target_triple" -static -no-pie -Os -s "$src" -o "$out_bin"
    elif [[ "$target_triple" == "x86_64-linux-musl" ]] && command -v gcc >/dev/null 2>&1; then
        if gcc -static -no-pie -Os -s "$src" -o "$out_bin" 2>/dev/null; then
            :
        else
            gcc -no-pie -Os -s "$src" -o "$out_bin"
        fi
    else
        echo "Warning: No cross-compiler (zig) found for $target_triple; skipping $out_bin" >&2
        return 1
    fi
    chmod 0755 "$out_bin"
    return 0
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

finalize_linux_tree() {
    local dir="$1"
    local has_arm_launcher="$2"
    local arm_bin="$3"
    cp -f "$LINUX_LAUNCHER_X64" "$dir/$PKG_NAME"
    chmod 0755 "$dir/$PKG_NAME"
    if [[ "$has_arm_launcher" == "1" && -f "$arm_bin" ]]; then
        cp -f "$arm_bin" "$dir/${PKG_NAME}-arm64"
        chmod 0755 "$dir/${PKG_NAME}-arm64"
    fi
    if [[ -f "$dir/${PKG_NAME}.sh" ]]; then
        patch_linux_sh "$dir/${PKG_NAME}.sh"
    fi
    if [[ -d "$dir/lib/py3-linux-x86_64" ]]; then
        chmod 0755 "$dir/lib/py3-linux-x86_64/"*
    fi
    if [[ -d "$dir/lib/py3-linux-aarch64" ]]; then
        chmod 0755 "$dir/lib/py3-linux-aarch64/"*
    fi
}

ensure_android_keystore() {
    local ks="$PROJECT_DIR/android.keystore"
    local bks="$PROJECT_DIR/bundle.keystore"
    if [[ ! -f "$ks" ]]; then
        echo "Generating Android signing keystore at $ks..."
        keytool -genkeypair \
            -keystore "$ks" \
            -alias android \
            -keyalg RSA \
            -keysize 2048 \
            -keypass android \
            -storepass android \
            -dname "CN=dibin666, O=NaishoNoMahou" \
            -validity 20000
    fi
    if [[ ! -f "$bks" ]]; then
        cp -f "$ks" "$bks"
    fi
}

build_web_dist() {
    if [[ ! -d "$RENPY_SDK/web" ]]; then
        echo "Skipping Web build ($RENPY_SDK/web not installed)."
        return 0
    fi
    local web_dir="$DIST_DIR/${PKG_DIR_NAME}-web"
    rm -rf "$web_dir" "${web_dir}.zip"
    SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
        "$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" web_build \
        "$PROJECT_DIR" \
        --destination "$web_dir"
}

build_android_dist() {
    if [[ ! -d "$RENPY_SDK/rapt" ]]; then
        echo "Skipping Android build ($RENPY_SDK/rapt not installed)."
        return 0
    fi
    ensure_android_keystore
    # RAPT writes local.properties using ISO-8859-1 Java Properties encoding;
    # pass an ASCII symlink so non-ASCII parent directories never break key.store lookup.
    local android_proj="$TMP_BUILD_DIR/android_project"
    ln -sfn "$PROJECT_DIR" "$android_proj"
    SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
        "$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" android_build \
        "$android_proj" \
        --destination "$DIST_DIR"
    for apk in "$DIST_DIR"/*-release.apk; do
        if [[ -f "$apk" ]]; then
            mv -f "$apk" "$DIST_DIR/${PKG_DIR_NAME}-android.apk"
            break
        fi
    done
}

echo "[1/5] Compiling Ren'Py scripts and bytecode..."
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
    "$RENPY_SDK/renpy.sh" "$PROJECT_DIR" compile

echo "[2/5] Building Linux click-to-play ELF launchers (x86_64 + aarch64)..."
LINUX_LAUNCHER_X64="$TMP_BUILD_DIR/$PKG_NAME"
LINUX_LAUNCHER_ARM64="$TMP_BUILD_DIR/${PKG_NAME}-arm64"
compile_linux_launcher "x86_64-linux-musl" "$LINUX_LAUNCHER_X64"
HAS_ARM_LAUNCHER=0
if compile_linux_launcher "aarch64-linux-musl" "$LINUX_LAUNCHER_ARM64"; then
    HAS_ARM_LAUNCHER=1
fi

echo "[3/5] Running Ren'Py desktop distribute..."
if [[ $# -gt 0 ]]; then
    if [[ "$1" == "--android-only" ]]; then
        build_android_dist
    elif [[ "$1" == "--web-only" ]]; then
        build_web_dist
    else
        SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
            "$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" distribute \
            --no-update \
            --destination "$DIST_DIR" \
            "$@" \
            "$PROJECT_DIR"
    fi
else
    if [[ ! -d "$RENPY_SDK/lib/py3-linux-aarch64" ]]; then
        echo "Warning: $RENPY_SDK/lib/py3-linux-aarch64 not found; Linux package will lack ARM64 runtime." >&2
    fi

    SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
        "$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" distribute \
        --no-update \
        --package linux \
        --package win \
        --package mac \
        --destination "$DIST_DIR" \
        "$PROJECT_DIR"

    echo "[4/5] Building Web and Android distributions (if SDK modules are installed)..."
    build_web_dist
    build_android_dist
fi

echo "[5/5] Finalizing click-and-play packages and extracted folders..."

LINUX_TAR="$DIST_DIR/${PKG_DIR_NAME}-linux.tar.bz2"
LINUX_DIR="$DIST_DIR/${PKG_DIR_NAME}-linux"
if [[ -f "$LINUX_TAR" ]]; then
    rm -rf "$LINUX_DIR"
    tar -xjf "$LINUX_TAR" -C "$DIST_DIR"
    finalize_linux_tree "$LINUX_DIR" "$HAS_ARM_LAUNCHER" "$LINUX_LAUNCHER_ARM64"
    tar -cjf "${LINUX_TAR}.tmp" -C "$DIST_DIR" "${PKG_DIR_NAME}-linux"
    mv -f "${LINUX_TAR}.tmp" "$LINUX_TAR"
fi

WIN_ZIP="$DIST_DIR/${PKG_DIR_NAME}-win.zip"
WIN_DIR="$DIST_DIR/${PKG_DIR_NAME}-win"
if [[ -f "$WIN_ZIP" ]]; then
    rm -rf "$WIN_DIR"
    unzip -q -o "$WIN_ZIP" -d "$DIST_DIR"
fi

MAC_ZIP="$DIST_DIR/${PKG_DIR_NAME}-mac.zip"
MAC_DIR="$DIST_DIR/${PKG_DIR_NAME}-mac"
if [[ -f "$MAC_ZIP" ]]; then
    rm -rf "$MAC_DIR"
    mkdir -p "$MAC_DIR"
    unzip -q -o "$MAC_ZIP" -d "$MAC_DIR"
fi

PC_ZIP="$DIST_DIR/${PKG_DIR_NAME}-pc.zip"
PC_DIR="$DIST_DIR/${PKG_DIR_NAME}-pc"
if [[ -f "$PC_ZIP" ]]; then
    rm -rf "$PC_DIR"
    unzip -q -o "$PC_ZIP" -d "$DIST_DIR"
    finalize_linux_tree "$PC_DIR" "$HAS_ARM_LAUNCHER" "$LINUX_LAUNCHER_ARM64"
    (cd "$DIST_DIR" && rm -f "${PC_ZIP}.tmp" && zip -q -r "${PC_ZIP}.tmp" "${PKG_DIR_NAME}-pc")
    mv -f "${PC_ZIP}.tmp" "$PC_ZIP"
fi

echo "Packaging complete! Output in $DIST_DIR:"
ls -lh "$DIST_DIR"
