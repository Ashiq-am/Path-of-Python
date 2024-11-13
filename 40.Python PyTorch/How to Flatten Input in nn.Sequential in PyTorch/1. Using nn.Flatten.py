import torch
import torch.nn as nn

# Define a simple CNN model using nn.Sequential
model = nn.Sequential(
    nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Flatten(),  # Flatten the output before the linear layer
    nn.Linear(32 * 14 * 14, 128),  # Assuming input size is (1, 28, 28)
    nn.ReLU(),
    nn.Linear(128, 10),
    nn.LogSoftmax(dim=1)
)

# Example input
input_tensor = torch.randn(1, 1, 28, 28)
output = model(input_tensor)
print(output)
