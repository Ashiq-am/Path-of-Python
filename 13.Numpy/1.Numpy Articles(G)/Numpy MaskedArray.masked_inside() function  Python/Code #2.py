# Python program explaining
# numpy.MaskedArray.masked_inside() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([5e8, 3e-5, -45.0, 4e4, 5e2])
print ("Input array : ", in_arr)

# applying MaskedArray.masked_inside methods
# to input array in the range[5e2, 5e8]
mask_arr = ma.masked_inside(in_arr, 5e2, 5e8)
print ("Masked array : ", mask_arr)
