# import numpy and hermmul
import numpy as np
from numpy.polynomial.hermite import hermmul

series1 = np.array([1, 2, 3, 4, 5])
series2 = np.array([6, 7, 8, 9, 10])

# using np.hermmul() method
gfg = hermmul(series1, series2)

print(gfg)
