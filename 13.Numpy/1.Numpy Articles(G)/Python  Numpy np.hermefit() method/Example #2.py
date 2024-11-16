# import numpy and hermefit
import numpy as np
from numpy.polynomial.hermite_e import hermefit

x = np.array([11, 22, 33, 44])
y = np.array([1, 2, 3, 4])
deg = 2
# using np.hermefit() method
gfg = hermefit(x, y, deg)

print(gfg)
