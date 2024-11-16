import numpy as np

# creating array
arr = np.array([2, 4, 6, 8, 10])

# creating copy of array
c = arr.copy()

# both arr and c have different id
print("id of arr", id(arr))
print("id of c", id(c))

# changing original array
# this will not effect copy
arr[0] = 12

# printing array and copy
print("original array- ", arr)
print("copy- ", c)
