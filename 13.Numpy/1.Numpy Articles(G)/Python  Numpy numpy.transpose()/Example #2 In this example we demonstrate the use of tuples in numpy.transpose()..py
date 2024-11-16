# importing python module named numpy
import numpy as np

# making a 3x3 array
gfg = np.array([[1, 2],
				[4, 5],
				[7, 8]])

# before transpose
print(gfg, end ='\n\n')

# after transpose
print(gfg.transpose(1, 0))
