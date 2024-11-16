# import the numpy module
import numpy

# import hermite_se
from numpy.polynomial import hermite_e

# create array of coefficients with 5 elements each
coefficients_data = np.arange(4).reshape(2,2)

# Display the coefficients
print(coefficients_data)

# get the shape
print(f"\nShape of an array: {coefficients_data.shape}")

# get the dimensions
print(f"Dimension: {coefficients_data.ndim}")

h = [3,1]

# Evaluate a Hermite_e series at points - [3,1]
print("\nHermite_e series", hermite_e.hermeval(
h,coefficients_data))
