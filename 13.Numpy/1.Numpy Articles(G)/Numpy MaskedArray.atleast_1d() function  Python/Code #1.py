# Python program explaining
# numpy.MaskedArray.atleast_1d() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input arrays
in_arr1 = geek.array([[1, 2], [3, -1], [5, -3]])
print("1st Input array : ", in_arr1)

in_arr2 = geek.array(2)
print("2nd Input array : ", in_arr2)

# Now we are creating masked array.
# by making entry as invalid.
mask_arr1 = ma.masked_array(in_arr1, mask=[[1, 0], [0, 1], [0, 0]])
print("1st Masked array : ", mask_arr1)

mask_arr2 = ma.masked_array(in_arr2, mask=0)
print("2nd Masked array : ", mask_arr2)

# applying MaskedArray.atleast_1d methods
# to masked array
out_arr = ma.atleast_1d(mask_arr1, mask_arr2)
print("Output masked array : ", out_arr)
