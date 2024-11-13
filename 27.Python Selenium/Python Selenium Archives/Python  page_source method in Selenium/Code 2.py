# importing webdriver from selenium
from selenium import webdriver

# Here Chrome will be used
driver = webdriver.Chrome()

# Getting current URL source code
get_source = driver.page_source

# Printing the URL
print(get_source)
