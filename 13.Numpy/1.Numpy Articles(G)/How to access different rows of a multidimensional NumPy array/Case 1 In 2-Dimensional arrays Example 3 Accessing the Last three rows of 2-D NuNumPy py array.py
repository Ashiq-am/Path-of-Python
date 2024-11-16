# Importing Numpy module
import numpy as np

# Creating a 4X4 2-D Numpy array
arr = np.array([[1, 20, 3, 1],
				[40, 5, 66, 7],
				[70, 88, 9, 11],
			[80, 100, 50, 77]])

print("Given Array :")
print(arr)

# Access the Last three rows of array
res_arr = arr[[1,2,3]]
print("\nAccessed Rows :")
print(res_arr)
