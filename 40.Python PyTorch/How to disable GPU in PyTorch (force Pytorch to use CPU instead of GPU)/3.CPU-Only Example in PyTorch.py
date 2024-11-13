import torch
import torch.nn as nn

device = torch.device("cpu")
# Create a  model
model = nn.Linear(5,1)
# send existing model to device
model = model.to(device)

# Create input data inside CPU
inputs = torch.randn(12, 5, device=device)
# Perform forward pass on the model
output = model(inputs)
print(output)
