# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np
import matplotlib.pyplot as plt

# loading iamge
img = mahotas.demos.load('lena')

# filtering image
img = img.max(2)

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
