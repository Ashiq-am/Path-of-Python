# import numpy and hermvander3d
import numpy as np
from numpy.polynomial.hermite import hermvander3d

x = np.array([1, 2])
y = np.array([-1, -2])
z = np.array([1, -2])
x_deg, y_deg, z_deg = 2, 2, 2

# using np.hermvander3d() method
gfg = hermvander3d(x, y, z, [x_deg, y_deg, z_deg])

print(gfg)
