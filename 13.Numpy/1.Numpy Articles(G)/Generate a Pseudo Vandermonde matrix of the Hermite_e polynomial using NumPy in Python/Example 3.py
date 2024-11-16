# import numpy and hermite_e libraries
import numpy as np
from numpy.polynomial import hermite_e

# Now create arrays of point coordinates
# x, y and z
x = np.array([3, 1])
y = np.array([2, 3])
z = np.array([4, 7])

# assign the degree to x, y and z
deg_of_x = 3
deg_of_y = 2
deg_of_z = 1

# use the hermite.hermevander3d() function
# to generate a pseudo Vandermonde
# matrix of the Hermite_e polynomial
# and x, y, z as the sample points
print(hermite_e.hermevander3d(x, y, z, [deg_of_x, deg_of_y, deg_of_z]))
