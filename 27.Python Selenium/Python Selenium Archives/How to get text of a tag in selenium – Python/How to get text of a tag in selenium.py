# Import Library
from selenium import webdriver

# Chrome Path
driver = webdriver.Chrome()

# Web URL
driver.get('https://phptravels.com/demo/')

element = driver.find_element_by_tag_name('a')

# Get Text
print(element.text)

# Close the window
driver.close()
