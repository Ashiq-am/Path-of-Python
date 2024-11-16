# Python program explaining
# numpy.MaskedArray.mean() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([[1, 0, 3], [4, 1, 6]])
print("Input array : ", in_arr)

# Now we are creating a masked array.
# by making one entry as invalid.
mask_arr = ma.masked_array(in_arr, mask=[[0, 0, 0], [0, 0, 1]])
print("Masked array : ", mask_arr)

# applying MaskedArray.mean methods
# to masked array
out_arr1 = mask_arr.mean(axis=0)
print("mean of masked array along 0 axis : ", out_arr1)

out_arr2 = mask_arr.mean(axis=1)
print("mean of masked array along 1 axis : ", out_arr2)
