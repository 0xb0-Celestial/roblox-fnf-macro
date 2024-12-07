from keyboard import press,release
from time import sleep
from pyautogui import pixel
from win32gui import GetForegroundWindow, SetWindowPos
from win32con import HWND_TOPMOST
from multiprocessing import Process
from os import system

y = 190

def window_settings():
    hwnd = GetForegroundWindow()
    SetWindowPos(hwnd,HWND_TOPMOST,100,100,475,300,0)
def LeftArrow():
    system('cls')
    print("important! add these arrow binds: \nLeft-F\nUp-G\nDown-K\nRight-L")
    while True:
        if pixel(735,y)[1] == 75:
            press("f")
            if pixel(735,y+51)[1] != 75:
                release("f")
def DownArrow():
    print("observing pixels...")
    while True:
        if pixel(885,y)[1] == 255:
            press("g")
            if pixel(885,y+51)[1] != 255:
                release("g")
def UpArrow():
    while True:
        if pixel(1034,y)[1] == 250:
            press("k")
            if pixel(1034,y+51)[1] != 250:
                release("k")
def RightArrow():
    while True:
        if pixel(1180,y)[1] == 57:
            press("l")
            if pixel(1180,y+51)[1] != 57:
                release("l")
def parallel(*fns):
    if __name__ == "__main__":
        proc = []
        for fn in fns:
            p = Process(target=fn)
            print("tasks ready!")
            p.start()
            proc.append(p)
        for p in proc:
            p.join()

parallel(LeftArrow,DownArrow,UpArrow,RightArrow)
window_settings()
