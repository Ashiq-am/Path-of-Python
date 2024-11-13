# Python program to implement Locating by CSS Selector
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Replace this with your actual url
url = "https://www.geeksforgeeks.org/about/contact-us/"
driver.get(url)

try:

    # Replace this with the css selector of the element
    element = driver.find_element(By.CSS_SELECTOR, "div.title")
except NoSuchElementException:
    print("Not Found")
else:
    print("Found")
