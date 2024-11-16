# Python Program illustrating
# numpy.iscomplexobj() method
import numpy as geek

# Returns True/False value for each element
a = geek.arange(20).reshape(5, 4)
print("Is complex : \n", geek.iscomplexobj(a))

# Returns True/False value as ans
# because we have mentioned dtpe in the begining
b = geek.arange(20).reshape(5, 4).dtype = complex

print("\n", b)
print("\nIs complex : ", geek.iscomplexobj(b))

b = [[1j],
     [3]]
print("\nIs complex : \n", geek.iscomplexobj(b))
