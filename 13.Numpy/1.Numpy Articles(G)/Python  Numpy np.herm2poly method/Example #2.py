# import numpy and herm2poly
import numpy as np
from numpy.polynomial.hermite import herm2poly

x = np.array([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5])
# using np.herm2poly() method
gfg = herm2poly(x)

print(gfg)
