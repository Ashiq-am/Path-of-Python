# Python Program illustrating
# numpy.char.encode() method
import numpy as np

arr1 = ['eAAAa', 'ttttds', 'AAtAAt']
arr2 = ['11sf', 'sdsf2', '1111f2']

# Printing the array
print ("\narr1 : ", arr1)
print ("\narr2 : ", arr2)

print ("\nEncoded arr1 : \n", np.char.encode(arr1, encoding ='cp037'))
print ("\nEncoded arr2 : \n", np.char.encode(arr2, encoding ='utf8'))
print ("\nEncoded arr2 : \n", np.char.encode(arr2, encoding ='utf8',
												errors = 'strict'))
