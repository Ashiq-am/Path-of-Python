import numpy as np

# Example 2D array
matrix = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
])

# Splitting the array along the horizontal axis (axis=1)
slices = np.split(matrix, [1, 2])

# Displaying the slices
for i, slice_arr in enumerate(slices):
	print(f"Slice {i + 1}:\n{slice_arr}\n")
