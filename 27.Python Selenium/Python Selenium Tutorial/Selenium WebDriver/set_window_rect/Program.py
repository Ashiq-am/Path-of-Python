# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")


# set window position
driver.set_window_rect(x = 100, y = 200, width = 1024, height = 700)
