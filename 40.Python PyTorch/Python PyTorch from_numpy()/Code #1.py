# Importing the PyTorch library
import torch
import numpy

# A numpy array of size 6
a = numpy.array([1.0, -0.5, 3.4, -2.1, 0.0, -6.5])
print(a)

# Applying the from_numpy function and
# storing the resulting tensor in 't'
t = torch.from_numpy(a)
print(t)
