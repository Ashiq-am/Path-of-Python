# import the module
from vpython import *

# the box to be labelled
b = box(color = vector(1, 1, 0),
		size = vector(1, 1, 1))

# the label for the box
label(pos = b.pos,
	text = "This label is for the box",
	font = "sans",
	color = vector(0, 0, 1),
	linecolor = vector(0, 1, 1),
	linewidth = 3,
	yoffset = 150,
	xoffset = 150)
