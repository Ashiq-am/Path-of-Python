# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os
import matplotlib.pyplot as plt

# loading image
img = mahotas.imread('dog_image.png')


# filtering image
img = img[:, :, 0]

print("Image")

# showing image
imshow(img)
show()

# resizing image
new_img = mahotas.imresize(img, [200, 200])


# showing image
print("Resized Image")
imshow(new_img)
show()
