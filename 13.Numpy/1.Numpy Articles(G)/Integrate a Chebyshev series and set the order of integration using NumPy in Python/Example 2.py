# import the numpy module
import numpy

# import chebyshev
from numpy.polynomial import chebyshev

# Create an 2 D array of Chebyshev series
# coefficients with 6 elements
coefficient_array = numpy.array([[1, 2, 3, 4, 3, 5], [5, 6, 8, 9, 0, 0]])

# display array
print("Coefficient array: ", coefficient_array)

# display the dimensions
print("Dimensions: ", coefficient_array.ndim)

# integrate chebyshev series with order 3
print("\nChebyshev series with order 3",
	chebyshev.chebint(coefficient_array, m=3))

# integrate chebyshev series with order 4
print("\nChebyshev series with order 4",
	chebyshev.chebint(coefficient_array, m=4))

# integrate chebyshev series with order 1
print("\nChebyshev series with order 1",
	chebyshev.chebint(coefficient_array, m=1))

# integrate chebyshev series with order 6
print("\nChebyshev series with order 6",
	chebyshev.chebint(coefficient_array, m=6))
