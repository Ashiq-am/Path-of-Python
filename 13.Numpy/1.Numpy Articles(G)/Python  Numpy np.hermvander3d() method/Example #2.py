# import numpy and hermvander3d
import numpy as np
from numpy.polynomial.hermite import hermvander3d

x = np.array([0.5, 0.10, 0.10, 0.5])
y = np.array([1, 2, 3, 5])
z = np.array([10.1, 20.2, 30.3, -50])
x_deg, y_deg, z_deg = 1, 1, 1

# using np.hermvander3d() method
gfg = hermvander3d(x, y, z, [x_deg, y_deg, z_deg])

print(gfg)
