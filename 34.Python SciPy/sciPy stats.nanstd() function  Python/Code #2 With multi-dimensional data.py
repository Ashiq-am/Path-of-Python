# standard deviation
from scipy import std
from scipy import nanstd
import numpy as np

arr1 = [[1, 3, 27],
		[3, np.nan, 6],
		[np.nan, 6, 3],
		[3, 6, np.nan]]

print("standard deviation is :", std(arr1))
print("standard deviation handling nan :", nanstd(arr1))

# using axis = 0
print("\nstandard deviation is with default axis = 0 : \n",
	std(arr1, axis = 0))
print("\nstandard deviation handling nan with default axis = 0 : \n",
	nanstd(arr1, axis = 0))

# using axis = 1
print("\nstandard deviation is with default axis = 1 : \n",
	std(arr1, axis = 1))
print("\nstandard deviation handling nan with default axis = 1 : \n",
	nanstd(arr1, axis = 1))
