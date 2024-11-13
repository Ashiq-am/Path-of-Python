# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os


# loading image
img = mahotas.imread('dog_image.png')

# filtering image
img = img[:, :, 0]


# showing image
print("Image")

imshow(img)
show()

# making image wavelet center
fc = mahotas.wavelet_center(img)

# showing image
print("Image with wavelet center")
imshow(fc)
show()
