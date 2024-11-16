# Python program explaining
# binary_repr() function
import numpy as geek

in_arr = [5, -8]

print("Input array : ", in_arr)

# binary representation of first array
# element without using width parameter
out_num = geek.binary_repr(in_arr[0])
print("Binary representation of 5")
print("Without using width parameter : ", out_num)

# binary representation of first array
# element using width parameter
out_num = geek.binary_repr(in_arr[0], width=5)
print("Using width parameter: ", out_num)

print("\nBinary representation of -8")

# binary representation of 2nd array
# element without using width parameter
out_num = geek.binary_repr(in_arr[1])
print("Without using width parameter : ", out_num)

# binary representation of 2nd array
# element  using width parameter
out_num = geek.binary_repr(in_arr[1], width=5)
print("Using width parameter : ", out_num)
