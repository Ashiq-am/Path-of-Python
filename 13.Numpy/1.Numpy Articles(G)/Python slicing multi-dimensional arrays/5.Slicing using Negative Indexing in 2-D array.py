import numpy as np

# Create a 3-D NumPy array
array_3d = np.array([
	[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
	[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
	[[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])

# Display the original array
print("Original 3-D Array:")
print(array_3d)

# Slice the last row from each 2-D matrix
sliced_array = array_3d[:, :, -1]

# Display the sliced array
print("\nSliced 3-D Array (Last Row from Each 2-D Matrix):")
print(sliced_array)
