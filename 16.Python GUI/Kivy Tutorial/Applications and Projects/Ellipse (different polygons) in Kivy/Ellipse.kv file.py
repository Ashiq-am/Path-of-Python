''''''

'''
# Ellipse.kv file of the code 

################################################### 

# For the arcs, we have to give the start, 
# and the end angle. We use default number of segments, 
# 180, and 5, for the two ellipse arcs. 
# The rest of the kv file, corresponds, to the other, 
# 6 ellipse arcs, following the same pattern. 

#:set angle_start_row2 240 
#:set angle_end_row2 480 
#:set angle_start_row3 120 
#:set angle_end_row3 240 

################################################# 


<Ellipsekv>: 

	# Setting coloumn to 4 
	cols:4

################################################## 

# Row 1 
	
	# Creating Canvas 
	canvas: 
		Color: 
			rgb: 0, 0, 1
		Rectangle: 
			pos: self.pos 
			size: self.size 

	# This will create the circle 
	# as no segment is fixed in Ellipse 
	# so by default it creates the circle 
	RelativeLayout: 
		canvas: 
			Color: 
				rgb: 1, .8, .5
			Ellipse: 
				pos: 0, 0
				size: self.size 

	# This will create pentagon as 
	# segment = 5 
	RelativeLayout: 
		canvas: 
			Ellipse: 
				segments: 5
				pos: 0, 0
				size: self.size 

	# This will create square shape as 
	# segment = 4 
	RelativeLayout: 
		canvas: 
			Ellipse: 
				segments: 4
				pos: 0, 0
				size: self.size 

	# This will create triangle as 
	# segment = 3 
	RelativeLayout: 
		canvas: 
			Ellipse: 
				segments: 3
				pos: 0, 0
				size: self.size 
				
################################################# 

# Row 2 

	RelativeLayout: 
		canvas: 
			# Assigning colour to all in row 2 
			Color: 
				rgb: 1, .59, .86

			# Creating the arc as assigned above 
			Ellipse: 
				angle_start: angle_start_row2 
				angle_end: angle_end_row2 
				pos: 0, 0
				size: self.size 


	# Creating the arc as assigned above 
	# segment 5 
	RelativeLayout: 
		canvas: 
			Ellipse: 
				angle_start: angle_start_row2 
				angle_end: angle_end_row2 
				segments: 5
				pos: 0, 0
				size: self.size 

	# Creating the arc as assigned above 
	# segment 4 
	RelativeLayout: 
		canvas: 
			Ellipse: 
				angle_start: angle_start_row2 
				angle_end: angle_end_row2 
				segments: 4
				pos: 0, 0
				size: self.size 

	# Creating the arc as assigned above 
	# segment 5 
	RelativeLayout: 
		canvas: 
			Ellipse: 
				angle_start: angle_start_row2 
				angle_end: angle_end_row2 
				segments: 3
				pos: 0, 0
				size: self.size 

################################################# 

# Row 3 

	RelativeLayout: 
		canvas: 
			Color: 
				rgb: .5, .5, .5
			Ellipse: 
				angle_start: angle_start_row3 
				angle_end: angle_end_row3 
				pos: 0, 0
				size: self.size 

	RelativeLayout: 
		canvas: 
			Ellipse: 
				angle_start: angle_start_row3 
				angle_end: angle_end_row3 
				segments: 5
				pos: 0, 0
				size: self.size 

	RelativeLayout: 
		canvas: 
			Ellipse: 
				angle_start: angle_start_row3 
				angle_end: angle_end_row3 
				segments: 4
				pos: 0, 0
				size: self.size 

	RelativeLayout: 
		canvas: 
			Ellipse: 
				angle_start: angle_start_row3 
				angle_end: angle_end_row3 
				segments: 3
				pos: 0, 0
				size: self.size 

'''











"""This is the result. We have 3 rows and 4 columns. Rows 2 and 3 are arc shapes, 
while Row1 has the default angles, 0 and 360 to form a complete circle. 
By changing the size of the window manually, we can get ovals, and shapes based on them. 
For the arc, the number of segments, corresponds to the number of lines that approximate the 
circular portion."""