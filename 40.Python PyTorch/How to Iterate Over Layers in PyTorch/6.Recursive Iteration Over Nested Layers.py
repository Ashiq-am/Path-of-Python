import torch
import torch.nn as nn

# Define a custom initialization function
def custom_init(layer):
    if isinstance(layer, nn.Conv2d):
        nn.init.xavier_uniform_(layer.weight)
        if layer.bias is not None:
            nn.init.zeros_(layer.bias)

# Example neural network model with nested structures
class NestedCNN(nn.Module):
    def __init__(self):
        super(NestedCNN, self).__init__()
        self.conv_block1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.conv_block2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.fc_block = nn.Sequential(
            nn.Linear(in_features=64*7*7, out_features=128),
            nn.ReLU(),
            nn.Linear(in_features=128, out_features=10)
        )

    def forward(self, x):
        x = self.conv_block1(x)
        x = self.conv_block2(x)
        x = x.view(-1, 64*7*7)
        x = self.fc_block(x)
        return x

model = NestedCNN()
model.apply(custom_init)

# Function to recursively iterate over all layers
def iterate_layers(module):
    for name, layer in module.named_children():
        print(f"Layer Name: {name}, Layer Type: {type(layer)}")
        iterate_layers(layer)  # Recursively iterate over nested layers
iterate_layers(model)
