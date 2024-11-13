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

# making is labelled image
labeled, n = mahotas.label(gaussian)

# showing image
print("Labelled Image")
imshow(labelled)
show()

# getting haralick features
h_feature = mahotas.features.haralick(labelled)

# showing the feature
print("Haralick Features")
imshow(h_feature)
show()
