# Python Program illustrating
# numpy.char.count() method

import numpy as np

# 2D array
arr = ['vdsdsttetteteAAAa', 'AAAAAAAaattttds', 'AAaaxxxxtt', 'AAaaXDSDdscz']

print ("arr : ", arr)

print ("Count of 'tt'", np.char.count(arr, 'tt'))
print ("Count of 'tt'", np.char.count(arr, 'tt', start = 0))
print ("Count of 'tt'", np.char.count(arr, 'tt', start = 8))
