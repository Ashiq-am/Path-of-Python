from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# create instance of Chrome webdriver
driver = webdriver.Chrome()

driver.get("https://auth.geeksforgeeks.org/")

# find the element where we have to
# enter the xpath
# fill user or mail id
driver.find_element_by_xpath('//*[@id ="luser"]').send_keys('praveeny182')

# find the element where we have to
# enter the xpath
# fill password
driver.find_element_by_xpath('//*[@id ="password"]').send_keys('xXXXXX')

# find the element sign in
# request using xpath
# clicking on that element
driver.find_element_by_xpath('//*[@id ="Login"]/button').click()


