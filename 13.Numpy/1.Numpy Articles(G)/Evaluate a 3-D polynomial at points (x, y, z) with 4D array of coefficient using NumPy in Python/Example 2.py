# importing numpy module and polyval3d function
import numpy as np
from numpy.polynomial.polynomial import polyval3d

# creating an 4d array of coefficiets 'C'
C = np.arange(72).reshape(3,2,6,2)

# Now using polyval3d function evaluate
# the 3D polynomial at points (x,y,z)
x = [4,1]
y = [1,2]
z = [2,3]

print("The result of evaluation by polyval3d function is : \n",
	polyval3d(x, y, z, C))
