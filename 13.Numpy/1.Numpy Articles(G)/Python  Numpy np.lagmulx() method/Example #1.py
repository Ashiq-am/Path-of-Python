# import numpy and lagmulx
import numpy as np
from numpy.polynomial.laguerre import lagmulx

series = np.array([1, 2, 3, 4, 5])

# using np.lagmulx() method
gfg = lagmulx(series)

print(gfg)
