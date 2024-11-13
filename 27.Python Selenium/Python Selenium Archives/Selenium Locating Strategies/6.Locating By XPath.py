# Python program of Locating by XPath
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Replace this with your actual url
url = "https://www.geeksforgeeks.org/about/contact-us/"
driver.get(url)

try:

    # Replace this with the XPATH selector of the element
    element = driver.find_element(By.XPATH,
                                  "/html/body/div[3]/div[2]/div[1]/div/div")
except NoSuchElementException:
    print("Not Found")
else:
    print("Found")
