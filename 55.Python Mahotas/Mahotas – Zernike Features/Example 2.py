# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os
import matplotlib.pyplot as plt

# loading image
img = mahotas.imread('dog_image.png')


# filtering image
img = img[:, :, 0]

print("Image")

# showing image
imshow(img)
show()

# degree
degree = 10

# radius
radius = 10

# computing zernike feature
value = mahotas.features.zernike(img, degree, radius)


# printing value
print(value)
