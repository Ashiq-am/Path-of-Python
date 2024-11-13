import torch
import numpy

# create absolute lengths of 5 with float type
abs = torch.tensor([23, 45, 67, 54, 32], dtype=torch.float32)

# create 5 angles with float type
angle = torch.tensor([numpy.pi / 2, numpy.pi / 4, numpy.pi /
					3, numpy.pi / 5, 0], dtype=torch.float32)

# construct complex tensor
print(torch.polar(abs, angle))

# construct complex tensor and display
# the datatype
print(torch.polar(abs, angle).dtype)
