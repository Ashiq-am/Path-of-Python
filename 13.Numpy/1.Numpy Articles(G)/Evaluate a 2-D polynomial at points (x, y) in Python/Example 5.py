# importing numpy and polyval2d
import numpy as np
from numpy.polynomial.polynomial import polyval2d

# Create a multidimensional array of
# coefficients or a matrix
Arr = np.matrix([[4, 2], [6, 3]])

# Defining x and y
x = [2, 3]
y = [1, 2]

# in order to evaluate a 2-D polynomial
# at points (x, y), we are using the
# polynomial.polyval2d() method in Python
# Numpy
print(polyval2d(x, y, Arr))
