import config
from console.windows import set_title
from time import sleep

config.title_waiting = bool(False)
class Titles:

    def waiting():
        x = 0
        if(x == 0):
            set_title("INTEST | Status: Waiting.")
            x=1
            sleep(1)
        elif(x == 1):
            set_title("INTEST | Status: Waiting..")
            x=2
            sleep(1)
        elif(x == 2):
            set_title("INTEST | Status: Waiting...")
            x=0
            sleep(1)
        if(config.title_waiting == True):
            waiting()

config.title = bool(True)
Titles.waiting()
input(".")