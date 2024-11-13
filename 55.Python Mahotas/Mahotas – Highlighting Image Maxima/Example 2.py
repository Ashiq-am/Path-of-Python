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

# getting distance map
dmap = mahotas.distance(labelled)

# showing image
print("Distance Map")
imshow(dmap)
show()

# numpy ones array
Bc = np.ones((4, 1))

# getting maxima
maxima = mahotas.morph.regmax(dmap, Bc=Bc)

# showing image
print("Maxima")
imshow(maxima)
show()
