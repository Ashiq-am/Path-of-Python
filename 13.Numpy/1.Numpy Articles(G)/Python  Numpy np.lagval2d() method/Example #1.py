# import numpy and lagval2d
import numpy as np
from numpy.polynomial.laguerre import lagval2d

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 10], [15, 20]])
c = np.array([1, 2])

# import np.lagval2d() method
gfg = lagval2d(x, y, c)

print(gfg)
