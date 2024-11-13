# import required libraries
import torch
import torchvision.transforms as transforms
from PIL import Image

# Read the image from your computer
img = Image.open('geekslogo.png')

# get width and height of image
w, h = img.size

# pad 100 to left/right and 50 to top/bottom
transform = transforms.Pad((100, 50))

# add padding to image
img = transform(img)

# resize the image to original dimension
img = img.resize((w, h))

# display output
img.show()
