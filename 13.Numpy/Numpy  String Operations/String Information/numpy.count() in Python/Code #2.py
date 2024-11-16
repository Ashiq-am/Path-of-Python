# Python Program illustrating
# numpy.char.count() method
import numpy as np

# 2D array
arr = ['vdsdsttetteteAAAa', 'AAAAAAAaattttds', 'AAaaxxxxtt', 'AAaaXDSDdscz']

print ("arr : ", arr)

print ("Count of 'Aa'", np.char.count(arr, 'Aa'))
print ("Count of 'Aa'", np.char.count(arr, 'Aa', start = 8))
