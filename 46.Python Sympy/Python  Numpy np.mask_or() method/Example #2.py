# import numpy and mask_or
import numpy as np

m1 = np.array([1, 0, 0, 1, 0])
m2 = np.array([0, 0, 1, 1, 0])

# using np.mask_or() method
gfg = np.ma.mask_or(m1, m2)

print(gfg)
