# import numpy and hermvander
import numpy as np
from numpy.polynomial.hermite import hermvander

x = np.array([1, 2, 3, 5, 7, 11])
deg = 2

# using np.hermvander() method
gfg = hermvander(x, deg)

print(gfg)
