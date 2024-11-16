# import numpy and chebyshev libraries
import numpy as np
from numpy.polynomial import chebyshev as C

# Create arrays of point coordinates x, y and z
x = [1.2, 2.1]
y = [2.3, 3.2]
z = [3.1, 1.3]

# Assign degrees to x, y and z
deg_of_x = 2
deg_of_y = 1
deg_of_z = 3

# use chebvander3d() function to generate a
# pseudo Vandermonde matrix of the
# Chebyshev polynomial and x, y, z sample points
print(C.chebvander3d(x, y, z, [deg_of_x, deg_of_y, deg_of_z]))
