#!/usr/bin/env python3
"""Generate macOS (.icns), Web, and Android icon/presplash assets from extracted game assets."""

import io
import struct
from pathlib import Path
from PIL import Image, ImageDraw

ROOT_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = ROOT_DIR / "renpy_project"
GAME_DIR = PROJECT_DIR / "game"
WINDOW_ICON = GAME_DIR / "gui" / "window_icon.png"
MAINTITLE_PNG = GAME_DIR / "images" / "bg" / "maintitle.png"


def make_squircle_badge(size: int = 1024) -> Image.Image:
    """Create a rounded macOS/Web badge icon containing the Rhythm portrait."""
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    margin = int(size * 0.08)
    box = [margin, margin, size - margin, size - margin]
    radius = int(size * 0.20)

    # Soft pink gradient fill inside rounded square
    grad = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    px = grad.load()
    for y in range(margin, size - margin):
        t = (y - margin) / max(1, (size - 2 * margin))
        r = int(255)
        g = int(240 - t * 65)
        b = int(247 - t * 47)
        for x in range(margin, size - margin):
            px[x, y] = (r, g, b, 255)

    mask = Image.new("L", (size, size), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle(box, radius=radius, fill=255)
    canvas.paste(grad, (0, 0), mask)

    # Subtle Ojamajo pink border (drawn after portrait so clipped bottom/right edges sit behind the frame)
    portrait = Image.open(WINDOW_ICON).convert("RGBA")
    inner_sz = int((size - 2 * margin) * 1.03)
    portrait_scaled = portrait.resize((inner_sz, inner_sz), Image.Resampling.LANCZOS)
    px_off = (size - inner_sz) // 2 + int(size * 0.015)
    py_off = (size - margin) - inner_sz

    # Clip portrait cleanly to the rounded badge interior
    p_layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    p_layer.paste(portrait_scaled, (px_off, py_off), portrait_scaled)
    clipped = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    clipped.paste(p_layer, (0, 0), mask)
    out = Image.alpha_composite(canvas, clipped)
    bdraw = ImageDraw.Draw(out)
    bdraw.rounded_rectangle(box, radius=radius, outline=(255, 102, 163, 255), width=max(6, size // 30))
    return out


def write_icns(badge_1024: Image.Image, out_path: Path) -> None:
    """Write a modern PNG-chunk Apple ICNS file (128, 256, 512, 1024)."""
    chunk_specs = [
        (b"ic07", 128),
        (b"ic08", 256),
        (b"ic09", 512),
        (b"ic10", 1024),
    ]
    chunks = bytearray()
    for tag, sz in chunk_specs:
        resized = badge_1024 if sz == 1024 else badge_1024.resize((sz, sz), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        resized.save(buf, format="PNG", optimize=True)
        png_bytes = buf.getvalue()
        chunks.extend(tag)
        chunks.extend(struct.pack(">I", 8 + len(png_bytes)))
        chunks.extend(png_bytes)
    header = b"icns" + struct.pack(">I", 8 + len(chunks))
    out_path.write_bytes(header + bytes(chunks))


def write_android_adaptive_icon(out_fg: Path, out_bg: Path) -> None:
    """Write Android adaptive icon foreground & background (432x432)."""
    sz = 432
    bg = Image.new("RGBA", (sz, sz), (255, 240, 246, 255))
    bpx = bg.load()
    for y in range(sz):
        t = y / (sz - 1)
        r = 255
        g = int(242 - t * 88)
        b = int(248 - t * 62)
        for x in range(sz):
            bpx[x, y] = (r, g, b, 255)
    bg.save(out_bg, format="PNG", optimize=True)

    # Frame portrait inside a clean circle within the 288x288 adaptive safe zone
    portrait = Image.open(WINDOW_ICON).convert("RGBA")
    safe_r = 128
    cx = cy = sz // 2
    circle_mask = Image.new("L", (sz, sz), 0)
    ImageDraw.Draw(circle_mask).ellipse([cx - safe_r, cy - safe_r, cx + safe_r, cy + safe_r], fill=255)

    p_sz = int(safe_r * 1.95)
    p_scaled = portrait.resize((p_sz, p_sz), Image.Resampling.LANCZOS)
    p_layer = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
    p_layer.paste(p_scaled, (cx - p_sz // 2 + 6, cy + safe_r - p_sz), p_scaled)

    fg = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
    ImageDraw.Draw(fg).ellipse([cx - safe_r, cy - safe_r, cx + safe_r, cy + safe_r], fill=(255, 245, 250, 255))
    clipped = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
    clipped.paste(p_layer, (0, 0), circle_mask)
    fg = Image.alpha_composite(fg, clipped)
    ImageDraw.Draw(fg).ellipse(
        [cx - safe_r, cy - safe_r, cx + safe_r, cy + safe_r],
        outline=(255, 255, 255, 255),
        width=10,
    )
    fg.save(out_fg, format="PNG", optimize=True)


def main() -> None:
    if not WINDOW_ICON.is_file():
        raise FileNotFoundError(f"Missing window icon: {WINDOW_ICON}")
    if not MAINTITLE_PNG.is_file():
        raise FileNotFoundError(f"Missing maintitle image: {MAINTITLE_PNG}")

    badge_1024 = make_squircle_badge(1024)
    write_icns(badge_1024, PROJECT_DIR / "icon.icns")
    badge_1024.resize((512, 512), Image.Resampling.LANCZOS).save(PROJECT_DIR / "web-icon.png", format="PNG", optimize=True)

    write_android_adaptive_icon(
        PROJECT_DIR / "android-icon_foreground.png",
        PROJECT_DIR / "android-icon_background.png",
    )

    presplash = Image.open(MAINTITLE_PNG).convert("RGB")
    presplash.save(PROJECT_DIR / "web-presplash.jpg", format="JPEG", quality=92, optimize=True)
    presplash.save(PROJECT_DIR / "android-presplash.jpg", format="JPEG", quality=92, optimize=True)
    print("Generated platform icons and presplash assets in", PROJECT_DIR)


if __name__ == "__main__":
    main()
