# import numpy and harmeint
import numpy as np
from numpy.polynomial.hermite_e import hermeint

series = np.array([2, 0.3, 4, 0.5, 6])

# using np.harmeint() method
gfg = hermeint(series, m = 2)

print(gfg)
