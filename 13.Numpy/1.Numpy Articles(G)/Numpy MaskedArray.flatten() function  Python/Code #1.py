# Python program explaining
# numpy.MaskedArray.flatten() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array of 2 * 2
in_arr = geek.array([[10, 20], [-10, 40]])
print("Input array : ", in_arr)

# Now we are creating a masked array
# by making one entry as invalid.
mask_arr = ma.masked_array(in_arr, mask=[[1, 0], [0, 0]])
print("Masked array : ", mask_arr)

# applying MaskedArray.flatten methods to make
# it a 1D flattened array
out_arr = mask_arr.flatten()
print("Output flattened masked array : ", out_arr)
