''''''

"""
#.kv file implementation of FloatLayout 

# creating button feature 
<Button>: 
	font_size: 40
	
	# creating button 
	# a button 30 % of the width and 50 % 
	# of the height of the layout 
	size_hint: 0.3, 0.3

<FloatLayout>: 
	
	Button: 
		text: "Helooo !!!!! "
		background_color: 0.1, 0.5, 0.6, 1

		# positioned at 0 % right and 100 % up / top 
		# from botton left, i.e x, top = 0, 100 from bottom left: 
		pos_hint: {"x":0, "top":1} 

	Button: 
		text:"Rajnish:)"
		background_color: 1, 0, 0, 1
		pos_hint: {"x":0.35, "y":0.3} 

		
	Button: 
		text:"Ravi:)"
		background_color: 0.4, 0.5, 0.6, 1
		pos_hint: {"x":.7, "bottom":0} 

	Button: 
		text:"Sanjeev:)"
		background_color: 0, 0, 1, 1
		pos_hint: {"x":.7, "top":1} 

	Button: 
		text:"Suraj:)"
		background_color: 0.8, 0.9, 0.2, 1
		pos_hint: {"x":0, "bottom":1} 

"""