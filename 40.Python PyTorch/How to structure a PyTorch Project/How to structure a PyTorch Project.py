# This module defines a CNN model for image classification
import torch
import torch.nn as nn
import torch.nn.functional as F

class CNN(nn.Module):
    """A CNN model for image classification.

    Args:
        in_channels (int): The number of input channels.
        num_classes (int): The number of output classes.

    Attributes:
        conv1 (nn.Conv2d): The first convolutional layer.
        conv2 (nn.Conv2d): The second convolutional layer.
        pool (nn.MaxPool2d): The max pooling layer.
        fc1 (nn.Linear): The first fully connected layer.
        fc2 (nn.Linear): The second fully connected layer.
    """

    def __init__(self, in_channels, num_classes):
        super(CNN, self).__init__()
        # Define the convolutional layers
        self.conv1 = nn.Conv2d(in_channels, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        # Define the pooling layer
        self.pool = nn.MaxPool2d(2, 2)
        # Define the fully connected layers
        self.fc1 = nn.Linear(32 * 8 * 8, 64)
        self.fc2 = nn.Linear(64, num_classes)

    def forward(self, x):
        """The forward pass of the model.

        Args:
            x (torch.Tensor): The input tensor of shape (batch_size, in_channels, height, width).

        Returns:
            torch.Tensor: The output tensor of shape (batch_size, num_classes).
        """
        # Apply the convolutional layers and the pooling layer
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        # Flatten the tensor
        x = x.view(-1, 32 * 8 * 8)
        # Apply the fully connected layers
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
