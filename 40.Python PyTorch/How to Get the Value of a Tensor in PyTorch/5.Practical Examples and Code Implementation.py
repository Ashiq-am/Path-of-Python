import torch
import torch.nn as nn


# Defining a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)


# Creating an instance of the network
model = SimpleNN()

# Generating some random input data
input_tensor = torch.randn(1, 10)

# Forward pass through the network
output = model(input_tensor)

# Accessing the value of the output tensor
output_value = output.item()
print(f"Output value: {output_value}")
