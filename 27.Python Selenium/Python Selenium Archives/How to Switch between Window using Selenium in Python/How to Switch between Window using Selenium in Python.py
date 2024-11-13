# import selenium module
from selenium import webdriver

# import select class
from selenium.webdriver.support.ui import Select

# using chrome driver
driver = webdriver.Chrome()

# web page url and open first window page
driver.get("http://demo.automationtesting.in/Windows.html")

# find xpath of button for child window page
# this page no. 2
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

# return all handles value of open browser window
handles = driver.window_handles
for i in handles:
	driver.switch_to.window(i)

	# print every open window page title
	print(driver.title)
