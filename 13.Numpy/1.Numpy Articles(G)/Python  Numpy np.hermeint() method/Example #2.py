# import numpy and harmeint
import numpy as np
from numpy.polynomial.hermite_e import hermeint

series = np.array([1, 2, 3, 4, 5])

# using np.harmeint() method
gfg = hermeint(series, m = 3)

print(gfg)
