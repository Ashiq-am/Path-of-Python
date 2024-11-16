# import numpy and hermevander
import numpy as np
from numpy.polynomial.hermite_e import hermevander

x = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
deg = 3
# using np.hermevander() method
gfg = hermevander(x, deg)

print(gfg)
