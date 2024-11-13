# Python program to demonstrate
# selenium

# import webdriver
import element as element
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox()

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get elements
elements = driver.find_elements_by_xpath("//div[@name ='articlePath']")

# print complete elements list
print(element)
