# Python program explaining
# numpy.MaskedArray.resize() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([[[2e8, 3e-5]], [[-4e-6, 2e5]]])
print("Input array : ", in_arr)

# Now we are creating a masked array.
# by making one entry as invalid.
mask_arr = ma.masked_array(in_arr, mask=[[[1, 0]], [[0, 0]]])
print("Masked array : ", mask_arr)

# applying MaskedArray.resize methods to make
# it a 1 * 6 masked array
out_arr = ma.resize(mask_arr, (1, 6))
print("Output resized masked array : ", out_arr)
