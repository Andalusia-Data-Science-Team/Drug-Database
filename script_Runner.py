import time

import pyautogui

screen_width, screen_height = pyautogui.size()

# Define the target position (x, y)
target_x, target_y = 50, 50
while(1):
    for i in range(5):
        pyautogui.moveTo(target_x, target_y, duration=0.1)
        time.sleep(5)
        target_x, target_y = target_x+1, target_y+1
    target_x, target_y = target_x-5, target_y-5