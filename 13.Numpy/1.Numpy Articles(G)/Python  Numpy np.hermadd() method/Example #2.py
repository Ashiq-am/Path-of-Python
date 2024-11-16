# import numpy and hermadd
import numpy as np
from numpy.polynomial.hermite import hermadd

series1 = np.array([1, 0, 3, 0, 5])
series2 = np.array([0, 7, 0, 9, 0])

# using np.hermadd() method
gfg = hermadd(series1, series2)

print(gfg)
