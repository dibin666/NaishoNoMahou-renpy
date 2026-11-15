#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RENPY_SDK="${RENPY_SDK:-$HOME/.local/opt/renpy-8.6.0-sdk}"

if [[ ! -x "$RENPY_SDK/renpy.sh" ]]; then
    echo "Error: Ren'Py SDK not found at $RENPY_SDK" >&2
    echo "Set RENPY_SDK=/path/to/renpy-sdk and retry." >&2
    exit 1
fi

if [[ -n "${DISPLAY:-}" && -z "${SDL_VIDEODRIVER:-}" ]]; then
    export SDL_VIDEODRIVER="x11"
fi

exec "$RENPY_SDK/renpy.sh" "$SCRIPT_DIR/renpy_project" "$@"
