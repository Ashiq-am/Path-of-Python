''''''



"""
# Multiple_Slider.kv file of the main.py file. 

#.kv file to manipulate the window colour. 
<MultipleSliderWidget>: 
	
	# giving the orientation of Slider 
	orientation: "vertical"

	# initially providing this colour to window 
	slider_colors: 0.5, 0.5, 0.5

	# executed before the canvas group. 
	canvas.before: 
		Color: 
			rgb: root.slider_colors 
		Rectangle: 
			pos: root.pos 
			size: root.size 
			
	# creating the Slider 
	Slider: 
		min: 0 # minimum value of Slider 
		max: 1 # maximum value of Slider 
		value: 0.5 # initial value of Slider 
		
		# when slider moves then to increase value 
		on_value: root.slider_colors[0] = self.value; 

	Slider: 
		min: 0
		max: 1
		value: 0.5
		on_value: root.slider_colors[1] = self.value 

	Slider: 
		min: 0
		max: 1
		value: 0.5
		on_value: root.slider_colors[2] = self.value 

	# Adding The label 
	Label: 
		font_size: "30sp"
		# the for loop is for continuously changing 
		# the clour as slider value changes 
		text: "Color:" + ", ".join(["%.3f" %(i) for i in root.slider_colors]) 
		color: 0, 0, 1, 1

"""