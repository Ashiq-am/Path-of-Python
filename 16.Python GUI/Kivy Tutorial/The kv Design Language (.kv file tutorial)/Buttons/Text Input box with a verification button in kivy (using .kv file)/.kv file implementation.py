''''''


"""
## .kv file implementation of the App class 


# Creating the root widget 
<BtnTextInput>: 

	# To position widgetsin the proper orientation 
	# use of vertical orientation to set all widgets 
	orientation: "vertical"

	# Using the Box layout 
	BoxLayout: 
		height: "50dp"
		size_hint_y: None

		# Creating Test input 
		TextInput: 
			size_hint_x: 20

		# Creating Button 
		Button: 
			text: "Apply"
			size_hint_x: 25
			background_color: 0, 0, 1, 1
			font_size: 35

"""