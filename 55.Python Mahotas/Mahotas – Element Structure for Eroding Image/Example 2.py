# importing required libraries
import mahotas
import numpy as np
import matplotlib.pyplot as plt
import os

# loading image
img = mahotas.imread('dog_image.png')

# setting filter to the image
img = img[:, :, 0]

# otsu method
T_otsu = mahotas.otsu(img)

# image values should be greater than otsu value
img = img > T_otsu

print("Image threshold using Otsu Mehtod")

# showing image
imshow(img)
show()

# erode structure
es = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]], bool)

# eroding image using element structure
new_img = mahotas.morph.erode(img, es)

# showing dilated image
print("Eroded Image")
imshow(new_img)
show()
