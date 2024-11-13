# import required libraries
import torch
import torchvision.transforms as T
from PIL import Image

# read input image from computer
img = Image.open('Maximum subarray sum modulo m output.png')

# define a transform
transform = T.RandomHorizontalFlip(p=0.5)

# apply above defined transform to
# input image
img = transform(img)

# display result
img.show()



