# Python program explaining
# numpy.MaskedArray.any() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array

in_arr = geek.array([1, 20, 30, 40, 50])
print ("Input array : ", in_arr)

# Now we are creating a masked array by making
# all entry as invalid.
mask_arr = ma.masked_array(in_arr, mask ='True')
print ("Masked array : ", mask_arr)

# applying MaskedArray.any methods to mask array
out_arr = mask_arr.any()
print ("Output array : ", out_arr)
