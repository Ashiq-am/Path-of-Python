import torch
import torch.nn as nn
import torch.optim as optim

# Example dataset: XOR problem
X = torch.tensor([[0,0], [0,1], [1,0], [1,1]], dtype=torch.float)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float)

# Neural Network Structure
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(2, 2)  # Input layer to hidden layer
        self.fc2 = nn.Linear(2, 1)  # Hidden layer to output layer

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# Initialize the network
net = SimpleNet()
