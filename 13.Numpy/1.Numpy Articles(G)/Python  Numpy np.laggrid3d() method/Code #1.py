# Python program explaining
# numpy.laggrid3d() method

# importing numpy as np

import numpy as np
from numpy.polynomial.laguerre import laggrid3d

# Input laguerre series coefficients
c = np.array([[1, 3, 5], [2, 4, 6], [10, 11, 12]])

# using np.laggrid3d() method
ans = laggrid3d([7, 9], [8, 10], [5, 6], c)
print(ans)
