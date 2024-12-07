from keyboard import press_and_release
from pyautogui import pixel
from win32gui import GetForegroundWindow, SetWindowPos
from win32con import HWND_TOPMOST

y = 200
hwnd = GetForegroundWindow()
SetWindowPos(hwnd,HWND_TOPMOST,100,100,475,300,0)

print("important! add these arrow binds: \nLeft-F\nUp-G\nDown-K\nRight-L")
print("btw it can't hold hold notes \n so play maps with the least hold notes")
print("observing pixels...")
while True:
    if pixel(730,y)[0] == 194:
        press_and_release("f")
        print("pressed LeftArrow")
    if pixel(880,y)[0] == 0:
        press_and_release("g")
        print("pressed UpArrow")
    if pixel(1030,y)[0] == 18:
        press_and_release("k")
        print("pressed DownArrow")
    if pixel(1200,y)[0] == 249:
        press_and_release("l")
        print("pressed RightArrow")
