# import required libraries
import torch
import torchvision.transforms as transforms
from PIL import Image

# Read image
image = Image.open('pic.jpg')

# create an transform for crop the image
# 200px height and 400px wide
transform = transforms.RandomCrop((200, 400))

# use above created transform to crop
# the image
image_crop = transform(image)

# display result
image_crop.show()
