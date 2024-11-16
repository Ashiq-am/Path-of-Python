# import numpy and hermpow
import numpy as np
from numpy.polynomial.hermite import hermpow

series = np.array([1, 2, 3, 4, 5])

# using np.hermpow() method
gfg = hermpow(series, 2)

print(gfg)
