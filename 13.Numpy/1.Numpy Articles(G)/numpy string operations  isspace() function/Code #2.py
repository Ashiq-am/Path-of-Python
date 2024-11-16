# Python program explaining
# numpy.char.isspace() method

import numpy as geek

# input arrays containing string along with space
in_arr = geek.array([ 'Geeks\nfor\ngeeks', 'Code\tchef'] )
print ("Input array : ", in_arr)

out_arr = geek.char.isspace(in_arr)
print ("Output array: ", out_arr)
