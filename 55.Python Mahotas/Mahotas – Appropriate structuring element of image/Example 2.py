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

# getting structring element
value = mahotas.get_structuring_elem(img, 2)

# showing value
print(value)
