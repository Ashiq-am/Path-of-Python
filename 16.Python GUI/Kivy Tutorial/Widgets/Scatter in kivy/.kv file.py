""""""


'''
# .kv file implementation 

# Create the square to show scatter 
<SquareWidget>: 
	size: 100, 100
	canvas: 
		Color: 
			rgb: [0.345, 0.85, 0.456] 
		Rectangle: 
			size: self.size 
			pos: self.pos 


# Create the scatter properties		 
<Scatter_App>: 
	
	canvas: 
		Color: 
			rgb: .8, .5, .4
		Rectangle: 
			size: self.size 
			pos: self.pos 

	ScatterWidget: 
		id: square_widget_id 
		SquareWidget: 

	# Showing the current position of the box 
	Label: 
		text: 'Position: ' + str(square_widget_id.pos) 
		size_hint: .1, .1
		pos: 500, 300



'''