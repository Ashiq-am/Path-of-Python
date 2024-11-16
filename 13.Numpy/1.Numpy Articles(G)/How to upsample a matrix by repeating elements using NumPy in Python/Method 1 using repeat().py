# importing required module
import numpy as np

# declaring an array
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# use the repeat function to upsample the array
print(np.repeat(a, 5, axis=1).repeat(3, axis=0))
