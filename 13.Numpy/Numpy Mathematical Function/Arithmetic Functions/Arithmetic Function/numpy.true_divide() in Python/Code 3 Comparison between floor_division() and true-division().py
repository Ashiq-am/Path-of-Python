# Python program explaining
# true_divide() function
import numpy as np

# input_array
arr1 = np.arange(5)
arr2 = [2, 3, 4, 5, 6]
print ("arr1		 : ", arr1)
print ("arr1		 : ", arr2)

# output_array
out = np.floor_divide(arr1, arr2)
out_arr = np.true_divide(arr1, arr2)
print ("\nOutput array with floor divide : \n", out)
print ("\nOutput array with true divide : \n", out_arr)


print ("\nOutput array with floor divide(//) : \n", arr1//arr2)
print ("\nOutput array with true divide(/) : \n", arr1/arr2)
