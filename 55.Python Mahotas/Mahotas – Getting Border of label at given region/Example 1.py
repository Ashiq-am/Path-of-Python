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


# showing the labelled image
print("Labelled Image")
imshow(labelled)
show()

# getting border for label at given point
relabeled = mahotas.labelled.border(labelled, 0, 20)

# showing the image
print("Labels With borders at given point")
imshow(relabelled)
show()
