from keyboard import press,release
from time import sleep
from pyautogui import pixel
from win32gui import GetForegroundWindow, SetWindowPos
from win32con import HWND_TOPMOST
from multiprocessing import Process

y = 190

def LeftArrow():
    while True:
        if pixel(735,y)[1] == 75:
            press("f")
            if pixel(735,y+51)[1] != 75:
                release("f")
def DownArrow():
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

if __name__ == "__main__":
    hwnd = GetForegroundWindow()
    SetWindowPos(hwnd,HWND_TOPMOST,100,100,475,300,0)
    print("important! add these arrow binds: \nLeft-F\nUp-G\nDown-K\nRight-L")
    print("observing pixels...")
    p1 = Process(target=LeftArrow)
    p1.start()
    print("task 1 ready!")
    p2 = Process(target=UpArrow)
    p2.start()
    print("task 2 ready!")
    p3 = Process(target=DownArrow)
    p3.start()
    print("task 3 ready!")
    p4 = Process(target=RightArrow)
    p4.start()
    print("task 4 ready!")
    p1.join()
    p2.join()
    p3.join()
    p4.join() 
