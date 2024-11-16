# importing numpy module and polyval3d function
import numpy as np
from numpy.polynomial.polynomial import polyval3d

# creating an 4d array of coefficiets 'C'
# using numpy
C = np.arange(24).reshape(2,2,3,2)

# Now using polyval3d function we are
# evaluating the 3D polynomial at points
# (x,y,z)
print(polyval3d([2,1],[1,2],[2,3], C))
