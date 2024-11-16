# Importing Numpy module
import numpy as np

# Creating a 2-D Numpy array
n_arr = np.array([[45, 52, 10],
				[1, 5, 25],
				[50, 40, 81]])

print("Given array:")
print(n_arr)

print("\nReplace all elements of array which are less than or equal to 25 with Nan")

print("else with 1 ")
print(np.where(n_arr <= 25, np.nan, 1))
