import numpy as geek

# Defining the array
x = geek.arange(35).reshape(7, 5)

# Performing Boolean Indexing
mask_array = x[:, 0] < 10
print(x[mask_array])
