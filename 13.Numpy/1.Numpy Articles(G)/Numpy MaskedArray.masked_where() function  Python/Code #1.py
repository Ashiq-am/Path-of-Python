# Python program explaining
# numpy.MaskedArray.masked_where() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([1, 2, 3, -1, 2])
print ("Input array : ", in_arr)

# applying MaskedArray.masked_where methods
# to input array where value<= 1
mask_arr = ma.masked_where(in_arr<= 1, in_arr)
print ("Masked array : ", mask_arr)
