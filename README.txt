# New AI — Kivy Android Project

This project converts the original terminal-based Python program into a Kivy mobile UI.

## What it does

1. Type a prompt into the text box.
2. Tap CREATE IMAGE.
3. The app creates a Pollinations image URL and loads the generated image inside the app.
4. Internet permission is included for Android.

## Project files

- main.py
- buildozer.spec
- README.txt

## Build an APK

On a compatible Linux/WSL Buildozer environment:

    buildozer android debug

The first build can take a while because Android build dependencies must be downloaded.

## Important

The image service is an external online service, so the phone needs internet access.

The app is intended as a small personal/friends test app. It is not published to Google Play by this project.
