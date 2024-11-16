# import the numpy module
import numpy

# import hermite
from numpy.polynomial import hermite

# create array of coefficients with 5 elements each
coefficients_data = numpy.array(
	[[1, 2, 3, 4, 5], [3, 4, 2, 6, 7], [43, 45, 2, 6, 7]])

# Display the coefficients
print(coefficients_data)

# get the shape
print(f"\nShape of an array: {coefficients_data.shape}")

# get the dimensions
print(f"Dimension: {coefficients_data.ndim}")

# using hermite.hermder() method to differentiate a Hermite series.
print("\nHermite series", hermite.hermder(coefficients_data, m=2, axis=1))
