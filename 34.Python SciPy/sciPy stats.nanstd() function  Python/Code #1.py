# standard deviation
import scipy
import numpy as np

arr1 = [1, 3, np.nan, 27]

print("standard deviation using nanstd :", scipy.nanstd(arr1))

print("standard deviation without handling nan value :", scipy.std(arr1))
