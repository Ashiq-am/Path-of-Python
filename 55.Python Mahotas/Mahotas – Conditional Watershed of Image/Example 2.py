# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os

# loading image
img = mahotas.imread('dog_image.png')


# filtering image
img = img[:, :, 0]

# otsu method
T_otsu = mahotas.otsu(img)

# image values should be greater than otsu value
img = img > T_otsu

print("Image threshold using Otsu Mehtod")

# showing image
imshow(img)
show()

# creating a labelled image
marker, n_nucleus = mahotas.label(img)

# watershed of image
new_img = mahotas.cwatershed(img, marker)

print("CWatershed Image")

# showing image
imshow(new_img)
show()
