''''''


"""
# Creating the main .kv files 
# the difference is that it is 
# the heart of the Application 
# Other are just Organs 

<main_kv>: 

	# Assigning Grids 
	cols: 3

	# Creating AnchorLayout 
	AnchorLayout: 
		anchor_x: 'left'
		anchor_y: 'center'

		# Canvas creation 
		canvas: 
			Color: 
				rgb: [1, 0, 0] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		
		Box1: 
			size_hint: [None, None] 
			size: [app.x, app.y] 

	AnchorLayout: 
		anchor_x: 'center'
		anchor_y: 'center'
		canvas: 
			Color: 
				rgb: [0, 1, 0] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		Box2: 
			size_hint: [None, None] 
			size: [app.x, app.y] 

	AnchorLayout: 
		anchor_x: 'right'
		anchor_y: 'center'
		canvas: 
			Color: 
				rgb: [0, 0, 1] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		Box3: 
			size_hint: [None, None] 
			size: [app.x, app.y] 

"""