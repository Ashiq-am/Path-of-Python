# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os

# loading image
img = mahotas.imread('dog_image.png')

# setting filter to the image
img = img[:, :, 0]

print("Image")

# shoing the image
imshow(img)
show()

# bernsen threshold
img = mahotas.thresholding.bernsen(img, 5, 100)

print("Image with bernsen threshold")

# showing image
imshow(img)
show()
