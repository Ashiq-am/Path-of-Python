# Python program explaining
# numpy.char.lstrip() method

import numpy as geek

# input arrays
in_arr = geek.array([ 'Geeks', 'For', 'Geeks'] )
print ("Input array : ", in_arr)

out_arr = geek.char.lstrip(in_arr, chars ='s')
print ("Output array: ", out_arr)
# Arrays remain unchanged as there are
# no strings which start with 's'
