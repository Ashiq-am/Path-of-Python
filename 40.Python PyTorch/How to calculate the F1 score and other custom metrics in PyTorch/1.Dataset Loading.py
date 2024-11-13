import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load CIFAR-10 dataset
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_data = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
test_data = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

# Filtering for binary classification
binary_train_data = Subset(train_data, [i for i in range(len(train_data)) if train_data.targets[i] <= 1])
binary_test_data = Subset(test_data, [i for i in range(len(test_data)) if test_data.targets[i] <= 1])

train_loader = DataLoader(dataset=binary_train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=binary_test_data, batch_size=64, shuffle=False)
