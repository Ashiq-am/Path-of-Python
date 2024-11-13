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

# applying majority filter
new_img = mahotas.majority_filter(img)


# showing image
print("Majority Filter")
imshow(new_img)
show()
