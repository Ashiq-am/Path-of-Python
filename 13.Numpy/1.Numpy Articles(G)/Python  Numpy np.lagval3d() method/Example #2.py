# import numpy and lagval3d
import numpy as np
from numpy.polynomial.laguerre import lagval3d

x, y, z = 1, 2, 3
c = np.array([1, 2])

# import np.lagval3d() method
gfg = lagval3d(x, y, z, c)

print(gfg)
