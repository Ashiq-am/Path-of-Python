# import required libraries
import torch
import torchvision.transforms as T
from PIL import Image

# read the image
img = Image.open('GFG.jpg')

# define a transform to rotate the image
transform = T.RandomRotation(degrees=(60, 90))

# use above transform to rotate the image
img = transform(img)

# display result
img.show()
