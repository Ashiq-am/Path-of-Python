# import necessary packages
import numpy as np
import numpy.polynomial.chebyshev as c

# create 1D array of coefficients for the given polynomial
coeff = np.array([0, 10, -1, 1, 0, 0])

# returns array where trailing zeroes got removed
print(c.chebtrim(coeff))
