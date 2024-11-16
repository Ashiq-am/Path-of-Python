# Python program explaining
# numpy.char.isdecimal() method

import numpy as geek

# input array contains digits along with space and alphabets
in_arr = geek.array([ '1000 2', 'a1000', '1234 ab'] )
print ("Input array : ", in_arr)

out_arr = geek.char.isdecimal(in_arr)
print ("Output array: ", out_arr)
