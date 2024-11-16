# import numpy and poly2herm
import numpy as np
from numpy.polynomial.hermite import poly2herm

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
# using np.poly2herm() method
gfg = poly2herm(x)

print(gfg)
