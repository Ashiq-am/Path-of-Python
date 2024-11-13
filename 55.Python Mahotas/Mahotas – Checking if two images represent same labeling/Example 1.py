# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os

# loading nuclear image
f1 = mahotas.demos.load('nuclear')

# setting filter to the image
f1 = f1[:, :, 0]


# setting gaussian filter
f1 = mahotas.gaussian_filter(f1, 4)

# setting threshold value
f1 = (f1> f1.mean())

# creating a labeled image
labeled1, n_nucleus1 = mahotas.label(f1)

# showing the labeleed image
print("Labelled 1 Image")
imshow(labeled1)
show()

# loading nuclear image
f2 = mahotas.demos.load('nuclear')

# setting filter to the image
f2 = f2[:, :, 0]

# setting gaussian filter
f2 = mahotas.gaussian_filter(f2, 4)

# setting threshold value
f2 = (f2> f2.mean())

# creating a labeled image
labeled2, n_nucleus2 = mahotas.label(f2)


# showing the labeleed image
print("Labelled 2 Image")
imshow(labeled2)
show()

# c hecking if both the labeled images are same
check = mahotas.labeled.is_same_labeling(labeled1, labeled2)

# printing check
print("Same Labelling : "+ str(check))
