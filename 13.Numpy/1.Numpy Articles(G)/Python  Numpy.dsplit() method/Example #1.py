# import numpy
import numpy as np

# using Numpy.dsplit() method
gfg = np.array([[1, 2, 5],
				[3, 4, 10],
				[5, 6, 15],
				[7, 8, 20]])

gfg = gfg.reshape(1, 2, 6)
print(gfg)

gfg = np.dsplit(gfg, 2)
print(gfg)
