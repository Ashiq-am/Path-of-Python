# importing required libraries
import mahotas
import numpy as np
import matplotlib.pyplot as plt
import os

# loading image
img = mahotas.imread('dog_image.png')

# filtering image
img = img[:, :, :3]

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
