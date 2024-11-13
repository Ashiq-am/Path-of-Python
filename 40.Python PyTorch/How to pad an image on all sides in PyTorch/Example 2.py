# import required libraries
import torch
import torchvision.transforms as transforms
from PIL import Image

# Read the image from your computer
img = Image.open('geekslogo.png')

# get width and height of image
w, h = img.size

# pad 10 to left, 20 to top, 30 to right,
# 50 bottom
transform = transforms.Pad((10, 20, 50, 50))

# add padding to image
img = transform(img)

# resize the image to original dimension
img = img.resize((w, h))

# display output
img.show()
