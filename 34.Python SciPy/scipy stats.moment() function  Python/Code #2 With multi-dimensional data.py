# Moment
from scipy import stats
import numpy as np

arr1 = [[1, 3, 27],
		[3, 4, 6],
		[7, 6, 3],
		[3, 6, 8]]

print("Oth moment : \n", stats.moment(arr1, moment = 0))

print("\n6th moment : \n", stats.moment(arr1, moment = 6))

print("\n9th moment : \n", stats.moment(arr1, moment = 9, axis = None))

print("\n12th moment : \n", stats.moment(arr1, moment = 12, axis = 1))

print("\n10th moment : \n", stats.moment(arr1, moment = 10, axis = 1))
