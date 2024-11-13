def Glogin(mail_address, password):
	# Login Page
	driver.get(
		'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

	# input Gmail
	driver.find_element_by_id("identifierId").send_keys(mail_address)
	driver.find_element_by_id("identifierNext").click()
	driver.implicitly_wait(10)

	# input Password
	driver.find_element_by_xpath(
		'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
	driver.implicitly_wait(10)
	driver.find_element_by_id("passwordNext").click()
	driver.implicitly_wait(10)

	# go to google home page
	driver.get('https://google.com/')
	driver.implicitly_wait(100)
