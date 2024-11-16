import numpy as geek

# Defining the array
x = geek.arange(35).reshape(7, 5)

print(geek.delete(x, [0, 1, 2], axis=0))
