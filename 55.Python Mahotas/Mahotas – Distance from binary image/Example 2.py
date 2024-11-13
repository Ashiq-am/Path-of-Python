# importing required libraries
import numpy as np
import mahotas
from pylab import imshow, show

# loading image
img = mahotas.imread('dog_image.png')

# filtering the image
img = img[:, :, 0]

# setting gaussian filter
gaussian = mahotas.gaussian_filter(img, 15)

# setting threshold value
gaussian = (gaussian > gaussian.mean())

# creating a labeled image
labeled, n_nucleus = mahotas.label(gaussian)

print("Image")
# showing the gaussian filter
imshow(labeled)
show()

# getting distance map
dmap = mahotas.distance(labeled)

# showing image
print("Distance Map")
imshow(dmap)
show()
