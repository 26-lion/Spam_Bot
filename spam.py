import pyautogui
import time
time.sleep(10)
t = "Spam"
for _ in range(100):
    pyautogui.typewrite(t)
    pyautogui.press("enter")
