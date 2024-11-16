# import the numpy module
import numpy
# import hermite_e
from numpy.polynomial import hermite_e

# create array of coefficients with 8 elements
coefficients_data = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])

# Display the coefficients
print("Coefficients: ", coefficients_data)

# Hermite_e series of power-4
print("\nHermite_e series of power-4: ",
	hermite_e.hermepow(coefficients_data, 4))
