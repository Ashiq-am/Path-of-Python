def AskToJoin():
	# Ask to Join meet
	time.sleep(5)
	driver.implicitly_wait(2000)
	driver.find_element_by_css_selector(
		'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
	# Ask to join and join now buttons have same xpaths
