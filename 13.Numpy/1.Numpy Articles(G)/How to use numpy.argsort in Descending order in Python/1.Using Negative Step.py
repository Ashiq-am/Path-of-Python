import numpy as np
arr = np.array([5, 2, 8, 3, 6, 10])

# get the indices that would sort the array in ascending order
ascending_indices = arr.argsort() # [1 3 0 4 2 5]

# reverse the ascending indices to get descending indices
descending_indices = ascending_indices[::-1] # [5 2 4 0 3 1]

# use the descending indices to get the elements in descending order
sorted_elements_descending = arr[descending_indices] # [10 8 6 5 32]

print("Sorted Indices (Descending):", descending_indices)
print("Sorted Elements (Descending):", sorted_elements_descending)
