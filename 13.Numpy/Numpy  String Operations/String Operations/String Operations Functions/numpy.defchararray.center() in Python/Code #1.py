# Python Program illustrating
# numpy.char.center() method
import numpy as np

arr1 = ['eAAAa', 'ttttds', 'AAtAAt']
print ("arr1 : ", arr1)

print ("\narr1 : ", np.char.center(arr1, 7, fillchar ='z'))
print ("\narr1 : ", np.char.center(arr1, [9, 9, 11],fillchar =['z', '1', '3']))

print ("\narr1 : ", np.char.center(arr1, 11, fillchar ='z'))
