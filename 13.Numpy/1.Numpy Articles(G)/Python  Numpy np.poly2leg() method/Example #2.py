# import numpy and poly2leg
import numpy as np
from numpy.polynomial.legendre import poly2leg

arr = np.array([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5])
# using np.poly2leg() method
ans = poly2leg(arr)

print(ans)
