# Palette

Gruvbox Archipelago uses the canonical Gruvbox palette. The Islands themes use
three background layers — editor, tool window, and main window — selected from
the Hard, Medium, or Soft variant. Mainland uses the classic flat layout.

## Background layers

### Dark

| Role | Hard | Medium | Soft |
| --- | --- | --- | --- |
| Editor background | `#1d2021` | `#282828` | `#32302f` |
| Tool window / island | `#282828` | `#32302f` | `#3c3836` |
| Main window backdrop | `#32302f` | `#3c3836` | `#504945` |

### Light

| Role | Hard | Medium | Soft |
| --- | --- | --- | --- |
| Editor background | `#f9f5d7` | `#fbf1c7` | `#f2e5bc` |
| Tool window / island | `#fbf1c7` | `#f2e5bc` | `#ebdbb2` |
| Main window backdrop | `#ebdbb2` | `#d5c4a1` | `#d5c4a1` |

## UI roles

| Role | Dark | Light |
| --- | --- | --- |
| Raised surface | `#3c3836` | `#f9f5d7` |
| Selection | `#504945` | `#ebdbb2` |
| Muted border | `#665c54` | `#bdae93` |
| Disabled text | `#7c6f64` | `#a89984` |
| Muted text | `#a89984` | `#7c6f64` |
| Secondary text | `#bdae93` | `#665c54` |
| Foreground | `#ebdbb2` | `#3c3836` |
| Bright foreground | `#fbf1c7` | `#282828` |

## Accents

| Role | Dark | Light |
| --- | --- | --- |
| Brand | `#458588` | `#076678` |
| Link / selected tab underline | `#83a598` | `#076678` |
| Red | `#fb4934` | `#9d0006` |
| Green | `#b8bb26` | `#79740e` |
| Yellow | `#fabd2f` | `#b57614` |
| Purple | `#d3869b` | `#8f3f71` |
| Aqua | `#8ec07c` | `#427b58` |
| Orange | `#fe8019` | `#af3a03` |

## Mainland

Mainland uses the classic flat layout: editor, tool windows, and main window
all use the selected background. The shipped Mainland themes use Medium
(`#282828` dark, `#fbf1c7` light). Borders and selection use the common UI roles
above.

## Canonical usage

UI surfaces, text, borders, selection, tabs, feedback states, and all six editor
schemes resolve to canonical Gruvbox hex values, or to canonical Gruvbox colors
with alpha. IntelliJ's 16-step primitive ramps and the welcome-screen gradients
need intermediate shades, so those are mixed only from canonical Gruvbox colors
and the selected variant's background. No JetBrains gray or blue values are
used.

## Islands contrast

The Islands guidance recommends at least **1.20:1** contrast between the main
window backdrop and the editor/tool-window layers.

| Theme | Editor → backdrop | Ratio |
| --- | --- | --- |
| Dark Hard | `#1d2021` → `#32302f` | 1.25:1 |
| Dark Medium | `#282828` → `#3c3836` | 1.27:1 |
| Dark Soft | `#32302f` → `#504945` | 1.49:1 |
| Light Hard | `#f9f5d7` → `#ebdbb2` | 1.25:1 |
| Light Medium | `#fbf1c7` → `#d5c4a1` | 1.51:1 |
| Light Soft | `#f2e5bc` → `#d5c4a1` | 1.37:1 |

The tool-window layer sits between the editor and the main backdrop, creating
three visually distinct planes without drawing hard borders.

## Editor schemes

The Hard schemes are derived from Vincent Parizet's hard dark/light schemes and
preserve their syntax-color roles. Medium and Soft are generated from Hard by
`scripts/generate_schemes.py`; only the surface colors change. See
[NOTICE](../NOTICE).
