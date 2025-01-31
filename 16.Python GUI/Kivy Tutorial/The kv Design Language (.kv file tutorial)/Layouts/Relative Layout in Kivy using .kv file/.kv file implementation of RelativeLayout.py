''''''

"""
#.kv file implementation of RelativeLayout 

# creating button feature 
<Button>: 
		# size of text on button 
		font_size: 20
			
		# creating button 
		# a button 20 % of the width and 20 % 
		# of the height of the layout 
		size_hint: 0.2, 0.2

<RelativeLayout>: 

		# The Canvas is the root object 
		# used for drawing by a Widget. 

		canvas: 
				Color: 
						rgb:0, 1, 1
				Rectangle: 
						# creating rectangle 
						# pos = 20 % and size = 60 % of the layout 
						pos:[0.2 * coord for coord in self.size] 
						size:[0.6 * coord for coord in self.size] 


		# creating the button 

		Button: 
			
				text:"B1"

				background_color: 0.1, 0.5, 0.6, 1
			
				# positioned at 0 % in x axis and 0 % in y axis 
				# from botton left, i.e x, y = 0, 0 from bottom left: 
				pos_hint: {"x":0, "y":0} 

		Button: 
				text:"B2"
				background_color: 1, 0, 0, 1
				pos_hint: {"right":1, "y":0} 

					
		Button: 
				text:"Yash"
				background_color: 0.4, 0.5, 0.6, 1
				pos_hint: {"center_x":.5, "center_y":.5} 

		Button: 
				text:"B3"
				background_color: 0, 0, 1, 1
				pos_hint: {"x":0, "top":1} 

		Button: 
				text:"B4"
				background_color: 0.8, 0.9, 0.2, 1
				pos_hint: {"right":1, "top":1} 

"""