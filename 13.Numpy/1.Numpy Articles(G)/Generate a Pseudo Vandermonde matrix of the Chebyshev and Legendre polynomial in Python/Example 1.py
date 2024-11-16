# import numpy and legendre libraries
import numpy as np
from numpy.polynomial import legendre

# Create arrays of point coordinates x, y and z
x = np.array([2.4, 1.2])
y = np.array([7.1, 2.7])
z = np.array([3.4, 2.2])

# Assign degrees to x, y and z
deg_of_x = 3
deg_of_y = 1
deg_of_z = 2

# use chebvander3d() function to generate a
# pseudo Vandermonde matrix of the
# Chebyshev polynomial and x, y, z sample points
print(legendre.legvander3d(x, y, z, [deg_of_x, deg_of_y, deg_of_z]))
