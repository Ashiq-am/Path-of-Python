""""""


"""
# .kv file implementation of the code 

<textinp>: 
	title: 'InputDialog'
	auto_dismiss: False
	id: test1 

	# Using relative layout to arrange properly 
	RelativeLayout: 
		orientation: 'vertical'
		pos: self.pos 
		size: root.size 
		id: test2 

		# Defining text input in .kv 
		# And giving it the look . pos and features 
		TextInput: 
			id: input
			hint_text:'Enter text'
			pos_hint: {'center_x': 0.5, 'center_y': 0.705} 
			size_hint: 0.95, 0.5
			on_text: app.process() 

"""