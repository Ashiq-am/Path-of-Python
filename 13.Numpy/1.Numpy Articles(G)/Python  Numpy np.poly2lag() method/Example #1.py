# import numpy and poly2lag
import numpy as np
from numpy.polynomial.laguerre import poly2lag

arr = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
# using np.poly2lag() method
ans = poly2lag(arr)

print(ans)
