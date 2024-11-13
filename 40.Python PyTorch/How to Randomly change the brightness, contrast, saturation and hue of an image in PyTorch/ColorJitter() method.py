# import required libraries
import torch
import torchvision.transforms as transforms
from PIL import Image

# Read the image from computer
input_img = Image.open('Maximum subarray sum modulo m output.png')

# define a transform
transform = transforms.ColorJitter(
	brightness=0.5, contrast=1, saturation=0.1, hue=0.5)

# apply the above transform on image
output_img = transform(input_img)

# display result
output_img.show()
