''''''



"""<Tester>: 
	orientation: "vertical"
	spacing: 50
	space_x: self.size[0]/3
	canvas.before: 
		Color: 
			rgba: (0, 0, 0, 0) 
		Rectangle: 
			size: self.size 
			pos: self.pos 

	FloatLayout: 
		orientation:'vertical'
		padding:100
		spacing:30
		Button: 
			size_hint:0.6, 0.1
			pos_hint :{'center_x':0.5, 'center_y':0.3} 
			text:'PLAY'
			bold:True
			background_color: (1, .36, .4, .55) 
			on_release: root.play_sound() """
