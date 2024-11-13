from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

# Set up Chrome options
chrome_options = Options()

# Path to your ChromeDriver
chrome_driver_path = 'chromedriverPath'

# Initialize ChromeDriver with the specified options
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Go to the Chrome Web Store URL of the desired extension
extension_url = 'https://chromewebstore.google.com/detail/todoist-for-chrome/jldhpllghnbhlbpcmnajkpdmadaolakh'
driver.get(extension_url)
driver.maximize_window();

# Wait for the page to load
time.sleep(5)  # Adjust time as needed

actions = ActionChains(driver)
try:
    # Find the "Add to Chrome" button
    add_to_chrome_button = driver.find_element(By.XPATH, '//button[span[contains(text(),"Add to Chrome")]]')

    # Click the "Add to Chrome" button
    add_to_chrome_button.click()

    time.sleep(8)
    pyautogui.press('tab', presses=1)
    time.sleep(1)

    # Use PyAutoGUI to press Enter to confirm "Add to Extension"
    pyautogui.press('enter')

    # Wait for the "Add Extension" confirmation dialog
    time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

# Wait to observe the added extension
time.sleep(5)

# Close the browser
driver.quit()
