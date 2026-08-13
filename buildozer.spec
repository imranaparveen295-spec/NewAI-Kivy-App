[app]

title = New AI
package.name = newai
package.domain = org.sahil

source.dir = .
source.main = main.py

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

version = 1.0

android.archs = arm64-v8a, armeabi-v7a
android.api = 35
android.minapi = 21

android.permissions = INTERNET

source.include_exts = py,png,jpg,jpeg,kv,atlas

# Optional:
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
