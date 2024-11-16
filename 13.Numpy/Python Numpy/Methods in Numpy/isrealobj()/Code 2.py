# Python Program illustrating
# numpy.isrealobj() method
import numpy as geek

# Returns True/False value for each element
a = geek.arange(20).reshape(5, 4)
print("Is real : ", geek.isrealobj(a))

# Returns True/False value as ans
# because we have mentioned dtpe in the beginning
b = geek.arange(20).reshape(5, 4).dtype = complex

print("\n", b)
print("\nIs real : ", geek.isrealobj(b))

b = [[1j],
     [3]]
print("\nIs real : ", geek.isrealobj(b))
