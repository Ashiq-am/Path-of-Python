# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os

# loading image
img = mahotas.imread('dog_image.png')

# filtering image
img = img[:, :, :3]

# showing image
print("Image")
imshow(img)
show()

# getting infocusness of each pixel
focus = np.array([mahotas.sobel(t, just_filter=True) for t in img])

# showing focus pixel
print("Foucs Image")
imshow(focus)
show()
