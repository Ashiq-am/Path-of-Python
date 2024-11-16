# Python program explaining
# numpy.MaskedArray.masked_invalid() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array with invalid values
in_arr = geek.array([1, 2, geek.nan, -1, geek.inf])
print ("Input array : ", in_arr)

# applying MaskedArray.masked_invalid
# methods to input array
mask_arr = ma.masked_invalid(in_arr)
print ("Masked array : ", mask_arr)
