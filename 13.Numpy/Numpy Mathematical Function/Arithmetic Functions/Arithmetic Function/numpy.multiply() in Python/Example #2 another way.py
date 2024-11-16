import numpy as geek

in_arr1 = geek.matrix([[2, -7, 5], [-6, 2, 0]])
in_arr2 = geek.matrix([[0, -7, 8], [5, -2, 9]])

print("1st Input array : ", in_arr1)
print("2nd Input array : ", in_arr2)

out_arr = geek.array(in_arr1) * geek.array(in_arr2)
print("Resultant output array: ", out_arr)
