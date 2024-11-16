# import the numpy module
import numpy

# import hermite_se
from numpy.polynomial import hermite_e

# create array of coefficients with 5 elements
coefficients_data = numpy.array([1, 2, 3, 4, 5])

# Display the coefficients
print(coefficients_data)

# get the shape
print(f"\nShape of an array: {coefficients_data.shape}")

# get the dimensions
print(f"Dimension: {coefficients_data.ndim}")

# Evaluate a Hermite_e series at points - [2,4]
print("\nHermite_e series", hermite_e.hermeval(
	[2, 4], coefficients_data, tensor=False))
