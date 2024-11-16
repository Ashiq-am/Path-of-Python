# import numpy and hermsub
import numpy as np
from numpy.polynomial.hermite import hermsub

series1 = np.array([1, 0, 3, 0, 5])
series2 = np.array([0, 7, 0, 9, 0])

# using np.hermsub() method
gfg = hermsub(series1, series2)

print(gfg)
