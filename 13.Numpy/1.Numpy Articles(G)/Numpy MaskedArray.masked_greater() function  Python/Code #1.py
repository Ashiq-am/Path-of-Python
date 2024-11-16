# Python program explaining
# numpy.MaskedArray.masked_greater() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([1, 2, 3, -1, 2])
print ("Input array : ", in_arr)

# applying MaskedArray.masked_greater methods
# to input array where value>2
mask_arr = ma.masked_greater(in_arr, 2)
print ("Masked array : ", mask_arr)
