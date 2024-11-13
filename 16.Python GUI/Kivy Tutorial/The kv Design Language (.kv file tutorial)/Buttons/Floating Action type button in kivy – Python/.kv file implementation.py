""""""


"""
#.kv file implementation of Float Button 


# using Float Layout for the creation of Floatbutton 
# Here we are creating the properties of button 
# Button will be created in Main window Box Layout 

<FloatButton@FloatLayout> 
	id: float_root # Giving id to button 
	size_hint: (None, None) 
	text: '' 
	btn_size: (70, 70) 
	size: (70, 70) 
	bg_color: (0.404, 0.227, 0.718, 1.0) 
	pos_hint: {'x': .6} 

	# Adding shape and all, size, position to button 
	Button: 
		text: float_root.text 
		markup: True
		font_size: 40
		size_hint: (None, None) 
		size: float_root.btn_size 
		pos_hint: {'x': 5.5, 'y': 3.8} 
		background_normal: '' 
		background_color: (0, 0, 0, 0) 
		canvas.before: 
			Color: 
				rgba: (0.404, 0.227, 0.718, 1.0) 
			Ellipse: 
				size: self.size 
				pos: self.pos 
		
# Creation of main window 
<MainWindow>: 
	BoxLayout: 
		
		# Creating the Float button 
		FloatButton: 
			text: '+'
			markup: True
			background_color: 1, 0, 1, 0

				

"""