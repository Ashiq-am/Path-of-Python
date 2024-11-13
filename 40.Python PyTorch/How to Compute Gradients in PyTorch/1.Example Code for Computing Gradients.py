import torch

# Initialize tensor with gradient tracking
x = torch.tensor([2.0], requires_grad=True)

# Define the operation
y = x ** 2

# Compute gradients
y.backward()

# Print the gradient
print(x.grad)  # Output: tensor([4.0])
