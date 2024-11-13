# Python program to implement Locating by name
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Replace this with your actual url
url = "https://www.geeksforgeeks.org/about/contact-us/"
driver.get(url)

# Replace ID_NAME with the Id of your element
try:

    # Replace this with the name of the element
    element = driver.find_element(By.NAME, "feedback_area")
except NoSuchElementException:
    print("Not Found")
else:
    print("Found")
