# Readme

Change your background at the rythm of Rick !

You can run Downloader and you're set to go. It creates a folder in `/usr/local`
and downloads the images required to run the wallpaper. Then it downloads the
script to change the background and installs it in the crontab. 

In case gnome is not your desktop environment, "feh" is needed to display the wallpaper.

You can also download the debug and param scripts. The debug script is for
testing which wallpaper comes out at a certain hour
```
./setbgDEBUG 21 35 # sets the wallpaper that will be on screen at 9:35 pm
```
and the param script to test certain wallpaper
```
./setbgParam 135 # sets the wallpaper named thumb135.png in the images folder
```

The commands used to get the video frames and renaming are listed in the not executable file `commands`, but be careful because those haven't been polished.
