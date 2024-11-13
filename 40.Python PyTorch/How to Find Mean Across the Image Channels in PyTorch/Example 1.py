# import required libraries
import torch
from PIL import Image
import torchvision.transforms as transforms

# Read input image
img = Image.open('Maximum subarray sum modulo m output.png')

# create a transform
transform = transforms.ToTensor()

# convert the image to PyTorch Tensor
imgTensor = transform(img)

# Compute the mean of Image across the
# channels RGB
r, g, b = torch.mean(imgTensor, dim=[1, 2])

# Display Result
print("Mean for Red channel: ", r)
print("Mean for Green channel: ", g)
print("Mean for Blue channel: ", b)
