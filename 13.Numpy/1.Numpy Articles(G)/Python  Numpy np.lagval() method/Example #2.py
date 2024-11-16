# import numpy and lagval
import numpy as np
from numpy.polynomial.laguerre import lagval

x = np.array([[1, 5], [2, 10]])
c = np.array([3, 1])

# import np.lagval() method
gfg = lagval(x, c)

print(gfg)
