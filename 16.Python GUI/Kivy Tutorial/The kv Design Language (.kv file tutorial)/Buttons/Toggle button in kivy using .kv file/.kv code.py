""""""


"""
# .kv file implementation opf the code 

<Toggle_btn>: 

	# Coloums divides screen in two parts 
	cols:2

	# Create Toogle button 1 
	RelativeLayout: 
		canvas: 
			Color: 
				rgb: 0, 0, 1
			Rectangle: 
				size: root.width, root.height 
		ToggleButton: 
			size_hint: None, None
			size: 0.25 * root.width, 0.25 * root.height 
			pos: 0.125 * root.width, 0.350 * root.height 
			text: 'Toggle Button 1'
			group: 'geometry'

# Create Toogle button 2 
	RelativeLayout: 
		canvas: 
			Color: 
				rgb: 0, 1, 1
			Rectangle: 
				size: root.width, root.height 
		ToggleButton: 
			size_hint: None, None
			size: 0.25 * root.width, 0.25 * root.height 
			pos: 0.125 * root.width, 0.350 * root.height 
			text: 'Toggle Button 2'
			group: 'geometry'

"""