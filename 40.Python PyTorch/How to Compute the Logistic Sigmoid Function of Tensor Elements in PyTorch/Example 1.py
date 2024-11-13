import torch

# create 1D tensor with 6 elements
t1 = torch.arange(1, 13)

# display
print(t1)

# Compute the logistic sigmoid
# function of elements in the
# above tensor
print(torch.sigmoid(t1))
