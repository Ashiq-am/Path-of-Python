import pyautogui

# To Move the mouse to specific coordinates
pyautogui.moveTo(200, 200, duration=2) # Move the mouse to (200, 200)

# To Click the mouse at current position
pyautogui.click()

# To Double-click the mouse at specific position
pyautogui.doubleClick(400, 400)

# To Drag the mouse from one position to another
# Drag the mouse to (600, 600) over 1 second
pyautogui.dragTo(600, 600, duration=1)

# To Scroll the mouse up and down
pyautogui.scroll(20) # Scroll up by 20 units
pyautogui.scroll(-20) # Scroll down by 20 units

# Get the current mouse position
x, y = pyautogui.position()
print(f"Current mouse position: ({x}, {y})")
