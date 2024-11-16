# import numpy and hermdomain
import numpy as np
from numpy.polynomial.hermite import hermdomain

# using np.hermedomain() method
for i in range(5):
	gfg = hermdomain + [i-1, i + 1]
	print(gfg)
