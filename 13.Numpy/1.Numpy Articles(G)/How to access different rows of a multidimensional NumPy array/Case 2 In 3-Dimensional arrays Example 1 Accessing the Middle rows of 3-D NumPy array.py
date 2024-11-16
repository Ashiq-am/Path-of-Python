# Importing Numpy module
import numpy as np

# Creating 3-D Numpy array
n_arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]],
				[[50, 65, 8], [70, 85, 10], [11, 22, 33]]])

print("Given 3-D Array:")
print(n_arr)

# Access the Middle rows of 3-D array
res_arr = n_arr[:,[1]]
print("\nAccessed Rows :")
print(res_arr)
