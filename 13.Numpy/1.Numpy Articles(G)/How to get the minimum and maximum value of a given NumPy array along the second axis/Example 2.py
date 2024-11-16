# Import numpy library
import numpy as np

# Create a numpy array
arr = np.array([[10, 34, 45],
				[22, -3, 46],
				[33, 4, 6]])

print("Given array:\n",
	arr)

# find row-wise max values
rslt1 = np.amax(arr, 1)
print("\nMaximum value along the second axis:",
	rslt1)

# find row-wise min values
rslt2 = np.amin(arr, 1)
print("\nMinimum value along the second axis:",
	rslt2)
