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

# Power for first dimension
p0 = 10.5

# Power for second dimension
p1 = 2.5


# getting moments
moment = mahotas.moments(img, p0, p1)


# printing moments
print("Moment value = " + str(moment))
