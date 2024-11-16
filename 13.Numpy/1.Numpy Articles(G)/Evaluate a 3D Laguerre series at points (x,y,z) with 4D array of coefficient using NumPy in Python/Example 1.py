# import numpy module
import numpy
# import laguerre
from numpy.polynomial import laguerre

# Create 1d array of 6 elements
coefficient_array = numpy.arange(48).reshape(2,2,6,2)

# Display
print(coefficient_array)

# display the Dimensions
print(coefficient_array.ndim)

# display Shape
print(coefficient_array.shape)

# Evaluate a 3D Laguerre series at
# points (x,y) - [3,4],[1,2],[6,7]
print(laguerre.lagval3d([3,4],[1,2],[6,7],coefficient_array))
