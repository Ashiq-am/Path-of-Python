# Python program explaining
# load() function

import numpy as geek

# a and b are numpy arrays.
a = geek.array(([i + j for i in range(3)
					for j in range(3)]))
b = geek.array([i + 1 for i in range(3)])

# a and b are printed.
print("a is:")
print(a)
print("b is:")
print(b)

# a and b are stored in geekfile.npz
geek.savez('geekfile.npz', a = a, b = b)

print("a and b are stored in geekfile.npz")

# compressed file is loaded
c = geek.load('geekfile.npz')

print("after loading...")
print("a is:", c['a'])
print("b is:", c['b'])
