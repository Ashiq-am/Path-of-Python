# Python Program illustrating
# numpy.inner() method

import numpy as geek

# 1D array
vector_a = geek.array([[1, 4], [5, 6]])
vector_b = geek.array([[2, 4], [5, 2]])

product = geek.inner(vector_a, vector_b)
print("inner Product : \n", product)

product = geek.inner(vector_b, vector_a)
print("\ninner Product : \n", product)
