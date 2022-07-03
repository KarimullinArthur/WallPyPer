# WallPyper

WallPyPer - is small utility, work via 
[foo-Wallpaper-Feh-Gif ](https://github.com/thomas10-10/foo-Wallpaper-Feh-Gif) and [feh](https://github.com/derf/feh).

<img src="./docs/media/demo.gif"  />

WallPyPer can work with images and gifs.

## Install

Dependencies:

* [feh](https://github.com/derf/feh)                                
* [foo-Wallpaper-Feh-Gif ](https://github.com/thomas10-10/foo-Wallpaper-Feh-Gif)  
* [apscheduler](https://github.com/agronholm/apscheduler)

**feh** is most likely already in tour list of repositories.

Debiadn/Ubuntu:
```
sudo apt install feh
```
Arch:
```
pacman -S feh
```



**foo-Wallpaper-feh-gif** is just bash script, you can download it [here](https://github.com/thomas10-10/foo-Wallpaper-Feh-Gif/blob/master/back4.sh)
```
curl -L https://raw.githubusercontent.com/thomas10-10/foo-Wallpaper-Feh-Gif/master/install.sh | bash 
```



Install apscheduler
```
pip install apscheduler
```



Then download WallPyPer and make main.py an run file.
```
git clone https://github.com/KarimullinArthur/WallPyPer.git

cd WallPyPer

chmod +x main.py
```

And after create symbolic a link in one of the PATH var.
For example
```
cd /usr/local/bin/

ln -s <abs_path_to_download_repo>/main.py wallpyper
```

The absolute path you cat get via command *pwd*

## Configuration

Create conifg in *~/.config/wallpyper/config*
and put this:
```
{
         "path_to_wallpapers":"your_path",
         "second":"*",
         "minute":"*/1",
         "hour":"*"
}
``` 

Where *path_to_wallpapers* is *absolute* path to wallpapers.
*second*, *minute* and *hour* set auto change via cron.


[More infarmation about cron](https://en.wikipedia.org/wiki/Cron)

[crontab.guru](https://crontab.guru)

## Auto Start

For **i3wm** add in your ~/.conifg/i3/config one string:
```
exec wallpyper
```

Author - Karimullin Arthur
		 Mail - KarimullinArthur@riseup.net
