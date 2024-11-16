# import the numpy module
import numpy

# import hermite
from numpy.polynomial import hermite

# Create an 2d array of hermite series
# coefficients with 6 elements each
coefficient_array = numpy.array([[1, 2, 3, 4, 3, 5],
								[4, 5, 6, 4, 3, 2]])

# display array
print("Coefficient array: ", coefficient_array)

# display the dimensions
print("Dimensions: ", coefficient_array.ndim)

# integrate hermite series with scale=-1
print( hermite.hermint(coefficient_array, scl=-1))
