# Python program explaining
# loadtxt() function
import numpy as geek

# StringIO behaves like a file object
from io import StringIO

c = StringIO("1, 2, 3\n4, 5, 6")
x, y, z = geek.loadtxt(c, delimiter =', ', usecols =(0, 1, 2),
												unpack = True)

print("x is: ", x)
print("y is: ", y)
print("z is: ", z)
