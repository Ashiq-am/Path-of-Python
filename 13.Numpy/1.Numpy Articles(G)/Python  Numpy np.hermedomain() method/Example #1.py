# import numpy and hermedomain
import numpy as np
from numpy.polynomial.hermite_e import hermedomain

# using np.hermedomain() method
for i in range(5):
	gfg = hermedomain + [i, i + 1]
	print(gfg)
