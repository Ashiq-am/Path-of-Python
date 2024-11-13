import pyautogui

# moving the cursor left 498 px & down
# 998px from it's cuurent position
pyautogui.moveRel(-498,996, duration = 1)

# clicks at the present location
pyautogui.click()

# moves to the specified location
pyautogui.moveTo(1165,637, duration = 1)

# right clicks at the present cursor
# location
pyautogui.click(button="right")

# moves to the specified location
pyautogui.moveTo(1207,621, duration = 1)

# clicks at the present location
pyautogui.click()
