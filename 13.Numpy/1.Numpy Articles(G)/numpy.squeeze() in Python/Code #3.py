# Python program explaining
# numpy.squeeze function
# when value error occurs
import numpy as geek

in_arr = geek.arange(9).reshape(1, 3, 3)

print ("Input array : ", in_arr)
out_arr = geek.squeeze(in_arr, axis = 1)

print ("output array : ", out_arr)
print("The shapes of Input and Output array : ")

print(in_arr.shape, out_arr.shape)
