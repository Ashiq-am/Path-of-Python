# Import required module
import time
from selenium import webdriver

# Import Select class
from selenium.webdriver.support.ui import Select



# Using chrome driver
driver = webdriver.Chrome()

# Web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")



# Find id of option
x = driver.find_element_by_id('RESULT_RadioButton-9')
drop = Select(x)

# Select by value
drop.select_by_value("Radio-0")
time.sleep(4)
driver.close()
