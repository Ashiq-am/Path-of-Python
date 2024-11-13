#Import neccessary libraries

import torch
from torchsummary import summary
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torchvision.transforms import ToTensor, Normalize
from torchvision.datasets import MNIST, CIFAR10
from torch.utils.data import DataLoader

# Step 1: Choose a Pre-Trained Model
import torchvision.models as models

# Load the pre-trained ResNet-50 model
model = models.resnet50(pretrained=True)
