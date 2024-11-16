# import numpy
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
# using np.coords() method
gfg = a.flat
next(gfg)
next(gfg)
next(gfg)
next(gfg)
print(gfg.coords)
