# Python Program illustrating
# numpy.char.add() method
import numpy as np

arr1 = 'This is geeks '
arr2 = 'for geeks '

print ("\narr1 + arr2\n", np.char.add(arr1, arr2))
print ("\narr2 + arr1\n", np.char.add(arr2, arr1))
