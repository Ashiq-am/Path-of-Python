# import numpy and hermeweight
import numpy as np
from numpy.polynomial.hermite_e import hermeweight

poly = np.array([1.1, 2.2, 3.3, 4.4])

# using np.hermeweight() method
gfg = hermeweight(poly)

print(gfg)
