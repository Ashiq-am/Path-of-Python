# Importing Numpy module
import numpy as np

# Creating 5X4 2-D Numpy array
n_arr = np.array([[10.5, 22.5, 3.8, 5],
				[23.45, 50, 78.7, 3.5],
				[41, np.nan, np.nan, 0],
				[20, 50.20, np.nan, 2.5],
				[18.8, 50.60, 8.8, 58.6]])

print("Given array:")
print(n_arr)

print("\nRemove all rows containing non-numeric elements")
print(n_arr[~np.isnan(n_arr).any(axis=1)])
