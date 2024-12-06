from keyboard import press_and_release
from pyautogui import pixel
import win32gui
import win32con

y = 200
hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,475,300,0)

print("important! add these arrow binds: \nLeft-F\nUp-G\nDown-K\nRight-L")
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
