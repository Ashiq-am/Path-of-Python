import torch
from PIL import Image
import torchvision.transforms as transforms

# Define the desired output size
output_size = (32,32)

# Load an image using PIL
image = Image.open("gfg1.jpeg").convert('L') # convert to grayscale

# Resize the image using transforms.Resize
image = transforms.Resize(output_size)(image)

# Convert the image to a PyTorch tensor
image_tensor = transforms.ToTensor()(image)
print(image_tensor.shape)

# Find the standard deviation
std_dev = torch.std(image_tensor)
print('standard deviation : ')
print(std_dev)
