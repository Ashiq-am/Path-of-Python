import numpy as np


arry = np.array([1,3,5], dtype=np.float64)

# Size of the array
print(arry.size)

# Length of one array element in bytes,
print( arry.itemsize)

# Total bytes consumed by the elements
# of the array
print(arry.nbytes)
