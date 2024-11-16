# Python program explaining
# numpy.char.rstrip() method

import numpy as geek

# input arrays
in_arr = geek.array([ 'GeeksG', 'ForG', 'Geeks'] )
print ("Input array : ", in_arr)

out_arr = geek.char.rstrip(in_arr, chars ='G')

# will strip 'G' from right side
# from each element(if exists)
print ("Output array: ", out_arr)
