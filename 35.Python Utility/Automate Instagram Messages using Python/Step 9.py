for i in user:

	# enter the username
	self.bot.find_element_by_xpath(
		'/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
	time.sleep(2)

	# click on the username
	self.bot.find_element_by_xpath(
		'/html/body/div[4]/div/div/div[2]/div[2]/div').click()
	time.sleep(2)

	# next button
	self.bot.find_element_by_xpath(
		'/html/body/div[4]/div/div/div[1]/div/div[2]/div/button').click()
	time.sleep(2)

	# click on message area
	send = self.bot.find_element_by_xpath(
		'/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

	# types message
	send.send_keys(self.message)
	time.sleep(1)

	# send message
	send.send_keys(Keys.RETURN)
	time.sleep(2)

	# clicks on pencil icon
	self.bot.find_element_by_xpath(
		'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
	time.sleep(2)
	# here will take the next username from the user's list.
