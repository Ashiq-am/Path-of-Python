import torch

# Define tensors
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = 3*x + 2

# Compute gradients without altering .grad attribute
grads = torch.autograd.grad(outputs=y.sum(), inputs=x)

print("Gradients without accumulation:", grads)
