# importing required libraries
import mahotas
import numpy as np
import matplotlib.pyplot as plt
import os

# loading image
img = mahotas.imread('dog_image.png')

# filtering image
img = img[:, :, :3]

# rgb to xyz
xyz_img = mahotas.colors.rgb2xyz(img)

# showing new image
print("Image")
imshow(xyz_img)
show()

# getting lab image
new_img = mahotas.colors.xyz2lab(xyz_img)

# showing image
print("New Image")
imshow(new_img)
show()
