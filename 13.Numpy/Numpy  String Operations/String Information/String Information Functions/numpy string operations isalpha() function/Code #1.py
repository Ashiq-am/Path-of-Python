# Python program explaining
# numpy.char.isalpha() method

import numpy as geek

# input array
in_arr = geek.array([ 'abcd', 'ac1bd', 'abdc', 'dcba', 'ab cd'] )
print ("Input array : ", in_arr)

out_arr = geek.char.isalpha(in_arr)
print ("Output array: ", out_arr)
