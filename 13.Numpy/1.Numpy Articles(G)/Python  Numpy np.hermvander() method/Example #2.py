# import numpy and hermvander
import numpy as np
from numpy.polynomial.hermite import hermvander

x = np.array([5, 10, -10, -5])
deg = 3

# using np.hermvander() method
gfg = hermvander(x, deg)

print(gfg)
