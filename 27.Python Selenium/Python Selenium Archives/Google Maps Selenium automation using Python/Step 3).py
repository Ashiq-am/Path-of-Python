# search locations
def searchplace():
	Place = driver.find_element_by_class_name("tactile-searchbox-input")
	Place.send_keys("Tiruchirappalli")
	Submit = driver.find_element_by_xpath(
		"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
	Submit.click()

searchplace()
