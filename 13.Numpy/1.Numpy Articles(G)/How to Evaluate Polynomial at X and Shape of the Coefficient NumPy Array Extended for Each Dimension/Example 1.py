# importing neccessary libraries
import numpy as np
from numpy.polynomial.polynomial import polyval

# Create a multidimensional array 'Arr'
# of coefficients
Arr = np.matrix([[7,6],[2,3]])

# To evaluate a polynomial at points x,
# we use the polynomial.polyval()
# function in Python Numpy
print(polyval([1,2], Arr, tensor=True))
