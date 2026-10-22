# Palette

Gruvbox Archipelago uses the canonical Gruvbox palette, with the editor
backgrounds from the **hard** variants and three UI layers for the Islands
layout.

## Dark

| Role | Hex |
| --- | --- |
| Editor background (hard) | `#1d2021` |
| Tool window / island | `#282828` |
| Main window backdrop | `#32302f` |
| Raised surface / border | `#3c3836` |
| Selection | `#504945` |
| Muted border | `#665c54` |
| Disabled text | `#7c6f64` |
| Muted text | `#a89984` |
| Secondary text | `#bdae93` |
| Foreground | `#ebdbb2` |
| Bright foreground | `#fbf1c7` |
| Accent (brand) | `#458588` |
| Link | `#83a598` |
| Selected tab underline | `#83a598` |
| Red | `#fb4934` |
| Green | `#b8bb26` |
| Yellow | `#fabd2f` |
| Purple | `#d3869b` |
| Aqua | `#8ec07c` |
| Orange | `#fe8019` |

## Light

| Role | Hex |
| --- | --- |
| Editor background (hard) | `#f9f5d7` |
| Tool window / island | `#fbf1c7` |
| Main window backdrop | `#ebdbb2` |
| Raised surface / border | `#d5c4a1` |
| Selection | `#ebdbb2` |
| Muted border | `#bdae93` |
| Disabled text | `#a89984` |
| Muted text | `#7c6f64` |
| Secondary text | `#665c54` |
| Foreground | `#3c3836` |
| Bright foreground | `#282828` |
| Accent (brand) | `#076678` |
| Link | `#076678` |
| Selected tab underline | `#076678` |
| Red | `#9d0006` |
| Green | `#79740e` |
| Yellow | `#b57614` |
| Purple | `#8f3f71` |
| Aqua | `#427b58` |
| Orange | `#af3a03` |

## Islands contrast

The Islands guidance recommends at least **1.20:1** contrast between the main
window backdrop and the editor/tool-window layers.

| Theme | Pair | Ratio |
| --- | --- | --- |
| Dark | `#1d2021` editor → `#32302f` backdrop | 1.25:1 |
| Light | `#f9f5d7` editor → `#ebdbb2` backdrop | 1.25:1 |

The tool-window layer sits between the two, creating three visually distinct
planes without drawing hard borders.

## Editor schemes

The editor schemes are derived from the hard dark/light schemes in Vincent
Parizet's original Gruvbox theme and preserve its syntax-color roles. See
[NOTICE](../NOTICE).
