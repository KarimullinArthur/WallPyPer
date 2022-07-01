import os 
import random
import sys
home = os.path.expanduser('~')
sys.path.insert(0, home+"/.config")
#sys.path.insert(0, '.config/wallpyper')
from wallpyper import config


PATH = config.path_to_wallpapers
files = os.listdir(PATH) 

def run(command,output=False):
    devNull = ">/dev/null"
    if output == True:
        os.system(command)
    else:
        os.system(command + devNull)

def kill():
    '''
    back4.sh will output artifacts if run more 2 processes
    It function read PID in /tmp/back4.sh.pid, and kill process.
    '''
    with open('/tmp/back4.sh.pid','r') as file:
        for pid in file:
            run(f'kill {pid}')

def setWallPaper():
    media = random.choices(files)[0]

    if media[-4:] != '.gif':
        run(f"feh --bg-scale {PATH}{media}")
    else:
        run(f"back4.sh auto {PATH}{media} & echo $! > /tmp/back4.sh.pid",True)
        # > tmp/back4.sh.pid write PID for kill()
