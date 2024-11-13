""""""



'''
# .kv file 

# Extension of ProgBar class in .kv file 
<ProgBar>: 

	orientation: 'vertical'
	# Creating the background of the App 
	canvas: 
		Color: 
			rgb: .45, .28, .5
		Rectangle: 
			pos: self.pos 
			size: self.size 

	# Providing label to the pg bar 
	Label: 
		text: '[size = 40px]Progress Bar 1 (at .25)'
		color: .5, 0, .5, 1
		markup: True

	# Creating thepg bar of specific value 
	ProgressBar: 
		value: .25
		min: 0
		max: 1
		pos_hint: {'x':.1} 
		size_hint_x: .8

	# Providing label to the pg bar 
	Label: 
		text: '[size = 40px]Progress Bar 2 (at .55)'
		color: .5, 0, .5, 1
		markup: True

	# Creating thepg bar of specific value 
	ProgressBar: 
		value: .55
		min: 0
		max: 1
		pos_hint: {'x':.1} 
		size_hint_x: .8
	

'''