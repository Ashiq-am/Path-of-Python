# Python Program to find element by text

#import webdriver
from selenium import webdriver

#import time
from time import sleep

# create webdriver object
driver = webdriver.Chrome(
	executable_path="C:\selenium\chromedriver_win32\chromedriver.exe")

# get the website
driver.get("http://bit.ly/vinayakgfg")

# sleep for some time
sleep(3)

# get element through text
driver.find_element_by_xpath("// a[contains(text(),'5 CHEAP HOLIDAY')]").click()

# sleep for some time
sleep(4)
