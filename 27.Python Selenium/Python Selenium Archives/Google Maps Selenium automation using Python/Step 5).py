# find place
def find():
	sleep(6)
	find = driver.find_element_by_xpath(
		"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
	find.send_keys("Tirunelveli")
	sleep(2)
	search = driver.find_element_by_xpath(
		"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
	search.click()

find()
