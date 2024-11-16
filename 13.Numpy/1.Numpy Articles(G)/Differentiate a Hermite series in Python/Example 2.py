import numpy as np
from numpy.polynomial import hermite

gfg = np.array([56,84,87,44,98])

print("Array - ", gfg)

print("Dimension of Array:-",gfg.ndim)

print("Datatype of Array:-",gfg.dtype)

print("Shape of Array:-",gfg.shape)

print("Differentiated Hermite series", hermite.hermder(gfg, m=2))
