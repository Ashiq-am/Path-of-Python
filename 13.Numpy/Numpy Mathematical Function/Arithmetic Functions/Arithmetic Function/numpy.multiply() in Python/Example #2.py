''''''


"""The following code is also known as the Hadamard product which is nothing but the 
element-wise-product of the two matrices. It is the most commonly used product for those who 
are interested in Machine Learning or statistics."""




# Python program explaining
# numpy.multiply() function

import numpy as geek

in_arr1 = geek.array([[2, -7, 5], [-6, 2, 0]])
in_arr2 = geek.array([[0, -7, 8], [5, -2, 9]])

print("1st Input array : ", in_arr1)
print("2nd Input array : ", in_arr2)

out_arr = geek.multiply(in_arr1, in_arr2)
print("Resultant output array: ", out_arr)
