# import numpy and harmint
import numpy as np
from numpy.polynomial.hermite import hermint

series = np.array([2, 0.3, 4, 0.5, 6])
# using np.harmint() method
gfg = hermint(series, m = 1)

print(gfg)
