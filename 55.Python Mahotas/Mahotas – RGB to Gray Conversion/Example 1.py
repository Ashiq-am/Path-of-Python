# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# loading image
img = mahotas.demos.load('lena')


# showing image
print("Image")
imshow(img)
show()

# rgb to gray
new_img = mahotas.colors.rgb2gray(img)

# showing new image
print("New Image")
imshow(new_img)
show()
