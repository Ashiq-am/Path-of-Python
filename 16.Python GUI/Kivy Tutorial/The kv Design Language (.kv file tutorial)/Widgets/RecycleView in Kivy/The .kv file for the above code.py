""""""


'''
<ExampleViewer>: 
	viewclass: 'Button' # defines the viewtype for the data items. 
	orientation: "vertical"
	spacing: 40
	padding:10, 10
	space_x: self.size[0]/3

	RecycleBoxLayout: 
		color:(0, 0.7, 0.4, 0.8) 
		default_size: None, dp(56) 

		# defines the size of the widget in reference to width and height 
		default_size_hint: 0.4, None
		size_hint_y: None
		height: self.minimum_height 
		orientation: 'vertical' # defines the orientation of data items 


'''