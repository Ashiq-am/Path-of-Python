# Python program explaining
# numpy.MaskedArray.astype() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([1, 2, 3, -1, 5])
print ("Input array : ", in_arr)

# Now we are creating a masked array of int32
# and making third entry as invalid.
mask_arr = ma.masked_array(in_arr, mask =[0, 0, 1, 0, 0])
print ("Masked array : ", mask_arr)

# printing the data type of masked aaray
print(mask_arr.dtype)

# applying MaskedArray.astype methods to mask array
# and converting it to float64
out_arr = mask_arr.astype('float64')
print ("Output typecasted array : ", out_arr)

# printing the data type of typecasted masked aaray
print(out_arr.dtype)
