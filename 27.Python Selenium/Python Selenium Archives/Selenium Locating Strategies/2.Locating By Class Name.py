# Python program to implement Locating by Class Name
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Replace this with your actual url
url = "https://www.geeksforgeeks.org/data-structures/?ref=shm"
driver.get(url)

# Replace ID_NAME with the Id of your element
try:

    # Replace this with the id of the element
    element = driver.find_element(By.CLASS_NAME, "entry-title")
except NoSuchElementException:
    print("Not Found")
else:
    print("Found")
