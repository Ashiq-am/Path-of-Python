# Python program explaining
# numpy.asscalar() function
import numpy as geek

in_list = [2 ]

# changing the list to size 1 array
arr = geek.array(in_list)

print ("Input array from list : ", arr)

# changing the array to scalar
scalar = geek.asscalar(arr)

print ("output scalar from input list : ", scalar)
