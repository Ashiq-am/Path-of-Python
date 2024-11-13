import torch
import torch.nn as nn

class CustomLoss(nn.Module):
    def __init__(self, weight):
        super(CustomLoss, self).__init__()
        self.weight = weight

    def forward(self, input, target):
        # Compute the loss
        loss = torch.mean(self.weight * (input - target) ** 2)
        return loss

# Example usage:
# Create an instance of the custom loss function
weight = torch.tensor(0.5)  # You can adjust the weight according to your needs
loss_function = CustomLoss(weight)

# Define input and target tensors
input_tensor = torch.randn(3, requires_grad=True)
target_tensor = torch.randn(3)

# Compute the loss
loss = loss_function(input_tensor, target_tensor)
print(loss)
