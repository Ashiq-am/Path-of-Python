# Python program explaining
# numpy.MaskedArray.default_fill_value() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array
in_arr = geek.array([[1 + 2j, 2 + 3j],
                     [3 - 2j, -1 + 2j],
                     [5 - 4j, -3 - 3j]])
print("Input array : ", in_arr)

# Now we are creating a masked array.
# by making two entry as invalid.
mask_arr = ma.masked_array(in_arr,
                           mask=[[1, 0], [1, 0], [0, 0]])

print("Masked array : ", mask_arr)

# applying MaskedArray.default_fill_value
# methods to masked array
out_val = ma.default_fill_value(mask_arr)
print("Default filled value : ", out_val)
