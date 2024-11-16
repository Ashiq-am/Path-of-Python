import numpy as np

arr = np.array([8, 4, 10, 3, 6])

# get the indices that sort the array in ascending order
sorted_indices = np.argsort(arr)

# reversing the order of elements
sorted_indices_descending = np.flip(sorted_indices)

# get the elements corresponding to sorted indices in descending order
sorted_elements = arr[sorted_indices_descending]

print("Sorted Indices (Descending):",sorted_indices_descending)
print("Sorted Elements (Descending):",sorted_elements)
