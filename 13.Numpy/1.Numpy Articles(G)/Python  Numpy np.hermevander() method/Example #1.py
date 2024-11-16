# import numpy and hermevander
import numpy as np
from numpy.polynomial.hermite_e import hermevander

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
deg = 3
# using np.hermevander() method
gfg = hermevander(x, deg)

print(gfg)
