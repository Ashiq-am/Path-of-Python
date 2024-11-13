# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os

# loading image
img = mahotas.imread('dog_image.png')


# filtering image
img = img[:, :, 0]

# showing image
imshow(img)
show()

# getting center of mass
center = mahotas.center_of_mass(img)

# printing center of mass co-ordinate
print("Center of Mass : " + str(center))
