import numpy as np

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Reshape the 2D array into a 3D array with shape (2, 2, 3)
array_3d = array_2d.reshape((2, 2, 3))

print("Original 2D array:")
print(array_2d)
print("\nReshaped 3D array:")
print(array_3d)
