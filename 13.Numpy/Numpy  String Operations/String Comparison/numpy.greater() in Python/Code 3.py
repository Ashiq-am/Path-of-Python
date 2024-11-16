# Python Program illustrating
# numpy.greater() method

import numpy as geek

# Here we will compare Complex values with int
a = geek.array([1j, 2])
b = geek.array([1, 2])

# indicating 1j is greater than 1
print("Comparing complex with int : ", a < b)

# indicating 1j is greater than 1
d = geek.greater(a, b)
print("\nComparing complex with int using .greater() : ", d)
