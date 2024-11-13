# Python program showing
# subtraction of two scalars

import theano
from theano import tensor

# Declaring variables
a = tensor.dscalar()
b = tensor.dscalar()

# Subtracting
res = a - b
# Converting it to a callable object
# so that it takes matrix as parameters
func = theano.function([a, b], res)

# Calling function
assert 20.0 == func(30.5, 10.5)








'''It will not provide any output as the assertion of two numbers matches the number given, 
hence it results into a true value.'''






