import torch
import numpy

# create absolute lengths of 2 with float type
abs = torch.tensor([3, 2], dtype=torch.float64)

# create 2 angles with float type
angle = torch.tensor([numpy.pi / 2, numpy.pi / 4],
					dtype=torch.double)

# construct complex tensor
print(torch.polar(abs, angle))

# construct complex tensor and display
# the datatype
print(torch.polar(abs, angle).dtype)
