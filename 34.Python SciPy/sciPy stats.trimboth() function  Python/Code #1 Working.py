# stats.trimboth() method
import numpy as np
from scipy import stats

arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\narr1 : ", arr1)

print("\nclipped arr1 : \n", stats.trimboth(arr1, proportiontocut=.3))
print("\nclipped arr1 : \n", stats.trimboth(arr1, proportiontocut=.1))
