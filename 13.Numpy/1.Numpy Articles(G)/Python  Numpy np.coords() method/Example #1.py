# import numpy
import numpy as np

a = np.array([1, 2, 3])
# using np.coords() method
gfg = a.flat
next(gfg)
print(gfg.coords)
