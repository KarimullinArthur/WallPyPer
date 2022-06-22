import os 
import random

from apscheduler.schedulers.background import BlockingScheduler   

PATH = '/home/arthur/img/Wallpapers/test/'# path to media
files = os.listdir(PATH) 

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
    media = random.choices(files)[0]

    if media[-4:] != '.gif':
        run(f"feh --bg-scale {PATH}{media}")
    else:
        run(f"back4.sh auto {PATH}{media} & echo $! > /tmp/wallpyper",True)
