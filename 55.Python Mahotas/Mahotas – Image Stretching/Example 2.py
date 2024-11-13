# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os
import matplotlib.pyplot as plt

# loading iamge
img = mahotas.imread('dog_image.png')

# fltering image
img = img[:, :, 0]

print("Image")

# showing image
imshow(img)
show()

# strecting image
new_img = mahotas.stretch(img)

# Stretched image
print("Stretched Image")
imshow(new_img)
show()
