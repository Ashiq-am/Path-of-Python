# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os

# loading nuclear image
f = mahotas.demos.load('nuclear')

# setting filter to the image
f = f[:, :, 0]

# setting gaussian filter
f = mahotas.gaussian_filter(f, 4)

# setting threshold value
f = (f> f.mean())

# creating a labelled image
labelled, n_nucleus = mahotas.label(f)

# printing number of labels
print("Count : " + str(n_nucleus))

# showing the labelled image
print("Labelled Image")
imshow(labelled)
show()


# filtering the label image
# adding max size filter
relabelled, n_left = mahotas.labelled.filter_labelled(labelled, max_size = 7000)

# showing number of labels
print("Count : " + str(n_left))

# showing the image
print("Max size 7000 Label")
imshow(relabelled)
show()
