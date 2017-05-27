import datetime
import platform
import subprocess

#home=/usr/local/sadRick/images
HOME = '/usr/local/sadRick/images/'
THUMB = 'thumb%.3d.png'

def get_picture(h, m):
    return THUMB % (((h * 60 + m) / 8 + 37) % 180 + 1)

time = datetime.datetime.now()
picture = THUMB % 100 #get_picture(time.hour, time.minute)
path = HOME + picture

os_name = platform.system()

if os_name == 'Darwin':
    print subprocess.call(['osascript', '-e', '"tell application \\\"Finder\\\" to set desktop picture to POSIX file \\\"%s\\\""' % path])

"""
if [ "$(uname)" == "Darwin" ]; then
	osascript -e
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  export DISPLAY=:0
  case $DESKTOP_SESSION in
  gnome )
      gsettings set org.gnome.desktop.background picture-uri "file://$home/thumb$(printf "%03d" $(( 10#$picture )) ).png"
      ;;
  * )
      feh --bg-scale "$home/thumb$(printf "%03d" $(( 10#$picture )) ).png"
      ;;
  esac
fi
"""
