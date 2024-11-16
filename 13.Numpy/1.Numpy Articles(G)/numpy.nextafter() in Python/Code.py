# Python program illustrating
# nextafter() method
import numpy as np

arr1 = 3
arr2 = 4

print ("arr1 : ", arr1)
print ("arr2 : ", arr2)

print ("\nCheck sign of arr1 : ", np.nextafter(arr1, arr2))
