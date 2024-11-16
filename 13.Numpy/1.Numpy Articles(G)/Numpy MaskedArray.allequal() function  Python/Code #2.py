# importing numpy as geek
# and numpy.ma module as ma
import numpy as geek
import numpy.ma as ma

# creating 1st input array
in_arr1 = geek.array([2e8, 3e-5, -45.0])
print ("1st Input array : ", in_arr1)

# Now we are creating 1st masked array by making third entry as invalid.
mask_arr1 = ma.masked_array(in_arr1, mask =[0, 0, 1])
print ("1st Masked array : ", mask_arr1)

# creating 2nd input array
in_arr2 = geek.array([2e8, 3e-5, 15.0])
print ("2nd Input array : ", in_arr2)

# Now we are creating 2nd masked array by making third entry as invalid.
mask_arr2 = ma.masked_array(in_arr2, mask =[0, 0, 1])
print ("2nd Masked array : ", mask_arr2)
# applying MaskedArray.allequal method
out_arr = ma.allequal(mask_arr1, mask_arr2, fill_value = True)
print ("Output array : ", out_arr)
