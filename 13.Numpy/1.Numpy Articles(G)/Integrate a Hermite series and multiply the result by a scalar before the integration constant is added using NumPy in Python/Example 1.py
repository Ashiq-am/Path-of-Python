# import the numpy module
import numpy

# import hermite
from numpy.polynomial import hermite

# Create an array of hermite series
# coefficients with 6 elements
coefficient_array = numpy.array([1, 2, 3, 4, 3, 5])

# display array
print("Coefficient array: ", coefficient_array)

# display the dimensions
print("Dimensions: ", coefficient_array.ndim)

# integrate hermite series with scale=2
print( hermite.hermint(coefficient_array, scl=-2))
