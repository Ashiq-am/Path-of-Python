# Python Program illustrating
# working of diag_indices()

import numpy as geek

# Creates a 5 X 5 array and returns indices of
# main diagonal elements
d = geek.diag_indices(5)
print("Indices of diagnol elements as tuple : ")
print(d, "\n")

array = geek.arange(16).reshape(4,4)
print("Initial array : \n", array)

# Here we can manipulate diagonal elements
# by accessing the diagonal elements
d = geek.diag_indices(4)
array[d] = 25
print("\n New array : \n", array)
