# Python Program illustrating
# numpy.char.add() method
import numpy as np

arr1 = ['vdteteAAAa', 'AAAttttds', 'AAaxtt']
arr2 = ['1111sfdsf', '1111111sdsf2', '1111111sfsf2']

print ("\narr1 : ", arr1)
print ("\narr2 : ", arr2)

print ("\narr1 + arr2\n", np.char.add(arr1, arr2))
print ("\narr2 + arr1\n", np.char.add(arr2, arr1))
