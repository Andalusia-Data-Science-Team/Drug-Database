import time
import pyautogui

def code():
    x, y = pyautogui.position()
    pyautogui.moveTo(x + 5, y + 5)
    time.sleep(5)
    pyautogui.moveTo(x, y)
    time.sleep(50)
while (1):
    try:
        code()
    except:
        code()