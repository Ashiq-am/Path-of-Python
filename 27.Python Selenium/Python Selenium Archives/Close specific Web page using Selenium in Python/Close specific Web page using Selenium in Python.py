# import modules
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# use chrome driver
driver = webdriver.Chrome()

# assign web page url
driver.get("http://demo.automationtesting.in/Windows.html")

# find XPath
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

# return all handles value of open browser window
handles = driver.window_handles

for i in handles:
	driver.switch_to.window(i)

	# close specified web page
	if driver.title == "Frames & windows":
		time.sleep(2)
		driver.close()
