""""""


'''
# .kv file of the main.py code 
# Adding Button widget 

<Button_Widget>: 

	# defining Button size 
	size: 100, 100

	# creating Canvas 
	canvas.before: 
		Color: 
			rgba: 0.72, 0.62, 0.92, 1
		Rectangle: 
			pos: self.pos 
			size: self.size 

'''