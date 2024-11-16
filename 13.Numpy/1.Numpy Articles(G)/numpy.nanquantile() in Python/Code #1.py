# Python Program illustrating
# numpy.nanquantile() method
import numpy as np

# 1D array
arr = [20, 2, 7, np.nan, 34]
print("arr : ", arr)

print("\n-Q1 quantile of arr : ", np.quantile(arr, .50))
print("Q2 - quantile of arr : ", np.quantile(arr, .25))
print("Q3 - quantile of arr : ", np.quantile(arr, .75))

print("\nQ1 - nanquantile of arr : ", np.nanquantile(arr, .50))
print("Q2 - nanquantile of arr : ", np.nanquantile(arr, .25))
print("Q3 - nanquantile of arr : ", np.nanquantile(arr, .75))
