# importing required modules
import pyautogui
import time
# Take a break of 5 sec
time.sleep(5)
pyautogui.click() # using .click() method to click
l = 200
a = 4
x, y = pyautogui.position()

# making a square first

pyautogui.dragRel(200, 0, 0.2)
x1, y1 = pyautogui.position()
a -= 1
pyautogui.dragRel(0, 200, 0.2)
a -= 1
pyautogui.dragRel(-200, 0, 0.2)
a -= 1
pyautogui.dragRel(0, -200, 0.2)
a -= 1

# making a triangle over the square
pyautogui.click(x, y)
pyautogui.dragRel(100, -100, 0.2)
pyautogui.click(x1, y1)
pyautogui.dragRel(-100, -100, 0.2)

# making rest of the body of the hut
pyautogui.dragRel(350, 0, 0.2)
pyautogui.dragRel(0, 300, 0.2)
pyautogui.dragRel(-290, 0, 0.2)
pyautogui.click(x1, y1)
pyautogui.dragRel(250, 0, 0.2)
