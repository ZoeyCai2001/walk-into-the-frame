#!/usr/bin/env python3
"""Compose original/generated photo pairs without cropping or distorting them."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps


PAIR_RE = re.compile(r"^(\d+)-([12])\.(jpe?g|png|webp|tiff?)$", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--only", type=int, help="Compose only one numbered pair.")
    parser.add_argument(
        "--match-edge",
        type=int,
        default=1800,
        help="Common width for horizontal pairs or height for vertical pairs.",
    )
    parser.add_argument("--margin", type=int, default=72)
    parser.add_argument("--gap", type=int, default=36)
    parser.add_argument(
        "--background",
        default="auto",
        help="Outer paper color, or 'auto' to sample the generated collage.",
    )
    parser.add_argument("--shadow", action="store_true", default=True)
    return parser.parse_args()


def collect_pairs(input_dir: Path) -> dict[int, dict[int, Path]]:
    pairs: dict[int, dict[int, Path]] = {}
    for path in input_dir.iterdir():
        if not path.is_file():
            continue
        match = PAIR_RE.match(path.name)
        if not match:
            continue
        number, version = int(match.group(1)), int(match.group(2))
        pairs.setdefault(number, {})[version] = path
    return pairs


def open_normalized(path: Path) -> Image.Image:
    image = ImageOps.exif_transpose(Image.open(path))
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGB")
    return image.copy()


def resize_to_edge(image: Image.Image, edge: int, horizontal: bool) -> Image.Image:
    if horizontal:
        width = edge
        height = round(image.height * edge / image.width)
    else:
        height = edge
        width = round(image.width * edge / image.height)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def estimate_paper_color(image: Image.Image) -> tuple[int, int, int]:
    """Estimate the collage's paper base from small patches near its corners."""
    rgb = image.convert("RGB")
    patch_size = max(4, min(rgb.width, rgb.height) // 40)
    inset = max(2, patch_size // 2)
    boxes = [
        (inset, inset, inset + patch_size, inset + patch_size),
        (rgb.width - inset - patch_size, inset, rgb.width - inset, inset + patch_size),
        (inset, rgb.height - inset - patch_size, inset + patch_size, rgb.height - inset),
        (
            rgb.width - inset - patch_size,
            rgb.height - inset - patch_size,
            rgb.width - inset,
            rgb.height - inset,
        ),
    ]
    pixels = []
    for box in boxes:
        pixels.extend(rgb.crop(box).getdata())
    channels = []
    for channel in range(3):
        values = sorted(pixel[channel] for pixel in pixels)
        channels.append(values[len(values) // 2])
    return tuple(channels)  # type: ignore[return-value]


def paste_with_shadow(canvas: Image.Image, image: Image.Image, xy: tuple[int, int]) -> None:
    x, y = xy
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow_layer = Image.new("RGBA", image.size, (35, 28, 20, 46))
    shadow.paste(shadow_layer, (x + 10, y + 12), shadow_layer)
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    canvas.alpha_composite(shadow)
    canvas.paste(image, (x, y), image if image.mode == "RGBA" else None)


def compose_pair(
    original_path: Path,
    generated_path: Path,
    output_path: Path,
    match_edge: int,
    margin: int,
    gap: int,
    background: str,
) -> None:
    original = open_normalized(original_path)
    generated = open_normalized(generated_path)
    horizontal = original.width >= original.height

    original = resize_to_edge(original, match_edge, horizontal)
    generated = resize_to_edge(generated, match_edge, horizontal)
    if background.lower() == "auto":
        background = estimate_paper_color(generated)

    if horizontal:
        content_width = match_edge
        content_height = original.height + gap + generated.height
    else:
        content_width = original.width + gap + generated.width
        content_height = match_edge

    canvas = Image.new(
        "RGBA",
        (content_width + margin * 2, content_height + margin * 2),
        background,
    )
    original_xy = (margin, margin)
    generated_xy = (
        margin,
        margin + original.height + gap,
    ) if horizontal else (
        margin + original.width + gap,
        margin,
    )

    paste_with_shadow(canvas, original, original_xy)
    paste_with_shadow(canvas, generated, generated_xy)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output_path, quality=95, optimize=True)


def main() -> None:
    args = parse_args()
    pairs = collect_pairs(args.input_dir)
    selected = [args.only] if args.only is not None else sorted(pairs)
    for number in selected:
        pair = pairs.get(number, {})
        if 1 not in pair or 2 not in pair:
            print(f"skip {number}: missing -1 or -2")
            continue
        output = args.output_dir / f"{number}-comparison.jpg"
        compose_pair(
            pair[1],
            pair[2],
            output,
            args.match_edge,
            args.margin,
            args.gap,
            args.background,
        )
        print(output)


if __name__ == "__main__":
    main()
