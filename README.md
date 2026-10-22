# Gruvbox Archipelago

A modern **Gruvbox-inspired** theme for JetBrains IDEs with first-class support
for the **Islands UI** — plus classic flat variants for people who prefer the
pre-Islands look.

> **Status:** early development (`0.1.0`). Built and verified against
> IntelliJ IDEA 2026.2.1. Marketplace publication is next.

## Themes

| Theme | Layout | Mode |
| --- | --- | --- |
| **Archipelago Dark** | Islands (rounded, floating panels) | Dark |
| **Archipelago Light** | Islands (rounded, floating panels) | Light |
| **Mainland Dark** | Classic flat UI | Dark |
| **Mainland Light** | Classic flat UI | Light |

The Islands variants inherit from JetBrains' `Islands Dark` / `Islands Light`
themes, so they pick up the platform's rounded corners, spacing, and island
borders. The Mainland variants inherit from the classic `ExperimentalDark` /
`ExperimentalLight` themes and intentionally stay flat.

## Highlights

- Gruvbox hard/soft background layering tuned for Islands contrast.
- Separate UI and editor-scheme palettes for dark and light.
- Editor schemes cover Java, Kotlin, Rust, Python, JavaScript/TypeScript,
  HTML/XML, SQL, shell, diff, VCS, and more.
- Transparent toolbar/status-bar borders in the Islands variants.
- New UI tab treatment with a Gruvbox blue selected-tab accent.
- No bundled fonts, no runtime dependencies. Themes only.

## Installation

### From a release ZIP

1. Download the latest `gruvbox-archipelago-*.zip` from Releases.
2. In the IDE: **Settings → Plugins → ⚙ → Install Plugin from Disk…**
3. Pick the ZIP and restart the IDE.
4. Choose a theme in **Settings → Appearance & Behavior → Appearance**.

### From source

```bash
./gradlew buildPlugin
# ZIP: build/distributions/gruvbox-archipelago-0.1.0.zip
```

To build against the IntelliJ installation already on your machine instead of
downloading a platform distribution:

```bash
./gradlew buildPlugin -PlocalIdePath="/Applications/IntelliJ IDEA.app"
```

Requires **JDK 17+** and **Gradle 9** (the wrapper handles Gradle).

## Compatibility

- IntelliJ Platform **2025.3+** (`since-build 253`).
- Verified with IntelliJ IDEA **2026.2.1** (`build 262.9437.185`).
- Works in any JetBrains IDE that supports custom themes and the Islands UI.

## How it is built

The four theme JSON files and the two editor schemes live in
`src/main/resources/themes/`. The JSON files are generated from a shared,
versioned palette by `scripts/generate_themes.py`:

```bash
python3 scripts/generate_themes.py
```

This keeps the dark/light and Islands/classic variants in sync.

## Project layout

```text
src/main/resources/
├── META-INF/plugin.xml
├── META-INF/pluginIcon*.svg
└── themes/
    ├── archipelago-dark.theme.json
    ├── archipelago-light.theme.json
    ├── mainland-dark.theme.json
    ├── mainland-light.theme.json
    └── schemes/
        ├── archipelago-dark.xml
        └── archipelago-light.xml
```

## Credits

- **Gruvbox palette** — [Pavel Pertsev (morhetz)](https://github.com/morhetz/gruvbox), MIT.
- **Original IntelliJ Gruvbox theme and editor schemes** —
  [Vincent Parizet](https://github.com/Vincent-P/gruvbox-intellij-theme), MIT.
  The original project is deprecated; this is an independent, maintained
  derivative focused on Islands support.
- **Islands theme guidance** — [IntelliJ Platform SDK](https://plugins.jetbrains.com/docs/intellij/supporting-islands-theme.html).

JetBrains and IntelliJ IDEA are trademarks of JetBrains s.r.o. This project is
not affiliated with or endorsed by JetBrains.

## License

[MIT](LICENSE). See [NOTICE](NOTICE) for upstream attribution.
