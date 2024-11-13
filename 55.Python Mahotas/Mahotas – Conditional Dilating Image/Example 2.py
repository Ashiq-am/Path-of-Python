# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os

# loading image
img = mahotas.imread('dog_image.png')

# grey image
g = img[:, :, 2]

# multiplying grey image values
g = g * 100

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

# dilating image using conditional grey image
dilate_img = mahotas.cdilate(img, g)

# showing dilated image
print("Dilated Image")
imshow(dilate_img)
show()
