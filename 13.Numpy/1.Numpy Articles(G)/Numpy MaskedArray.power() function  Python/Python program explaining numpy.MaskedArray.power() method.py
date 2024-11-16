# Python program explaining
# numpy.MaskedArray.power() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating base array
base_arr = geek.array([0, 1, 2, 3, 4, 5])
print("Input base array : ", base_arr)

# Now we are creating a base masked array.
# by making one entry as invalid.
base_mask_arr = ma.masked_array(base_arr, mask=[0, 0, 0, 0, 1, 0])
print("Base Masked array : ", base_mask_arr)

# creating exponent array
exp_arr = geek.array([0, 2, 1, 4, 2, 3])
print("Input exponent array : ", exp_arr)

# Now we are creating a exponent masked array.
# by making one entry as invalid.
exp_mask_arr = ma.masked_array(exp_arr, mask=[0, 1, 0, 0, 1, 0])
print("Exponent Masked array : ", exp_mask_arr)

# applying MaskedArray.power methods
# to masked array
out_arr = ma.power(base_mask_arr, exp_mask_arr)
print("Output masked array : ", out_arr)
