# Python program explaining
# numpy.laggrid2d() method

# importing numpy as np
import numpy as np
from numpy.polynomial.laguerre import laggrid2d

# Input laguerre series coefficients
c = np.array([[1, 3, 5], [2, 4, 6]])

# using np.laggrid2d() method
ans = laggrid2d(7, 8, c)

print(ans)
