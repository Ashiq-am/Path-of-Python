''''''


'''

# .kv file implementation of the App 

# Using Grid layout 
GridLayout: 
	
	cols: 4
	rows: 3
	padding: 10

	# Adding label 
	Label: 
		text: "I am a Label"

	# Add Button 
	Button: 
		text: "bouton 1"

	# Add CheckBox 
	CheckBox: 
		active: True

	# Add Image 
	Image: 
		source: 'html.png'

	# Add Slider 
	Slider: 
		min: -100
		max: 100
		value: 25

	# Add progress Bar 
	ProgressBar: 
		min: 50
		max: 100

	# Add TextInput 
	TextInput: 
		text: "Enter the text"

	# Add toggle Button 
	ToggleButton: 
		text: " Poetry Mode "

	# Add Switch 
	Switch: 
		active: True
	





'''