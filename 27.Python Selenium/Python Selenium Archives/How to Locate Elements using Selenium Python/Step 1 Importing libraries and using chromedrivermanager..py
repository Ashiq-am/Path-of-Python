import selenium
import time
import webdriver_manager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# To make it work on older versions
# of chrome we will use ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.google.com')
