# Python program explaining
# numpy.leggrid3d() method

# importing numpy as np

import numpy as np
from numpy.polynomial.legendre import leggrid3d

# Input legendre series coefficients
c = np.array([[1, 3, 5], [2, 4, 6], [10, 11, 12]])

# using np.leggrid3d() method
ans = leggrid3d([7, 9], [8, 10], [5, 6], c)
print(ans)
