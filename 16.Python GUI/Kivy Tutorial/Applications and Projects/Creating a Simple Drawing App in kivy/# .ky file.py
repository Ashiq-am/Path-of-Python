""""""


'''
# Drawing.kv implementation 

# for assigning random color to the brush 
#:import rnd random 

# Paint brush coding 
<Paint_brush>: 
	size_hint: None, None
	size: 25, 50
	canvas: 
		Color: 
			rgb: rnd.random(), rnd.random(), rnd.random() 
		Triangle: 
			points: 
				(self.x, self.y, self.x + self.width / 4, self.y, 
				self.x + self.width / 4, self.y + self.height / 4) 

# Drawing pad creation			 
<Drawing>: 
	canvas: 
		Color: 
			rgb: .2, .5, .5
		Rectangle: 
			size: root.size 
			pos: root.pos 

'''