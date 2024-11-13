# Arithmetic mode
from scipy import stats
import numpy as np

arr1 = np.array([[1, 3, 27, 13, 21, 9],
				[8, 12, 8, 4, 7, 10]])


print("Arithmetic mode is : \n", stats.mode(arr1))
