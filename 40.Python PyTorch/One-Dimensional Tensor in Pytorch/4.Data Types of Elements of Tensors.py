# importing torch module
import torch

# create one dimensional tensor with integer type elements
a = torch.tensor([10, 20, 30, 40, 50])

# get data type of vector a
print(a.dtype)

# create one dimensional tensor with float type elements
b = torch.tensor([10.12, 20.56, 30.00, 40.3, 50.4])

# get data type of vector b
print(b.dtype)
