# import numpy and hermvander2d
import numpy as np
from numpy.polynomial.hermite import hermvander2d

x = np.array([1, 2])
y = np.array([-1, -2])
x_deg, y_deg = 2, 2

# using np.hermvander2d() method
gfg = hermvander2d(x, y, [x_deg, y_deg])

print(gfg)
