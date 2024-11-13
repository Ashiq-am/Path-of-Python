# import required libraries
import torch
import torchvision.transforms as T
from PIL import Image

# read image
img = Image.open('a.jpg')

# define a transform
transform = T.RandomRotation(degrees=(30, 45))

# use above transform to rotate the image
img = transform(img)

# display result
img.show()
