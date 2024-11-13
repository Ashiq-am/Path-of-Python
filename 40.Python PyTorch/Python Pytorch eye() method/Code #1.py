# Importing the PyTorch library
import torch


# Applying the eye function and
# storing the resulting tensor in 'a'
a = torch.eye(3, 4)
print("a = ", a)

b = torch.eye(3, 3)
print("b = ", b)

c = torch.eye(5, 1)
print("c = ", c)
