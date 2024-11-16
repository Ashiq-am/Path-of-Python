# Python Program illustrating
# numpy.random.randn() method

import numpy as geek

# 3D Array
array = geek.random.randn(2, 2, 2)
print("3D Array filled with random values : \n", array);

# Multiplying values with 3
print("\nArray * 3 : \n", array * 3)

# Or we cab directly do so by
array = geek.random.randn(2, 2, 2) * 3 + 2
print("\nArray * 3 + 2 : \n", array);
