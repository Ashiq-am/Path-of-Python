# import numpy and herme2poly
import numpy as np
from numpy.polynomial.hermite_e import herme2poly

x = np.array([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5])
# using np.herme2poly() method
gfg = herme2poly(x)

print(gfg)
