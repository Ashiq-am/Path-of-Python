# importing required libraries
import numpy as np
import mahotas
from pylab import imshow, show

# loading image
img = mahotas.imread('dog_image.png')

# filtering the image
img = img[:, :, 0]

print("Image with filter")
# showing the image
imshow(img)
show()


# setting gaussian filter
gaussian = mahotas.gaussian_filter(img, 15)

print("Image with gaussian filter")
# showing the gaussian filter
imshow(gaussian)
show()
