import pyautogui
import time

# Delay before starting automation
time.sleep(2)

#Open Edge browser
pyautogui.press('win')
pyautogui.typewrite('Edge')
pyautogui.press('enter')

time.sleep(2)

#Open your Socia media
pyautogui.typewrite('www.quora.com')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
#Calculate the Hide button position using trial and error
Hide_button_position = (1125,345)
pyautogui.moveTo(*Hide_button_position )

time.sleep(2)
pyautogui.click()
