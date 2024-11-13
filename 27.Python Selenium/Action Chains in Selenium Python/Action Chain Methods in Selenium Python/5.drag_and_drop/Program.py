# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get source element
source_element = driver.find_element_by_link_text("Courses")

# get target element
target_element = driver.find_element_by_link_text("Hard")

# create action chain object
action = ActionChains(driver)

# drag and drop the item
action.drag_and_drop(source_element, target_element)

# perform the operation
action.perform()
