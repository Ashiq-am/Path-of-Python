from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# Set the path to the ChromeDriver executable
chrome_driver_path = "V:\\VISHESH AGRAWAL\\Software\\chromedriver.exe"

# Set the path to the directory containing your unpacked extension
extension_path = "V:\\VISHESH AGRAWAL\\Chrome Extension\\Word Counter"

# Configure ChromeOptions to load the extension
chrome_options = Options()
chrome_options.add_argument("load-extension=" + extension_path)


# Initialize WebDriver with the configured ChromeOptions
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Maximize the browser window
driver.maximize_window()

# Add implicit wait
driver.implicitly_wait(10)

# Navigate to a page where you want to test the word counter
driver.get("https://www.example.com")
time.sleep(15)

# Close the browser (optional, can be removed if you don't want to close immediately)
driver.quit()
