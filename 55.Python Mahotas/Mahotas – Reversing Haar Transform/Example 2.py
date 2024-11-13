# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os


# loading iamge
img = mahotas.imread('dog_image.png')

# filtering iamge
img = img[:, :, 0]


# haar transform
h = mahotas.haar(img)

# showing image
print("Image with haar transform")
imshow(h)
show()

# reversing haar transform
r = mahotas.ihaar(h)

# showing image
print("Reversed haar transform")
imshow(r)
show()
