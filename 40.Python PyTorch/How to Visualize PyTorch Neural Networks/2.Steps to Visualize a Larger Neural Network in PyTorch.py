import torch
import torch.nn as nn
import torch.nn.functional as F
from torchviz import make_dot
import numpy as np

# Define a larger neural network
class LargerNet(nn.Module):
    def __init__(self):
        super(LargerNet, self).__init__()
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 64)
        self.fc5 = nn.Linear(64, 10)  # Output layer for 10 classes

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = self.fc5(x)
        return x

# Create dummy input
dummy_input = torch.randn(1, 784)

# Instantiate the model and perform a forward pass
model = LargerNet()
output = model(dummy_input)

# Create and save the visualization of the computational graph
dot = make_dot(output, params=dict(model.named_parameters()))
dot.format = 'png'
dot.render('larger_net')

print("Visualization saved as 'larger_net.png'.")
