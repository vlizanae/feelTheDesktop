#!/usr/bin/env python

import datetime
import platform
import subprocess
import os

HOME = '/usr/local/sadRick/images/'
THUMB = 'thumb%.3d.png'

def get_picture(h, m):
    return THUMB % (((h * 60 + m) / 8 + 37) % 180 + 1)

time = datetime.datetime.now()
picture = get_picture(time.hour, time.minute)
path = HOME + picture

os_name = platform.system()

if os_name == 'Darwin':
    subprocess.call(['osascript', '-e', r'tell application "Finder" to set desktop picture to POSIX file "%s"' % path])

elif os_name == 'Linux':
    subprocess.call(['export', 'DISPLAY=:0'])
    dekstop_session = os.environ['DESKTOP_SESSION']

    if dekstop_session == 'gnome':
        subprocess.call(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', 'file://' + path])
    else:
        subprocess.call(['feh', '--bg-scale', path])
