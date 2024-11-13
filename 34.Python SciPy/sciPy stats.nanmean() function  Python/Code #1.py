# Arithmetic Mean
import scipy
import numpy as np

arr1 = [1, 3, np.nan, 27]

print("Arithmetic Mean using nanmean :", scipy.nanmean(arr1))

print("Arithmetic Mean without handling nan value :", scipy.mean(arr1))
