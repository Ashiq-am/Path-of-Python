# importing required libraries
import numpy as np
import mahotas
from pylab import imshow, show
from mahotas.features import surf

# loading image
img = mahotas.imread('dog_image.png')

# filtering the image
img = img[:, :, 0]

# setting gaussian filter
gaussian = mahotas.gaussian_filter(img, 5)

# showing image
print("Image")
imshow(gaussian)
show()

# getting Speeded-Up Robust Features
spoints = surf.surf(gaussian)
print("No of points: {}".format(len(spoints)))
