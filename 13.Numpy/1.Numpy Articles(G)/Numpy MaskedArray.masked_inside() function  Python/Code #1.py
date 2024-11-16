# Python program explaining
# numpy.MaskedArray.masked_inside() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([1, 2, 3, -1, 2])
print ("Input array : ", in_arr)

# applying MaskedArray.masked_inside methods
# to input array in the range[-1, 1]
mask_arr = ma.masked_inside(in_arr, -1, 1)
print ("Masked array : ", mask_arr)
