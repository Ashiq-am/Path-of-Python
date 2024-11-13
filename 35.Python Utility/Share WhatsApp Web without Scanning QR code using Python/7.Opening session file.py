def sessionOpener(sessionFilePath):

	# 2.1 Verify that session file is exist
	if sessionFilePath == "":
		raise IOError('"' + sessionFilePath + '" is not exist.')

	# 2.2 Read the given file into "session" variable
	with open(sessionFilePath, "r", encoding="utf-8") as sessionFile:
		session = sessionFile.read()

	# 2.3 Open Chrome browser
	browser = webdriver.Chrome()

	# 2.4 Open Web Whatsapp
	browser.get("https://web.whatsapp.com/")

	# 2.5 Wait for Web Whatsapp to be loaded properly
	_wait_for_presence_of_an_element(browser, QR_CODE)

	# 2.6 Execute javascript in browser to inject
	# session by using vaarible "session"
	print("Injecting session...")
	browser.execute_script(INJECT_SESSION, session)

	# 2.7 Refresh the page
	browser.refresh()

	# 2.8 Ask for user to enter any key to close browser
	input("Press enter to close browser.")
