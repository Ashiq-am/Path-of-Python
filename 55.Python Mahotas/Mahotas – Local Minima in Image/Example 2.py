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

# getting local minima of the image
new_img = mahotas.locmin(img)


# showing image
print("Local Minima")
imshow(new_img)
show()
