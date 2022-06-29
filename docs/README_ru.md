# WallPyPer

WallPyPer - это маленькая утилита, которая работает
с помощью [foo-Wallpaper-Feh-Gif ](https://github.com/thomas10-10/foo-Wallpaper-Feh-Gif) и [feh](https://github.com/derf/feh).

WallPyPer умеет работать как с картинками так с гифками!

## Установка

Зависимости 

* [feh](https://github.com/derf/feh)
* [foo-Wallpaper-Feh-Gif ](https://github.com/thomas10-10/foo-Wallpaper-Feh-Gif)

**feh** скорее всего уже есть в вашем списке репозиториев.

Debian/Ubuntu:
```
sudo apt install feh
```
Arch:
```
pacman -S feh
```

**foo-WallPaper-Feh-Gif** это всего лишь Bash скрипт его можно скачать [тут](https://github.com/thomas10-10/foo-Wallpaper-Feh-Gif/blob/master/back4.sh).
```
curl -L https://raw.githubusercontent.com/thomas10-10/foo-Wallpaper-Feh-Gif/master/install.sh | bash
```

После этого скачайте WallPyPer и сделайте main.py исполняемым файлом.
```
git clone https://github.com/KarimullinArthur/WallPyPer.git

cd WallPyPer

chmod +x main.py
```

И после этого создайте ссылку в одном из каталогов перменной PATH.
например
```
cd /usr/local/bin/

ln -s <абсолютный_путь_к_скачанному_репозиторию>/main.py wallpyper
```

Абсолютный путь можно получить командной pwd в катологе WallPyPery.

## Автозагрузка

Для **i3wm** добавте в свой ~/.config/i3/config строчку:
```
exec wallpyper
```
