# import numpy module
import numpy

# import hermite
from numpy.polynomial import hermite

# Create 1d array of 6 elements
coefficient_array = numpy.array([45, 67, 54, 53, 67, 15])

# Display
print(coefficient_array)

# display the Dimensions
print(coefficient_array.ndim)

# display Shape
print(coefficient_array.shape)

# Evaluate a 2D hermite series at points
# (x,y) - [1,4],[1,2]
print(hermite.hermval2d([1, 4], [1, 2], coefficient_array))
