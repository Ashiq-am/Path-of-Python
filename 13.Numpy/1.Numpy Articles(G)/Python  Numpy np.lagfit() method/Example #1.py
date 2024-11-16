# import numpy and lagfit
import numpy as np
from numpy.polynomial.laguerre import lagfit

x, y = [1, 2], [3, 4]
deg = 2

# import np.lagfit() method
gfg = lagfit(x, y, deg)

print(gfg)
