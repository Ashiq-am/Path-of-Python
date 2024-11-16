# Importing Numpy module
import numpy as np

# Creating a 3-D Numpy array
n_arr = np.array([[[11, 25.5, 70.6], [30.9, 45.5, 55.9], [20.7, 45.8, 7.1]],
				[[50.1, 65.9, 8.2], [70.4, 85.8, 10.3], [11.3, 22.2, 33.6]],
				[[19.9, 69.7, 36.8], [1.2, 5.1, 24.4], [4.9, 20.8, 96.7]]])

print("Given array:")
print(n_arr)

print("\nReplace all elements of array which are less than 10 to Nan")
n_arr[n_arr < 10.] = np.nan

print("New array :\n")
print(n_arr)
