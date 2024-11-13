# Python program showing
# addition of two matrices

# Adding two matrices
import numpy
import theano.tensor as T
from theano import function
x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y
f = function([x, y], z)

f([[30, 50], [2, 3]], [[60, 70], [3, 4]])
