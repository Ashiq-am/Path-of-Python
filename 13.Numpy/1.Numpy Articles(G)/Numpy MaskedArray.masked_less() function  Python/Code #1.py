# Python program explaining
# numpy.MaskedArray.masked_less() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([1, 2, 3, -1, 2])
print ("Input array : ", in_arr)

# applying MaskedArray.masked_less methods
# to input array where value<2
mask_arr = ma.masked_less(in_arr, 2)
print ("Masked array : ", mask_arr)
