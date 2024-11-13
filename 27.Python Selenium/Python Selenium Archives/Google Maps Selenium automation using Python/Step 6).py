# get transportation details
def kilometers():
	sleep(5)
	Totalkilometers = driver.find_element_by_xpath(
		"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div")
	print("Total Kilometers:", Totalkilometers.text)
	sleep(5)
	Bus = driver.find_element_by_xpath(
		"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
	print("Bus Travel:", Bus.text)
	sleep(7)
	Train = driver.find_element_by_xpath(
		"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[1]/div")
	print("Train Travel:", Train.text)
	sleep(7)

kilometers()
