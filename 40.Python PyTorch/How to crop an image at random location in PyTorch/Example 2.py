# import required libraries
import torch
import torchvision.transforms as transforms
from PIL import Image

# Read image
image = Image.open('a.jpg')

# create an transform for crop the image
transform = transforms.RandomCrop(300)

# use above created transform to crop
# the image
image_crop = transform(image)

# display result
image_crop.show()
