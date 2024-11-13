# import required libraries
import torch
import torchvision.transforms as transforms
from PIL import Image

# Read image
image = Image.open('a.jpg')

# define an transform, height=180 width=300
transform = transforms.CenterCrop((180, 300))

# use above created transform to crop
# the image
image_crop = transform(image)

# display result
image_crop.show()
