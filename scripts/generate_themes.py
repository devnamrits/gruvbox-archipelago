#!/usr/bin/env python3
"""Generate the Gruvbox Archipelago theme JSON files.

Every UI colour is derived from the canonical Gruvbox palette.  The Islands
variants inherit from Islands Dark/Light; the classic variants inherit from the
non-islands Experimental themes.  Primitive ramps are overridden too, because
otherwise the parent themes leak their own blue/gray primitives into components
we have not named explicitly.

The Hard editor schemes are hand-maintained XML files.  Medium and Soft
schemes are derived from them by scripts/generate_schemes.py.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES_DIR = ROOT / "src" / "main" / "resources" / "themes"

# ---------------------------------------------------------------------------
# Canonical Gruvbox palettes.
# ---------------------------------------------------------------------------

DARK = {
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

# Anchors used by the shared primitive ramps.  The order is always
# dark contrast -> neutral -> bright contrast, which is exactly how Gruvbox
# names its 0/1 accent pairs.
ACCENT_ANCHORS = {
    "blue": ("#076678", "#458588", "#83a598"),
    "green": ("#79740e", "#98971a", "#b8bb26"),
    "red": ("#9d0006", "#cc241d", "#fb4934"),
    "yellow": ("#b57614", "#d79921", "#fabd2f"),
    "orange": ("#af3a03", "#d65d0e", "#fe8019"),
    "purple": ("#8f3f71", "#b16286", "#d3869b"),
    "teal": ("#427b58", "#689d6a", "#8ec07c"),
}

DARK_BG = "#1d2021"
LIGHT_BG = "#f9f5d7"

BG_KEYS = {"hard": "bg0_h", "medium": "bg0", "soft": "bg0_s"}


def surface_layers(dark: bool, islands: bool, background: str) -> tuple[str, str, str]:
    """Return the editor, tool-window, and main-window background keys."""
    editor = BG_KEYS[background]

    if not islands:
        return editor, editor, editor

    if dark:
        tool, main = {
            "hard": ("bg0", "bg0_s"),
            "medium": ("bg0_s", "bg1"),
            "soft": ("bg1", "bg2"),
        }[background]
    else:
        tool, main = {
            "hard": ("bg0", "bg1"),
            "medium": ("bg0_s", "bg2"),
            "soft": ("bg1", "bg2"),
        }[background]

    return editor, tool, main


THEMES = [
    {
        "file": "archipelago-dark.theme.json",
        "name": "Archipelago Dark",
        "dark": True,
        "islands": True,
        "background": "medium",
        "parent": "Islands Dark",
        "scheme": "/themes/schemes/archipelago-dark-medium.xml",
        "palette": DARK,
    },
    {
        "file": "archipelago-dark-hard.theme.json",
        "name": "Archipelago Dark Hard",
        "dark": True,
        "islands": True,
        "background": "hard",
        "parent": "Islands Dark",
        "scheme": "/themes/schemes/archipelago-dark-hard.xml",
        "palette": DARK,
    },
    {
        "file": "archipelago-dark-soft.theme.json",
        "name": "Archipelago Dark Soft",
        "dark": True,
        "islands": True,
        "background": "soft",
        "parent": "Islands Dark",
        "scheme": "/themes/schemes/archipelago-dark-soft.xml",
        "palette": DARK,
    },
    {
        "file": "archipelago-light.theme.json",
        "name": "Archipelago Light",
        "dark": False,
        "islands": True,
        "background": "medium",
        "parent": "Islands Light",
        "scheme": "/themes/schemes/archipelago-light-medium.xml",
        "palette": LIGHT,
    },
    {
        "file": "archipelago-light-hard.theme.json",
        "name": "Archipelago Light Hard",
        "dark": False,
        "islands": True,
        "background": "hard",
        "parent": "Islands Light",
        "scheme": "/themes/schemes/archipelago-light-hard.xml",
        "palette": LIGHT,
    },
    {
        "file": "archipelago-light-soft.theme.json",
        "name": "Archipelago Light Soft",
        "dark": False,
        "islands": True,
        "background": "soft",
        "parent": "Islands Light",
        "scheme": "/themes/schemes/archipelago-light-soft.xml",
        "palette": LIGHT,
    },
    {
        "file": "mainland-dark.theme.json",
        "name": "Mainland Dark",
        "dark": True,
        "islands": False,
        "background": "medium",
        "parent": "ExperimentalDark",
        "scheme": "/themes/schemes/archipelago-dark-medium.xml",
        "palette": DARK,
    },
    {
        "file": "mainland-light.theme.json",
        "name": "Mainland Light",
        "dark": False,
        "islands": False,
        "background": "medium",
        "parent": "ExperimentalLight",
        "scheme": "/themes/schemes/archipelago-light-medium.xml",
        "palette": LIGHT,
    },
]


# ---------------------------------------------------------------------------
# Colour helpers.
# ---------------------------------------------------------------------------


def rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def hexcolour(value: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*value)


def mix(a: str, b: str, amount: float) -> str:
    """Mix *a* and *b* in sRGB; amount=0 is a, amount=1 is b."""
    ar, ag, ab = rgb(a)
    br, bg, bb = rgb(b)
    return hexcolour(
        (
            round(ar + (br - ar) * amount),
            round(ag + (bg - ag) * amount),
            round(ab + (bb - ab) * amount),
        )
    )


def alpha(value: str, aa: str) -> str:
    return value + aa


# ---------------------------------------------------------------------------
# Primitive ramps.
# ---------------------------------------------------------------------------


def build_scales() -> dict[str, str]:
    scales: dict[str, str] = {}

    gray = [
        "#1d2021",
        "#282828",
        "#32302f",
        "#3c3836",
        "#504945",
        "#665c54",
        "#7c6f64",
        "#928374",
        "#a89984",
        "#bdae93",
        "#d5c4a1",
        "#ebdbb2",
        "#f2e5bc",
        "#fbf1c7",
        "#f9f5d7",
        "#f9f5d7",
    ]
    for i, key in enumerate(range(10, 161, 10)):
        scales[f"gray-{key}"] = gray[i]

    for name, (dark, neutral, bright) in ACCENT_ANCHORS.items():
        values = [
            mix(DARK_BG, dark, 0.10),
            mix(DARK_BG, dark, 0.18),
            mix(DARK_BG, dark, 0.28),
            mix(DARK_BG, dark, 0.38),
            mix(DARK_BG, dark, 0.50),
            mix(DARK_BG, dark, 0.62),
            mix(DARK_BG, dark, 0.74),
            mix(DARK_BG, dark, 0.87),
            dark,
            neutral,
            bright,
            mix(bright, LIGHT_BG, 0.35),
            mix(bright, LIGHT_BG, 0.55),
            mix(bright, LIGHT_BG, 0.72),
            mix(bright, LIGHT_BG, 0.86),
            mix(bright, LIGHT_BG, 0.94),
        ]
        for i, key in enumerate(range(10, 161, 10)):
            scales[f"{name}-{key}"] = values[i]
        if name == "teal":
            for i, key in enumerate(range(10, 161, 10)):
                scales[f"aqua-{key}"] = values[i]

    return scales


def build_classic_scales(dark: bool, palette: dict[str, str], scales: dict[str, str]) -> dict[str, str]:
    """The classic parent uses its own Gray1..14 / Blue1..13 names."""
    if dark:
        gray = [
            palette["bg0_h"],
            palette["bg0"],
            palette["bg0_s"],
            palette["bg1"],
            palette["bg2"],
            palette["bg3"],
            palette["bg4"],
            palette["gray"],
            palette["fg4"],
            palette["fg3"],
            palette["fg2"],
            palette["fg1"],
            palette["fg0"],
            palette["fg0"],
        ]
    else:
        gray = [
            palette["fg0"],
            palette["fg1"],
            palette["fg2"],
            palette["fg3"],
            palette["fg4"],
            palette["gray"],
            palette["bg4"],
            palette["bg3"],
            palette["bg2"],
            palette["bg1"],
            palette["bg0_s"],
            palette["bg0"],
            palette["bg0_h"],
            palette["bg0_h"],
        ]

    families = {
        "Blue": ["blue-20", "blue-30", "blue-40", "blue-50", "blue-60", "blue-80", "blue-90", "blue-100", "blue-110", "blue-120", "blue-130", "blue-140", "blue-150"],
        "Green": ["green-20", "green-30", "green-40", "green-50", "green-60", "green-90", "green-100", "green-110", "green-120", "green-130", "green-140", "green-150"],
        "Red": ["red-20", "red-30", "red-40", "red-50", "red-60", "red-90", "red-100", "red-110", "red-120", "red-130", "red-140", "red-150"],
        "Yellow": ["yellow-20", "yellow-30", "yellow-40", "yellow-50", "yellow-60", "yellow-90", "yellow-100", "yellow-110", "yellow-120", "yellow-130", "yellow-140"],
        "Orange": ["orange-20", "orange-30", "orange-40", "orange-50", "orange-60", "orange-90", "orange-100", "orange-110", "orange-120", "orange-130", "orange-140"],
        "Purple": ["purple-20", "purple-30", "purple-40", "purple-50", "purple-60", "purple-90", "purple-100", "purple-110", "purple-120", "purple-130", "purple-140", "purple-150"],
        "Teal": ["teal-20", "teal-30", "teal-40", "teal-50", "teal-60", "teal-90", "teal-100", "teal-110", "teal-120", "teal-130", "teal-140", "teal-150"],
    }
    if not dark:
        families = {
            "Blue": ["blue-20", "blue-40", "blue-60", "blue-80", "blue-90", "blue-100", "blue-110", "blue-120", "blue-130", "blue-140", "blue-150", "blue-160", "blue-160"],
            "Green": ["green-20", "green-40", "green-60", "green-80", "green-90", "green-100", "green-110", "green-120", "green-130", "green-140", "green-150"],
            "Red": ["red-20", "red-40", "red-60", "red-80", "red-90", "red-100", "red-110", "red-120", "red-130", "red-140", "red-150", "red-160"],
            "Yellow": ["yellow-20", "yellow-40", "yellow-60", "yellow-80", "yellow-90", "yellow-100", "yellow-110", "yellow-120", "yellow-130", "yellow-140"],
            "Orange": ["orange-20", "orange-40", "orange-60", "orange-80", "orange-90", "orange-100", "orange-110", "orange-120", "orange-130"],
            "Purple": ["purple-20", "purple-40", "purple-60", "purple-80", "purple-90", "purple-100", "purple-110", "purple-120", "purple-130", "purple-140"],
            "Teal": ["teal-20", "teal-40", "teal-60", "teal-80", "teal-90", "teal-100", "teal-110", "teal-120", "teal-130"],
        }

    out: dict[str, str] = {}
    for i, value in enumerate(gray, start=1):
        out[f"Gray{i}"] = value
    for family, refs in families.items():
        for i, ref in enumerate(refs, start=1):
            out[f"{family}{i}"] = scales[ref]
    out["windowsPopupBorder"] = palette["bg2"]
    return out


# ---------------------------------------------------------------------------
# Semantic colour map.
# ---------------------------------------------------------------------------


def build_colors(
    palette: dict[str, str], dark: bool, islands: bool, background: str
) -> dict[str, str]:
    scales = build_scales()
    colors: dict[str, str] = {}
    colors.update(palette)
    colors.update(scales)

    editor_bg, tool_bg, main_bg = surface_layers(dark, islands, background)
    hard = background == "hard"
    popup_bg = "bg1" if dark else "bg0_h"

    if hard:
        # Preserve the original Hard mapping exactly; it is the reference
        # variant used for the first screenshots.
        editor_tabs_bg = "bg0_h" if dark else "bg0"
        dialog_bg = "bg0_h" if dark else "bg0"
        dialog_bg_inline = "bg0" if dark else "bg0_h"
        control_bg = "bg0_h"
        feedback_bg_inline = "bg0_h" if dark else "bg0"
        selection_inactive = "bg0_s" if dark else "bg1"
        tab_selected_bg = "bg2" if dark else "bg0_h"
        tab_selected_bg_inactive = "bg0_s"
        tab_hover = "#28282866" if dark else "#fbf1c766"
        editor_bg_inline = "bg0" if dark else "bg0_h"
        tool_bg_inline = "bg0" if dark else "bg0_h"
        layer_0_bg = "bg0_h"
        layer_0_bg_inline = "bg0" if dark else "bg0_h"
        layer_1_bg = "bg0_s" if dark else "bg0"
        layer_1_bg_inline = "bg1" if dark else "bg0_h"
        layer_2_bg = "bg1" if dark else "bg0_h"
        layer_2_bg_inline = "bg2" if dark else "bg0"
    else:
        if dark:
            editor_tabs_bg = editor_bg
            secondary_bg = tool_bg if islands else "bg1"
            tab_selected_bg = "bg2"
            hover_bg = tool_bg if islands else "bg1"
        else:
            # Keep the light tab bar one step darker than the editor so the
            # selected tab can use the editor background without merging.
            editor_tabs_bg = {"hard": "bg0", "medium": "bg0_s", "soft": "bg1"}[background]
            secondary_bg = editor_tabs_bg
            tab_selected_bg = editor_bg
            hover_bg = main_bg if islands else "bg2"

        dialog_bg = editor_bg
        dialog_bg_inline = tool_bg
        control_bg = editor_bg
        feedback_bg_inline = editor_bg
        selection_inactive = secondary_bg
        tab_selected_bg_inactive = secondary_bg
        tab_hover = palette[hover_bg] + "66"
        editor_bg_inline = editor_bg
        tool_bg_inline = tool_bg
        layer_0_bg = editor_bg
        layer_0_bg_inline = tool_bg
        layer_1_bg = tool_bg
        layer_1_bg_inline = main_bg
        layer_2_bg = main_bg
        layer_2_bg_inline = popup_bg

    control_bg_raised = "bg1" if dark else "bg0_h"
    control_bg_small = "bg2" if dark else "bg1"
    control_bg_small_disabled = "bg1"
    feedback_bg = "bg1" if dark else "bg0_h"
    # Hard keeps its original two-tone inactive header.  Medium and Soft use
    # the active header color so an inactive tool window cannot fall back to
    # the Hard-only near-black/bright surface.
    header_inactive_bg = "bg0_h" if hard else "bg0_s"
    tab_selected_border = "blue-110" if dark else "blue-90"
    tab_selected_border_inactive = "bg3" if dark else "bg2"
    text = "fg1"
    text_muted = "fg4"
    text_secondary = "fg3"
    text_disabled = "bg4"
    text_link = "blue-110" if dark else "blue-90"
    accent_brand = "blue-100" if dark else "blue-90"
    accent_brand_secondary = "#45858833" if dark else "#07667826"
    accent_brand_border_secondary = "#458588" if dark else "#076678"
    accent_error = "red-100" if dark else "red-90"
    accent_error_secondary = "#cc241d33" if dark else "#cc241d26"
    accent_error_border_secondary = "#cc241d" if dark else "#9d0006"
    accent_warning = "yellow-90"
    accent_warning_secondary = "#d7992133" if dark else "#d7992126"
    accent_warning_border_secondary = "#d79921" if dark else "#b57614"
    accent_success = "green-90"
    accent_success_secondary = "#98971a33" if dark else "#79740e26"
    accent_success_border_secondary = "#98971a" if dark else "#79740e"

    colors.update(
        {
            # Window layers
            "editor-bg": editor_bg,
            "editor-tabs-bg": editor_tabs_bg,
            "tool-window-bg": tool_bg,
            "main-window-bg": main_bg,
            "tool-window-header-inactive-bg": header_inactive_bg,
            "tool-window-bg-alt": "bg0_s" if dark else "bg0_h",
            "tool-window-bg-inline": tool_bg_inline,
            "tool-window-border": "bg1" if dark else "bg2",
            "tool-window-border-inline": "bg2",
            "editor-border": "bg1" if dark else "bg2",
            "editor-border-alt": "bg1" if dark else "bg2",
            "editor-border-inline": "bg2",
            "main-window-bg-alt": "bg1" if dark else "bg0_s",
            "main-window-border": "bg2",
            "dialog-bg": dialog_bg,
            "dialog-bg-inline": dialog_bg_inline,
            "dialog-border": "bg2",
            "popup-bg": popup_bg,
            "popup-bg-inline": popup_bg,
            "popup-border": "bg2",
            "popup-border-inline": "bg2",
            "popup-border-windows": "bg2",
            "editor-bg-inline": editor_bg_inline,
            "editor-floating-toolbar-bg": "bg1" if dark else "bg0_h",
            # Layer tokens
            "layer-0-bg": layer_0_bg,
            "layer-0-bg-inline": layer_0_bg_inline,
            "layer-0-border": "bg1" if dark else "bg2",
            "layer-0-border-inline": "bg1" if dark else "bg2",
            "layer-1-bg": layer_1_bg,
            "layer-1-bg-inline": layer_1_bg_inline,
            "layer-1-border": "bg2",
            "layer-1-border-inline": "bg2",
            "layer-2-bg": layer_2_bg,
            "layer-2-bg-inline": layer_2_bg_inline,
            "layer-2-border": "bg2",
            "layer-2-border-inline": "bg3" if dark else "bg2",
            # Text and icons
            "text-default": text,
            "text-muted": text_muted,
            "text-secondary": text_secondary,
            "text-disabled": text_disabled,
            "text-link": text_link,
            "editor-text": text,
            "icon-default-stroke": "fg3",
            "icon-green-stroke": "green-110" if dark else "green-90",
            "icon-over-accent": "#ffffff",
            "text-over-accent": "#ffffff",
            "text-over-accent-inverted": "#000000",
            # Selection and tabs
            "selection-bg-active": "bg2" if dark else "bg1",
            "selection-bg-active-muted": "bg1",
            "selection-bg-inactive": selection_inactive,
            "selection-bg-hovered": tab_hover,
            "tab-selected-bg-active": tab_selected_bg,
            "tab-selected-bg-inactive": tab_selected_bg_inactive,
            "tab-selected-border-active": tab_selected_border,
            "tab-selected-border-inactive": tab_selected_border_inactive,
            "tab-bg-hovered": tab_hover,
            "tab-file-color-mask-bg": tab_hover,
            # Accent roles
            "accent-brand-bg": accent_brand,
            "accent-brand-border": accent_brand,
            "accent-brand-bg-secondary": accent_brand_secondary,
            "accent-brand-border-secondary": accent_brand_border_secondary,
            "accent-error-bg": accent_error,
            "accent-error-border": accent_error,
            "accent-error-bg-secondary": accent_error_secondary,
            "accent-error-border-secondary": accent_error_border_secondary,
            "accent-warning-bg": accent_warning,
            "accent-warning-border": accent_warning,
            "accent-warning-bg-secondary": accent_warning_secondary,
            "accent-warning-border-secondary": accent_warning_border_secondary,
            "accent-success-bg": accent_success,
            "accent-success-border": accent_success,
            "accent-success-bg-secondary": accent_success_secondary,
            "accent-success-border-secondary": accent_success_border_secondary,
            "accent-ai-bg": "#b1628633" if dark else "#8f3f7126",
            "accent-ai-border": "#b16286" if dark else "#8f3f71",
            "accent-neutral-bg": "gray",
            "text-error": "red-110" if dark else "red-90",
            "text-warning": "yellow-110" if dark else "yellow-90",
            "text-success": "green-110" if dark else "green-90",
            # Toolbar states
            "toolbar-selected-bg": "blue-100" if dark else "blue-90",
            "toolbar-selected-bg-hovered": "#458588cc" if dark else "#076678cc",
            "toolbar-selected-bg-active": accent_brand,
            "toolbar-run-bg": accent_success,
            "toolbar-run-bg-hovered": "green-90",
            "toolbar-stop-bg": accent_error,
            "toolbar-stop-bg-hovered": "red-90",
            # Controls and chrome
            "control-bg": control_bg,
            "control-bg-disabled": control_bg,
            "control-bg-raised": control_bg_raised,
            "control-bg-small": control_bg_small,
            "control-bg-small-disabled": control_bg_small_disabled,
            "control-border": "bg2",
            "control-border-disabled": "bg1" if dark else "bg2",
            "control-border-raised": "bg3",
            "control-border-small": "bg3",
            "control-border-over-accent": "#ffffff80",
            "control-success-border": "green-90",
            "toolbar-bg-hovered": "bg1",
            "toolbar-bg-pressed": "bg2",
            "transparent-border": "#00000000",
            "toggle-border": "bg3",
            "toggle-button-bg": "bg2",
            "toggle-off-bg": "bg1",
            "tree-indent-guide-border": "bg1",
            "search-match-bg": "#d7992140" if dark else "#d7992133",
            "popup-completion-match-text": text_link,
            # Feedback
            "feedback-bg": feedback_bg,
            "feedback-bg-inline": feedback_bg_inline,
            "feedback-border": "bg2",
            "feedback-control-border": "bg3" if dark else "bg2",
            "feedback-brand-bg": accent_brand_secondary,
            "feedback-brand-border": accent_brand_border_secondary,
            "feedback-error-bg": accent_error_secondary,
            "feedback-error-border": accent_error_border_secondary,
            "feedback-success-bg": accent_success_secondary,
            "feedback-success-border": accent_success_border_secondary,
            "feedback-warning-bg": accent_warning_secondary,
            "feedback-warning-border": accent_warning_border_secondary,
            "feedback-ai-bg": "#b1628633" if dark else "#8f3f7126",
            "feedback-ai-border": "#b16286" if dark else "#8f3f71",
            # Onboarding
            "got-it-bg": "bg2" if dark else "bg0_s",
            "got-it-border": "bg3" if dark else "bg2",
            "got-it-code-border": "bg3" if dark else "bg2",
            "got-it-contrast-button-bg": accent_brand,
            "got-it-shortcut-bg": "bg1",
            "got-it-text-link": "blue-110" if dark else "blue-90",
            "got-it-text-step": "fg4",
            "presentation-assistant-bg": "bg2" if dark else "bg0_s",
        }
    )

    # Parent-theme aliases and transparency helpers.  The bundled themes define
    # these names themselves, so overriding them prevents their blue-tinted
    # whites/blacks from leaking into components we do not name explicitly.
    colors.update(
        {
            "transparent": "#00000000",
            "transparent-border": "#00000000",
            "black": "#000000",
            "white": "#ffffff",
            "transparent-black-10": "#00000008",
            "transparent-black-20": "#00000012",
            "transparent-black-30": "#00000020",
            "transparent-black-40": "#00000030",
            "transparent-black-50": "#00000045",
            "transparent-white-10": "#ffffff10",
            "transparent-white-20": "#ffffff17",
            "transparent-white-30": "#ffffff21",
            "transparent-white-40": "#ffffff29",
            "transparent-white-50": "#ffffff3b",
            "core-bg-transparent-hovered": "#ebdbb214" if dark else "#3c383614",
            "core-bg-transparent-pressed": "#ebdbb226" if dark else "#3c383626",
            "core-border-transparent": "#ebdbb233" if dark else "#3c383633",
            "inlay-bg": "#50494533" if dark else "#d5c4a133",
            "inlay-border": "#7c6f6480" if dark else "#bdae9380",
            "control-brand-bg": accent_brand,
            "control-brand-border": accent_brand,
            "control-error-bg": accent_error,
            "control-error-border": accent_error,
            "control-error-border-secondary": "red-60" if dark else "red-130",
            "control-success-bg": accent_success,
            "control-warning-bg": accent_warning,
            "control-warning-border": accent_warning,
            "control-warning-border-secondary": "yellow-60" if dark else "yellow-130",
            "toolbar-border": "core-border-transparent",
        }
    )

    if not islands:
        colors.update(build_classic_scales(dark, palette, scales))

    return colors


# ---------------------------------------------------------------------------
# UI overrides.
# ---------------------------------------------------------------------------


def build_ui(dark: bool, islands: bool) -> dict:
    border_color = "transparent-border" if islands else "bg2"
    disabled_border = "bg1" if dark else "bg2"
    stripe = "bg0_s"
    table_header = "bg0_s"
    inline_code_bg = "#50494566" if dark else "#d5c4a166"
    combo_border = "#504945" if dark else "#d5c4a1"

    ui: dict = {
        "*": {
            "background": "tool-window-bg",
            "foreground": "text-default",
            "inactiveBackground": "dialog-bg",
            "borderColor": "bg2",
            "disabledBackground": "dialog-bg",
            "disabledBorderColor": disabled_border,
            "disabledText": "text-disabled",
            "disabledForeground": "text-disabled",
            "inactiveForeground": "text-muted",
            "selectionBackground": "selection-bg-active",
            "lightSelectionBackground": "selection-bg-active-muted",
            "selectionForeground": "fg0",
            "selectionInactiveBackground": "selection-bg-inactive",
            "selectionInactiveForeground": "fg0",
            "hoverBackground": "selection-bg-hovered",
            "infoForeground": "text-muted",
            "acceleratorForeground": "text-secondary",
            "shortcutForeground": "text-secondary",
            "underlineColor": "text-link",
            "inactiveUnderlineColor": "bg3",
            "focusColor": "text-link",
            "separatorColor": "bg2",
            "separatorForeground": "bg2",
            "modifiedItemForeground": "text-link",
        },
        "Panel": {
            "background": "tool-window-bg",
            "foreground": "text-default",
        },
        "Label": {
            "foreground": "text-default",
            "errorForeground": "text-error",
            "warningForeground": "text-warning",
            "successForeground": "text-success",
        },
        "Link": {
            "activeForeground": "text-link",
            "hoverForeground": "text-link",
            "pressedForeground": "text-link",
            "visitedForeground": "text-link",
            "secondaryForeground": "text-link",
            "focusedBorderColor": "text-link",
        },
        "MainWindow.background": "main-window-bg",
        "ToolWindow": {
            "background": "tool-window-bg",
            "borderColor": border_color,
            "Header": {
                "background": "bg0_s",
                "inactiveBackground": "tool-window-header-inactive-bg",
                "borderColor": "tool-window-border",
            },
            "HeaderTab": {
                "hoverInactiveBackground": "tool-window-header-inactive-bg",
                "selectedInactiveBackground": "tool-window-header-inactive-bg",
            },
            "Stripe": {
                "background": "main-window-bg",
                "borderColor": "transparent-border",
            },
        },
        "EditorTabs": {
            "background": "editor-tabs-bg",
            "hoverBackground": "tab-bg-hovered",
            "hoverInactiveBackground": "tab-bg-hovered",
            "selectedBackground": "tab-selected-bg-inactive",
            "selectedInactiveBackground": "tab-selected-bg-inactive",
            "underlinedTabBackground": "tab-selected-bg-active",
            "inactiveUnderlinedTabBackground": "tab-selected-bg-inactive",
            "underlinedBorderColor": "tab-selected-border-active",
            "inactiveUnderlinedTabBorderColor": "tab-selected-border-inactive",
            "underlineColor": "tab-selected-border-active",
            "underTabsBorderColor": "editor-border",
            "inactiveMaskColor": "tab-file-color-mask-bg",
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
        "MainMenu": {
            "background": "main-window-bg",
            "foreground": "text-default",
            "selectionBackground": "selection-bg-active",
            "selectionForeground": "text-default",
            "transparentSelectionBackground": "#3c383633" if dark else "#ebdbb233",
        },
        "PopupMenu": {
            "background": "popup-bg",
            "foreground": "text-default",
        },
        "Menu": {
            "background": "popup-bg",
            "foreground": "text-default",
            "separatorColor": "popup-border",
        },
        "MenuItem": {
            "background": "popup-bg",
            "foreground": "text-default",
            "selectionBackground": "selection-bg-active",
            "selectionForeground": "text-default",
            "acceleratorForeground": "text-secondary",
        },
        "Borders.color": "bg2",
        "Borders.ContrastBorderColor": "bg2",
        "Separator.separatorColor": "bg2",
        "Separator.foreground": "bg2",
        # Keep the fill on the rounded start/end keys. A separate solid
        # "background" key paints a square behind the button arc.
        "Button": {
            "arc": 8,
            "foreground": "text-default",
            "startBackground": "control-bg",
            "endBackground": "control-bg",
            "startBorderColor": "bg2",
            "endBorderColor": "bg2",
            "focusedBorderColor": "control-bg",
            "shadowColor": "transparent",
            "loadingForeground": "text-secondary",
            "disabledForeground": "text-disabled",
            "default": {
                "foreground": "fg0",
                "startBackground": "bg0_s",
                "endBackground": "bg0_s",
                "startBorderColor": "bg2",
                "endBorderColor": "bg2",
                "focusedBorderColor": "control-bg",
                "shadowColor": "transparent",
                "loadingForeground": "text-muted",
            },
            "Split": {
                "default": {
                    "iconColor": "fg0",
                    "separatorColor": "#ffffff66",
                }
            },
        },
        "TextField": {
            "background": "control-bg",
            "foreground": "text-default",
            "borderColor": "bg2",
            "inactiveBackground": "control-bg",
            "disabledBackground": "control-bg-disabled",
            "disabledForeground": "text-disabled",
        },
        "TextArea": {
            "background": "control-bg",
            "foreground": "text-default",
            "borderColor": "bg2",
        },
        "PasswordField": {
            "background": "control-bg",
            "foreground": "text-default",
            "borderColor": "bg2",
        },
        "Spinner": {
            "background": "control-bg",
            "foreground": "text-default",
            "borderColor": "bg2",
        },
        "ComboBox": {
            "background": "control-bg",
            "foreground": "text-default",
            "nonEditableBackground": "control-bg",
            "disabledBackground": "control-bg-disabled",
            "borderColor": "bg2",
            "ArrowButton": {
                "background": "control-bg",
                "nonEditableBackground": "control-bg",
                "iconColor": "fg0",
                "disabledIconColor": "text-disabled",
            },
        },
        "ComboPopup.border": f"1,1,1,1,{combo_border}",
        "ScrollBar": {
            "background": "editor-bg",
            "trackColor": "editor-bg",
            "thumbColor": "bg2",
            "thumbBorderColor": "bg2",
            "hoverTrackColor": "editor-bg",
            "hoverThumbColor": "bg1",
            "hoverThumbBorderColor": "bg1",
            "Transparent": {
                "trackColor": "editor-bg",
                "thumbColor": "bg2",
                "thumbBorderColor": "bg2",
                "hoverTrackColor": "editor-bg",
                "hoverThumbColor": "bg1",
                "hoverThumbBorderColor": "bg1",
            },
            "Mac": {
                "background": "editor-bg",
                "trackColor": "editor-bg",
                "thumbColor": "bg2",
                "thumbBorderColor": "bg2",
                "hoverTrackColor": "editor-bg",
                "hoverThumbColor": "bg1",
                "hoverThumbBorderColor": "bg1",
                "Transparent": {
                    "trackColor": "editor-bg",
                    "thumbColor": "bg2",
                    "thumbBorderColor": "bg2",
                    "hoverTrackColor": "editor-bg",
                    "hoverThumbColor": "bg1",
                    "hoverThumbBorderColor": "bg2",
                },
            },
        },
        "Table": {
            "gridColor": "bg2",
            "stripeColor": stripe,
            "alternativeRowBackground": stripe,
            "hoverBackground": "selection-bg-hovered",
            "hoverInactiveBackground": "selection-bg-hovered",
        },
        "TableHeader": {
            "background": table_header,
            "foreground": "text-secondary",
            "bottomSeparatorColor": "bg2",
            "separatorColor": "bg2",
        },
        "List": {
            "background": "tool-window-bg",
            "foreground": "text-default",
            "hoverBackground": "selection-bg-hovered",
            "hoverInactiveBackground": "selection-bg-hovered",
            "selectionBackground": "selection-bg-active",
            "selectionForeground": "text-default",
            "selectionInactiveBackground": "selection-bg-inactive",
            "selectionInactiveForeground": "text-default",
            "Tag": {
                "background": "bg2" if dark else "bg1",
                "foreground": "fg3",
            },
        },
        "Tree": {
            "background": "tool-window-bg",
            "foreground": "text-default",
            "hoverBackground": "selection-bg-hovered",
            "hoverInactiveBackground": "selection-bg-hovered",
            "hash": "bg1",
        },
        "ToolTip": {
            "background": "feedback-bg",
            "border": "feedback-border",
            "foreground": "text-default",
            "selectionBackground": "selection-bg-active",
        },
        "Editor.ToolTip": {
            "background": "popup-bg",
            "border": "popup-border",
            "foreground": "text-default",
            "selectionBackground": "selection-bg-active",
            "errorBackground": "feedback-error-bg",
            "errorBorder": "feedback-error-border",
            "successBackground": "feedback-success-bg",
            "successBorder": "feedback-success-border",
            "warningBackground": "feedback-warning-bg",
            "warningBorder": "feedback-warning-border",
            "iconHoverBackground": "selection-bg-hovered",
        },
        "Notification": {
            "background": "feedback-bg",
            "borderColor": "feedback-border",
            "foreground": "text-default",
            "linkForeground": "text-link",
            "iconHoverBackground": "selection-bg-hovered",
            "Button": {
                "background": "feedback-bg",
                "borderColor": "feedback-control-border",
                "foreground": "text-default",
            },
            "MoreButton": {
                "background": "feedback-bg-inline",
                "innerBorderColor": "feedback-border",
                "foreground": "text-muted",
            },
        },
        "ParameterInfo": {
            "background": "popup-bg",
            "currentOverloadBackground": "selection-bg-active",
            "borderColor": "feedback-border",
            "foreground": "text-default",
            "currentParameterForeground": "text-default",
            "disabledForeground": "text-secondary",
            "infoForeground": "text-muted",
            "lineSeparatorColor": "feedback-border",
        },
        "SearchMatch": {
            "startBackground": "search-match-bg",
            "endBackground": "search-match-bg",
        },
        "CompletionPopup": {
            "foreground": "text-default",
            "matchForeground": "text-link",
            "Advertiser": {
                "foreground": "text-secondary",
                "background": "bg1",
            },
        },
        "SearchEverywhere": {
            "List.settingsBackground": "bg1",
            "Tab": {
                "selectedBackground": "selection-bg-active",
                "selectedForeground": "text-default",
            },
            "SearchField.background": "control-bg",
            "Advertiser": {
                "foreground": "text-secondary",
                "background": "bg1",
            },
        },
        "Code": {
            "Inline": {
                "backgroundColor": inline_code_bg,
                "backgroundOpacity": 26,
            },
            "Block": {
                "borderColor": "editor-border",
                "EditorPane": {
                    "backgroundColor": "editor-bg",
                    "borderColor": "editor-border",
                },
            },
        },
        "Counter": {
            "background": "gray-60",
            "foreground": "fg0" if dark else "#ffffff",
        },
        "Tag.background": "bg2",
        "Tag.foreground": "fg2",
        "Badge": {
            "greenOutlineForeground": "text-success",
            "greenOutlineBorderColor": "control-success-border",
            "blueBackground": "blue" if dark else "blue",
            "blueForeground": "bg0_h" if dark else "#ffffff",
            "blueSecondaryBackground": "#458588b3" if dark else "#07667829",
            "blueSecondaryForeground": "blue-110" if dark else "blue-90",
            "greenBackground": "green" if dark else "green",
            "greenForeground": "bg0_h" if dark else "#ffffff",
            "greenSecondaryBackground": "#98971ab3" if dark else "#79740e29",
            "greenSecondaryForeground": "green-110" if dark else "green-90",
            "purpleBackground": "purple" if dark else "purple",
            "purpleForeground": "bg0_h" if dark else "#ffffff",
            "purpleSecondaryBackground": "#b16286b3" if dark else "#8f3f7129",
            "purpleSecondaryForeground": "purple-110" if dark else "purple-90",
            "graySecondaryBackground": "#fbf1c729" if dark else "#2828281a",
            "graySecondaryForeground": "fg1",
            "disabledBackground": "#fbf1c729" if dark else "#2828281a",
            "disabledForeground": "#fbf1c766" if dark else "#28282866",
        },
        "FileColor": {
            "Yellow": "#fabd2f22" if dark else "#b5761422",
            "Green": "#b8bb2622" if dark else "#79740e22",
            "Blue": "#83a59822" if dark else "#07667822",
            "Violet": "#d3869b22" if dark else "#8f3f7122",
            "Orange": "#fe801922" if dark else "#af3a0322",
            "Rose": "#cc241d22",
            "Gray": "#92837422",
        },
        "VersionControl": {
            "Log": {
                "Commit": {
                    "currentBranchBackground": "bg2",
                    "unmatchedForeground": "text-muted",
                    "hoveredBackground": "bg1",
                    "Reference.foreground": "text-muted",
                }
            },
            "FileHistory.Commit.selectedBranchBackground": "bg2",
            "MarkerPopup": {
                "borderColor": "bg2",
            },
            "GitLog": {
                "headIconColor": "yellow" if dark else "yellow_dim",
                "localBranchIconColor": "green" if dark else "green",
                "otherIconColor": "text-muted",
                "remoteBranchIconColor": "purple" if dark else "purple",
                "tagIconColor": "text-muted",
            },
            "Merge.Status.NoConflicts.foreground": "green" if dark else "green",
        },
        "Debugger": {
            "Variables": {
                "valueForeground": "orange" if dark else "orange",
                "collectingDataForeground": "text-muted",
                "evaluatingExpressionForeground": "text-muted",
                "changedValueForeground": "text-link",
                "modifyingValueForeground": "text-link",
                "errorMessageForeground": "text-error",
                "exceptionForeground": "text-error",
                "typeForeground": "text-muted",
            }
        },
        "DataSummary.Chart.barColor": "text-link",
        "MemoryIndicator": {
            "allocatedBackground": "bg1",
            "usedBackground": "#d7992180" if dark else "#b5761480",
        },
        "HelpBrowser.titleHighlightForeground": "text-link",
        "Lesson.shortcutBackground": "bg2",
        "Review": {
            "Branch": {
                "Background": "bg1",
                "Background.Hover": "bg2",
            },
            "State": {
                "Background": "bg2",
                "Foreground": "text-secondary",
            },
            "ChatItem.Hover": "#3c383633" if dark else "#ebdbb233",
        },
        "UnattendedHostStatus": {
            "dangerBackground": "red" if dark else "red",
            "warningBackground": "yellow" if dark else "yellow",
            "warningForeground": "bg0_h",
        },
        "PresentationAssistant": {
            "Bright.keymapLabel": "text-muted",
            "Pale.Popup.border": "bg2",
            "Pale.PopupBackground": "bg1" if dark else "popup-bg",
            "Pale.Popup.foreground": "text-default",
            "Pale.keymapLabel": "text-secondary",
        },
        "NuGet.section.background": "bg0" if dark else "bg0_h",
        "NuGet.section.hoverBackground": "bg1",
        "ManagedIdeBadgeBorder": "bg2",
        "ManagedIdeBadgeBackground": "bg1",
        "ManagedIdeBadgeBackgroundHover": "bg2",
        "ManagedIdeMenuItemHover": "bg2",
        "Slider": {
            "buttonColor": "fg2",
            "buttonBorderColor": "editor-bg",
            "tickColor": "fg4",
            "trackColor": "bg3" if dark else "bg2",
        },
        "Editor.SearchField": {
            "background": "editor-bg-inline",
            "borderColor": "editor-border-inline",
        },
        "Editor.Toolbar": {
            "borderColor": "editor-border-inline",
        },
        "WelcomeScreen.Details.background": "dialog-bg",
        "WelcomeScreen.SidePanel.background": "dialog-bg",
        "WelcomeScreen.Banner.background": "dialog-bg-inline",
        "WelcomeScreen.Projects.actions.background": "bg1",
        "OnePixelDivider.background": "bg2",
        "ToolBar.separatorColor": "bg2",
        "MenuBar.borderColor": "bg2",
        "ValidationTooltip": {
            "errorBackground": "feedback-error-bg",
            "errorBorderColor": "feedback-error-border",
            "errorForeground": "text-default",
            "warningBackground": "feedback-warning-bg",
            "warningBorderColor": "feedback-warning-border",
            "warningForeground": "text-default",
        },
        "NotificationsToolwindow": {
            "newNotification.background": "bg1",
            "newNotification.hoverBackground": "bg2",
            "Notification.hoverBackground": "bg0_s",
        },
        "NewUiOnboarding.Dialog.background": "dialog-bg",
        "MainWindow.Tab": {
            "background": "main-window-bg",
            "foreground": "text-muted",
            "hoverBackground": "bg1",
            "hoverForeground": "text-default",
            "selectedBackground": "main-window-bg",
            "selectedForeground": "text-default",
            "selectedInactiveBackground": "bg1",
            "separatorColor": "bg2",
            "borderColor": "main-window-bg",
        },
        "TitlePane": {
            "background": "tool-window-bg",
            "inactiveBackground": "tool-window-bg",
            "foreground": "text-default",
        },
        "GotItTooltip": {
            "background": "got-it-bg",
            "borderColor": "got-it-border",
            "foreground": "text-default",
            "Header.foreground": "text-default",
            "secondaryActionForeground": "got-it-text-link",
            "linkForeground": "got-it-text-link",
            "linkUnderlineDefaultColor": "got-it-text-link",
            "linkUnderlineHoveredColor": "got-it-text-link",
            "stepForeground": "got-it-text-step",
            "shortcutForeground": "text-default",
            "shortcutBackground": "got-it-shortcut-bg",
            "codeForeground": "text-default",
            "codeBackground": "got-it-bg",
            "codeBorderColor": "got-it-code-border",
            "iconFillColor": "got-it-bg",
            "iconBorderColor": "icon-over-accent",
            "imageBorderColor": "got-it-bg",
            "animationBackground": "bg1",
            "Button": {
                "foreground": "text-default",
                "startBackground": "transparent",
                "endBackground": "transparent",
                "startBorderColor": "feedback-control-border",
                "endBorderColor": "feedback-control-border",
                "contrastBackground": "got-it-contrast-button-bg",
            },
        },
        "Tooltip.Learning": {
            "background": "got-it-bg",
            "borderColor": "got-it-border",
            "foreground": "text-default",
            "Header.foreground": "text-default",
            "stepNumberForeground": "got-it-text-step",
            "secondaryActionForeground": "got-it-text-link",
            "linkForeground": "got-it-text-link",
            "linkUnderlineDefaultColor": "got-it-text-link",
            "linkUnderlineHoveredColor": "got-it-text-link",
            "spanBackground": "got-it-shortcut-bg",
            "spanForeground": "text-default",
            "codeBorderColor": "got-it-code-border",
            "iconFillColor": "got-it-bg",
            "iconBorderColor": "icon-over-accent",
        },
        "DragAndDrop.areaBackground": "#07667833",
        "DragAndDrop.rowBackground": "#07667826",
        "ToolWindow.Button.DragAndDrop.buttonDropBackground": "#07667880",
        "ToolWindow.Button.DragAndDrop.buttonDropBorderColor": "accent-brand-border",
        "ToolWindow.DragAndDrop.areaBackground": "#0766784d",
        "RunWidget": {
            "iconColor": "icon-default-stroke",
            "runIconColor": "icon-green-stroke",
            "runningBackground": "toolbar-run-bg",
            "stopBackground": "toolbar-stop-bg",
            "runningIconColor": "icon-over-accent",
            "hoverBackground": "toolbar-bg-hovered",
            "pressedBackground": "toolbar-bg-pressed",
        },
    }

    # Less common components that the bundled themes hardcode.  Keeping these
    # here means a profiling session, trial banner, plugin search or AI recap
    # cannot reintroduce JetBrains blue/gray.
    ui.update(
        {
            "ActionButton.hoverBackground": "#ebdbb20f" if dark else "#3c38360f",
            "ActionButton.hoverBorderColor": "#00000000",
            "ActionButton.pressedBackground": "#ebdbb21f" if dark else "#3c38361f",
            "ActionButton.pressedBorderColor": "#00000000",
            "Abbreviation.background": "#665c5440" if dark else "#bdae9340",
            "DisclosureButton.defaultBackground": "#00000000",
            "DisclosureButton.hoverOverlay": "core-bg-transparent-hovered",
            "DisclosureButton.pressedOverlay": "core-bg-transparent-pressed",
            "WelcomeScreen.Frame.DisclosureButton.hoverOverlay": "core-bg-transparent-hovered",
            "WelcomeScreen.Frame.DisclosureButton.pressedOverlay": "core-bg-transparent-pressed",
            "InlineBanner.hoverBackground": "core-bg-transparent-hovered",
            "InlineBanner.pressedBackground": "core-bg-transparent-pressed",
            "MainToolbar.Dropdown.transparentHoverBackground": "core-bg-transparent-hovered",
            "TitlePane.Button.hoverBackground": "core-bg-transparent-hovered",
            "EditorTabs.inactiveColoredFileBackground": "tab-file-color-mask-bg",
            "List.Button.separatorColor": "bg3",
            "MainWindow.FullScreeControl.Background": "bg3",
            "Notification.WelcomeScreen.separatorColor": "bg2",
            "ProgressBar.progressCounterBackground": "accent-brand-bg",
            "Plugins.background": "dialog-bg",
            "CodeWithMe.Users.4.StopFollowingLinkForeground": "text-link",
            "CodeWithMe.Users.6.StopFollowingLinkForeground": "text-link",
            "HelpBrowser.AiEditor.background": "feedback-ai-bg",
            "HelpBrowser.AiEditor.verticalMarkerColor": "accent-ai-border",
            "LineProfiler.Line.foreground": "text-muted",
            "LineProfiler.Line.labelBackground": "bg0_s",
            "LineProfiler.HotLine.labelBackground": "feedback-error-bg",
            "LineProfiler.HotLine.foreground": "text-error",
            "LineProfiler.HotLine.hoverBackground": "selection-bg-active",
            "LineProfiler.IgnoredLine.foreground": "text-disabled",
            "Profiler.CpuChart.inactiveBackground": "#79740e33" if dark else "#b8bb2633",
            "Profiler.MemoryChart.inactiveBackground": "#07667833" if dark else "#83a59833",
            "TrialWidget.Default.foreground": "text-default",
            "TrialWidget.Default.background": "bg0_s",
            "TrialWidget.Default.borderColor": "bg2",
            "TrialWidget.Default.hoverForeground": "fg0",
            "TrialWidget.Default.hoverBackground": "bg1",
            "TrialWidget.Default.hoverBorderColor": "bg3",
            "TrialWidget.Active.foreground": "text-success",
            "TrialWidget.Active.background": "bg0_s",
            "TrialWidget.Active.borderColor": "accent-success-border",
            "TrialWidget.Active.hoverForeground": "text-success",
            "TrialWidget.Active.hoverBackground": "bg1",
            "TrialWidget.Active.hoverBorderColor": "accent-success-border",
            "TrialWidget.Alert.foreground": "text-warning",
            "TrialWidget.Alert.background": "bg0_s",
            "TrialWidget.Alert.borderColor": "bg2",
            "TrialWidget.Alert.hoverForeground": "text-warning",
            "TrialWidget.Alert.hoverBackground": "bg1",
            "TrialWidget.Alert.hoverBorderColor": "bg3",
            "TrialWidget.Expiring.foreground": "text-error",
            "TrialWidget.Expiring.background": "bg0_s",
            "TrialWidget.Expiring.borderColor": "bg2",
            "TrialWidget.Expiring.hoverForeground": "text-error",
            "TrialWidget.Expiring.hoverBackground": "bg1",
            "TrialWidget.Expiring.hoverBorderColor": "bg3",
            "TrialWidget.Progress.foreground": "text-muted",
            "TrialWidget.Progress.background": "bg0_s",
            "TrialWidget.Progress.borderColor": "bg2",
            "TrialWidget.Progress.hoverForeground": "text-muted",
            "TrialWidget.Progress.hoverBackground": "bg1",
            "TrialWidget.Progress.hoverBorderColor": "bg3",
            "Recap.ijnext": "accent-brand-bg",
            "Recap.cardBackground": "bg0_s",
            "Recap.cardBorderColor": "bg2",
            "Recap.cardHeaderTitle": "fg0",
            "Recap.cardHeaderLinkBackground": "bg1",
            "Recap.cardHeaderSubtitle": "text-muted",
            "Recap.cardFooterForeground": "text-muted",
            "Recap.chroniclesBackground": "bg1",
            "Recap.chroniclesBorderColor": "bg2",
            "Recap.chroniclesBackgroundHovered": "bg2",
            "Recap.chroniclesForeground": "text-default",
            "Recap.chroniclesForegroundGreyed": "text-muted",
            "Recap.errorBackground": "feedback-error-bg",
            "Recap.errorBorder": "feedback-error-border",
            "Recap.errorForeground": "text-default",
            "PackageSearch.SearchResult.background": "bg0_s",
            "PackageSearch.SearchResult.hoverBackground": "bg1",
            "PackageSearch.SearchResult.PackageTag.background": "bg2",
            "PackageSearch.SearchResult.PackageTag.hoverBackground": "bg3",
            "PackageSearch.PackageTag.hoverBackground": "bg3",
            "FlameGraph.Tooltip.scaleBackground": "bg2",
            "FlameGraph.Tooltip.scaleColor": "accent-brand-bg",
            "FlameGraph.Tooltip.foreground": "text-default",
        }
    )

    # Welcome-screen project gradients, built from the same accent anchors.
    recent = [
        ("orange", "red"),
        ("yellow", "yellow_dim"),
        ("green", "green_dim"),
        ("aqua", "blue"),
        ("blue", "purple"),
        ("purple", "purple_dim"),
        ("purple", "blue"),
        ("aqua", "aqua_dim"),
        ("green", "aqua"),
    ]
    palette = DARK if dark else LIGHT
    for i, (start, end) in enumerate(recent, start=1):
        avatar_start = palette[start]
        avatar_end = palette[end]
        if dark:
            grad_start = mix("#282828", palette[start], 0.22)
        else:
            grad_start = mix("#f9f5d7", palette[start], 0.12)
        ui[f"RecentProject.Color{i}.Avatar.Start"] = avatar_start
        ui[f"RecentProject.Color{i}.Avatar.End"] = avatar_end
        ui[f"RecentProject.Color{i}.MainToolbarGradientStart"] = grad_start

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


# ---------------------------------------------------------------------------
# Theme assembly.
# ---------------------------------------------------------------------------


def build_grad_colors(dark: bool, bg: str) -> dict[str, str]:
    groups = [
        ("amber", "#fe8019", "#af3a03"),
        ("rust", "#fb4934", "#9d0006"),
        ("olive", "#b8bb26", "#79740e"),
        ("sky", "#83a598", "#076678"),
        ("cobalt", "#83a598", "#076678"),
        ("plum", "#d3869b", "#8f3f71"),
        ("violet", "#d3869b", "#8f3f71"),
        ("ocean", "#8ec07c", "#427b58"),
        ("grass", "#b8bb26", "#79740e"),
    ]
    out: dict[str, str] = {}
    for i, (name, bright, darkaccent) in enumerate(groups, start=1):
        accent = bright if dark else darkaccent
        if dark:
            a1 = mix(bg, accent, 0.55)
            a1_secondary = mix(bg, accent, 0.25)
            a2 = mix(bg, accent, 0.18)
            base = mix(bg, accent, 0.10)
        else:
            a1 = mix(bg, accent, 0.16)
            a1_secondary = mix(bg, accent, 0.08)
            a2 = mix(bg, accent, 0.05)
            base = mix(bg, accent, 0.03)
        out[f"grad-g{i}-{name}-a1"] = a1 + "ff"
        out[f"grad-g{i}-{name}-a1-secondary"] = a1_secondary
        out[f"grad-g{i}-{name}-a1-transparent"] = a1 + "00"
        out[f"grad-g{i}-{name}-a2"] = a2
        out[f"grad-g{i}-{name}-bg"] = base
    if dark:
        out.update(
            {
                "grad-hor-left": "#3c383633",
                "grad-hor-right": "#3c38364d",
                "grad-ver-top": "#3c38361a",
                "grad-ver-bottom": "#3c383680",
            }
        )
    else:
        out.update(
            {
                "grad-hor-left": "#ebdbb233",
                "grad-hor-right": "#ebdbb24d",
                "grad-ver-top": "#ebdbb21a",
                "grad-ver-bottom": "#ebdbb280",
            }
        )
    return out


def build_theme(spec: dict) -> dict:
    dark = spec["dark"]
    islands = spec["islands"]
    background = spec["background"]
    colors = build_colors(spec["palette"], dark, islands, background)
    colors.update(
        build_grad_colors(dark, spec["palette"][BG_KEYS[background]])
    )
    return {
        "name": spec["name"],
        "dark": dark,
        "author": "devnamrits",
        "editorScheme": spec["scheme"],
        "parentTheme": spec["parent"],
        "colors": colors,
        "ui": build_ui(dark, islands),
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
