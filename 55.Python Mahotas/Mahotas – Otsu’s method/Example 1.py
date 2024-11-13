# importing required libraries
import mahotas
import mahotas.demos
import numpy as np
from pylab import imshow, gray, show
from os import path

# loading the image
photo = mahotas.demos.load('luispedro')

# showing original image
print("Original Image")
imshow(photo)
show()

# loading image as grey
photo = mahotas.demos.load('luispedro', as_grey = True)

# converting image type to unit8
# beacuse as_grey returns floating values
photo = photo.astype(np.uint8)

# otsu method
T_otsu = mahotas.otsu(photo)

# printing otsu value
print("Otsu Method value : " + str(T_otsu))

print("Image threshold using Otsu Mehtod")
# showing image
# image values should be greater than otsu value
imshow(photo > T_otsu)
show()
