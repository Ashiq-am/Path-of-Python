# Import all the methods from sympy
from sympy import *

# Make a matrix
gfg_mat = Matrix([[1, 2], [2, 1]])

# use the row_insert() method for matrix
new_mat = gfg_mat.row_insert(2, Matrix([[13, 24]]))

print(new_mat)
