import torch
import torch.nn as nn
import torch.nn.functional as F

# Define input and target tensors
input = F.log_softmax(torch.tensor([[0.8, 0.15, 0.05]]), dim=1)
target = torch.tensor([[0.7, 0.2, 0.1]])

# Initialize KLDivLoss
criterion = nn.KLDivLoss(reduction='batchmean')

# Compute loss
loss = criterion(input, target)
print(loss)
