# import numpy
import numpy as np
import numpy.ma as ma

gfg1 = np.array([1, 2, 3])
gfg2 = np.array([4, 5, 6])

# using np.ma.concatenate() method
gfg = ma.concatenate([gfg1, gfg2])

print(gfg)
