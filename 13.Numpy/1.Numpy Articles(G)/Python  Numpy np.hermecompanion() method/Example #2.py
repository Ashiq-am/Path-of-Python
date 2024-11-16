# import numpy and hermecompanion
import numpy as np
from numpy.polynomial.hermite_e import hermecompanion

series = np.array([1, 2, 3, 4, 5])
# using np.hermecompanion() method
gfg = hermecompanion(series)

print(gfg)
