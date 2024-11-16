import numpy as np

# Create a 3D array of shape (3, 3, 3)
val_arr = np.arange(27).reshape(3, 3, 3)

# Create a 2D array of indices of shape (3, 3)
z_indices = np.array([[1, 0, 2],
                      [0, 0, 1],
                      [2, 0, 1]])
