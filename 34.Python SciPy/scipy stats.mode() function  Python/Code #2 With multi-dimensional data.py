# Arithmetic mode
from scipy import stats
import numpy as np

arr1 = [[1, 3, 27],
        [3, 4, 6],
        [7, 6, 3],
        [3, 6, 8]]

print("Arithmetic mode is : \n", stats.mode(arr1))

print("\nArithmetic mode is : \n", stats.mode(arr1, axis=None))

print("\nArithmetic mode is : \n", stats.mode(arr1, axis=0))

print("\nArithmetic mode is : \n", stats.mode(arr1, axis=1))
