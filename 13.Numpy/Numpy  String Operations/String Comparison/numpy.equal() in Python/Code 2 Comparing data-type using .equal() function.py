# Python Program illustrating
# numpy.equal() method
import numpy as geek

# Here we will compare Complex values with int
a = geek.array([0 + 1j, 2])
b = geek.array([1,2])

d = geek.equal(a, b)
print("Comparing complex with int using .equal() : ", d)
