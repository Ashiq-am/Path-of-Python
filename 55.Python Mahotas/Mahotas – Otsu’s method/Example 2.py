# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os

# loading image
img = mahotas.imread('dog_image.png')

# setting filter to the image
img = img[:, :, 0]

imshow(img)
show()

# otsu method
T_otsu = mahotas.otsu(img)

# printing otsu value
print("Otsu Method value : " + str(T_otsu))

print("Image threshold using Otsu Mehtod")
# showing image
# image values should be greater than otsu value
imshow(img > T_otsu)
show()
