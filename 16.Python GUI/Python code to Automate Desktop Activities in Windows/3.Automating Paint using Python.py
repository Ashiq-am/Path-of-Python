import pyautogui
import time

time.sleep(2)
pyautogui.press('win')
pyautogui.typewrite('Paint')
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(400, 400, duration=1)
pyautogui.dragTo(400,600, duration=1)
pyautogui.dragTo(600,600, duration=1)
pyautogui.dragTo(600,400, duration=1)
pyautogui.dragTo(400,400, duration=1)
time.sleep(1)
