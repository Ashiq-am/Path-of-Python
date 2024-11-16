# Python Program illustrating
# numpy.char.index() method
import numpy as np

arr = ['this is geeks for geek']

print ("\nindex of 'geeks' : ", np.char.index(arr, 'geeks', start = 2))
print ("\nindex of 'geeks' : ", np.char.index(arr, 'geeks', start = 10))
print ("\nindex of 'geek' : ", np.char.index(arr, 'geek', start = 10))
