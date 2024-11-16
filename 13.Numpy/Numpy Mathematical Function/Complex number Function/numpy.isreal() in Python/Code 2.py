# Python Program illustrating
# numpy.isreal() method

import numpy as geek

# Returns True/False value for each element
a = geek.arange(20).reshape(5, 4)
print("Is Real : \n", geek.isreal(a), "\n")

# Returns True/False value as ans
# because we have mentioned dtpe in the beginning
a = geek.arange(20).reshape(5, 4).dtype = float
print("\nIs Real : ", geek.isreal(a))
