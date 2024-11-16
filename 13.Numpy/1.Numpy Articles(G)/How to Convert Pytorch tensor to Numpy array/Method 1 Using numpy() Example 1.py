# importing torch module
import torch

# import numpy module
import numpy

# create one dimensional tensor with
# float type elements
b = torch.tensor([10.12, 20.56, 30.00, 40.3, 50.4])

print(b)

# convert this into numpy array using
# numpy() method
b = b.numpy()

# display
b
