import numpy as np

# Create a 3D array of shape (3, 3, 3)
val_arr = np.arange(27).reshape(3, 3, 3)

# Create a 2D array of indices of shape (3, 3)
z_indices = np.array([[1, 0, 2],
                      [0, 0, 1],
                      [2, 0, 1]])

# Expand the dimensions of z_indices to match the dimensions of val_arr
z_indices_expanded = np.expand_dims(z_indices, axis=-1)

# Use take_along_axis to select the elements
result_arr = np.take_along_axis(val_arr, z_indices_expanded, axis=0)

# Squeeze the result to remove the extra dimension
result_arr = np.squeeze(result_arr, axis=-1)

print(result_arr)
