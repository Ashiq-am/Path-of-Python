# import numpy and hermevander2d
import numpy as np
from numpy.polynomial.hermite_e import hermevander2d

x = np.array([0.1, 0.2])
y = np.array([2, 0.2])
x_deg, y_deg = 2, 3
# using np.hermevander2d() method
gfg = hermevander2d(x, y, [x_deg, y_deg])

print(gfg)
