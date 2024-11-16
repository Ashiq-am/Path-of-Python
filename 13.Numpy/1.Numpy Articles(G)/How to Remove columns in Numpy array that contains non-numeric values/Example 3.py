# Importing Numpy module
import numpy as np

# Creating 5X3 2-D Numpy array
n_arr = np.array([[10.5, 22.5, 3.8],
				[23.45, 50, 78.7],
				[41, np.nan, np.nan],
				[20, 50.20, np.nan],
				[18.8, 50.60, 8.8]])

print("Given array:")
print(n_arr)

print("\nRemove all columns containing non-numeric elements ")
print(n_arr[:, ~np.isnan(n_arr).any(axis=0)])
