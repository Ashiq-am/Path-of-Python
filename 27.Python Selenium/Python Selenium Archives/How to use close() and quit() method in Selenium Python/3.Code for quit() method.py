# importing webdriver from selenium
from selenium import webdriver

# Here Chrome will be used
driver = webdriver.Chrome()

# URL of website
url = "https://www.geeksforgeeks.org/"

# Opening the website
driver.get(url)

# All windows related to driver instance will quit
driver.quit()
