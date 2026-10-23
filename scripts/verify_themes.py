#!/usr/bin/env python3
"""Validate the generated themes, editor schemes, and palette coverage."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES = ROOT / "src" / "main" / "resources" / "themes"
SCHEMES = THEMES / "schemes"
PLUGIN_XML = ROOT / "src" / "main" / "resources" / "META-INF" / "plugin.xml"

sys.path.insert(0, str(ROOT / "scripts"))
import generate_themes as palette  # noqa: E402

CANONICAL = {
    value.lower().lstrip("#")
    for source in (palette.DARK, palette.LIGHT)
    for value in source.values()
}
CANONICAL.update({"000000", "ffffff"})

MIXED_TOKEN = re.compile(
    r"^(?:[A-Z][a-z]+\d+|(?:blue|gray|red|green|yellow|purple|orange|aqua|teal|magenta|pink|cyan)-\d+|grad-.*|using-.*|underline-.*)$"
)
RAW_NEUTRAL = {
    "black",
    "white",
    "transparent",
    "transparent-border",
    "icon-over-accent",
    "text-over-accent",
    "text-over-accent-inverted",
    "control-border-over-accent",
}


def strip_alpha(value: str) -> str:
    value = value.lower().lstrip("#")
    return value[:6] if len(value) == 8 else value


def is_canonical(value: str) -> bool:
    return strip_alpha(value) in CANONICAL


def resolve(colors: dict[str, str], value: str) -> str:
    seen: set[str] = set()
    while value in colors and value not in seen:
        seen.add(value)
        value = colors[value]
    return value


def luminance(value: str) -> float:
    value = strip_alpha(value)
    rgb = [int(value[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [
        channel / 12.92
        if channel <= 0.04045
        else ((channel + 0.055) / 1.055) ** 2.4
        for channel in rgb
    ]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: str, b: str) -> float:
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def check_ui_refs(value, colors: dict[str, str], path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            check_ui_refs(child, colors, f"{path}.{key}" if path else key, errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            check_ui_refs(child, colors, f"{path}[{index}]", errors)
    elif isinstance(value, str):
        if value in colors or value.startswith("#"):
            return
        if re.search(r"#[0-9a-fA-F]{6,8}$", value):
            return
        if re.fullmatch(r"-?\d+(?:\.\d+)?", value) or value in {"true", "false"}:
            return
        errors.append(f"{path}: unresolved reference {value!r}")


def check_colors(theme: dict, errors: list[str]) -> None:
    colors = theme.get("colors", {})
    for key, value in colors.items():
        if not isinstance(value, str) or not value.startswith("#"):
            continue
        if MIXED_TOKEN.match(key) or key in RAW_NEUTRAL:
            continue
        if not is_canonical(value):
            errors.append(f"colors.{key}: off-palette value {value}")


def main() -> int:
    errors: list[str] = []
    plugin = ET.parse(PLUGIN_XML).getroot()
    providers = plugin.findall("./extensions/themeProvider")
    theme_paths = sorted(THEMES.glob("*.theme.json"))

    if len(providers) != 8:
        errors.append(f"plugin.xml: expected 8 themeProvider entries, found {len(providers)}")
    if len(theme_paths) != 8:
        errors.append(f"themes: expected 8 theme JSON files, found {len(theme_paths)}")

    provider_paths = {provider.get("path", "").lstrip("/") for provider in providers}
    provider_ids = [provider.get("id", "") for provider in providers]
    if len(set(provider_ids)) != len(provider_ids):
        errors.append("plugin.xml: duplicate themeProvider ids")

    theme_names: list[str] = []
    scheme_names: dict[str, str] = {}
    print("Themes")
    for path in theme_paths:
        theme = json.loads(path.read_text(encoding="utf-8"))
        name = theme.get("name", path.stem)
        theme_names.append(name)
        relative = path.relative_to(ROOT / "src" / "main" / "resources").as_posix()

        if relative not in provider_paths:
            errors.append(f"{path.name}: missing themeProvider for {relative}")
        if not isinstance(theme.get("dark"), bool):
            errors.append(f"{path.name}: missing boolean dark flag")
        if not theme.get("parentTheme"):
            errors.append(f"{path.name}: missing parentTheme")

        scheme_path = theme.get("editorScheme", "").lstrip("/")
        scheme_file = ROOT / "src" / "main" / "resources" / scheme_path
        text_bg = None
        if not scheme_file.is_file():
            errors.append(f"{path.name}: missing editorScheme {scheme_path}")
        else:
            try:
                scheme = ET.parse(scheme_file).getroot()
                scheme_name = scheme.get("name", "")
                if not scheme_name:
                    errors.append(f"{scheme_file.name}: missing scheme name")
                previous = scheme_names.get(scheme_name)
                if previous and previous != scheme_file.name:
                    errors.append(
                        f"{scheme_file.name}: duplicate scheme name {scheme_name!r} "
                        f"also used by {previous}"
                    )
                else:
                    scheme_names[scheme_name] = scheme_file.name
                if not scheme.get("parent_scheme"):
                    errors.append(f"{scheme_file.name}: missing parent_scheme")
                text_bg_option = scheme.find(
                    "attributes/option[@name='TEXT']/value/option[@name='BACKGROUND']"
                )
                if text_bg_option is not None:
                    text_bg = text_bg_option.get("value")
                for value in re.findall(r'value="([0-9a-fA-F]{6,8})"', scheme_file.read_text()):
                    if not is_canonical(value):
                        errors.append(f"{scheme_file.name}: off-palette {value}")
            except ET.ParseError as exc:
                errors.append(f"{scheme_file.name}: invalid XML: {exc}")

        check_ui_refs(theme.get("ui", {}), theme.get("colors", {}), "ui", errors)
        check_colors(theme, errors)

        colors = theme.get("colors", {})
        editor = resolve(colors, colors.get("editor-bg", ""))
        backdrop = resolve(colors, colors.get("main-window-bg", ""))
        ratio = contrast(editor, backdrop) if editor and backdrop else 0
        print(f"  {name:28} editor={editor or '?':9} backdrop={backdrop or '?':9} contrast={ratio:.2f}:1")

        if scheme_file.is_file():
            if not text_bg:
                errors.append(f"{scheme_file.name}: missing TEXT background")
            elif strip_alpha(text_bg) != strip_alpha(editor):
                errors.append(
                    f"{scheme_file.name}: TEXT background {text_bg} "
                    f"does not match editor-bg {editor}"
                )

        if name.startswith("Archipelago") and ratio < 1.20:
            errors.append(f"{path.name}: Islands contrast {ratio:.2f}:1 is below 1.20:1")

    if len(set(theme_names)) != len(theme_names):
        errors.append("theme names are not unique")

    print("\nSchemes")
    for path in sorted(SCHEMES.glob("*.xml")):
        try:
            scheme = ET.parse(path).getroot()
            print(f"  {path.name:34} {scheme.get('name')}")
        except ET.ParseError as exc:
            errors.append(f"{path.name}: invalid XML: {exc}")

    if errors:
        print("\nFAILED")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"\nOK: {len(theme_paths)} themes, {len(providers)} theme providers, "
          f"{len(list(SCHEMES.glob('*.xml')))} schemes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
