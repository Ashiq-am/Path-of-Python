# import necessary packages
import numpy as np
import numpy.polynomial.chebyshev as c

# create 1D array of coefficients for the
# given polynomial
coeff = np.array([0, -1, -2, 3, 4])

# returns array where trailing zeroes got removed
print(c.chebtrim(coeff))
