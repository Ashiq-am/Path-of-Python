# import numpy and hermweight
import numpy as np
from numpy.polynomial.hermite import hermweight

series = np.array([0, -7, 8, -9, 1])
# using np.hermweight() method
gfg = hermweight(series)

print(gfg)
