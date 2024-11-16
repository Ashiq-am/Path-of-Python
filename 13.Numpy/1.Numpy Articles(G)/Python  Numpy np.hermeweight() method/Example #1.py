# import numpy and hermeweight
import numpy as np
from numpy.polynomial.hermite_e import hermeweight

poly = np.array([0.1, 0.2, 0.3])

# using np.hermeweight() method
gfg = hermeweight(poly)

print(gfg)
