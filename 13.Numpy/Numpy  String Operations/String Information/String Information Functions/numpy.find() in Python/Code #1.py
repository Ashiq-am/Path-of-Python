# Python Program illustrating
# numpy.char.find() method
import numpy as np

arr = ['vdsdsttetteteAAAa', 'AAAAAAAaattttds', 'AAaaxxxxtt', 'AAaaXDSDdscz']

print ("arr : ", arr)

print ("\nfind of 'tt'", np.char.find(arr, 'tt'))
print ("find of 'tt'", np.char.find(arr, 'tt', start = 0))
print ("find of 'tt'", np.char.find(arr, 'tt', start = 8))
