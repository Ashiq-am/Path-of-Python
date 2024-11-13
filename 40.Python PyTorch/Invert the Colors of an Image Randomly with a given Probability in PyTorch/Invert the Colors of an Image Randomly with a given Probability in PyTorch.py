# import required libraries
import torch
import torchvision.transforms as T
from PIL import Image

# read image from your computer
img = Image.open('a.png')

# invert the colors with probability=1
transform = T.RandomInvert(p=1)
img = transform(img)

# display result
img.show()
