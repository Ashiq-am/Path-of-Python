import numpy as np
from numpy.polynomial import hermite

gfg = np.array([1,2,3,4,5,6,7,8,9,10])

print("Array - ", gfg)

print("Dimension of Array:-",gfg.ndim)

print("Datatype of Array:-",gfg.dtype)

print("Shape of Array:-",gfg.shape)

print("Differentiated Hermite series", hermite.hermder(gfg))
