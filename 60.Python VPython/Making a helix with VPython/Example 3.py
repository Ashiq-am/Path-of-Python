# import the module
from vpython import *

# the first helix
helix(pos = vector(-2, 2, 0),
	length = 3,
	radius = 1,
	coils = 10,
	thickness = 0.5,
	color = vector(0.5, 0, 0))

# the second helix
helix(pos = vector(1, -1, 5),
	color = vector(0, 1, 0),
	coils = 20)
