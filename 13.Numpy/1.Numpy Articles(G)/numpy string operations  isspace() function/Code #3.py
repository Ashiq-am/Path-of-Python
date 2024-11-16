# Python program explaining
# numpy.char.isspace() method

import numpy as geek

# input arrays containing only white space
in_arr = geek.array([ '\n', '\t', ' ', '\n\t '] )
print ("Input array : ", in_arr)

out_arr = geek.char.isspace(in_arr)
print ("Output array: ", out_arr)
