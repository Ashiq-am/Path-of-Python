# stats.obrientransform() method
import numpy as np
from scipy import stats

arr1 = [20, 2, 7, 1, 34]
arr2 = [50, 12, 12, 34, 4]

print("arr1 : ", arr1)
print("\narr2 : ", arr2)

print("\n O Brien Transform : \n", stats.obrientransform(arr1, arr2))

transform_arr1, transform_arr2 = stats.obrientransform(arr1, arr2)

print("\n O Brien Transform of arr1: \n", transform_arr1)
print("\n O Brien Transform of arr2: \n", transform_arr2)
