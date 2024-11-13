# import the module
from vpython import *

# the first ring
ring(pos = vector(-2, 2, 0),
	axis = vector(0, 0, 1),
	radius = 2,
	thickness = 1,
	color = vector(0.2, 0.7, 0))

# the second ring
ring(pos = vector(1, -1, 5),
	axis = vector(0, 0, 1),
	radius = 5,
	color = vector(0, 0.2, 0.8))
