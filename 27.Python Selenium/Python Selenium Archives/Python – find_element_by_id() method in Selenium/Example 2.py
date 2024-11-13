#importing webdriver from selenium
from selenium import webdriver

# Here Chrome will be used
driver=webdriver.Chrome()

# URL of website
url = "https://www.geeksforgeeks.org/"

# Opening the website
driver.get(url)

# finds button using its id
bt = driver.find_element_by_id('scrollTopBtn')
