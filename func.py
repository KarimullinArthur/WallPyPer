import os 
import random

PATH = '/home/arthur/img/Wallpapers/media/'# path to media

files = os.listdir(PATH) 

media = random.choices(files)[0]

def run(command,output=False):
    devNull = ">/dev/null"
    if output == True:
        os.system(command)
    else:
        os.system(command + devNull)

def kill():
    with open('/tmp/wallpyper','r') as file:
        for pid in file:
            run(f'kill {pid}')

def setWallPeper():
    if media[-4:] != '.gif':
        run(f"feh --bg-scale {PATH}{media}")
    else:
        run(f"back4.sh auto {PATH}{media} & echo $! > /tmp/wallpyper",True)
