# get directions
def directions():
	sleep(10)
	directions = driver.find_element_by_xpath(
		"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div/button")
	directions.click()

directions()
