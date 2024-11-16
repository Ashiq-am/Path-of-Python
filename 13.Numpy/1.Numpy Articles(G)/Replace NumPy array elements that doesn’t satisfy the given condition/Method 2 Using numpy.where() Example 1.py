# Importing Numpy module
import numpy as np

# Creating a 2-D Numpy array
n_arr = np.array([[45, 52, 10],
				[1, 5, 25]])

print("Given array:")
print(n_arr)

print("\nReplace all elements of array which are greater than or equal to 25 to 0")

print("else remains the same ")
print(np.where(n_arr >= 25, 0, n_arr))
