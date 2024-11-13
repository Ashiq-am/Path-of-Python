import torch

# create 2D tensor with 3 elements each
t1 = torch.tensor([[-20, 34, 56, ], [78, 90, 8]])

# display
print(t1)

# Compute the logistic sigmoid
# function of elements in the
# above tensor
print(torch.special.expit(t1))
