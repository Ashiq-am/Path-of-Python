# median
from scipy import median
from scipy import nanmedian
import numpy as np

arr1 = [[1, 3, 27],
		[3, np.nan, 6],
		[np.nan, 6, 3],
		[3, 6, np.nan]]

print("median is :", median(arr1))
print("median handling nan :", nanmedian(arr1))

# using axis = 0
print("\nmedian is with default axis = 0 : \n",
	median(arr1, axis = 0))
print("\nmedian handling nan with default axis = 0 : \n",
	nanmedian(arr1, axis = 0))

# using axis = 1
print("\nmedian is with default axis = 1 : \n",
	median(arr1, axis = 1))
print("\nmedian handling nan with default axis = 1 : \n",
	nanmedian(arr1, axis = 1))
