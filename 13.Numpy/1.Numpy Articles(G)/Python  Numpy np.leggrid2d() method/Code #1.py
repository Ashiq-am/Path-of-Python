# Python program explaining
# numpy.leggrid2d() method

# importing numpy as np

import numpy as np
from numpy.polynomial.legendre import leggrid2d

# Input legendre series coefficients
c = np.array([[1, 3, 5], [2, 4, 6]])

# using np.leggrid2d() method
ans = leggrid2d([7, 9], [8, 10], c)
print(ans)
