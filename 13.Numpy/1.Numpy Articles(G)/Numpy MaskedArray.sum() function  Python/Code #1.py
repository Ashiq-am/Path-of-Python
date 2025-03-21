# Python program explaining
# numpy.MaskedArray.sum() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([[1, 2], [3, -1], [5, -3]])
print("Input array : ", in_arr)

# Now we are creating a masked array.
# by making entry as invalid.
mask_arr = ma.masked_array(in_arr, mask=[[1, 0], [1, 0], [0, 0]])
print("Masked array : ", mask_arr)

# applying MaskedArray.sum
# methods to masked array
out_arr = ma.sum(mask_arr)
print("sum of masked array along default axis : ", out_arr)
