# Python3 program explaining
# arctan2() function

import numpy as np

arr1 = [-1, +1, +1, -1]
arr2 = [-1, -1, +1, +1]

ans = np.arctan2(arr2, arr1) * 180 / np.pi

print ("x-coordinates : ", arr1)
print ("y-coordinates : ", arr2)

print ("\narctan2 values : \n", ans)
