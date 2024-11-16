# Python program explaining
# logical_xor() function
import numpy as np

# input
arr1 = np.arange(8)
print ("arr1 : ", arr1)

print ("\narr1>3 : \n", arr1>3)
print ("\narr1<6 : \n", arr1<6)

print ("\nXOR Value : \n", np.logical_xor(arr1>3, arr1<6))
