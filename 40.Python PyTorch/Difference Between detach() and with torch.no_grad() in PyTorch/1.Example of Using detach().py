import torch

# Create a tensor with requires_grad=True
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Perform an operation
y = x * 2

# Detach y from the computational graph
y_detached = y.detach()

# Check requires_grad attribute
print(y.requires_grad)
print(y_detached.requires_grad)
