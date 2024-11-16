import numpy as np

# creating array
arr = np.array([2, 4, 6, 8, 10])

# assigning arr to nc
nc = arr

# both arr and nc have same id
print("id of arr", id(arr))
print("id of nc", id(nc))

# updating nc
nc[0]= 12

# printing the values
print("original array- ", arr)
print("assigned array- ", nc)
