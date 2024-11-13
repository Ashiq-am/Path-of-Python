# import required libraries
import torch
import torchvision.transforms as transforms
from PIL import Image

# Read image
image = Image.open('pic.png')

# create an transform for crop the image
# 300px height and 600px wide
transform = transforms.RandomResizedCrop(size=(300, 600))

# use above created transform to crop
# the image
image_crop = transform(image)

# display result
image_crop.show()
