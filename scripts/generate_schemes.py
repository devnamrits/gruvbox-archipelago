#!/usr/bin/env python3
"""Generate the Medium and Soft editor schemes from the Hard schemes.

The syntax attributes are shared by every background variant.  Only the
surface colours (editor/gutter/console, caret row, separators, scrollbars) are
retuned to the canonical Gruvbox background for the variant.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMES = ROOT / "src" / "main" / "resources" / "themes" / "schemes"

VARIANTS = {
    "dark": {
        "base": "archipelago-dark-hard.xml",
        "name": "Dark",
        "bg": {"medium": "282828", "soft": "32302f"},
        "caret": {"medium": "3c3836", "soft": "504945"},
        "separator": {"medium": "3c3836", "soft": "504945"},
        "documentation": {"medium": "32302f", "soft": "3c3836"},
        "scrollbar_bg": {"medium": "32302f", "soft": "3c3836"},
        "scrollbar_hover": {"medium": "282828", "soft": "32302f"},
    },
    "light": {
        "base": "archipelago-light-hard.xml",
        "name": "Light",
        "bg": {"medium": "fbf1c7", "soft": "f2e5bc"},
        "caret": {"medium": "ebdbb2", "soft": "ebdbb2"},
        "separator": {"medium": "ebdbb2", "soft": "ebdbb2"},
        "documentation": {"medium": "f9f5d7", "soft": "f9f5d7"},
        "scrollbar_bg": {"medium": "f2e5bc", "soft": "ebdbb2"},
        "scrollbar_hover": {"medium": "fbf1c7", "soft": "f2e5bc"},
    },
}

SCROLLBAR_HOVER_TRACKS = [
    "ScrollBar.hoverTrackColor",
    "ScrollBar.Mac.hoverTrackColor",
    "ScrollBar.Transparent.hoverTrackColor",
    "ScrollBar.Mac.Transparent.hoverTrackColor",
]


def set_option(text: str, name: str, value: str) -> str:
    pattern = re.compile(
        rf'(<option name="{re.escape(name)}"\s+value=")[^"]*("\s*/>)'
    )
    text, count = pattern.subn(rf"\g<1>{value}\g<2>", text, count=1)
    if count != 1:
        raise SystemExit(f"missing option: {name}")
    return text


def set_attribute_background(text: str, attribute: str, value: str) -> str:
    pattern = re.compile(
        rf'(<option name="{re.escape(attribute)}">\s*<value>.*?'
        rf'<option name="BACKGROUND" value=")[^"]*("\s*/>)',
        re.S,
    )
    text, count = pattern.subn(rf"\g<1>{value}\g<2>", text, count=1)
    if count != 1:
        raise SystemExit(f"missing attribute background: {attribute}")
    return text


def build_variant(base: str, mode: str, variant: str) -> str:
    cfg = VARIANTS[mode]
    text = (SCHEMES / base).read_text(encoding="utf-8")

    title = f"Gruvbox Archipelago {cfg['name']} {variant.title()}"
    comment = f"""<!--
  {title}
  Derived from the Gruvbox editor scheme in Vincent Parizet's
  gruvbox-intellij-theme, retuned to the canonical Gruvbox {variant.title()}
  background.
  Copyright (c) 2019 Vincent Parizet. MIT licensed; see NOTICE.
-->"""
    text, count = re.subn(r"<!--.*?-->", comment, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"missing comment block: {base}")

    text, count = re.subn(
        r'<scheme name="[^"]+"', f'<scheme name="{title}"', text, count=1
    )
    if count != 1:
        raise SystemExit(f"missing scheme name: {base}")

    bg = cfg["bg"][variant]
    for option in ("CONSOLE_BACKGROUND_KEY", "GUTTER_BACKGROUND"):
        text = set_option(text, option, bg)
    text = set_option(text, "CARET_ROW_COLOR", cfg["caret"][variant])
    text = set_option(text, "METHOD_SEPARATORS_COLOR", cfg["separator"][variant])
    text = set_option(text, "DOCUMENTATION_COLOR", cfg["documentation"][variant])
    text = set_attribute_background(text, "TEXT", bg)
    text = set_option(text, "ScrollBar.background", cfg["scrollbar_bg"][variant])
    for option in SCROLLBAR_HOVER_TRACKS:
        text = set_option(text, option, cfg["scrollbar_hover"][variant])

    return text


def main() -> None:
    for mode, cfg in VARIANTS.items():
        for variant in ("medium", "soft"):
            text = build_variant(cfg["base"], mode, variant)
            path = SCHEMES / f"archipelago-{mode}-{variant}.xml"
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
