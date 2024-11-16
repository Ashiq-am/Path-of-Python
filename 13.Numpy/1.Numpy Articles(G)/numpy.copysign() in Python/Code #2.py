# Python program illustrating
# copysign() method
import numpy as np

arr1 = [1, -23, +34, 11]

print ("\nCheck sign of arr2 : ", np.signbit(arr1))
print ("\nCheck for copysign : ", np.signbit(np.copysign(arr1, -3)))
