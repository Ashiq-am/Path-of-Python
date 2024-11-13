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

# setting threshold
img = (img < img.mean())

print("Image with Threshold")
# showing the threshold image
imshow(img)
show()
