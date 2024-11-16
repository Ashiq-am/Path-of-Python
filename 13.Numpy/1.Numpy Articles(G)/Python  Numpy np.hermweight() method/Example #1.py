# import numpy and hermweight
import numpy as np
from numpy.polynomial.hermite import hermweight

series = np.array([6, 7, 8, 9, 10])
# using np.hermweight() method
gfg = hermweight(series)

print(gfg)
