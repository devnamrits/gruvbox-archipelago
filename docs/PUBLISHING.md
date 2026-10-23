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

The Marketplace listing accepts up to ten screenshots. Use one per theme, with
the default Medium variants first:

- `screenshots/01-archipelago-dark.png` — Islands Dark, Medium default.
- `screenshots/02-archipelago-light.png` — Islands Light, Medium default.
- `screenshots/03-archipelago-dark-hard.png`
- `screenshots/04-archipelago-dark-soft.png`
- `screenshots/05-archipelago-light-hard.png`
- `screenshots/06-archipelago-light-soft.png`
- `screenshots/07-mainland-dark.png`
- `screenshots/08-mainland-light.png`

For a shorter listing, the two Medium defaults plus Dark Soft and Light Soft are
enough; the full set above shows every variant.

For consistent shots:

1. Use a clean IDE profile and a representative project.
2. Set the editor font to **IBM Plex Mono 14** (the font used by the original
   Gruvbox screenshots) or keep the IDE default.
3. Disable **Settings → Editor → Inlay Hints → Code Vision → Author** so the
   VCS author handle is not captured. Hide personal paths, tokens, and
   unrelated notifications too.
4. Select the open source file in the Project tree so the selection highlight is
   visible; do not select a build output folder.
5. Capture the whole IDE window, not just the editor. Avoid the macOS menu bar
   and full-screen letterboxing.
6. Normalize the files before upload:

   ```bash
   python3 scripts/prepare_screenshots.py
   ```

   This writes sRGB PNGs to `screenshots/marketplace/`, removes the black macOS
   strip when present, strips EXIF/XMP metadata, and checks the 1280×800 minimum.
   Upload the files from `screenshots/marketplace/`.

Keep text at a readable size. A retina capture around 2940×1846 is fine; do not
downscale it below 1280×800.

## 4. Sign the plugin (recommended)

Generate a signing key pair once and keep it out of the repository:

```bash
mkdir -p ~/.gruvbox-signing && chmod 700 ~/.gruvbox-signing

openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 \
  -aes-256-cbc -out ~/.gruvbox-signing/private.pem
chmod 600 ~/.gruvbox-signing/private.pem

# Keep the certificate subject neutral: it is embedded in the signed ZIP.
openssl req -new -x509 -key ~/.gruvbox-signing/private.pem \
  -out ~/.gruvbox-signing/cert.pem -days 3650 \
  -subj "/CN=Gruvbox Archipelago/O=devnamrits"
```

Use the standalone Marketplace ZIP Signer CLI, not the obsolete
`-Psigning.*` Gradle properties. Download
`marketplace-zip-signer-cli-0.1.43.jar` from
<https://github.com/JetBrains/marketplace-zip-signer/releases>, then sign the
exact ZIP you intend to upload. Export the key password in the same terminal
first; `read -s` keeps it out of shell history:

```bash
read -s SIGNING_PASSWORD
export SIGNING_PASSWORD

java -jar marketplace-zip-signer-cli-0.1.43.jar sign \
  -in build/distributions/gruvbox-archipelago-0.1.0.zip \
  -out build/distributions/gruvbox-archipelago-0.1.0-signed.zip \
  -cert-file ~/.gruvbox-signing/cert.pem \
  -key-file ~/.gruvbox-signing/private.pem \
  -key-pass "$SIGNING_PASSWORD"
```

If the signer reports `password empty`, the variable was not exported. If it
reports `1.2.840.113549.1.5.13 not available`, re-encrypt the key with the
signer-compatible PBE scheme:

```bash
openssl pkcs8 -topk8 -in ~/.gruvbox-signing/private.pem \
  -out ~/.gruvbox-signing/private-3des.pem -v1 PBE-SHA1-3DES
```

and use `-key-file ~/.gruvbox-signing/private-3des.pem`.

Upload the `-signed.zip`; do not upload the unsigned ZIP or re-zip the signed
one. Record the signed ZIP's SHA-256. Keep `private.pem` in a password manager
or CI secret, never in the repository.

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
