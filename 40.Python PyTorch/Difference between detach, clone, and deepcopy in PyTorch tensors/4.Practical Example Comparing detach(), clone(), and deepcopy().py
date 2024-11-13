import torch
import copy

# Create an initial tensor
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Clone the tensor (with gradient tracking)
x_clone = x.clone()

# Detach the tensor (no gradient tracking)
x_detached = x.detach()

# Deepcopy the tensor (independent copy, with gradient tracking)
x_deepcopy = copy.deepcopy(x)

# Perform operations on all
y_original = x ** 2
y_clone = x_clone ** 2
y_detached = x_detached ** 2
y_deepcopy = x_deepcopy ** 2

# Backpropagate on original, clone, and deepcopy (not detached)
y_original.sum().backward()
y_clone.sum().backward()
y_deepcopy.sum().backward()

# Display gradients
print("Original tensor gradient:", x.grad)  # Gradients from y_original
print("Cloned tensor gradient:", x_clone.grad)  # Gradients from y_clone
print("Detached tensor gradient:", x_detached.requires_grad)  # No gradient tracking
print("Deepcopied tensor gradient:", x_deepcopy.grad)  # Gradients from y_deepcopy
