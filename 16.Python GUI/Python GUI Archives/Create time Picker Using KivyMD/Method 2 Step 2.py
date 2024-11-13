# writing kv lang
KV = '''
# declaring layout
MDFloatLayout:

	# creating a button
	MDFillRoundFlatButton:
		text: "Set Time"
		pos_hint: {'center_x': .5, 'center_y': .5}

		# creating button event
		# this will trigger time_picker
		on_release: app.show_time_picker()
'''
