""""""

'''
# Implementation of .kv file of Anchor layout 

################################################ 


# creating the features of Button 
<MyButton@Button>: 
	size_hint: [None, None] 
	size: [100, 100] 

# creating the root of .kv 
<Anchor_Layout>: 

	# Assigning grids 
	rows: 3

	# Anchor Layout 1 
	AnchorLayout: 
		
		# position of Anchor Layout 
		anchor_x: 'left'
		anchor_y: 'top'

		# creating Canvas 
		canvas: 
			Color: 
				rgb: [.5, .324, .384] 
			Rectangle: 
				pos: self.pos 
				size: self.size 

		# creating Button 
		MyButton: 
			text: 'B1'

	# Anchor Layout 2 
	AnchorLayout: 
		anchor_x: 'center'
		anchor_y: 'top'
		canvas: 
			Color: 
				rgb: [.5, .692, .498] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		MyButton: 
			text: 'B2'

	# Anchor Layout 3 
	AnchorLayout: 
		anchor_x: 'right'
		anchor_y: 'top'
		canvas: 
			Color: 
				rgb: [.5, .692, 1] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		MyButton: 
			text: 'B3'

	# Anchor Layout 4 
	AnchorLayout: 
		anchor_x: 'left'
		anchor_y: 'center'
		canvas: 
			Color: 
				rgb: [.789, .5, .699] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		MyButton: 
			text: 'B4'

	# Anchor Layout 5 
	AnchorLayout: 
		anchor_x: 'center'
		anchor_y: 'center'
		canvas: 
			Color: 
				rgb: [.333, .5, .673] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		MyButton: 
			text: 'B5'
			
	# Anchor Layout 6 
	AnchorLayout: 
		anchor_x: 'right'
		anchor_y: 'center'
		canvas: 
			Color: 
				rgb: [.180, .5, .310] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		MyButton: 
			text: 'B6'

	# Anchor Layout 7 
	AnchorLayout: 
		anchor_x: 'left'
		anchor_y: 'bottom'
		canvas: 
			Color: 
				rgb: [.180, .398, .5] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		MyButton: 
			text: 'B7'

	# Anchor Layout 8 
	AnchorLayout: 
		anchor_x: 'center'
		anchor_y: 'bottom'
		canvas: 
			Color: 
				rgb: [.438, .329, .5] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		MyButton: 
			text: 'B8'

	# Anchor Layout 9 
	AnchorLayout: 
		anchor_x: 'right'
		anchor_y: 'bottom'
		canvas: 
			Color: 
				rgb: [.611, .021, .5] 
			Rectangle: 
				pos: self.pos 
				size: self.size 
		MyButton: 
			text: 'B9'	

'''