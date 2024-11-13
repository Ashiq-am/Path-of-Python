# importing required libraries
import numpy as np
import mahotas
from pylab import imshow, show
import matplotlib.pyplot as plt

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

# Computing Linear Binary Patterns
value = mahotas.features.lbp(labelled, 200, 5, ignore_zeros=False)

# showing histograph
plt.hist(value)
