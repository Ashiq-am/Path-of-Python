# Python program explaining
# numpy.MaskedArray.argsort() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([5, -5, 0, -10, 2])
print ("Input array : ", in_arr)

# Now we are creating a masked array
# by making first third entry as invalid.
mask_arr = ma.masked_array(in_arr, mask =[1, 0, 1, 0, 0])
print ("Masked array : ", mask_arr)

# applying MaskedArray.argminmethods to mask array
# and filling the masked location by 1
out_arr = mask_arr.argsort(fill_value = 1)
print ("output array of indices: ", out_arr)
