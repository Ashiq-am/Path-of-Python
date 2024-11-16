# import numpy and lagval3d
import numpy as np
from numpy.polynomial.laguerre import lagval3d

x = np.array([[1, 2], [3, 4]])
y = np.array([[-5, -10], [-15, -20]])
z = np.array([[1, 2], [3, 4]])
c = np.array([1, 2])

# import np.lagval3d() method
gfg = lagval3d(x, y, z, c)

print(gfg)
