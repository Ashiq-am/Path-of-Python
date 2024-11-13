def reset_app():
		# get the global variable timer and set it to None again.
	global timer, user_text

	# delete the text typed in typing area, using delete method.
	# 1.0 is the starting index, i.e., the first character and end means
	# delete all character till last character.
	typing_area.delete('1.0', 'end')
	user_text = ""
	timer = None
	return
