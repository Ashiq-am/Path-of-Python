# import numpy
import numpy as np

# using Numpy.expand_dims() method
gfg = np.array([[1, 2], [7, 8], [5, 10]])
gfg = gfg.reshape(1, 2, 3)
print(gfg)

gfg = np.dsplit(gfg, 3)
print(gfg)
