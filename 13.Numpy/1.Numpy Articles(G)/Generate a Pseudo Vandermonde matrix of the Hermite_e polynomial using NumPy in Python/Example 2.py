# import numpy and hermite_e libraries
import numpy as np
from numpy.polynomial import hermite_e as H

# Now create arrays of point coordinates x and y
x = [5, 2]
y = [3, 4]

# Define the degrees of x and y
deg_of_x = 2
deg_of_y = 3

# To generate a pseudo Vandermonde matrix of
# the Hermite_e polynomial,
# use the hermite_e.hermevander2d() method
print(H.hermevander2d(x,y, [deg_of_x, deg_of_y]))
