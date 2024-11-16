# Python program explaining
# numpy.MaskedArray.masked_where() method

# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating input array in_arr1
in_arr1 = geek.arange(4)
print ("1st Input array : ", in_arr1)

# applying MaskedArray.masked_where methods
# to input array in_arr1 where value = 1
mask_arr1 = ma.masked_where(in_arr1 == 1, in_arr1)
print ("1st Masked array : ", mask_arr1)

# creating input array in_arr2
in_arr2 = geek.arange(4)
print ("2nd Input array : ", in_arr2)

# applying MaskedArray.masked_where methods
# to input array in_arr2 where value = 1
mask_arr2 = ma.masked_where(in_arr2 == 3, in_arr2)
print ("2nd Masked array : ", mask_arr2)

# applying MaskedArray.masked_where methods
# to 1st masked array where second masked array
# is used as condition
res_arr = ma.masked_where(mask_arr1 == 3, mask_arr2)
print("Resultant Masked array : ", res_arr)
