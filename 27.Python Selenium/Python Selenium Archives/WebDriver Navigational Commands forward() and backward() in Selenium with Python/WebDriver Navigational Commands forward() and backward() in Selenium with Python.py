# importing the modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# using chrome driver
driver = webdriver.Chrome()

# taking first url
driver.get("https://www.geeksforgeeks.org/")
# getting title
print(driver.title)

# taking 2nd url
driver.get("https://www.youtube.com/")
# getting the title
print(driver.title)

# given time open url
time.sleep(2)

# WebDriver Navigational Commands backward
driver.back()
# given time open url
time.sleep(2)
# if back then given previous title
print(driver.title)

# WebDriver Navigational Commands backward
driver.forward()
# given time open url
time.sleep(2)
# if goto forward then given next title
print(driver.title)

driver.close()
