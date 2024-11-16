# Import numpy library
import numpy as np

# Create a numpy array
arr = np.array([[0, 1],
				[2, 3]])

print("Given Array:\n",
	arr)

# find row-wise max values
rslt1 = np.amax(arr, 1)
print("\nMaximum Value:",
	rslt1)

# find row-wise min values
rslt2 = np.amin(arr, 1)
print("\nMinimum Value:",
	rslt2)
