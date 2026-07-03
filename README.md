# Talky — Downloads

Talky is a fully offline AI dictation app for Windows: hold a hotkey, talk, and
the words land at your cursor. Whisper runs on **your** machine — no audio or
text ever leaves it. This repo hosts the downloadable builds only; the source
code is private.

## Get it

Grab the newest version from **[Releases](https://github.com/ihdiot/talky-releases/releases)**:

| File | Pick it when… |
|------|---------------|
| `talky-hideable.exe` | **Most people want this one.** Runs from the tray, console hidden. |
| `talky.exe` | Same app with a visible console (handy for troubleshooting). |
| `Talky-Portable-*-win64.zip` | No-install edition: unzip and run `Talky.exe` from the folder — works offline from first launch, even on locked-down machines. |

## First run

1. Windows SmartScreen will warn about an unknown publisher (the build isn't
   code-signed yet). Click **More info → Run anyway**.
2. First launch downloads the speech model (skip this wait with the Portable
   zip — its model is already inside).
3. Hold the hotkey, talk, release — the text types itself. Right-click the
   tray icon for settings.

## Verify your download (optional)

Each file ships with a `.sha256` checksum. In PowerShell:

```powershell
Get-FileHash .\talky-hideable.exe -Algorithm SHA256
```

The output should match the contents of the matching `.sha256` file.
