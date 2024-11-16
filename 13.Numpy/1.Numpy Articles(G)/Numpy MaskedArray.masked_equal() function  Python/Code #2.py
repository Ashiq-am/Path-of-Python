# Python program explaining
# numpy.MaskedArray.masked_equal() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([2e8, 3e-5, -45.0, 2e5, 5e2])
print ("Input array : ", in_arr)

# applying MaskedArray.masked_equal methods
# to input array where value = 5e2
mask_arr = ma.masked_equal(in_arr, 5e2)
print ("Masked array : ", mask_arr)
