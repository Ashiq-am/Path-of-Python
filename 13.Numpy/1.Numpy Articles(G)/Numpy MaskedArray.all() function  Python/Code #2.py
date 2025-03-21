# Python program explaining
# numpy.MaskedArray.all() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([1, 2, 3, -1, 5])
print ("Input array : ", in_arr)

# Now we are creating a masked array by
# making all entry as invalid.
mask_arr = ma.masked_array(in_arr, mask =[1, 1, 1, 1, 1])
print ("Masked array : ", mask_arr)

# applying MaskedArray.all methods to mask array
out_arr = mask_arr.all()
print ("Output array : ", out_arr)
