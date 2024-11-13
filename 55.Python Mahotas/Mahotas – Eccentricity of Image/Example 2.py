# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os
import matplotlib.pyplot as plt

# loading image
img = mahotas.imread('dog_image.png')


# fltering image
img = img[:, :, 0]

print("Image")

# showing image
imshow(img)
show()

# computing eccentricity value
value = mahotas.features.eccentricity(img)


# showing value
print("Eccentricity value = " + str(value))
