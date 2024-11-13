# importing required libraries
import mahotas
import mahotas.demos
import numpy as np
from pylab import imshow, gray, show
from os import path

# loading the image
photo = mahotas.demos.load('luispedro')

# showing original image
print("Origial Image")
imshow(photo)
show()

# loading image as grey
photo = mahotas.demos.load('luispedro', as_grey = True)

# converting image type to unit8
# beacuse as_grey returns floating values
photo = photo.astype(np.uint8)

# riddler calvard
T_rc = mahotas.rc(photo)

# printing otsu value
print("R C value : " + str(T_rc))

print("Image threshold using riddler calvard method")
# showing image
# image values should be greater than T_rc value
imshow(photo > T_rc)
show()
