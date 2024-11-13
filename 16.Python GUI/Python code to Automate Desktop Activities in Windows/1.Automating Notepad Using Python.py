import pyautogui
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.typewrite('Notepad')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("The text is written in Notepad using pyautogui.")
