''''''


# Line.kv file of the code

# Creating Different types of Lines(or shapes through line)

###########################################

# Row 1:

# Ellipse(1st row 1st element)

"""

<LineEllipse1>:

	# Creating Canvas
	canvas:
		Color:
			rgba: 1, .1, .1, .9
		# Ellipse Creation
		Line:
			width: 2.
			ellipse: (self.x, self.y, self.width, self.height)

	# Label the figure
	Label:
		center: root.center
		text: 'Ellipse'


############################################

# Ellipse from 90 to 180((1st row 2nd element))

<LineEllipse2>:
	canvas:
		Color:
			rgba: 1, .1, .1, .9
		Line:
			width: 2.
			ellipse: (self.x, self.y, self.width, self.height, 90, 180)
	Label:
		center: root.center
		text: 'Ellipse from 90 to 180'


############################################


# Ellipse from 90 to 720, 10 segments(1st row 3rd element)

<LineEllipse3>:
	canvas:
		Color:
			rgba: 1, .1, .1, .9
		Line:
			width: 2.
			ellipse: (self.x, self.y, self.width, self.height, 90, 720, 10)
	Label:
		center: root.center
		text: 'Ellipse from 90 to 720, 10 segments'
		halign: 'center'

############################################

# Circle(2nd row 1st element)
<LineCircle1>:
	canvas:
		Color:
			rgba: .1, 1, .1, .9
		Line:
			width: 2.
			circle:
				(self.center_x, self.center_y, min(self.width, self.height)
				/ 2)
	Label:
		center: root.center
		text: 'Circle'

############################################

# Circle from 90 to 180(2nd row 2nd element)
<LineCircle2>:
	canvas:
		Color:
			rgba: .1, 1, .1, .9
		Line:
			width: 2.
			circle:
				(self.center_x, self.center_y, min(self.width, self.height)
				/ 2, 90, 180)
	Label:
		center: root.center
		text: 'Circle from 90 to 180'

############################################
# Circle from 90 to 180, 10 segments(1st row 3rd element)
<LineCircle3>:
	canvas:
		Color:
			rgba: .1, 1, .1, .9
		Line:
			width: 2.
			circle:
				(self.center_x, self.center_y, min(self.width, self.height)
				/ 2, 90, 180, 10)
	Label:
		center: root.center
		text: 'Circle from 90 to 180, 10 segments'
		halign: 'center'

############################################

# Circle from 0 to 360 (3rd row 1st element)
<LineCircle4>:
	canvas:
		Color:
			rgba: .1, 1, .1, .9
		Line:
			width: 2.
			circle:
				(self.center_x, self.center_y, min(self.width, self.height)
				/ 2, 0, 360)
	Label:
		center: root.center
		text: 'Circle from 0 to 360'
		halign: 'center'

############################################

# Rectangle (3rd row 2nd element)
<LineRectangle>:
	canvas:
		Color:
			rgba: .1, .1, 1, .9
		Line:
			width: 2.
			rectangle: (self.x, self.y, self.width, self.height)
	Label:
		center: root.center
		text: 'Rectangle'

############################################

# Bezier (3rd row 3rd element)
<LineBezier>:
	canvas:
		Color:
			rgba: .1, .1, 1, .9
		Line:
			width: 2.
			bezier:
				(self.x, self.y, self.center_x - 40, self.y + 100,
				self.center_x + 40, self.y - 100, self.right, self.y)
	Label:
		center: root.center
		text: 'Bezier'
		
"""
