# Python program explaining
# numpy.MaskedArray.conjugate() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([[1 + 2j, 2 + 3j], [3 - 2j, -1 + 2j], [5 - 4j, -3 - 3j]])
print("Input array : ", in_arr)

# Now we are creating a masked array.
# by making two entry as invalid.
mask_arr = ma.masked_array(in_arr, mask=[[1, 0], [1, 0], [0, 0]])
print("Masked array : ", mask_arr)

# applying MaskedArray.conjugate
# methods to masked array
out_arr = ma.conjugate(mask_arr)
print("conjugate of masked array : ", out_arr)
