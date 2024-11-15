# Define tensors with requires_grad=True to track computation history
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

# Perform a computation
z = x**2 + y**3
print("Output tensor z:", z)

# Compute gradients
z.backward()
print("Gradient of x:", x.grad)
print("Gradient of y:", y.grad)
