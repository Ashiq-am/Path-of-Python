# Python program illustrating
# copysign() method
import numpy as np

arr1 = [1, -23, +34, 11]
arr2 = [-1, 2, -3, -4]

print ("arr1 : ", arr1)
print ("arr2 : ", arr2)

print ("\nCheck sign of arr1 : ", np.signbit(arr1))
print ("\nCheck sign of arr2 : ", np.signbit(arr1))
print ("\nCheck for copysign : ", np.signbit(np.copysign(arr1, arr2)))
