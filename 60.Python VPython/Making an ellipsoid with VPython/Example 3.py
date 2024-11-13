# import the module
from vpython import *

# the first ellipsoid
ellipsoid(pos = vector(-2, 2, 0),
		length = 3,
		height = 2,
		width = 2,
		color = vector(1, 0.6, 0))

# the second ellipsoid
ellipsoid(pos = vector(1, -1, 5),
		width = 3,
		color = vector(0, 1, 0))
