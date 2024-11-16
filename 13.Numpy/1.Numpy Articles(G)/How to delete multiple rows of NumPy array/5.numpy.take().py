import numpy as geek

# Defining the array
x = geek.arange(35).reshape(7, 5)

# applying numpy.take() function
print(geek.take(x, [0, 2, 6], axis=0))
