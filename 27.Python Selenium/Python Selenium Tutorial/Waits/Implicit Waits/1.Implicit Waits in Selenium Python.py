# import webdriver
from selenium import webdriver

driver = webdriver.Firefox()

# set implicit wait time
driver.implicitly_wait(10) # seconds

# get url
driver.get("http://somedomain / url_that_delays_loading")

# get element after 10 seconds
myDynamicElement = driver.find_element_by_id("myDynamicElement")
