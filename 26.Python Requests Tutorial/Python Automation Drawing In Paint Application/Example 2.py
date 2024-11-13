# importing pyautogui module
import pyautogui
# importing time module
import time
# Make a delay of 2 sec
time.sleep(2)
pyautogui.click()
l = 200 # initialising variable l
a = 4 # initialising variable a

pyautogui.dragRel(200, 0, 0.1)
a -= 1
pyautogui.dragRel(0, 200, 0.1)
a -= 1
pyautogui.dragRel(-200, 0, 0.1)
a -= 1
pyautogui.dragRel(0, -200, 0.1)
a -= 1
