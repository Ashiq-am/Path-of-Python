# stats.zmap() method
import numpy as np
from scipy import stats

arr1 = [[20, 2, 7, 1, 34],
        [50, 12, 12, 34, 4]]

arr2 = [[50, 12, 12, 34, 4],
        [12, 11, 10, 34, 21]]

print("\narr1 : ", arr1)
print("\narr2 : ", arr2)

print("\nZ-score : \n", stats.zmap(arr1, arr2))
