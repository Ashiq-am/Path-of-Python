# Create two arrays to concatenate
array3 = np.array([[1, 2], [3, 4]])
array4 = np.array([[5, 6], [7, 8]])

# Concatenate arrays vertically
vertical_concat = np.vstack((array3, array4))
print("\nVertically concatenated array:\n", vertical_concat)

# Concatenate arrays horizontally
horizontal_concat = np.hstack((array3, array4))
print("\nHorizontally concatenated array:\n", horizontal_concat)