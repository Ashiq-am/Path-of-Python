# Python program explaining
# loadtxt() function
import numpy as geek

# StringIO behaves like a file object
from io import StringIO

d = StringIO("M 21 72\nF 35 58")
e = geek.loadtxt(d, dtype ={'names': ('gender', 'age', 'weight'),
								'formats': ('S1', 'i4', 'f4')})

print(e)
