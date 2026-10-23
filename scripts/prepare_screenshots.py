#!/usr/bin/env python3
"""Prepare Marketplace screenshots.

The captures from macOS can include a black full-screen strip at the top and
carry a Display P3 ICC profile.  Marketplace listings are more predictable when
the screenshots are window-only, sRGB, and free of EXIF/XMP metadata.

Run this after copying the raw captures into ``screenshots/``:

    python3 scripts/prepare_screenshots.py

The cleaned files are written to ``screenshots/marketplace/``; the originals
are left untouched.
"""

from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageCms

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = ROOT / "screenshots"
DEFAULT_OUTPUT = DEFAULT_SOURCE / "marketplace"
MIN_WIDTH = 1280
MIN_HEIGHT = 800
MAX_TOP_CROP = 160


def top_black_strip(image: Image.Image) -> int:
    """Return the height of an opaque black strip at the top, if present."""
    rgb = image.convert("RGB")
    pixels = rgb.load()
    width, height = rgb.size

    for y in range(min(height, MAX_TOP_CROP)):
        for x in range(0, width, 8):
            if max(pixels[x, y]) > 8:
                return y
    return 0


def to_srgb(image: Image.Image) -> Image.Image:
    """Convert an embedded Display P3 (or other) profile to sRGB."""
    embedded = image.info.get("icc_profile")
    if not embedded:
        return image.convert("RGB")

    source = ImageCms.ImageCmsProfile(BytesIO(embedded))
    return ImageCms.profileToProfile(
        image.convert("RGB"),
        source,
        ImageCms.createProfile("sRGB"),
        outputMode="RGB",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    files = sorted(
        path
        for path in args.source.iterdir()
        if path.is_file() and path.suffix.lower() == ".png"
    )
    if not files:
        raise SystemExit(f"No PNG screenshots found in {args.source}")

    args.output.mkdir(parents=True, exist_ok=True)

    for path in files:
        with Image.open(path) as original:
            image = to_srgb(original)
            top = top_black_strip(image)
            if top:
                image = image.crop((0, top, image.width, image.height))

        if image.width < MIN_WIDTH or image.height < MIN_HEIGHT:
            raise SystemExit(
                f"{path.name}: {image.width}x{image.height} is smaller than "
                f"the required {MIN_WIDTH}x{MIN_HEIGHT}"
            )

        destination = args.output / path.name
        # Saving without metadata also drops EXIF/XMP from the capture.
        image.save(destination, "PNG", optimize=True)
        crop_note = f", cropped {top}px top" if top else ""
        print(
            f"{path.name}: {image.width}x{image.height}{crop_note} "
            f"-> {destination}"
        )


if __name__ == "__main__":
    main()
