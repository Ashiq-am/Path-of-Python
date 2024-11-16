# import numpy
import numpy as np
import numpy.ma as ma

gfg1 = np.array([11, 22, 33])
gfg2 = np.array([41, 52, 63])

# using np.ma.concatenate() method
gfg = ma.concatenate([[gfg1], [gfg2]])

print(gfg)
