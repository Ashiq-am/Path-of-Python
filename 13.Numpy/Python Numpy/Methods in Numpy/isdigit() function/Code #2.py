# Python program explaining
# numpy.char.isdigit() method

import numpy as geek

# input array contains digits along with space and alphabets
in_arr = geek.array([ '1000 2', 'a1000', '1234 ab'] )
print ("Input array : ", in_arr)

out_arr = geek.char.isdigit(in_arr)
print ("Output array: ", out_arr)
