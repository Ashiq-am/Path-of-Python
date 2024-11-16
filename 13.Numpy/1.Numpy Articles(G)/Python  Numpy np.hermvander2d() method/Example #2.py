# import numpy and hermvander2d
import numpy as np
from numpy.polynomial.hermite import hermvander2d

x = np.array([0.5, 0.10, 0.10, 0.5])
y = np.array([1, 2, 3, 5])
x_deg, y_deg = 1, 1

# using np.hermvander2d() method
gfg = hermvander2d(x, y, [x_deg, y_deg])

print(gfg)
