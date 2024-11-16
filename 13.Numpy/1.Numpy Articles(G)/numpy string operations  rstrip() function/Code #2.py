# Python program explaining
# numpy.char.rstrip() method

import numpy as geek

# input arrays
in_arr = geek.array([ 'Geeks', 'For', 'Geeks'] )
print ("Input array : ", in_arr)

out_arr = geek.char.rstrip(in_arr, chars ='s')

#'s' removed from arr[0] and
# arr[2] as we have set chars ='s'
print ("Output array: ", out_arr)
