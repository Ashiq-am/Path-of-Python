# import the torch module
import torch

# create real and img with float type
real = torch.tensor([78.2, 23.2], dtype=torch.float32)
img = torch.tensor([32, 41], dtype=torch.float32)

# create the complex number
t1 = torch.complex(real, img)

print(t1)

# get the inverse hyperbolic
# cosine values of the complex tensor.
print(torch.acosh(t1))
