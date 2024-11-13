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

# creating a labelled image
labelled, n_nucleus = mahotas.label(gaussian)

# printing number of labels
print("Count : " + str(n_nucleus))

print("Labelled Image")
# showing the gaussian filter
imshow(labelled)
show()

# removing border labels
labelled = mh.labelled.remove_bordering(labelled)

# relabling the labelled image
relabelled, n_left = mahotas.labelled.relabel(labelled)

# showing number of labels
print("Count : " + str(n_left))

# showing the image
print("No border Label")
imshow(relabelled)
show()
