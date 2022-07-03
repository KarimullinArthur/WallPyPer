#!/usr/bin/python3

from apscheduler.schedulers.background import BlockingScheduler 
from func import *

def start():
    try:
        kill()
    except FileNotFoundError:
        setWallPaper()
        
    setWallPaper()

if __name__ == '__main__':
    start()

    sched = BlockingScheduler()

    sched.add_job(start,'cron',\
        second=configParsing()['second'],\
        minute=configParsing()['minute'],\
        hour=configParsing()['hour'])

    sched.start()
