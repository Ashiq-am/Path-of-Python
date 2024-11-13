import torch.nn as nn
import torch

class_weights = torch.tensor([0.1, 0.9])

# Use the weights in CrossEntropyLoss
criterion = nn.CrossEntropyLoss(weight=class_weights)
outputs = torch.randn(10, 2)
labels = torch.randint(0, 2, (10,))

loss = criterion(outputs, labels)
print(loss.item())
