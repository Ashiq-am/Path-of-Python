# import numpy and hermfit
import numpy as np
from numpy.polynomial.hermite import hermfit

x = np.array([-2, -1, 0, 1, 2])
y = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
deg = 3

# using np.hermfit() method
gfg = hermfit(x, y, deg)

print(gfg)
