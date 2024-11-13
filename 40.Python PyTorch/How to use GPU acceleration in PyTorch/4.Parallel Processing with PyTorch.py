import torch
import torch.nn as nn

model = nn.Conv2d(3, 64, 3, 1, 1) # Create a model

model = nn.DataParallel(model) # Wrap the model with DataParallel

model = model.to('cuda') # Move the model to the GPU
# Perform forward pass on the model
input_data = torch.randn(20, 3, 32, 32).to('cuda')
output = model(input_data)
