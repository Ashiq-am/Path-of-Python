# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# loading image
img = mahotas.demos.load('lena')

# rgb to xyz
xyz_img = mahotas.colors.rgb2xyz(img)

# showing new image
print("Image")
imshow(xyz_img)
show()

# getting rgb image
new_img = mahotas.colors.xyz2rgb(xyz_img)

# showing image
print("New Image")
imshow(new_img)
show()
