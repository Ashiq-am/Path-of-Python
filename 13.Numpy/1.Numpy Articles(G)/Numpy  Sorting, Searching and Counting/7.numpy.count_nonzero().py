import numpy as np

# Counting the number of non-zero values in the entire array
a = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])

# Counting the number of non-zero values along axis 0 (column-wise)
b = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]], axis=0)

print("Number of nonzero values in the entire array is:", a)
print("Number of nonzero values along axis 0 is:", b)
