import numpy as np
# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array:")
print(array_2d)

# Reshape the 2D array into a 3D array with shape (3, 3, 1)
array_3d = array_2d.reshape((3, 3, 1))
print("\nReshaped 3D array:")
print(array_3d)
