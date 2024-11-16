# import numpy and hermfit
import numpy as np
from numpy.polynomial.hermite import hermfit

x = np.array([-3, -2, -1])
y = np.array([1, 2, 3])
deg = 2

# using np.hermfit() method
gfg = hermfit(x, y, deg)

print(gfg)
