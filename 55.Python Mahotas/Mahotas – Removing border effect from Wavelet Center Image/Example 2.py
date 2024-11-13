# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os


# loading image
img = mahotas.imread('dog_image.png')

# filtering image
img = img[:, :, 0]


# making image wavelet center
fc = mahotas.wavelet_center(img)

# showing image
print("Image with wavelet center")
imshow(fc)
show()

# restoring image
rd = mahotas.wavelet_decenter(fc, img.shape)


# showing image
print("Restored Image")
imshow(rd)
show()
