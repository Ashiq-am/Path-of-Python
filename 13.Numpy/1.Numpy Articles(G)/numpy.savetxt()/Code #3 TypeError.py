# Python program explaining
# savetxt() function

import numpy as geek

x = geek.arange(0, 10, 1)
y = geek.arange(0, 20, 1)
z = geek.arange(0, 30, 1)
print("x is:")
print(x)

print("y is:")
print(y)

print("z is:")
print(z)

# x, y, z are 3 numpy arrays without having same dimension
c = geek.savetxt('geekfile.txt', (x, y, z))
