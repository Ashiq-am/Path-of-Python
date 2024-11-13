# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os

# loading iamge
img = mahotas.imread('dog_image.png')

# getting grey image
g = img[:, :, 0]

# multiplying grey image values
g = g * 2

# fltering image
img = img[:, :, 0]

# otsu method
T_otsu = mahotas.otsu(img)

# image values should be greater than otsu value
img = img > T_otsu

print("Image threshold using Otsu Mehtod")

# showing image
imshow(img)
show()

# eroding image using conditional grey image
new_img = mahotas.cerode(img, g)

# showing eroded image
print("Eroded Image")
imshow(new_img)
show()
