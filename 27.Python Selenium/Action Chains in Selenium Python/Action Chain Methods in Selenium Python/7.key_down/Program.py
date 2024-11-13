# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# import KEYS
from selenium.webdriver.common.keys import Keys

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# create action chain object
action = ActionChains(driver)

# perform the oepration
action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()
