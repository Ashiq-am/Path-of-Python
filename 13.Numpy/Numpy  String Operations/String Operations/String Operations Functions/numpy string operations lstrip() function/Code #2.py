# Python program explaining
# numpy.char.lstrip() method

import numpy as geek

# input arrays
in_arr = geek.array([ 'Geeks', 'For', 'Geeks'] )
print ("Input array : ", in_arr)

out_arr = geek.char.lstrip(in_arr, chars ='G')

# 'G' removed from arr[0] and arr[2]
# as we have set chars ='G'
print ("Output array: ", out_arr)
