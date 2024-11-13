import torch
import torch.nn as nn
import torch.optim as optim

# Example model
model = nn.Linear(10, 1)
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dummy data
inputs = torch.randn(10)
targets = torch.randn(1)

# Forward pass
outputs = model(inputs)
loss = nn.MSELoss()(outputs, targets)

# Backward pass (without zeroing gradients)
loss.backward()

# Check gradients
print("Gradients after first backward pass:")
print(model.weight.grad)

# Perform another forward and backward pass
outputs = model(inputs)
loss = nn.MSELoss()(outputs, targets)
loss.backward(retain_graph=True)  # Retain the graph for another backward pass

# Check gradients again (they are accumulated)
print("Gradients after second backward pass (accumulated):")
print(model.weight.grad)

# Now reset gradients and do a backward pass again
optimizer.zero_grad()
loss.backward()
print("Gradients after resetting and third backward pass:")
print(model.weight.grad)
