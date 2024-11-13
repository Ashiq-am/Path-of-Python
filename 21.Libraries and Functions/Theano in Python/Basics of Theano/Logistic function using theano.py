# Python program to illustrate logistic
# sigmoid function using theano
# Load theano library

import theano
from theano import tensor

# Declaring variable
a = tensor.dmatrix('a')

# Sigmoid function
sig = 1 / (1 + tensor.exp(-a))

# Now it takes matrix as parameters
log = theano.function([a], sig)

# Calling function
print(log([[0, 1], [-1, -2]]))








'''Theano is a foundation library mainly used for deep learning research and development and directly to 
create deep learning models or by convenient libraries 
such as Keras.It supports both convolutional networks and recurrent networks, as well as combinations of the two.'''