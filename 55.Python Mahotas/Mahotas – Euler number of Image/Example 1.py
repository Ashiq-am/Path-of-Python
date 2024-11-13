# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# loading image
img = mahotas.demos.load('lena')



# filtering image
img = img.max(2)

# otsu method
T_otsu = mahotas.otsu(img)

# image values should be greater than otsu value
img = img > T_otsu

print("Image threshold using Otsu Mehtod")

# creating a labeled image
marker, n_nucleus = mahotas.label(img)

# showing image
imshow(img)
show()


# euler number of image of image
euler = mahotas.euler(img)

print("Euler Number of Image : " + str(euler))
