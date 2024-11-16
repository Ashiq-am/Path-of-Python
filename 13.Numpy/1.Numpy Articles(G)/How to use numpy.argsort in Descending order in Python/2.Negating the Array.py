import numpy as np
arr = np.array([8, 2, 5, 7, 10, 4])

# get the indices that would sort the array in ascending order
ascending_indices = arr.argsort()

# getting the indices that sort the array in descending order by negating the array and sorting it
descending_indices = (-arr).argsort()

# Use the descending indices to get the elements in descending order
sorted_elements_descending = arr[descending_indices]

print("Sorted Indices (Descending):",descending_indices)
print("Sorted Elements (Descending):",sorted_elements_descending)
