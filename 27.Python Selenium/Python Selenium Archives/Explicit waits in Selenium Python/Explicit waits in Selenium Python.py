# import necessary classes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create driver object
driver = webdriver.Firefox()

# A URL that delays loading
driver.get("http://somedomain / url_that_delays_loading")

try:
	# wait 10 seconds before looking for element
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "myDynamicElement"))
	)
finally:
	# else quit
	driver.quit()
