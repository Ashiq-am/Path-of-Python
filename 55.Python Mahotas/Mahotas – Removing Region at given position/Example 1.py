# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os

# loading image
img = mahotas.imread('dog_image.png')

# setting filter to the image
img = img[:, :, 0]

# setting gaussian filter
img = mahotas.gaussian_filter(img, 15)

# setting threshold value
img = (img > img.mean())

# creating a labelled image
labeled1, n_nucleus1 = mahotas.label(img)

# showing the labelled image
print("Labelled Image")
imshow(labelled1)
show()

# removing region
labelled2 = mahotas.labelled.remove_regions(labelled1, 1, 1)

# showing the labelled image
print("Labelled Image with removed region")
imshow(labelled2)
show()
