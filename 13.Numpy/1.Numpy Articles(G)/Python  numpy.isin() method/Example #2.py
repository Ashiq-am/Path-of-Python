# import numpy
import numpy as np

# using numpy.isin() method
gfg1 = np.array([[1, 3], [5, 7], [9, 11]])
lis = [1, 3, 11, 9]
gfg = np.isin(gfg1, lis)

print(gfg)
