# Python Program illustrating
# numpy.delete()

import numpy as geek

arr = geek.arange(5)
print("Original array : ", arr)
mask = geek.ones(len(arr), dtype=bool)

# Equivalent to np.delete(arr, [0,2,4], axis=0)
mask[[0,2]] = False
print("\nMask set as : ", mask)
result = arr[mask,...]
print("\nDeletion Using a Boolean Mask : ", result)
