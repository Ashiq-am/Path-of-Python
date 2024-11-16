import numpy as np
import mxnet as mx

# Attempt to use MXNet with an incompatible version of NumPy
a = mx.nd.array([1, 2, 3])
print(a)
