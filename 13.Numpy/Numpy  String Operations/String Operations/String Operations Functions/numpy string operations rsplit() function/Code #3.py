# Python program explaining
# numpy.char.rsplit() method

# importing numpy
import numpy as geek

# input array
in_arr = geek.array(['Num-py', 'Py-th-on', 'Pan-das'])
print ("Input array : ", in_arr)


# output array when maximum splitting
# of every array element is 1
out_arr = geek.char.rsplit(in_arr, sep ='-', maxsplit = 1)
print ("Output splitted array: ", out_arr)
