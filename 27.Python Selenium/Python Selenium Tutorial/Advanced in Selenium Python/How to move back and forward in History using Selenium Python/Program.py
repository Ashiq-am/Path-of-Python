# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get geeksforgeeks.org
driver.get("https://www.practice.geeksforgeeks.org/")

# one step backward in browser history
driver.back()

# one step backward in browser history
driver.forward()
