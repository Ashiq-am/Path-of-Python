# import the numpy module
import numpy

# import legendre
from numpy.polynomial import legendre

# create array of coefficients with 2 elements each
coefficients_data = numpy.array([6,4,7])

# Display the coefficients
print(coefficients_data)

# get the shape
print(f"\nShape of an array: {coefficients_data.shape}")

# get the dimensions
print(f"Dimension: {coefficients_data.ndim}")

h = [[1,3,4,5],[3,2,6,7]]

# Evaluate a legendre series at points - [6,4]
print("\nmultidimensional legendre series",
	legendre.legval(coefficients_data,h))
