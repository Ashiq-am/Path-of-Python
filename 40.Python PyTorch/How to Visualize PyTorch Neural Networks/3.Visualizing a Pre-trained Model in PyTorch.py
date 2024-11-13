import torch
import torchvision.models as models
from torchviz import make_dot

# Load a pre-trained ResNet18 model
model = models.resnet18(pretrained=True)

# Create a dummy input tensor with the shape expected by ResNet
dummy_input = torch.randn(1, 3, 224, 224)  # Batch size of 1, 3 channels, 224x224 image

# Perform a forward pass
output = model(dummy_input)

# Create and save the visualization of the computational graph
dot = make_dot(output, params=dict(model.named_parameters()))
dot.format = 'png'
dot.render('resnet18')

print("Visualization saved as 'resnet18.png'.")
