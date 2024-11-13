# percentileofscore
from scipy import stats
import numpy as np

# 1D array
arr = [20, 2, 7, 1, 7, 7, 34]
print("arr : ", arr)

print ("\nPercetile of 7 : ", stats.percentileofscore(arr, 7))

print ("\nPercetile of 34 : ", stats.percentileofscore(arr, 34))

print ("\nPercetile of 2 : ", stats.percentileofscore(arr, 2))
