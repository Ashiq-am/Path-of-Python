# Python program explaining
# numpy.MaskedArray.argsort() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([4, 2, 3, -1, 5])
print ("Input array : ", in_arr)

# Now we are creating a masked array
# by making third entry as invalid.
mask_arr = ma.masked_array(in_arr, mask =[0, 0, 1, 0, 0])
print ("Masked array : ", mask_arr)

# applying MaskedArray.argsort methods to mask array
out_arr = mask_arr.argsort()
print ("output array of indices: ", out_arr)
