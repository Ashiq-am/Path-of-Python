# import numpy
import numpy as np

# using Numpy.expand_dims() method
gfg = np.array([[1, 2], [7, 8]])
print(gfg.shape)

gfg = np.expand_dims(gfg, axis = 0)
print(gfg.shape)
