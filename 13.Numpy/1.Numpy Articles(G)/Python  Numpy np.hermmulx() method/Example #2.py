# import numpy and hermmulx
import numpy as np
from numpy.polynomial.hermite import hermmulx

series = np.array([1, 2, 3])

# using np.hermmulx() method
gfg = hermmulx(series)

print(gfg)
