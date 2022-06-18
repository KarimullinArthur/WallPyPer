import os 
import random

PATH = '/home/arthur/img/Wallpapers/gif/'# path to media

files = os.listdir(PATH) 

media = random.choices(files)[0]

if media[-4:] != '.gif':
    os.system(f"feh --bg-scale {PATH}{media}")
else:
    os.system(f"back4.sh auto {PATH}{media}")
