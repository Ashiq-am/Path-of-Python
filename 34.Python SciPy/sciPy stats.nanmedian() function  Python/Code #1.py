# median
import scipy
import numpy as np

arr1 = [1, 3, np.nan, 27, 2, 5]

print("median using nanmedian :", scipy.nanmedian(arr1))

print("median without handling nan value :", scipy.median(arr1))
