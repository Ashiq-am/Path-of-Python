# Python Program illustrating
# numpy.nanpercentile() method

import numpy as np

# 1D array
arr = [20, 2, 7, np.nan, 34]
print("arr : ", arr)
print("30th percentile of arr : ",
      np.percentile(arr, 50))
print("25th percentile of arr : ",
      np.percentile(arr, 25))
print("75th percentile of arr : ",
      np.percentile(arr, 75))

print("\n30th percentile of arr : ",
      np.nanpercentile(arr, 50))
print("25th percentile of arr : ",
      np.nanpercentile(arr, 25))
print("75th percentile of arr : ",
      np.nanpercentile(arr, 75))
