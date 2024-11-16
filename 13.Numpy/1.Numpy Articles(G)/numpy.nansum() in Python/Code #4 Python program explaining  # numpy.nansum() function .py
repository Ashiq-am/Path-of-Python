# Python program explaining
# numpy.nansum() function

import numpy as geek

in_arr1 = geek.array([2, -5, geek.nan, geek.inf])
in_arr2 = geek.array([1, 4, geek.inf, -geek.inf])

print("1st array elements: ", in_arr1)
print("2nd array elements: ", in_arr2)

out_sum1 = geek.nansum(in_arr1)
out_sum2 = geek.nansum(in_arr2)

print("sum of 1st array elements: ", out_sum1)
print("sum of 2nd array elements: ", out_sum2)
