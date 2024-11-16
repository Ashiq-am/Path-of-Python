# Python Program illustrating
# numpy.char.multiply() method
import numpy as np

arr1 = ['eAAAa', 'ttttds', 'AAt']
arr2 = ['11sf', 'sdsf2', '1111f2']

print ("\narr1 : ", arr1)
print ("\narr2 : ", arr2)

print ("\narr1 : ", np.char.multiply(arr1, 2))

# Separate multiplication
print ("\narr1 : ", np.char.multiply(arr1, [2, 4, 3]))
print ("\narr2 : ", np.char.multiply(arr2, 3))
