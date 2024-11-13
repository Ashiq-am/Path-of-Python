# import modules
from selenium import webdriver
import time

# assign path and driver
PATH = "C:/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# assign URL
driver.get("https://login.yahoo.com/")
print("First window title = " + driver.title)

# switch to new window
driver.find_element_by_class_name("privacy").click()
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
print("Second window title = " + driver.title)

# switch to new window
driver.execute_script("window.open()")
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.geeksforgeeks.org/")
print(driver.title)
