import numpy as np
arr = np.array([4, 1, 5, 7])

sorted_indices = arr.argsort()
sorted_indices_descending = (-1*arr).argsort()

sorted_elements= arr[sorted_indices_descending]

print("Sorted Indices (Descending):",sorted_indices_descending)
print("Sorted Elements (Descending):",sorted_elements)
