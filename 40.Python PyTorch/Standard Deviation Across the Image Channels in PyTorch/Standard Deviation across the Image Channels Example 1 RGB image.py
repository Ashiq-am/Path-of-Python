# import packages
import torch
from PIL import Image
import torchvision.transforms as transforms

# Define the desired output size
output_size = (32,32)

# Load an image using PIL
image = Image.open("gfg1.jpeg")

# # Resize the image using transforms.Resize
image = transforms.Resize(output_size)(image)

# Convert the image to a PyTorch tensor
image_tensor = transforms.ToTensor()(image)
print(image_tensor.shape)
# Get the standard deviation for each channel
red_std = torch.std(image_tensor[0])
green_std = torch.std(image_tensor[1])
blue_std = torch.std(image_tensor[2])

# Print the standard deviation of each channel
print('Red channel std dev:', red_std.item())
print('Green channel std dev:', green_std.item())
print('Blue channel std dev:', blue_std.item())
