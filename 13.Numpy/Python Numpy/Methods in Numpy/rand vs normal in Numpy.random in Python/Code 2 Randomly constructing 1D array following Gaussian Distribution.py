# Python Program illustrating
# numpy.random.normal() method

import numpy as geek

# 1D Array
array = geek.random.normal(0.0, 1.0, 5)
print("1D Array filled with random values "
	"as per gaussian distribution : \n", array)
# 3D array
array = geek.random.normal(0.0, 1.0, (2, 1, 2))
print("\n\n3D Array filled with random values "
	"as per gaussian distribution : \n", array)
