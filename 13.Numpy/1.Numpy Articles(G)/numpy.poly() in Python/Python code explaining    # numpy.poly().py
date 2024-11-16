# Python code explaining
# numpy.poly()

# importing libraries
import numpy as np

# Giving the roots
seq_1 = (2, 1, 0)
a = np.poly(seq_1)
print("Coefficients of the polynomial: ", a)

# Constructing polynomial
p1 = np.poly1d(a)
print("\nAbove polynomial = \n", p1)
