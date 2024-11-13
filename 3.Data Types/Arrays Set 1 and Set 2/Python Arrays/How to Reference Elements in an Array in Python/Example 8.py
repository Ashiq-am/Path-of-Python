# Importing numpy module
import numpy as np

# Creating a 2d-numpy-array of elements
arr = np.array([[4, 6, 3],
				[5, 9, 2],
				[1, 8, 7]])

# Referring rows of the 2d-array
# by row index to new variables
first_row = arr[0]
second_row = arr[1]
third_row = arr[2]

# Print the variables
print("First Row =", first_row)
print("Second Row =", second_row)
print("Third Row =", third_row)
