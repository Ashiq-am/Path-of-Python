# Arithmetic Mean
from scipy import mean
from scipy import nanmean
import numpy as np

arr1 = [[1, 3, 27],
		[3, np.nan, 6],
		[np.nan, 6, 3],
		[3, 6, np.nan]]

print("Arithmetic Mean is :", mean(arr1))
print("Arithmetic Mean handling nan :", nanmean(arr1))

# using axis = 0
print("\nArithmetic Mean is with default axis = 0 : \n",
	mean(arr1, axis = 0))
print("\nArithmetic Mean handling nan with default axis = 0 : \n",
	nanmean(arr1, axis = 0))

# using axis = 1
print("\nArithmetic Mean is with default axis = 1 : \n",
	mean(arr1, axis = 1))
print("\nArithmetic Mean handling nan with default axis = 1 : \n",
	nanmean(arr1, axis = 1))
