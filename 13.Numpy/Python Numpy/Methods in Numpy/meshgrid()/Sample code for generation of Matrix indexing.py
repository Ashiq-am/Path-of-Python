# Sample code for generation of Matrix indexing
import numpy as np


x = np.linspace(-4, 4, 9)
# numpy.linspace creates an array
# of 9 linearly placed elements between
# -4 and 4, both inclusive
y = np.linspace(-5, 5, 11)

# The meshgrid function returns
# two 2-dimensional arrays
x_1, y_1 = np.meshgrid(x, y)


x_2, y_2 = np.meshgrid(x, y, indexing = 'ij')

# The following 2 lines check if x_2 and y_2 are the
# transposes of x_1 and y_1 respectively
print("x_2 = ")
print(x_2)
print("y_2 = ")
print(y_2)

# np.all is Boolean and operator;
# returns true if all holds true.
print(np.all(x_2 == x_1.T))
print(np.all(y_2 == y_1.T))






"""
The sparse = True can also be added in the meshgrid function of Matrix indexing. In this 
case, the shape of x_2 will change from (9, 11) to (9, 1) and that of y_2 will change from 
(9, 11) to (1, 11).

"""