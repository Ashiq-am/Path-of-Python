# Python program explaining
# numpy.MaskedArray.reshape() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([1, 2, 3, -1])
print("Input array : ", in_arr)

# Now we are creating a masked array.
# by making third entry as invalid.
mask_arr = ma.masked_array(in_arr, mask=[1, 0, 1, 0])
print("Masked array : ", mask_arr)

# applying MaskedArray.reshape methods to make
# it a 2d masked array
out_arr = mask_arr.reshape(2, 2)
print("Output 2D masked array : ", out_arr)
