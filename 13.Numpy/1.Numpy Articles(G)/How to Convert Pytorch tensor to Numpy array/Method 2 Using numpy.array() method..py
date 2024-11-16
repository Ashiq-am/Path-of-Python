# importing torch module
import torch

# import numpy module
import numpy

# create two dimensional tensor with
# integer type elements
b = torch.tensor([[1, 2, 3, 4, 5], [3, 4, 5, 6, 7],
				[4, 5, 6, 7, 8]])

print(b)

# convert this into numpy array using
# numpy.array() method
b = numpy.array(b)

# display
b
