"""
"""


'''
# .kv file of canvas 

<CanvasWidget> 

	# Creating Canvas 
	canvas: 

		# Color is blue if button is pressed, 
		# otherwise color is red 
		Color: 
			rgb: (1, 0, 0, 1) if self.state == 'normal' else (0, 0, 1, 1) 
	
		# Rounded rectangle canvas 
		RoundedRectangle: 
			size: self.size 
			pos: self.pos 
			
			# Play with these if you want smooth corners for your button 
			radius: 100, 100, 100, 100
		

	# Print the text when touched or button pressed	 
	on_release: 
		print("I have been clicked") 

'''