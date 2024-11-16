# Python program explaining
# nonzero() function

import numpy as geek

arr = geek.array([[0, 8, 0], [7, 0, 0], [-5, 0, 1]])

print("Input array : \n", arr)

out_tpl = geek.nonzero(arr)
print("Indices of non zero elements : ", out_tpl)
