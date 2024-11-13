# on_press method takes
# key as argument


def on_press(key):

# start_stop_key will stop clicking
# if running flag is set to true
	if key == start_stop_key:
		if click_thread.running:
			click_thread.stop_clicking()
		else:
			click_thread.start_clicking()

	# here exit method is called and when
	# key is pressed it terminates auto clicker
	elif key == stop_key:
		click_thread.exit()
		listener.stop()


with Listener(on_press=on_press) as listener:
	listener.join()
