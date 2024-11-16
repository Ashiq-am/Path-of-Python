import numpy as np

arr = np.array([2, 3, 4, 5, 3, 3, 5, 4, 7, 8, 3])

print('Numpy Array:')
print(arr)

# Count '3' in array
count = (arr == 3).sum()

print('Occurences of "3" in array: ', count)
