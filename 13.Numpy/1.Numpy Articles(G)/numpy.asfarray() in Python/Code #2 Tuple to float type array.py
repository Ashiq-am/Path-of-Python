# Python program explaining
# numpy.asfarray() function

import numpy as geek

my_tuple = ([1, 3, 9], [8, 2, 6])

print("Input touple : ", my_tuple)

out_arr = geek.asfarray(my_tuple, dtype='int8')
print("output float type array from input touple : ", out_arr)
