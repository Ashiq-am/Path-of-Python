# Python program explaining
# numpy.lagdomain() method

# import numpy and lagdomain
import numpy as np
from numpy.polynomial.laguerre import lagdomain

# using np.lagdomain() method
for i in range(4):
	ans = lagdomain + [i-1, i + 1]
	print(ans)
