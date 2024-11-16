# import numpy and harmint
import numpy as np
from numpy.polynomial.hermite import hermint

series = np.array([1, 2, 3, 4, 5])
# using np.harmint() method
gfg = hermint(series, m = 2)

print(gfg)
