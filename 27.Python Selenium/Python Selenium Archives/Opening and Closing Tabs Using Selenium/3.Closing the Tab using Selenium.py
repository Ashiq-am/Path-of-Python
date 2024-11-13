# Import module
from selenium import webdriver

# Create object
driver = webdriver.Chrome()

# Fetching the Url
url = "https://www.geeksforgeeks.org/"

# Opening first url
driver.get(url)

# Closing the tab
driver.close()
