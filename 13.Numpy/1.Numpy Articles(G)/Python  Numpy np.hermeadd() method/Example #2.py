# import numpy and hermeadd
import numpy as np
from numpy.polynomial.hermite_e import hermeadd

series1 = np.array([11, 22, 33, 44])
series2 = np.array([10, 11, 12, 13])

# using np.hermeadd() method
gfg = hermeadd(series1, series2)

print(gfg)
