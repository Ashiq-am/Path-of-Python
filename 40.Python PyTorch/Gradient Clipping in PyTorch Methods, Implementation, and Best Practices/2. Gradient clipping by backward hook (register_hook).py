import torch
import torch.nn as nn
import torch.optim as optim

# Create synthetic data
X = torch.rand(100, 1)
y = 3 * X + 2 + 0.1 * torch.randn(100, 1)

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x):
        return self.fc(x)

# Instantiate the model
model = SimpleNN()

# Register backward hook
for p in model.parameters():
  p.register_hook(lambda grad: torch.clamp(grad, -0.1, 1.0))

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(100):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()

    # Update weights
    optimizer.step()

    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')
