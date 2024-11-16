# Python Program illustrating
# numpy.vdot() method

import numpy as geek

# 1D array
vector_a = geek.array([[1, 4], [5, 6]])
vector_b = geek.array([[2, 4], [5, 2]])

product = geek.vdot(vector_a, vector_b)
print("Dot Product : ", product)

product = geek.vdot(vector_b, vector_a)
print("\nDot Product : ", product)

""" 
How Code 2 works : 
array is being flattened 

1 * 2 + 4 * 4 + 5 * 5 + 6 * 2 = 55 
"""
