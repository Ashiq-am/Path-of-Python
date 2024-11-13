# return all handles value of open browser window
handles = driver.window_handles

for i in handles:
	driver.switch_to.window(i)

	# close specified web page
	if driver.title == "Frames & windows":
		time.sleep(2)
		driver.close()
