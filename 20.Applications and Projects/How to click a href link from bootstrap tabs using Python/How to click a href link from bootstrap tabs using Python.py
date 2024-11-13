# Import the webdriver from selenium library
from selenium import webdriver

# Link the driver of the browser
driver = webdriver.Chrome("C://Myspace/chromedriver.exe")

# Open the website using url
driver.get("https://avanishcodes.github.io/CompCode")

# Target the element using the href value
# In actual, search for an anchor tag and
# among anchor tags, select the one with
# given href value
target = driver.find_element_by_xpath('//a[@href="ref.html"]')

# Click the target to naviagate to destination
target.click()


# This Code has been contributed by Avanish Gupta
