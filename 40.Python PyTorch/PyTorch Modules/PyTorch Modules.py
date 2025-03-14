import torch
import torch.nn as nn


class MyModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out


# Example usage:
input_size = 10
hidden_size = 20
output_size = 5

model = MyModel(input_size, hidden_size, output_size)

# Assuming you have some input data 'x'
x = torch.randn(32, input_size)  # Example input data with batch size 32 and input size 10

# Forward pass
output = model(x)
print(output.shape)  # Output shape: (32, 5)
