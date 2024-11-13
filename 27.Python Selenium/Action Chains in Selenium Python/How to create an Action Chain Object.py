# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Firefox()

# create action chain object
action = ActionChains(driver)

