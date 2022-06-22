#!/usr/bin/python3

from func import *

def start():
    try:
        kill()
    except FileNotFoundError:
        setWallPeper()
        
    setWallPeper()

if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_job(start,'interval',minutes=1)
    sched.start()    
