import torch

# Define a tensor
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Define a hook function to modify gradients
def gradient_hook(grad):
    return grad * 2  # Modify gradients

# Register the tensor for a backward hook
hook_handle = tensor.register_hook(gradient_hook)

# Perform some operations involving the tensor
output = tensor.sum()

# Backward pass
output.backward()

# Remove the hook
hook_handle.remove()
