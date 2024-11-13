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
plt.imshow(img)
plt.show()

# rgb to sepia
new_img = mahotas.colors.rgb2sepia(img)

# showing new image
print("New Image")
plt.imshow(new_img)
plt.show()
