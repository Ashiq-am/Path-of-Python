import numpy as geek

# Defining the array
x = geek.arange(35).reshape(7, 5)

print(geek.delete(x, slice(0, 3), axis=0))
