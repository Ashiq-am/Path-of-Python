# Python program explaining
# numpy.nancumsum() function

import numpy as geek

in_arr = geek.array([[2, 4, 6], [1, 3, geek.nan]])

print("Input array : ", in_arr)

out_sum = geek.nancumsum(in_arr)
print("cumulative sum of array elements: ", out_sum)
