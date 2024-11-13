import torch
import torch.nn as nn

# Define your model
model = nn.Sequential(
    nn.Linear(1024, 512),
    nn.ReLU(),
    nn.Linear(512, 10)
)

# Wrap the model with DataParallel
model = torch.nn.DataParallel(model)
model.to('cuda')
