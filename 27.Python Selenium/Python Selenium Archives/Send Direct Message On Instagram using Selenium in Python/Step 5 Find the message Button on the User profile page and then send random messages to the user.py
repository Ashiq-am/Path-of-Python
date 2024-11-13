def send_message():

	# Find message button
	message = chrome.find_element_by_class_name('_862NM ')
	message.click()
	time.sleep(2)
	chrome.find_element_by_class_name('HoLwm ').click()
	time.sleep(1)
	l = ['hello', 'Hi', 'How are You', 'Hey', 'Bro whats up']
	for x in range(10):
		mbox = chrome.find_element_by_tag_name('textarea')
		mbox.send_keys(random.choice(l))
		mbox.send_keys(Keys.RETURN)
		time.sleep(1.2)
