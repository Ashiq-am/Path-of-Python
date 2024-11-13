# import required libraries
import torch
import torchvision.transforms as transforms
from PIL import Image

# Read image
image = Image.open('a.png')

# create an transform for crop the image
transform = transforms.RandomResizedCrop(size=(300, 600),
										scale=(0.2, 0.8))

# use above created transform to crop
# the image
image_crop = transform(image)

# display result
image_crop.show()
