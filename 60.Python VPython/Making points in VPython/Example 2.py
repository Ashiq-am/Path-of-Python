# import the module
from vpython import *

# first set of points
points(pos =[vector(-1, 0, 0),
			vector(1, 0, 0),
			vector(0, 1, 0),
			vector(0, -1, 0)],
	color = vector(1, 0, 0),
	radius = 10)

# second set of points
points(pos =[vector(-0.5, 0, 0),
			vector(0.5, 0, 0)],
	color = vector(1, 0, 1),
	radius = 20)
