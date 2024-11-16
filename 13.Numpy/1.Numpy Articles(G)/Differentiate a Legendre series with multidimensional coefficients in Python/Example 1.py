# import the numpy module
import numpy

# import legendre
from numpy.polynomial import legendre

# create array of coefficients with 5 elements each
coefficients_data = numpy.array(
	[[1, 2, 3, 4, 5], [3, 4, 2, 6, 7], [43, 45, 2, 6, 7]])

# Display the coefficients
print(coefficients_data)

# get the shape
print(f"\nShape of an array: {coefficients_data.shape}")

# get the dimensions
print(f"Dimension: {coefficients_data.ndim}")

# using legendre.legder() method to differentiate
# a legendre series.
print("\nDifferentiated legendre series", legendre.legder(coefficients_data))
