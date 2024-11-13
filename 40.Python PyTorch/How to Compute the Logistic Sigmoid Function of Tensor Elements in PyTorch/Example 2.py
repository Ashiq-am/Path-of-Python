import torch

# create 1D tensor with 5 elements
t1 = torch.arange(1, 6)

# display
print(t1)

# Compute the logistic sigmoid
# function of elements in the
# above tensor
print(torch.special.expit(t1))
