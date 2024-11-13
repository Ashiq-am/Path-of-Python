# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os


# loading image
img = mahotas.imread('dog_image.png')

# filtering image
img = img[:, :, 0]


# Transform using D8 Wavelet to obtain transformed image t
t = mahotas.daubechies(img, 'D8')


# showing transformed image
print("Transformed Image")
imshow(t)
show()

# reconstructed image
r = mahotas.idaubechies(t, 'D8')

# showing image
print("Reconstructed Image")
imshow(r)
show()
