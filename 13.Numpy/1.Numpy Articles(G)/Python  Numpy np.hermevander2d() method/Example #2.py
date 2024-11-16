# import numpy and hermevander2d
import numpy as np
from numpy.polynomial.hermite_e import hermevander2d

x = np.array([1.01, 2.02, 3.03])
y = np.array([10.1, 20.2, 30.3])
x_deg, y_deg = 1, 1
# using np.hermevander2d() method
gfg = hermevander2d(x, y, [x_deg, y_deg])

print(gfg)
