# import numpy and hermevander3d
import numpy as np
from numpy.polynomial.hermite_e import hermevander3d

x = np.array([1, 0.1])
y = np.array([2, 0.2])
z = np.array([3, 0.3])
x_deg, y_deg, z_deg = 2, 3, 1

# using np.hermevander3d() method
gfg = hermevander3d(x, y, z, [x_deg, y_deg, z_deg])

print(gfg)
