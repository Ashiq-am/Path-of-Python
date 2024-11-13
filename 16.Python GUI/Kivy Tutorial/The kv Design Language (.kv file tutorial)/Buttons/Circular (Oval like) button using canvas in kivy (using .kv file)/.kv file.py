""""""


"""
# .kv file of creating a circular button using canvas 

<CircularButton>: 

	# Creating Circular button 
	canvas: 

		# Color is different if button is pressed 
		Color: 
			rgb: (0, 1, 0, 1) if self.state == 'normal' else (1, 0, 1, 1) 
	
		# Rounded rectangle canvas 
		RoundedRectangle: 

						# Giving the size and the position 
			size: (self.size) 
			pos: (self.pos) 
			
			# This will force the rectangle to be the circle 
			radius: [400, ] 
		

	# Print the text when touched or button pressed	 
	on_release: 
		print("This is the button made up by the canvas") 

"""