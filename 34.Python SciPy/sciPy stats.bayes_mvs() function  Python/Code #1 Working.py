# stats.bayes_mvs() method
import numpy as np
from scipy import stats

arr1 = [[20, 2, 7, 1, 34],
        [50, 12, 12, 34, 4]]

arr2 = [50, 12, 12, 34, 4]

print("\narr1 : ", arr1)
print("\narr2 : ", arr2)

mean, var, std = stats.bayes_mvs(arr1, 0.9)

print("\nMean of array1 : ", mean)
print("\nvar of array1 : ", var)
print("\nstd of array1 : ", std)

mean, var, std = stats.bayes_mvs(arr2, 0.5)

print("\nMean of array2 : ", mean)
print("\nvar of array2 : ", var)
print("\nstd of array2 : ", std)

