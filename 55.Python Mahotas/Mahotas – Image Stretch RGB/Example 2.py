# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os
import matplotlib.pyplot as plt

# loading image
img = mahotas.imread('dog_image.png')


print("Image")

# showing image
imshow(img)
show()

# stretching image
new_img = mahotas.stretch_rgb(img)


# Stretched image
print("Stretched Image")
imshow(new_img)
show()
