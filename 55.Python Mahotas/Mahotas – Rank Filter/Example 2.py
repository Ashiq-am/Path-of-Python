# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os
import matplotlib.pyplot as plt

# loading iamge
img = mahotas.imread('dog_image.png')

# fltering image
img = img[:, :, 0]

print("Image")

# showing image
imshow(img)
show()

# neighbour pixel
neighbour = 3

# rank
rank = 2

# applaying rank filter
new_img = mahotas.rank_filter(img, neighbour, rank)

# showing image
print("Rank Filter")
imshow(new_img)
show()
