import torch

# Create a tensor with requires_grad=True
x = torch.tensor(2.0, requires_grad=True)

# Disable gradient computation within the context manager
with torch.no_grad():
    y = x ** 2
    print(y.requires_grad)

# Gradient computation is enabled again outside the context manager
print(y.requires_grad)
