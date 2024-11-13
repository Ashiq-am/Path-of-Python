# Create a sample input
input_tensor = torch.randn(1, 3, 32, 32)

# Forward pass with hooks
output = net(input_tensor)
