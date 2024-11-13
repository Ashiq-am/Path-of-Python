# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# write script
script = "alert('Alert via selenium')"

# generate a alert via javascript
driver.execute_script(script)
