# import numpy and as_series
import numpy as np
from numpy.polynomial import polyutils as pu

arr = np.array([0.1, 0.2, 0.3])

# using np.as_series() method
gfg = pu.as_series(arr)

print(gfg)
