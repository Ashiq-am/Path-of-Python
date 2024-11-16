# Python program explaining
# base_repr() function
import numpy as geek

in_arr = [5, -8, 21 ]

print ("Input array : ", in_arr)
print()

# binary representation of first array
# element without using padding parameter
out_num = geek.base_repr(in_arr[0], base = 2)
print("binary representation of 5")
print ("Without using padding parameter : ", out_num)

# binary representation of first array
# element using padding parameter
out_num = geek.base_repr(in_arr[0], base = 2, padding = 3)
print ("Using padding parameter: ", out_num)
print()

# octal representation of 2nd array
# element without using width parameter
out_num = geek.base_repr(in_arr[1], base = 8, padding = 0)
print("octal representation of -8")
print ("Without using padding parameter : ", out_num)

# octal representation of 2nd array
# element using padding parameter
out_num = geek.base_repr(in_arr[1], base = 8, padding = 4)
print ("Using padding parameter : ", out_num)
print()

# hexa-decimal representation of 3rd array
# element without using padding parameter
out_num = geek.base_repr(in_arr[2], base = 16, padding = 0)
print("hexa-decimal representation of 21")
print ("Without using padding parameter : ", out_num)

# hexa-decimal representation of 3rd array
# element using padding parameter
out_num = geek.base_repr(in_arr[2], base = 16, padding = 3)
print ("Using padding parameter : ", out_num)
