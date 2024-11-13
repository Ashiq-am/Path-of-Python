# Python program to search automatically
# on wikipedia using selenium

# Import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

# Initialize webdriver object
chromedriver_path = '<Chrome webdriver path>'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

try:
    # Opening wikipedia website
    webdriver.get("https://en.wikipedia.org")

    # Finding the search field by id
    input = webdriver.find_element_by_id("searchInput")

    # Sending input text to search field
    input.send_keys("Python")

    # Pressing enter to search input text
    input.send_keys(Keys.ENTER)
    sleep(10)

finally:

    # Closing the webdriver
    webdriver.close()
