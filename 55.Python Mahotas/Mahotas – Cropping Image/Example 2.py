# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os

# loading image
img = mahotas.imread('dog_image.png')

# showing image
print("Image")
imshow(img)
show()

# cropping image
img = img[:, 200:700]

# showing the image
print("Cropped Image")
imshow(img)
show()
