import numpy as np

arr1 = np.arange(5)
print("Initial arr1 : ", arr1)

# using out parameter
np.nanmax(arr, axis = 0, out = arr1)

print("Changed arr1(having results) : ", arr1)
