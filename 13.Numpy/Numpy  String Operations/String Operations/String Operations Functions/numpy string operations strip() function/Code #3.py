# Python program explaining
# numpy.char.strip() method

import numpy as geek

# input arrays
in_arr = geek.array([ 'Geeks', 'For', 'Geeks'] )
print ("Input array : ", in_arr)

out_arr = geek.char.strip(in_arr, chars ='G')

#'G' removed from arr[0] and arr[2]
# as we have set chars ='G'
print ("Output array: ", out_arr)
