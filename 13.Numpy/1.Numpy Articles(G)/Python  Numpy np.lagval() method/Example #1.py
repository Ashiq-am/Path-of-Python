# import numpy and lagval
import numpy as np
from numpy.polynomial.laguerre import lagval

x = 2
c = np.array([3, 10])

# import np.lagval() method
gfg = lagval(x, c)

print(gfg)
