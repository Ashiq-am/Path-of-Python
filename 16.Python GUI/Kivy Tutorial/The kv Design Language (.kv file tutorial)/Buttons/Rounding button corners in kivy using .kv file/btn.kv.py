"""

"""



"""
#.kv file implementation of rounding the corners of button 


# create a fully styled functional button 
# Adding images normal.png and down.png 
<Base>: 
	Button: 
		text: 'Hit me !!'

		# Button prpoerties for image 
		background_normal: 'normal.png'
		background_down: 'down.png'

		# To round the corners we use border 
		border: 30, 30, 30, 30

		# Adding background color to button you can comment it 
		background_color: 0.1, 0.5, 0.6, 1
		
		size_hint: .3, .3
		pos_hint: {"x":0.35, "y":0.3} 

"""