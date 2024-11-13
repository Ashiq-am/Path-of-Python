# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np
import matplotlib.pyplot as plt

# loading image
img = mahotas.demos.load('lena')

# filtering image
img = img.max(2)

print("Image")

# showing image
imshow(img)
show()

# applying mean filter
new_img = mahotas.mean_filter(img, n)


# showing image
print("Mean Filter")
imshow(new_img)
show()
