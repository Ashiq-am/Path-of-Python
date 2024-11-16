# import numpy and lagmulx
import numpy as np
from numpy.polynomial.laguerre import lagmulx

series = np.array([10, 20, 30])

# using np.lagmulx() method
gfg = lagmulx(series)

print(gfg)
