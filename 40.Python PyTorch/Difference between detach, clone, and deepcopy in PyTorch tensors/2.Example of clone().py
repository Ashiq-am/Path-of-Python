# Create a tensor with requires_grad=True
x = torch.tensor([2.0, 3.0], requires_grad=True)

# Clone the tensor
x_clone = x.clone()

# Perform operations on both the original and cloned tensors
y = x ** 2
z = x_clone ** 3

# Backpropagate both operations
y.sum().backward()
z.sum().backward()

print("Original tensor gradient:", x.grad)  # Gradients from both y and z
print("Cloned tensor gradient:", x_clone.grad)  # Independent gradients for the cloned tensor
