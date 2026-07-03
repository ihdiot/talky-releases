# Talky — Downloads

Talky is a fully offline AI dictation app for Windows and Apple Silicon Macs:
tap a hotkey, talk, tap it again — the words land at your cursor. Whisper runs
on **your** machine — no audio or text ever leaves it. This repo hosts the
downloadable builds only; the source code is private.

## Get it

Grab the newest version from **[Releases](https://github.com/ihdiot/talky-releases/releases)**:

| File | Pick it when… |
|------|---------------|
| `talky-hideable.exe` | **Most Windows people want this one.** Runs from the tray, console hidden. |
| `talky.exe` | Same app with a visible console (handy for troubleshooting). |
| `Talky-Portable-*-win64.zip` | No-install edition: unzip and run `Talky.exe` from the folder — works offline from first launch, even on locked-down machines. |
| `Talky-Portable-*-macos-arm64.zip` | **The Mac build** (alpha, Apple Silicon only): unzip and double-click `Talky.command` — model included, fully offline. |

## First run

**Windows**

1. SmartScreen will warn about an unknown publisher (the build isn't
   code-signed yet). Click **More info → Run anyway**.
2. First launch downloads the speech model (skip this wait with the Portable
   zip — its model is already inside).
3. Tap the hotkey, talk, tap it again — the text types itself. Right-click the
   tray icon for settings.

**Mac (alpha)**

1. Unzip and double-click `Talky.command`. If Gatekeeper blocks it, right-click
   → Open — or approve it under System Settings → Privacy & Security.
2. Allow microphone access when macOS asks.
3. Tap the hotkey (the welcome banner shows it), talk, tap it again — the text
   types itself. The Terminal window stays open while Talky runs; closing it
   quits Talky.

## Verify your download (optional)

Each file ships with a `.sha256` checksum. In PowerShell:

```powershell
Get-FileHash .\talky-hideable.exe -Algorithm SHA256
```

On a Mac:

```bash
shasum -a 256 -c Talky-Portable-*-macos-arm64.zip.sha256
```

The output should match the contents of the matching `.sha256` file.
