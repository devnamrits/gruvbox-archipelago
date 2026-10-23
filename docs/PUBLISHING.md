# Publishing

This checklist takes the project from a local build to a JetBrains Marketplace
listing.

## 1. Prepare the release

1. Update `version` in `build.gradle.kts`.
2. Regenerate the theme JSON files and editor schemes:

   ```bash
   python3 scripts/generate_themes.py
   python3 scripts/generate_schemes.py
   python3 scripts/verify_themes.py
   ```

3. Move the `Unreleased` notes in `CHANGELOG.md` under the new version.
4. Commit and tag:

   ```bash
   git add .
   git commit -m "release: v0.1.0"
   git tag -a v0.1.0 -m "Gruvbox Archipelago 0.1.0"
   git push origin main --tags
   ```

## 2. Build and verify

```bash
./gradlew clean buildPlugin verifyPluginStructure \
  verifyPluginProjectConfiguration \
  -PlocalIdePath="/Applications/IntelliJ IDEA.app"
```

The installable ZIP is written to
`build/distributions/gruvbox-archipelago-<version>.zip`.

Load it once in a clean IDE profile before publishing:

- **Settings → Plugins → ⚙ → Install Plugin from Disk…**
- Check all eight themes in **Settings → Appearance**.
- Verify tool windows, popups, the commit dialog, and the editor scheme.
- Switch between Hard, Medium, and Soft to confirm the tab and panel layers.

## 3. Screenshots for the listing

The Marketplace listing needs at least one screenshot. Use four or five PNGs at
1280×800 or larger:

- `screenshots/archipelago-dark.png` — Islands dark, Medium default.
- `screenshots/archipelago-light.png` — Islands light, Medium default.
- `screenshots/mainland-dark.png` — classic dark, Medium.
- `screenshots/mainland-light.png` — classic light, Medium.
- `screenshots/archipelago-variants.png` — optional Hard/Medium/Soft comparison.

For consistent shots:

1. Use a clean IDE profile and a representative project.
2. Set the editor font to **IBM Plex Mono 14** (the font used by the original
   Gruvbox screenshots) or keep the IDE default.
3. Hide personal paths, tokens, and unrelated notifications.
4. Capture the whole IDE window, not just the editor.

## 4. Sign the plugin (recommended)

Generate a signing key pair once and keep it out of the repository:

```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out private.pem
openssl req -new -x509 -key private.pem -out cert.pem -days 3650
```

Then sign the ZIP:

```bash
./gradlew signPlugin \
  -Psigning.certificateChain=cert.pem \
  -Psigning.privateKey=private.pem \
  -Psigning.password='<key-password>'
```

The Gradle IntelliJ Platform plugin also supports the
`CERTIFICATE_CHAIN`, `PRIVATE_KEY`, and `PRIVATE_KEY_PASSWORD` environment
variables in CI. Keep the private key in repository secrets.

## 5. Create the Marketplace listing

1. Sign in at <https://plugins.jetbrains.com/>.
2. **Upload plugin** → choose the signed ZIP.
3. Fill in:
   - **Name:** Gruvbox Archipelago
   - **Category:** Theme / User Interface
   - **Tags:** gruvbox, theme, islands, dark, light, hard, medium, soft
   - **Description:** reuse the README (Marketplace accepts HTML).
   - **Source code:** the GitHub repository URL.
   - **License:** MIT.
4. Upload the screenshots.
5. Submit for review.

## 6. Publish updates

Marketplace updates use the same upload flow. You can also automate it:

```bash
./gradlew publishPlugin \
  -PintellijPlatformPublishing.token="$JETBRAINS_MARKETPLACE_TOKEN"
```

Store `JETBRAINS_MARKETPLACE_TOKEN` as a GitHub Actions secret and add a release
workflow when the listing is live.

## 7. GitHub repository

The repository is live at
<https://github.com/devnamrits/gruvbox-archipelago> and the `origin` remote is
configured. After the Marketplace listing is live, enable Issues and
Discussions, add the Marketplace badge, and point the listing's **Source code**
field at the repository.
