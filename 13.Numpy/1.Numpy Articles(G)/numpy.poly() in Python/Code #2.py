# Python code explaining
# numpy.poly()

# importing libraries
import numpy as np

# Giving the roots
seq_2 = (2, 1, 0, 2, 4, 2)
b = np.poly(seq_2)
print("Coefficients of the polynomial: ", b)

# Constructing polynomial
p2 = np.poly1d(b)
print("\nAbove polynomial = \n", p2)
