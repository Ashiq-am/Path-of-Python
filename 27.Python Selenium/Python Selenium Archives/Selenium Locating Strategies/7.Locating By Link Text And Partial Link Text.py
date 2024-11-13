# Python program to implement Locating
# using Link Texts and Partial Link Texts
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Replace this with your url
url = "https://www.example.com"
driver.get(url)

# Replace Learn more with the Link Text of the element
element1 = driver.find_element(By.LINK_TEXT,
							"Learn more");

# Replace Click with the Link Text of the element
element2 = driver.find_element(By.PARTIAL_LINK_TEXT,
							"Click");
