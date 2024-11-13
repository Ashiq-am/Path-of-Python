import torch
import torch.nn as nn

# Define the custom Flatten class
class Flatten(nn.Module):
    def forward(self, x):
        return x.view(x.size(0), -1)

# Define the model using nn.Sequential
model = nn.Sequential(
    nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2, stride=2),
    Flatten(),  # Use custom Flatten class
    nn.Linear(32 * 14 * 14, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
    nn.LogSoftmax(dim=1)
)

# Create a dummy input tensor with shape (batch_size, channels, height, width)
# For example, let's use a batch size of 1, with 1 channel, and 28x28 image size
dummy_input = torch.randn(1, 1, 28, 28)

# Pass the dummy input through the model
output = model(dummy_input)
print(output)
