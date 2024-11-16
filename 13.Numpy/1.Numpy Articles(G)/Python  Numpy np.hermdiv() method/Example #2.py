# import numpy and hermdiv
import numpy as np
from numpy.polynomial.hermite import hermdiv

series1 = np.array([1, 2, 3])
series2 = np.array([1, 2, 3])

# using np.hermdiv() method
gfg = hermdiv(series1, series2)

print(gfg)
