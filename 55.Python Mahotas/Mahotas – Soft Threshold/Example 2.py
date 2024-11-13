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

# showing the image
imshow(img)
show()

# unit 8 valye
t = np.uint8(180)

# soft threshold
img = mahotas.thresholding.soft_threshold(img, t)

print("Image with soft threshold")

# showing image
imshow(img)
show()
