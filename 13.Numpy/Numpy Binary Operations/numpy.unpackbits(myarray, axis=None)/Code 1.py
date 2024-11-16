# Python program explaining
# numpy.unpackbits() function

# importing numpy
import numpy as geek

# creating input array using
# array function
in_arr = geek.array([171, 16], dtype = geek.uint8)
print ("Input array : ", in_arr)

# unpacking elements of an array
# using unpackbits() function
out_arr = geek.unpackbits(in_arr)

print ("Output unpacked array : ", out_arr)
