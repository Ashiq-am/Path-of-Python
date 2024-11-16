# Python program explaining
# numpy.MaskedArray.ravel() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([[1, 2], [3, -1]])
print("Input array : ", in_arr)

# Now we are creating a masked array.
# by making two entry as invalid.
mask_arr = ma.masked_array(in_arr, mask=[[0, 1], [1, 0]])
print("Masked array : ", mask_arr)

# applying MaskedArray.ravel methods to mask array
out_arr = mask_arr.ravel()
print("1D view of masked array : ", out_arr)
