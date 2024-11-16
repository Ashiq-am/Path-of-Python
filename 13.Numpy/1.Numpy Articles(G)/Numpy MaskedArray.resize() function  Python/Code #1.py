# Python program explaining
# numpy.MaskedArray.resize() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array of 2 * 2
in_arr = geek.array([[10, 20], [-10, 40]])
print("Input array : ", in_arr)

# Now we are creating a masked array.
# by making one entry as invalid.
mask_arr = ma.masked_array(in_arr, mask=[[1, 0], [0, 0]])
print("Masked array : ", mask_arr)

# applying MaskedArray.resize methods to make
# it a 3 * 3 masked array
out_arr = ma.resize(mask_arr, (3, 3))
print("Output resized masked array : ", out_arr)
