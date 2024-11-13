# importing required libraries
import mahotas
import mahotas.demos
import numpy as np
from pylab import imshow, gray, show
from os import path

# loading the image
photo = mahotas.demos.load('luispedro')


# loading image as grey
photo = mahotas.demos.load('luispedro', as_grey = True)

# converting image type to unit8
# beacuse as_grey returns floating values
photo = photo.astype(np.uint8)

# showing original image
print("Image")
imshow(photo)
show()

# bernsen threshold
photo = mahotas.thresholding.bernsen(photo, 7, 200)


print("Image with bernsen threshold")

# showing image
imshow(photo)
show()
