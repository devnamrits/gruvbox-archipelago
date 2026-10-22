#!/usr/bin/env python3
"""Generate the four Gruvbox Archipelago theme JSON files.

The editor schemes are hand-maintained XML files; this script only generates
the UI themes so the dark/light and Islands/classic variants stay in sync.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES_DIR = ROOT / "src" / "main" / "resources" / "themes"

DARK = {
    "bg0_hh": "#101415",
    "bg0_h": "#1d2021",
    "bg0": "#282828",
    "bg0_s": "#32302f",
    "bg1": "#3c3836",
    "bg2": "#504945",
    "bg3": "#665c54",
    "bg4": "#7c6f64",
    "fg0": "#fbf1c7",
    "fg1": "#ebdbb2",
    "fg2": "#d5c4a1",
    "fg3": "#bdae93",
    "fg4": "#a89984",
    "gray": "#928374",
    "red": "#fb4934",
    "red_dim": "#cc241d",
    "green": "#b8bb26",
    "green_dim": "#98971a",
    "yellow": "#fabd2f",
    "yellow_dim": "#d79921",
    "blue": "#83a598",
    "blue_dim": "#458588",
    "purple": "#d3869b",
    "purple_dim": "#b16286",
    "aqua": "#8ec07c",
    "aqua_dim": "#689d6a",
    "orange": "#fe8019",
    "orange_dim": "#d65d0e",
}

LIGHT = {
    "bg0_hh": "#fdf4c1",
    "bg0_h": "#f9f5d7",
    "bg0": "#fbf1c7",
    "bg0_s": "#f2e5bc",
    "bg1": "#ebdbb2",
    "bg2": "#d5c4a1",
    "bg3": "#bdae93",
    "bg4": "#a89984",
    "fg0": "#282828",
    "fg1": "#3c3836",
    "fg2": "#504945",
    "fg3": "#665c54",
    "fg4": "#7c6f64",
    "gray": "#928374",
    "red": "#9d0006",
    "red_dim": "#cc241d",
    "green": "#79740e",
    "green_dim": "#98971a",
    "yellow": "#b57614",
    "yellow_dim": "#d79921",
    "blue": "#076678",
    "blue_dim": "#458588",
    "purple": "#8f3f71",
    "purple_dim": "#b16286",
    "aqua": "#427b58",
    "aqua_dim": "#689d6a",
    "orange": "#af3a03",
    "orange_dim": "#d65d0e",
}

THEMES = [
    {
        "file": "archipelago-dark.theme.json",
        "name": "Archipelago Dark",
        "dark": True,
        "islands": True,
        "parent": "Islands Dark",
        "scheme": "/themes/schemes/archipelago-dark.xml",
        "palette": DARK,
    },
    {
        "file": "archipelago-light.theme.json",
        "name": "Archipelago Light",
        "dark": False,
        "islands": True,
        "parent": "Islands Light",
        "scheme": "/themes/schemes/archipelago-light.xml",
        "palette": LIGHT,
    },
    {
        "file": "mainland-dark.theme.json",
        "name": "Mainland Dark",
        "dark": True,
        "islands": False,
        "parent": "ExperimentalDark",
        "scheme": "/themes/schemes/archipelago-dark.xml",
        "palette": DARK,
    },
    {
        "file": "mainland-light.theme.json",
        "name": "Mainland Light",
        "dark": False,
        "islands": False,
        "parent": "ExperimentalLight",
        "scheme": "/themes/schemes/archipelago-light.xml",
        "palette": LIGHT,
    },
]


def build_colors(palette: dict[str, str], islands: bool, dark: bool) -> dict[str, str]:
    colors = dict(palette)

    tool_bg = "bg0" if dark else "bg0_s"
    main_bg = ("bg0_s" if dark else "bg1") if islands else tool_bg

    colors.update(
        {
            "transparent-border": "#00000000",
            # Window layers
            "editor-bg": "bg0_h",
            "tool-window-bg": tool_bg,
            "main-window-bg": main_bg,
            "tool-window-bg-alt": "bg1",
            "tool-window-border": "bg1" if dark else "bg2",
            "editor-border": "bg1" if dark else "bg2",
            "main-window-border": "bg2",
            "dialog-bg": "bg0",
            "dialog-border": "bg2",
            "popup-bg": "bg1" if dark else "bg0",
            "popup-border": "bg2",
            "popup-bg-inline": "bg1" if dark else "bg0",
            "popup-border-inline": "bg2",
            # Text and icons
            "text-default": "fg1",
            "text-muted": "fg4",
            "text-secondary": "fg3",
            "text-disabled": "bg4",
            "text-link": "blue",
            "editor-text": "fg1",
            "icon-default-stroke": "fg3",
            # Selection and tabs
            "selection-bg-active": "bg2",
            "selection-bg-active-muted": "bg1",
            "selection-bg-inactive": "bg1",
            "selection-bg-hovered": "bg1",
            "tab-selected-bg-active": "bg1",
            "tab-selected-bg-inactive": tool_bg,
            "tab-selected-border-active": "yellow_dim" if dark else "yellow",
            "tab-selected-border-inactive": "bg3",
            "tab-bg-hovered": "bg0_s" if dark else "bg1",
            # Accents
            "accent-brand-bg": "blue_dim",
            "accent-brand-border": "blue_dim",
            "accent-brand-bg-secondary": "bg1",
            "accent-brand-border-secondary": "bg2",
            "accent-error-bg": "red_dim",
            "accent-error-border": "red_dim",
            "accent-error-bg-secondary": "bg1",
            "accent-error-border-secondary": "red_dim",
            "accent-warning-bg": "yellow_dim",
            "accent-warning-border": "yellow_dim",
            "accent-warning-bg-secondary": "bg1",
            "accent-warning-border-secondary": "yellow_dim",
            "accent-success-bg": "green_dim",
            "accent-success-border": "green_dim",
            "accent-success-bg-secondary": "bg1",
            "accent-success-border-secondary": "green_dim",
            "text-error": "red",
            "text-warning": "yellow",
            "text-success": "green",
            "toolbar-selected-bg": "blue_dim",
            "toolbar-selected-bg-hovered": "blue" if dark else "blue_dim",
            "toolbar-selected-bg-active": "blue_dim",
            "toolbar-run-bg": "green_dim",
            "toolbar-run-bg-hovered": "green",
            "toolbar-stop-bg": "red_dim",
            "toolbar-stop-bg-hovered": "red",
            # Controls and chrome
            "control-border": "bg3",
            "control-bg-raised": "bg1",
            "control-bg-small": "bg2",
            "control-border-small": "bg3",
            "tree-indent-guide-border": "bg1" if dark else "bg2",
            "search-match-bg": "#b57614" if dark else "#fabd2f",
            "popup-completion-match-text": "yellow" if dark else "blue",
        }
    )
    return colors


def build_ui(dark: bool, islands: bool) -> dict:
    border_color = "transparent-border" if islands else "bg2"
    ui: dict = {
        "MainWindow.background": "main-window-bg",
        "ToolWindow": {
            "background": "tool-window-bg",
            "Header": {
                "background": "tool-window-bg",
                "inactiveBackground": "tool-window-bg",
            },
            "Stripe": {
                "background": "main-window-bg",
                "borderColor": border_color,
            },
        },
        "EditorTabs": {
            "background": "editor-bg",
            "hoverBackground": "tab-bg-hovered",
            "hoverInactiveBackground": "tab-bg-hovered",
            "underlinedTabBackground": "tab-selected-bg-active",
            "inactiveUnderlinedTabBackground": "tab-selected-bg-inactive",
            "underlinedBorderColor": "tab-selected-border-active",
            "inactiveUnderlinedTabBorderColor": "tab-selected-border-inactive",
        },
        "StatusBar": {
            "background": "main-window-bg",
            "borderColor": border_color,
        },
        "MainToolbar": {
            "background": "main-window-bg",
            "inactiveBackground": "main-window-bg",
            "borderColor": border_color,
        },
        "Borders.color": "bg2",
        "Borders.ContrastBorderColor": "bg2",
    }

    if islands:
        ui["Islands"] = 1
        ui["Island"] = {
            "arc": 20,
            "arc.compact": 16,
            "borderArcLength": 14,
            "borderArcLength.compact": 10,
            "borderWidth": 6,
            "borderWidth.compact": 4,
            "borderColor": "tool-window-bg",
            "inactiveAlpha": 0.56,
            "toolWindowAlpha": 0.2,
        }
    else:
        ui["Islands"] = 0

    return ui


def build_theme(spec: dict) -> dict:
    palette = spec["palette"]
    return {
        "name": spec["name"],
        "dark": spec["dark"],
        "author": "devnamrits",
        "editorScheme": spec["scheme"],
        "parentTheme": spec["parent"],
        "colors": build_colors(palette, spec["islands"], spec["dark"]),
        "ui": build_ui(spec["dark"], spec["islands"]),
    }


def main() -> None:
    THEMES_DIR.mkdir(parents=True, exist_ok=True)
    for spec in THEMES:
        path = THEMES_DIR / spec["file"]
        theme = build_theme(spec)
        path.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
