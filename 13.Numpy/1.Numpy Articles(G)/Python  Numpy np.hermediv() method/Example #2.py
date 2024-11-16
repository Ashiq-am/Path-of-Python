# import numpy and hermediv
import numpy as np
from numpy.polynomial.hermite_e import hermediv

series1 = np.array([11, 22, 33, 44])
series2 = np.array([10, 11, 12, 13])

# using np.hermediv() method
gfg = hermediv(series1, series2)

print(gfg)
