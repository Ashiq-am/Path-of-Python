# import numpy and hermecompanion
import numpy as np
from numpy.polynomial.hermite_e import hermecompanion

series = np.array([6, 7, 8, 9, 10])
# using np.hermecompanion() method
gfg = hermecompanion(series)

print(gfg)
