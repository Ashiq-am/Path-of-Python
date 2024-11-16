# Python program explaining
# load() function

import numpy as geek

a = geek.array(([i + j for i in range(3)
					for j in range(3)]))
# a is printed.
print("a is:")
print(a)

geek.save('geekfile', a)
print("the array is saved in the file geekfile.npy")

# the array is saved in the file geekfile.npy
b = geek.load('geekfile.npy')

# the array is loaded into b
print("b is:")
print(b)

# b is printed from geekfile.npy
print("b is printed from geekfile.npy")
