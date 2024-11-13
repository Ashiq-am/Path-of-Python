import torch
import torch.nn as nn

# Define a simple linear model
model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Sample input and target
input = torch.tensor([[1.0], [2.0]], requires_grad=True)
target = torch.tensor([[2.0], [4.0]])

# Forward pass
output = model(input)
loss = criterion(output, target)

# Backward pass
loss.backward()

# Optimizer step
optimizer.step()

print("Gradients after backward:", model.weight.grad)
