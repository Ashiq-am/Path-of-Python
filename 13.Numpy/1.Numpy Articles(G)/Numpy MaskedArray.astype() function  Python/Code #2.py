# Python program explaining
# numpy.MaskedArray.astype() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([10.1, 20.2, 30.3, 40.4, 50.5], dtype ='float64')
print ("Input array : ", in_arr)

# Now we are creating a masked array by making
# first and third entry as invalid.
mask_arr = ma.masked_array(in_arr, mask =[1, 0, 1, 0, 0])
print ("Masked array : ", mask_arr)

# printing the data type of masked aaray
print(mask_arr.dtype)

# applying MaskedArray.astype methods to mask array
# and converting it to int32
out_arr = mask_arr.astype('int32')
print ("Output typecasted array : ", out_arr)

# printing the data type of typecasted masked aaray
print(out_arr.dtype)
