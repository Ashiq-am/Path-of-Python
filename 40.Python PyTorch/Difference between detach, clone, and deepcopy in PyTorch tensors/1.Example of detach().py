import torch

# Create a tensor with requires_grad=True to track computation
x = torch.tensor([2.0, 3.0], requires_grad=True)

# Perform some operations
y = x ** 2

# Detach y from the computational graph
y_detached = y.detach()

# Backpropagation will not affect y_detached
y.sum().backward()

print("Original tensor:", x.grad)  # Shows gradient
print("Detached tensor:", y_detached.requires_grad)  # False, as it no longer requires gradient
