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

# riddler calvard
T_rc = mahotas.rc(img)

# printing otsu value
print("R C value : " + str(T_rc))

print("Image threshold using riddler calvard method")
# showing image
# image values should be greater than T_rc value
imshow(img > T_rc)
show()
