# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_link_text("Courses")

# get id of element
id = element._id

# create another element
element_clone = driver.create_web_element(id)
