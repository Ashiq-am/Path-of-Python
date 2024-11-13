#importing webdriver from selenium
from selenium import webdriver

# Here Chrome will be used
driver=webdriver.Chrome()

# Opening the website
driver.get(url)

# finds button using its id
form = driver.find_element_by_id('geek_id')
