""""""


"""
#.kv file implementation of RelativeLayout 

<RelativeLayout>: 

	# creating the Disabled button 
	Button: 
		
		text:"B1"

		background_color: 0.1, 0.5, 0.6, 1
	
		# positioned at 0 % in x axis and 0 % in y axis 
		# from botton left, i.e x, y = 0, 0 from bottom left: 
		pos_hint: {"x":0.2, "y":.4} 
		size_hint: 0.3, 0.2

		# Disabling button 
		disabled: True

		# working button 
	Button: 
		text:"B2"
		background_color: 1, 0, 0, 1
		pos_hint: {"x":.6, "y":.4} 
		size_hint: 0.3, 0.2

					

"""