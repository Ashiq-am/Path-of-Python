# import library
import numpy as np

# create 1d-array
a = np.array((1,2,3,4))

# create 1d-array
b = np.array((5,6,7,8))

# convert 1d-arrays into
# columns of 2d-array
c = np.column_stack((a, b))

print(c)
