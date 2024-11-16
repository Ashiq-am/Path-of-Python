import numpy as np
from numpy.polynomial import hermite

gfg = np.array([1,2,3,4,5,6,7,8,9,10])

print(gfg)
print("\nDimensions of our Array:-",gfg.ndim)
print("\nDatatype of Array:-",gfg.dtype)
print("\nShape of Array:-",gfg.shape)
print("\n Converrting Hermite series to a polynomial",hermite.herm2poly(gfg))
