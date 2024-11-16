# import numpy and hermmulx
import numpy as np
from numpy.polynomial.hermite import hermmulx

series = np.array([6, 7, 8, 9, 10])

# using np.hermmulx() method
gfg = hermmulx(series)

print(gfg)
