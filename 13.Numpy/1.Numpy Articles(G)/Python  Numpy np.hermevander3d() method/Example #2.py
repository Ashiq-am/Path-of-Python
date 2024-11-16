# import numpy and hermevander3d
import numpy as np
from numpy.polynomial.hermite_e import hermevander3d

x = np.array([1.01, 2.02, 3.03])
y = np.array([10.1, 20.2, 30.3])
z = np.array([0.1, 0.2, 0.3])
x_deg, y_deg, z_deg = 1, 1, 3

# using np.hermevander3d() method
gfg = hermevander3d(x, y, z, [x_deg, y_deg, z_deg])

print(gfg)
