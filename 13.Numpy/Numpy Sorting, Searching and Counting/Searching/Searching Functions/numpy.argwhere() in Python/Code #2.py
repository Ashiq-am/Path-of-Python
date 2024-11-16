# Python program explaining
# argwhere() function

import numpy as geek

# input array
in_arr = geek.arange(8).reshape(4, 2)
print ("Input array : ", in_arr)

out_arr = geek.argwhere(in_arr>4)
print ("Output indices greater than 4: \n", out_arr)
